from moviepy.editor import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import imageio
import os

def selectfile():
    try:
        if(clicked.get() == 'mp3'):
            filename = fd.askopenfilename(initialdir="/", title="Select File to convert", filetypes=(("Mp4 Files", "*.mp4"),))
        elif(clicked.get() == 'gif'):
            filename = fd.askopenfilename(initialdir="/", title="Select File to convert", filetypes=(("Mp4 Files", "*.mp4"), ("AVI Files", "*.avi"),))
        mp4_file_entry.delete(0, "end")
        mp4_file_entry.insert(0, filename)
    except AttributeError:
        pass

def convertMP3():
    mp4_file = mp4_file_entry.get()
    if(clicked.get() == 'mp3'):
        #this line changes the extension of the file in the path from mp4 to mp3
        mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
        #these lines use the moviepy library to convert the given mp4 file to mp3
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
        messagebox.showinfo('Success', 'Conversion Done')
    elif(clicked.get() == 'gif'):
        #we use the imageio library to convert an mp4 or AVI file to gif as it is comparatively faster than moviepy, moviepy also as a function to convert mp4 into gifs.
        outputfile = os.path.splitext(mp4_file)[0] + ".gif"
        reader = imageio.get_reader(mp4_file)
        fps = reader.get_meta_data()['fps']
        writer = imageio.get_writer(outputfile, fps=fps)
        for i,im in enumerate(reader):
            writer.append_data(im)
        writer.close()
        messagebox.showinfo('Success', 'Conversion Done')

converter = tk.Tk()
converter.title("Converter")
converter.geometry("350x180")
converter.config(bg = "#ffffff")

options = ['mp3', 'gif', 'mp3']
clicked = tk.StringVar()
clicked.set('mp3')

s = ttk.Style()
s.configure('TLabel', background='#ffffff')

ttk.Label(converter, text="Converter", padding=10, font=('Helvetica', 24), style="TLabel").grid(column=0, row=0, columnspan = 3)
converter.columnconfigure(0, weight = 1)
converter.rowconfigure(0, weight = 1)

ttk.Label(converter, text="Select File", padding=10, font=('Helvetica', 14), style="TLabel").grid(column=0, row=1, sticky=tk.W)

mp4_file_entry = ttk.Entry(converter)
mp4_file_entry.grid(column = 1, row = 1, padx=10, sticky=tk.W)

ttk.Button(converter, text = "Select", cursor="hand2", command = selectfile).grid(column = 2, row = 1, sticky=tk.W, padx=(0,10))

ttk.Label(converter, text="Convert to ", padding=10, font=('Helvetica', 14), style="TLabel").grid(column=0, row=2, sticky=tk.W)

ttk.OptionMenu(converter, clicked, *options).grid(column=1, row=2, sticky=tk.W+tk.E, padx=10)

ttk.Button(converter, text = "Convert", cursor="hand2", command = convertMP3).grid(column = 2, row = 2, sticky=tk.W, padx=(0,10))

converter.mainloop()
