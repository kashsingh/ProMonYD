from __future__ import unicode_literals
import youtube_dl


def extractor(url):
    #testURL="http://www.youtube.com/watch?v=BaW_jenozKc"
    #int(15.55555 * 10**2) / 10.0**2 usage for getting precison upto 2 decimal places
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(url,download=False)

    format_list=[]
    for d in info['formats']:
        format=d['format']
        ext = str(d['ext'])
        try:
            abr = str(d['abr'])
            try:
                filesize=d['filesize']/1024.0
                if filesize>1000.0:
                    filesize/=1000
                    filesize=int(filesize * 10**2)/10.0**2
                    format_list.append(format+u", "+ext+u"@"+abr+u"k audio"+", "+str(filesize)+"Mb")
                else:
                   filesize=int(filesize * 10**2)/10.0**2
                   format_list.append(format+u", "+ext+u"@"+abr+u"k audio"+", "+str(filesize)+"Kb")
            except:
                format_list.append(format+u", "+ext+u"@"+abr+u"k audio")
        except:
            format_list.append(format+u", "+ext)


    return format_list



