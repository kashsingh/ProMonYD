from PyQt4.QtGui import  *
from PyQt4.QtCore import *
import sys
import mainWindowGUI
import infoExtractor
import dialogGUI
import videoDownload
import os
import playlistDownload


class Mainwindow(QMainWindow, mainWindowGUI.Ui_MainWindow):

    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setupUi(self)
        self.downVideoID=0
        self.outputfolder="C:\\PMYD"
        self.start_no=1
        self.end_no=2
        self.outputBrowse.clicked.connect(self.browse_folder)
        self.videoDown.clicked.connect(self.ex_Info)
        self.playlistDown.clicked.connect(self.download_playlist)
        self.stopButton.clicked.connect(self.stop_threads)

    def ex_Info(self):
        self.url=str(self.videoURL.text())
        self.get_thread = getInfoThread(self.url)
        self.connect(self.get_thread, SIGNAL("open_dialog(QStringList)"), self.showDial)
        self.connect(self.get_thread, SIGNAL("run_ex_info_terminated(QString)"), self.ex_info_terminated)
        self.get_thread.start()

        self.statusValuelabel.setText("Downloading video formats, please wait...")
        self.videoDown.setEnabled(False)
        self.outputBrowse.setEnabled(False)
        self.playlistDown.setEnabled(False)
        self.videoURL.setReadOnly(True)
        self.outputDir.setReadOnly(True)
        self.playlistURL.setReadOnly(True)
        self.stopButton.setEnabled(True)
        self.progressBar.setEnabled(True)

    def browse_folder(self):
        dir= QFileDialog.getExistingDirectory(None, 'Select a folder:', "C:\\PMYD", QFileDialog.ShowDirsOnly)
        self.outputDir.setText(dir)
        self.create_out_dir()
        self.outputfolder = str(dir)

    def ex_info_terminated(self,v):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Please check the internet connection or the URL entered.")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        self.stop_threads()

    def showDial(self,f_data):
        info_formats=[str(f) for f in f_data]
        format_list=[]
        fid_dict={}
        for x in info_formats:
          data=x.split(" - ")
          format_list.append(data[1])
          fid_dict[data[1]]=data[0]
        Dialog = formatDialog(format_list,fid_dict)
        Dialog.setWindowModality(Qt.ApplicationModal)
        if Dialog.exec_():
          self.downVideoID=Dialog.download_id
          self.statusValuelabel.setText("Now downloading video/audio, please wait...")

          self.get_video_thread = videoDownload.download_video_thread(self.downVideoID,self.outputDir,self.url)
          self.get_video_thread.start()

          self.connect(self.get_video_thread, SIGNAL("progress_value(QString)"), self.progress_change)
          self.connect(self.get_video_thread, SIGNAL("status_value(QString)"), self.status_change)
          self.connect(self.get_video_thread,SIGNAL("finished()"),self.download_finished)

        else:
          self.videoDown.setEnabled(True)
          self.outputBrowse.setEnabled(True)
          self.playlistDown.setEnabled(True)
          self.videoURL.setReadOnly(False)
          self.outputDir.setReadOnly(False)
          self.playlistURL.setReadOnly(False)
          self.statusValuelabel.setText("")

    def download_finished(self):
        self.videoDown.setEnabled(True)
        self.outputBrowse.setEnabled(True)
        self.playlistDown.setEnabled(True)
        self.statusValuelabel.setText("Download finished.")
        self.progressBar.setValue(0)
        self.videoURL.setReadOnly(False)
        self.outputDir.setReadOnly(False)
        self.playlistURL.setReadOnly(False)
        self.progressBar.setEnabled(False)
        self.stopButton.setEnabled(False)

    def progress_change(self,progress_value):
        value=progress_value.toInt()
        self.progressBar.setValue(value[0])

    def status_change(self,status_value):
        value=str(status_value)
        self.statusValuelabel.setText(value)

    def create_out_dir(self):
        if not os.path.exists(self.outputfolder):
            os.makedirs(self.outputfolder)

    def download_playlist(self):
        self.start_no=int(self.startValue.value())
        self.end_no=int(self.endValue.value())
        self.url=str(self.playlistURL.text())

        self.videoDown.setEnabled(False)
        self.outputBrowse.setEnabled(False)
        self.playlistDown.setEnabled(False)
        self.videoURL.setReadOnly(True)
        self.outputDir.setReadOnly(True)
        self.playlistURL.setReadOnly(True)
        self.stopButton.setEnabled(True)
        self.progressBar.setEnabled(True)
        self.statusValuelabel.setText("Download playlist manifest, please wait...")

        self.get_playlist_thread = playlistDownload.download_playlist_thread(self.start_no,self.end_no,self.outputfolder,self.url)
        self.get_playlist_thread.start()
        self.connect(self.get_playlist_thread, SIGNAL("progress_value(QString)"), self.progress_change)
        self.connect(self.get_playlist_thread, SIGNAL("status_value(QString)"), self.status_change)
        self.connect(self.get_playlist_thread,SIGNAL("finished()"),self.download_finished)

    def stop_threads(self):
        try:
            if self.get_thread.isRunning()==True:
                self.get_thread.terminate()
        except:
            pass
        try:
            if self.get_video_thread.isRunning()==True:
                self.get_video_thread.terminate()
        except:
            pass
        try:
            if self.get_playlist_thread.isRunning()==True:
                self.get_playlist_thread.terminate()
        except:
            pass

        self.download_finished()
        self.statusValuelabel.setText('Download stopped.')

class getInfoThread(QThread):

    def __init__(self,url):
        QThread.__init__(self)
        self.url = url

    def __del__(self):
        self.wait()

    def run(self):
        try:
            info_list=infoExtractor.extractor(self.url)
            f_data=QStringList(info_list)
            self.emit(SIGNAL("open_dialog(QStringList)"),f_data)
        except:
            v=QString('over')
            self.emit(SIGNAL("run_ex_info_terminated(QString)"),v)

class formatDialog(QDialog,dialogGUI.Ui_Dialog):

    def __init__(self,format_list,fid_dict):
        super(formatDialog,self).__init__()
        self.setupUi(self)
        self.format_list=format_list
        self.fid_dict=fid_dict
        self.download_id=0

        for item in self.format_list:
            QListWidgetItem(item, self.listWidget)

        self.pushButtonDownload.clicked.connect(self.send_fid)

    def send_fid(self):
            try:
                selected_format=self.listWidget.currentItem()
                self.download_id= self.fid_dict[str(selected_format.text())]
                self.accept()
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Please select a format to download.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

def startGui():
    app=QApplication(sys.argv)
    form=Mainwindow()
    form.show()
    app.exec_()

if __name__=="__main__":
    startGui()






