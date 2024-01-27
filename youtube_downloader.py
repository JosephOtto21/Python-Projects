from pytube import YouTube
import os

class instalador:
	def __init__(self, url):
		self.url = url

	def mp4(self):
		self.yt = YouTube(self.url)

		self.stream = self.yt.streams.get_highest_resolution()

		self.destination = '.'

		self.out_file = self.stream.download(output_path=self.destination)

		print('Downloaded')
		print('Enter new option')

	def mp3(self):
		self.yt = YouTube(self.url)

		self.stream = self.yt.streams.filter(only_audio=True).first()

		self.destination = '.'

		self.out_file = self.stream.download(output_path=self.destination)

		print('Downloaded')
		print('Enter new option')

		self.base, self.ext = os.path.splitext(self.out_file) 

		self.new_file = self.base + '.mp3'

		os.rename(self.out_file, self.new_file) 

def Main():

	print(''' \033[91m
  __     __      _______    _                              
  \ \   / /     |__   __|  | |                             
   \ \_/ /__  _   _| |_   _| |__   ___                     
    \   / _ \| | | | | | | | '_ \ / _ \                    
     | | (_) | |_| | | |_| | |_) |  __/                    
     |_|\___/ \__,_|_|\__,_|_.__/ \___|                    
       _                     _                 _           
      | |                   | |               | |          
    __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
   \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
     ''')

	print('[1] Download MP4')
	print('[2] Download MP3')
	print('[3] List Directory')
	print('[4] Exit')

	while True:
		try:
			option = int(input('>> '))
		except ValueError:
			print('Incorrect option')
		else:
			if option == 1:
				print('Ingresa URL')
				video = instalador(str(input('>> ')))
				video.mp4()
			elif option == 2:
				print('Ingresa URL')
				video = instalador(str(input('>> ')))
				video.mp3()
			elif option == 3:
				print(os.listdir('.'))
			elif option == 4:
				break
			else:
				print('Incorrect option')

if __name__ == '__main__':
	Main()
