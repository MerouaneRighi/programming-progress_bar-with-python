from tkinter import *
from tkinter import ttk
import time
root =Tk()
root.title('Merouane.com')
#sroot.iconbitmap()
root.geometry("600x400")
def stop():
    my_progress.stop()
def start():
    #my_progress["value"] +=20
    my_progress.start()
my_progress=ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
my_progress.pack(pady=20)

my_button= Button(root,text="Stop",command=stop)
my_button.pack(pady=10)
#button

    
my_button= Button(root,text="Start",command=start)
my_button.pack(pady=10)
root.mainloop()
#chan https://youtu.be/Grbx15jRjQA
