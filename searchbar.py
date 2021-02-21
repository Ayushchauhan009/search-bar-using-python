from tkinter import *
import webbrowser
root=Tk()
root.title("Search bar")
def seacrh():
    url=entry.get()
    webbrpwser.open(url)
label1=Label(root,text="Enter url here...",font=("arial",15,"bold"))
label1.grid(row=0,column=0)
entry=Entry(root,width=35)
entry.grid(row=0,column=1)
btn=Button(root,text="Search",command=search,bg="blue",fg="white",font=("arial",14,"bold"))
btn.grid(row=1,column=0,columnspan=2,pady=10)
root.mainloop()