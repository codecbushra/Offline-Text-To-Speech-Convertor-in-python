from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
import pyttsx3
    

def play():
    engine=pyttsx3.init()
    audioStr=text.get('0.0',END)
    if audioStr:
        engine.say(audioStr)
        engine.runAndWait()
        engine.stop()


def saveAudioFile():
    engine=pyttsx3.init()
    audioStr=text.get('0.0',END)
    if audioStr:
        engine.save_to_file(audioStr,'Audio.mp3')
        engine.runAndWait()
        engine.stop()
        showinfo('Python says','Your audio file is saved!')



root=Tk()
root.title('Text To Speech Convertor')
root.resizable(0,0)
titlelabel=Label(root,font='Helvetica 20 bold italic',text="Offline Text To Speech Convertor",fg='crimson').grid(row=0,columnspan=3)
# titlelabel.pack()
root.configure(bg='white')

text = ScrolledText(root,width=50,height=20,wrap=WORD,padx=10,pady=10,bd=5,relief=RIDGE)
text.grid(row=1,columnspan=3)

ttk.Button(root,text='Play',width=7,command=play).grid(row=3,column=0,ipadx=2)
ttk.Button(root,text='Clear',width=7,command=lambda:text.delete('0.0',END)).grid(row=3,column=1,ipadx=2)
ttk.Button(root,text='Save',width=7,command=saveAudioFile).grid(row=3,column=2,ipadx=2)





root.mainloop()
