#setup Screen 
from tkinter import *
from PIL import Image,ImageTk 
import os
import time
import tkinter.messagebox
from pygame import mixer
from tkinter import filedialog
from mutagen.mp3 import MP3 #for song length, agr koi error show ho tou(terminal pay ja kar pip install mutagen ki command run karne hai)
mixer.init()

class musicplayer:
    def __init__(self,Tk): #yei function khud he run ho ga..
        self.root=Tk
        self.root.title('Music_Player')
        #width and height
        self.root.geometry('450x400')
        #background color
        self.root.configure(background='white')


        #openfile
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()


        #Menu
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        #Submenu
        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)

        #For Message
        def About():
            tkinter.messagebox.showinfo('About Us','Audio player created by Adil Sial')


        #Submenu 2
        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.submenu2)
        self.submenu2.add_command(label='About',command=About)


        #Adding Label
        self.filelabel=Label(text='Audio Player In Python',bg='black',fg='white',font=10)
        self.filelabel.place(x=20,y=50)

        def Songinfo():
            self.filelabel['text']='Current Music :-' + os.path.basename(filename)


        #Adding leftimage
        #L=left
        self.L_photo=ImageTk.PhotoImage(file='sound effect.jpeg')
        L_photo=Label(self.root,image=self.L_photo,bg='white').place(x=180,y=45,width=200,height=250)
        #Adding image
        self.photo=ImageTk.PhotoImage(file='Music.jpeg')
        photo=Label(self.root,image=self.photo,bg='white').place(x=30, y=100)

        #label
        self.label1=Label(self.root,text="Lets Play It",bg='black',fg='white',font=20)
        self.label1.pack(side=BOTTOM,fill=X)


        #for Song length
        def length_bar():
            #starting from zero
            current_time=mixer.music.get_pos()/1000
            #convert current time in min and second....
            convert_current_time=time.strftime('%M:%S',time.gmtime(current_time))
        

            #select Mp3 song
            song_mut=MP3(filename)
            #get length of the songs
            song_mut_length=song_mut.info.length
            #convert into min. and sec.
            convert_song_mut_length=time.strftime('%M:%S',time.gmtime(song_mut_length))
            #blit on screen 
            self.lengthbar.config(text=f'Total_length:-{convert_current_time}:{convert_song_mut_length}')
            self.lengthbar.after(1000,length_bar)
            #print(convert_song_mut_length)

        #label for length bar
        self.lengthbar=Label(self.root,text='Total_length:-00:00',font=15,bg='black',fg='white')
        self.lengthbar.place(x=10,y=220)



        #creating button

        #functions
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='Music_Playing..'
                    Songinfo()
                    length_bar()
                except:
                    tkinter.messagebox.showerror('Error','File could not found, Please try again later')
            else:
                mixer.music.unpause()
                self.label1['text']='Music_Unpause'

        #play button
        self.photo_B1=ImageTk.PhotoImage(file='play.jpeg')
        photo_B1=Button(self.root,image=self.photo_B1,bd=0,bg='white',command=playmusic).place(x=20,y=250)


        #function for stop button 
        
        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='Music_paused'


        #pause button
        self.photo_B2=ImageTk.PhotoImage(file='pause.jpeg')
        photo_B2=Button(self.root,image=self.photo_B2,bd=0,bg='white',command=pausemusic).place(x=80,y=250)
        
        #function for stop button 
        def stopmusic():
            mixer.music.stop()
            self.label1['text']='Music_stopped'

        
        #stop button
        self.photo_B3=ImageTk.PhotoImage(file='stop.jpeg')
        photo_B3=Button(self.root,image=self.photo_B3,bd=0,bg='white',command=stopmusic).place(x=140,y=250)
        
        #mute
        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='Mute.jpeg')
            mute=Button(self.root,image=self.mute,bg='white',bd=0,command=unmute).place(x=230,y=255)
            self.label1['text']='Music_mute'


        #unmute
        def unmute():
            self.scale.set(50)
            self.volimg=ImageTk.PhotoImage(file='volume.jpeg')
            volimg=Button(self.root,image=self.volimg,bg='white',bd=0,command=mute).place(x=230,y=255)
            self.label1['text']='Music_unmute'



        # #volume img
        self.volimg=ImageTk.PhotoImage(file='volume.jpeg')
        volimg=Button(self.root,image=self.volimg,bg='white',bd=0,command=mute).place(x=230,y=255)


        #function for volume bar
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)


        #Volume bar 
        self.scale=Scale(self.root,from_=0, to=100,bg='cyan',orient=HORIZONTAL,length=120,command=volume)
        self.scale.set(25)
        self.scale.place(x=280,y=260)
        
        


root=Tk()
obj=musicplayer(root)
root.mainloop()