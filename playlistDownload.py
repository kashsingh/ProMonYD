from __future__ import unicode_literals
import youtube_dl
from PyQt4.QtCore import *

# testplaylist "https://www.youtube.com/watch?v=4GFJbkCzDzc&list=PLUQS0IH7pX5QVCgrlYvFbejySmDKkS6WQ"
class download_playlist_thread(QThread):

    def __init__(self,start_no,end_no,out_dir,url):
        QThread.__init__(self)
        self.start_no=start_no
        self.end_no=end_no
        self.out_dir=out_dir
        self.url=url

    def __del__(self):
        self.wait()

    def run(self):
        self.downloadPlaylist()

    def my_hook(self,d):
        if d['status']== "downloading":
            downloadedB= int(d['downloaded_bytes'])
            totalB=int(d['total_bytes'])
            percent_download=downloadedB*100/totalB
            while percent_download<100:
                downloadedB= int(d['downloaded_bytes'])
                totalB=int(d['total_bytes'])
                percent_download=downloadedB*100/totalB
                percent_download=str(percent_download)
                try:
                    speed=d['speed']
                    if speed>1000 and speed<10**6:
                        speed/=1024
                        speed=int(speed * 10**2)/10.0**2
                        speed=str(speed)+" Kib/s"
                    else:
                        speed/=1024*10**3
                        speed=str(speed)+" Mib/s"
                        speed=int(speed * 10**2)/10.0**2

                    eta=str(d["eta"]/3600)+":"+str(d['eta']/60)+":"+str(d['eta']%60)
                    status="Downloading "+str(d['filename'])+" at "+speed+" ETA: "+eta
                    self.emit(SIGNAL('status_value(QString)'),status)
                except:
                    status="Downloading "+str(d['filename'])
                    self.emit(SIGNAL('status_value(QString)'),status)

                self.emit(SIGNAL('progress_value(QString)'), percent_download)


        if d['status'] == 'finished':
            self.emit(SIGNAL('finished()'), )

    def downloadPlaylist(self):

        ydl_opts = {
            'playliststart':self.start_no,
            'playlistend':self.end_no,
            #'restrictfilenames':True,
            'outtmpl':self.out_dir+"\\%(title)s.%(ext)s",
            'format': "best",
            'noplaylist' : False,
            'progress_hooks': [self.my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
