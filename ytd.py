'''
Author - Pasindu Marasinghe
pasindugayanthe@gmail.com

------------------
YouTube Downloader
------------------
'''


from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog


DOWN_PATH = ""

#function for the file location
def FileLocation():
    global DOWN_PATH
    DOWN_PATH = filedialog.askdirectory()

    if(len(DOWN_PATH) > 0):
        path_msg.config(text=DOWN_PATH,fg="black")
    else:
        path_msg.config(text="Please Choose Path",fg="red")


#function to download the video
def DownloadVideo():
    down_msg.config(text="")
    choice = choices.get()
    url = entry.get()


    if(len(url)>0):
        yt = YouTube(url)#this is the video

        if(choice == quality[0]):#144p
            select = yt.streams.get_by_itag(160)
        elif(choice == quality[1]):#240p
            select = yt.streams.get_by_itag(133)
        elif(choice == quality[2]):#360p
            select = yt.streams.get_by_itag(18)
        elif(choice == quality[3]):#480p
            select = yt.streams.get_by_itag(135)
        elif(choice == quality[4]):#720p
            select = yt.streams.get_by_itag(22)
        elif(choice == quality[5]):#1080p
            select = yt.streams.get_by_itag(137)
        else:
           down_msg.config(text="\nError!!\nTry Again",fg="red")
           return

    #download
    select.download(DOWN_PATH)
    down_msg.config(text="Download Complete",fg="black")

'''
link = "https://www.youtube.com/watch?v=7rNsPJHnvS0"

video = YouTube(link)
for s in video.streams:
    print(s)
'''

#GUI

root = Tk() #creating an instance of tkinker
root.title("DownTube") #title
root.geometry("700x400") #window size
root.columnconfigure(0,weight=1) #set all of the content in the center

#Download Link Label
enter_url_label = Label(root,text="\nEnter the URL",font=("helvetica",16))
enter_url_label.grid()

#Download Url Input Box
entry_url = StringVar()
entry = Entry(root,width=60,textvariable=entry_url)
entry.grid()


#File Path Label
enter_url_label = Label(root,text="\nChoose The Path to Download",font=("helvetica",16))
enter_url_label.grid()

#Choose Path Button
path_button = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=FileLocation)
path_button.grid()

#Path Message - Stating whether the pass is correct or else peint an error message
path_msg = Label(root,text="",fg="black",font=("helvetica",12))
path_msg.grid() #check whether it is possible to show/hide the path message

#Select Download Quality
down_quality = Label(root,text="\nSelect Download Quality",font=("helvetica",16))
down_quality.grid()

#Choices for the dropdown box
quality = ["144p","240p","360p","480p","720p","1080p"]
choices = ttk.Combobox(root,values=quality)
choices.grid()


#Download Button
down_button = Button(root,width=10,bg="red",fg="white",text="Download",command=DownloadVideo)
down_button.grid()

down_msg = Label(root,text="",fg="black",font=("helvetica",12))
down_msg.grid()


#display the GUI
root.mainloop()

