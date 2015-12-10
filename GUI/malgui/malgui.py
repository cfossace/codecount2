#Malstor GUI
#Robert Verrone, Christine Fosseseca, Chris Rinchiera

#Imports:
from Tkinter import *
import ttk
import os
import time
from subprocess import call
from tkFileDialog import askdirectory 
import requests
import sys



#Program Specifications:
#window creation
root = Tk()
#Shuts off Resizing.
root.resizable(0,0)
#Program Icon, Can be Changed
img=PhotoImage(file='Lockheed_Martin.png')
root.tk.call('wm','iconphoto',root._w,img)
#ProgramDimensions
root.title("Malstor")
root.geometry("426x308")
root.config(bg="lavender")
app = Frame(root)
app.grid()


global filename
global bucket

#Functions:
#Launch Sever
def runserver():
	#pb is a Progress Bar
	pb=ttk.Progressbar(app,orient=HORIZONTAL,length=420,mode="determinate")
        #pb.grid(row=2,column=0)
	pb["maximum"]=100
	pb["value"]=1
	pb.start
	#Needs Correct File for Crits Server Startup Below
	#os.chdir("../../repos/crits/script")
	pb["value"]=50
        print "start" 
	os.system("python malgui.py")
        print "end"
	#call(["sh", "server_boot"])
	pb["value"]=100
	#Shut Off label update since server doesn't start up just yet.
	serverlabel=Label(app,justify=LEFT,text="Server Up",width=53,foreground="green",bg="lavender",bd=0)
	#serverlabel.grid(row=2,column=0)

#Folder Path Button
def filechoose():
	global filename
	filename=askdirectory()
	print(filename)
	filepathlabel=Label(app,justify=LEFT,text=filename,width=53,foreground="green",bg="lavender",bd=0)
	filepathlabel.grid(row=4,column=0)

#Crits Popup
def popup():
	global bucket
	global c1
	global c2
	global top
	value = StringVar()
	top=Toplevel(app)
	top.config(bg="lavender")
	#top = Frame(root)
	#top.grid()
	c1=IntVar()
	check1=Checkbutton(top,text="Executable",variable=c1,bg="lavender")
	check1.pack()
	#check1.grid(row=0,column=0)
	c2=IntVar()
	check2=Checkbutton(top,text="Metadata",variable=c2,bg="lavender")
	check2.pack()
	#check2.grid(row=1,column=0)
	l=Label(top,text="Enter tags separated by commas: ",bg="lavender")
	l.pack()
	#l.grid(row=2,column=0)
	bucket=Entry(top)
	bucket.pack()
	#bucket.grid(row=3,column=0)
	submitit=Button(top,text='Ok',command=submit,bg="white")
	submitit.pack()
	#submit.grid(row=4,column=0)
	print bucket

def popup2():
	top=Toplevel(app)
	top.config(bg="lavender")
	l=Label(top,text="Please select Executable or Metadata, not both",bg="lavender")
	l.pack()

def popup3():
	top=Toplevel(app)
	top.config(bg="lavender")
	l=Label(top,text="Please select either Executable or Metadata",bg="lavender")
	l.pack()



def submit():
	global bucket
	global c1
	global c2
	if c1.get()==1 and c2.get()==1:
		popup2()
	elif c1.get()==1 and c2.get()==0:
		print("1")
		crits_exec()
	elif c1.get()==0 and c2.get()==1:
		print("2")
		crits_meta()
	else:
		popup3()
	
		
	value=bucket.get()
	top.destroy()
	


#Crits Executable Button
def crits_exec():
	global filename
	global bucket
	#CODE HERE
	#os.system("python samples_gui.py {}".format(filename))
	os.system("python many.py {}".format(filename))
	print ("crits") #Place Holder
	
	#Progress Bar
	pb=ttk.Progressbar(app,orient=HORIZONTAL,length=420,mode="determinate")
        pb.grid(row=6,column=0)
	pb["maximum"]=100
	pb["value"]=1
	pb.start
	pb["value"]=50
	pb["value"]=100
	pb.stop

#Crits Meta Button
def crits_meta():
        global filename
	global bucket
        #CODE HERE
        #os.system("python samples_gui.py {}".format(filename))
        os.system("python meta_many.py {} {}".format(filename, bucket))
        print (bucket) #Place Holder

        #Progress Bar
        pb=ttk.Progressbar(app,orient=HORIZONTAL,length=420,mode="determinate")
        pb.grid(row=6,column=0)
        pb["maximum"]=100
        pb["value"]=1
        pb.start
        pb["value"]=50
        pb["value"]=100
        pb.stop


#Laika Button
def laika():
	global filename
	#CODE HERE
	os.system("python pyscript5.py {}".format(filename))
	print("laika") #Place Holder
	#Progress Bar
	pb=ttk.Progressbar(app,orient=HORIZONTAL,length=420,mode="determinate")
        pb.grid(row=8,column=0)
	pb["maximum"]=100
	pb["value"]=1
	pb.start
	pb["value"]=50
	pb["value"]=100



#Image Declarations:
photo_top = PhotoImage(file='top.png')
image_top = Label(app,image=photo_top,bd=0)
image_top.grid(row=0,column=0)
#photo_lmco = PhotoImage(file='Lockheed_Martin.png')
#photo_vcoe = PhotoImage(file='seal.png')
#photo_waved = PhotoImage(file='waved.png')
#image_waved = Label(app,image=photo_waved,bd=0)
#image_lmco = Label(app,image=photo_lmco)
#image_vcoe = Label(app,image=photo_vcoe)
#image_lmco.grid(row=0,column=0)
#image_vcoe.grid(row=0,column=0)
#image_waved.grid(row=9,column=0)



#Buttons & Labels:
#Launch Server Button
serverbutton = Button(app,justify=LEFT, text = "Launch Server",width=50, command = runserver,bg="white",bd=0)
#serverbutton.grid(row=1,column=0)
#Sever Label
serverlabel=Label(app,justify=LEFT,text="Server Down",width=53,foreground="red",bg="lavender",bd=0)
#serverlabel.grid(row=2,column=0)
#FilePath Button
filepathbutton = Button(app,justify=LEFT, text = "Choose File Path",width=50, command = filechoose, bg="white",bd=0)
filepathbutton.grid(row=3,column=0)
#FilePath Label
filepathlabel=Label(app,justify=LEFT,text="Select a File Path",width=53,foreground="red",bg="lavender",bd=0,)
filepathlabel.grid(row=4,column=0)
#CRITS Button
critsbutton = Button(app,justify=LEFT, text = "Run CRITS",width=50,bg="white",bd=0,command=popup)
critsbutton.grid(row=5,column=0)
#Crits Label
filepathlabel=Label(app,justify=LEFT,text="Awaiting CRITS Analysis",width=53,foreground="red",bg="lavender",bd=0,)
filepathlabel.grid(row=6,column=0)
#LAIKA Button
laikabutton = Button(app,justify=LEFT, text = "Run LaikaBoss",width=50,bg="white",bd=0,command=laika)
laikabutton.grid(row=7,column=0,)
#Laika Label
filepathlabel=Label(app,justify=LEFT,text="Awaiting Laika Analysis",width=53,foreground="red",bg="lavender",bd=0,)
filepathlabel.grid(row=8,column=0)


#Program Startup
root.mainloop()
