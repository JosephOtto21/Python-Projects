import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from tkinter.filedialog import askdirectory
import urllib.request
import os
from pytube import YouTube
import threading

#Window propieties
root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('540x110')
root.resizable(0,0)

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()

wventana = 540
hventana = 110

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()

pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#Funcionalidades
dir_actual = os.getcwd()

global text_info

def browse():
	path_entry.delete(0, "end")
	filename = askdirectory()
	path_entry.insert(0, filename)

def mp4(url):
	yt = YouTube(url)

	stream = yt.streams.filter().get_highest_resolution()

	destination = path_entry.get()

	out_file = stream.download(output_path=destination)

def mp3(url):
	yt = YouTube(url)

	stream = yt.streams.filter(only_audio=True).first()

	destination = path_entry.get()

	out_file = stream.download(output_path=destination)

	base, ext = os.path.splitext(out_file)

	new_file = base + '.mp3'

	os.rename(out_file, new_file)

def limpiar_entry():
	url_entry.delete(0, "end")

def limpiar_text():
	text_info.config(text="")

def descargar():
	url_page = url_entry.get()
	comprobar(url_page)

	if valor == True :
		if len(path_entry.get()) > 0:
			if options.get() == "MP3":
				mp3(url_entry.get())
				limpiar_entry()
				text_info.config(text="Descarga Finalizada")
				timer = threading.Timer(3, limpiar_text)
				timer.start()
			elif options.get() == "MP4":
				mp4(url_entry.get())
				limpiar_entry()
				text_info.config(text="Descarga Finalizada")
				timer = threading.Timer(3, limpiar_text)
				timer.start()
			else:
				text_info.config(text="Añade una extensión")
				timer = threading.Timer(2, limpiar_text)
				timer.start()
		else:
			text_info.config(text="Añade una ruta")
			timer = threading.Timer(2, limpiar_text)
			timer.start()
	else:
		text_info.config(text="Añade una url válida")
		timer = threading.Timer(2, limpiar_text)
		timer.start()

def comprobar(url):
	global valor

	if url[0:32] == "https://www.youtube.com/watch?v=":
		try:
			response = urllib.request.urlopen(url)
			if len(response.read()) > 0:
				valor = True
		except:
			valor = False
	else:
		valor = False

#Primera fila

url_text = tk.Label(root, text="URL:")
url_text.grid(padx=5, row=0, column=0, pady=5)

url_entry = tk.Entry(root)
url_entry.grid(padx=5, row=0, column=1, ipadx=100, pady=5)

options = ttk.Combobox(root, state="readonly", values=["MP3", "MP4"], width=10)
options.grid(row=0, column=2, padx=5, pady=5)

#Segunda fila

path_text = tk.Label(root, text="Path:")
path_text.grid(padx=5, row=1, column=0, pady=5)

path_entry = tk.Entry(root, state="normal")
path_entry.insert(0, dir_actual)
path_entry.grid(padx=5, row=1, column=1, ipadx=100, pady=5)

browse = tk.Button(root, text="Browse", width=9, command=browse)
browse.grid(row=1, column=2, padx=5, pady=5)

#Tercera fila
text_info = tk.Label(root, text="")
text_info.grid(padx=5, row=2, column=0, columnspan=2, sticky = "W")

descargar = tk.Button(root, text= 'Descargar', width=9, command=descargar)
descargar.grid(row=2, column=2)

root.mainloop()	
 
