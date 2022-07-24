from pytube import YouTube
import PySimpleGUI as Sg
import pymsgbox as kd

Sg.theme('DarkAmber')
# All the stuff inside your window.
layout = [[Sg.Text('YT DOWNLOADER :D')],
          [Sg.Checkbox('Are You Sure?', key='sure', default=False)],
          [Sg.FolderBrowse(key='Lod')],
          [Sg.InputText('', key='link')],
          [Sg.Button('DOWNLOAD'), Sg.Button('Quit')],
          [Sg.Text(size=(0, 1), key='telk')]
          ]
window = Sg.Window('papinioo yt downloader', layout, no_titlebar=True)
while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED or event == 'Quit':  # if user closes window or clicks cancel
        window.close()
        break
    if event == Sg.WIN_CLOSED or event == 'DOWNLOAD' and values['link'] != "":
        yt = YouTube(values['link'])
        print(yt.views, yt.title, yt.author)
        name = yt.views, yt.title, yt.author
        window['telk'].update(value=name)
        window.refresh()
        yt.streams.filter(progressive=True, res="720p", file_extension='mp4')\
            .order_by('resolution').desc().first().download(values['Lod'])
        kd.alert(text="DOWNLOADED", title='Downloaded', button='OK')
