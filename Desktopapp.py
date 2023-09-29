
import tkinter as tk
import tkinter.messagebox
from pytube import YouTube


def dload():
    try:
        data = text_input.get()
        clip = YouTube(data)
        mp4 = clip.streams.get_highest_resolution()
        mp4.download('Video/')
        tkinter.messagebox.showinfo('Done','Succesfully downloaded in folder "Video" :D')
    except:
        tkinter.messagebox.showinfo('Error','Paste the goddamn URL!')
    

window=tk.Tk()                         
window.title('MyProgram :D')
window.minsize(width=150,height=100)

title_label =tk.Label(window, text="Youtube URL", fg='red', font=20)
title_label.pack()

text_input=tk.Entry(window)
text_input.pack()

ok_button=tk.Button(window,text='download',command=dload, fg='green')
ok_button.pack()

window.mainloop()