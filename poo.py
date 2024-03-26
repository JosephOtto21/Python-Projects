import tkinter as tk
from tkinter import ttk
import time
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444

class qqtimer:
	def __init__(self, root):
		self.root = root
		self.root_propieties()
		self.ventana_centrada()
		self.styles()
		
		#Frames
		self.frame_sup()
		self.frame_medium()
		self.frame_timer()		
		self.frame_times()
		self.frame_data()

		#Timer
		self.root.bind('<KeyPress>', self.tecla_presionada)
		self.combo_sup.bind('<<ComboboxSelected>>', self.select_scramble)

		#Times
		self.entry_texts = []
		self.buttons = []
		self.num_rows = 1
		self.num_cols = 0

	def create_widgets(self):
		self.entry = tk.Entry(self)
		self.entry.place(x=10, y=10, width=100, height=25)

		self.add_button = tk.Button(self, text="Add Button", command=self.add_button)
		self.add_button.place(x=120, y=10, width=100, height=25)

	def add_button(self, term):
		entry_text = term
		self.entry_texts.append(entry_text)

		new_button = tk.Button(frame_times, text=entry_text)
		new_button.place(x=self.num_cols*110, y=self.num_rows*40 + 40, width=100, height=25)
		self.buttons.append(new_button)

		self.num_cols += 1
		if self.num_cols > 3:
			self.num_cols = 0
			self.num_rows += 1

	def update_buttons_text(self, *args):
		for i, button in enumerate(self.buttons):
			button.config(text=self.entry_texts[i])

	def root_propieties(self):
		self.root.title('qqtimer')
		self.root.configure(bg='black')
		self.root.geometry('1366x768')
		self.root.resizable(0,0)

	def ventana_centrada(self):
		wtotal = self.root.winfo_screenwidth()
		htotal = self.root.winfo_screenheight()

		wventana = 1366
		hventana = 768

		pwidth = round(wtotal/2-wventana/2)
		pheight = round(htotal/2-hventana/2)

		self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

	def styles(self):
		self.style = ttk.Style()
		self.style.configure('Green.TFrame', background='#00ff00')
		self.style.configure('White.TFrame', background='white')
		self.style.configure('label1.TLabel', fg='black', font=('Arial', 12), background='#00ff00')
		self.style.configure('label2.TLabel', fg='black', font=('Arial', 12), background='white')
		self.style.configure('label3.TLabel', fg='black', font=('Arial', 60), background='white')
		self.style.configure('button1.TButton', borderwidth=0, background='white', foreground='blue', font=('Arial', 12))
		self.style.configure('button2.TButton', background='white', foreground='black', font=('Arial', 10))

	def frame_sup(self):
		self.frame_sup = ttk.Frame(self.root, width=1360, height=40, style='Green.TFrame')
		self.frame_sup.grid(row=0, column=0, columnspan=3, pady=5, padx=2)

		self.text_type = ttk.Label(self.frame_sup, text='Scramble type:', style='label1.TLabel')
		self.text_type.place(x=16, y=11)

		self.combo_sup = ttk.Combobox(self.frame_sup, state="readonly", values=['2x2x2', '3x3x3'], width=25)
		self.combo_sup.set('3x3x3')
		self.combo_sup.place(x=140, y=11)

		self.combo_state = ttk.Combobox(self.frame_sup, state="readonly", values=['random state'], width=25)
		self.combo_state.set('random state')
		self.combo_state.place(x=340, y=11)

	def frame_medium(self):
		scramble = scrambler333.get_WCA_scramble()
		
		self.frame_medium = ttk.Frame(self.root, width=1360, height=40, style='White.TFrame')
		self.frame_medium.grid(row=1, column=0, columnspan=3)

		self.text_scramble = ttk.Label(self.frame_medium, text=f"scramble: {scramble}", style='label2.TLabel')
		self.text_scramble.place(x=16, y=11)

	def frame_timer(self):
		self.frame_timer = ttk.Frame(self.root, width=765, height=670, style='White.TFrame')
		self.frame_timer.grid(row=2, column=0, padx=2, pady=5)

		self.text_timer = ttk.Label(self.frame_timer, text="Ready!", style='label3.TLabel')
		self.text_timer.place(x=260, y=250)
	
		self.tiempo_transcurrido = 0
		self.corriendo = False

	def frame_times(self):
		self.frame_times = ttk.Frame(self.root, width=290, height=670, style='White.TFrame')
		self.frame_times.grid(row=2, column=1, pady=5)

		self.timesoption_text = ttk.Label(self.frame_times, text="times(           ,              ):", style='label2.TLabel')
		self.timesoption_text.place(x=10, y=10)

		self.reset_button = ttk.Button(self.frame_times, text="reset", width=4, style='button1.TButton')
		self.reset_button.place(x=55, y=7)

		self.reset_button = ttk.Button(self.frame_times, text="import", width=5, style='button1.TButton')
		self.reset_button.place(x=105, y=7)

	def frame_data(self):	
		self.frame_data = ttk.Frame(self.root, width=290, height=670, style="White.TFrame")
		self.frame_data.grid(row=2, column=2, padx=2, pady=5)
		
		self.stats_text = ttk.Label(self.frame_data, text="stats: (           )", style='label2.TLabel')
		self.stats_text.place(x=10, y=10)

		self.state_button = ttk.Button(self.frame_data, text="hide", width=4, style='button1.TButton')
		self.state_button.place(x=60, y=7)

		self.ntimes_text = ttk.Label(self.frame_data, text="number of times: 0/0", style='label2.TLabel')
		self.ntimes_text.place(x=10, y=40)

		self.btime_text = ttk.Label(self.frame_data, text="best time: ", style='label2.TLabel')
		self.btime_text.place(x=10, y=70)
		
		self.wtime_text = ttk.Label(self.frame_data, text="worst time: ", style='label2.TLabel')
		self.wtime_text.place(x=10, y=100)

		self.savg_text = ttk.Label(self.frame_data, text="session avg: ", style='label2.TLabel')
		self.savg_text.place(x=10, y=160)
	
		self.savg_text = ttk.Label(self.frame_data, text="session mean: ", style='label2.TLabel')
		self.savg_text.place(x=10, y=190)

	def formato(self, tiempo):
		minutos = int(tiempo // 60)
		segundos = int(tiempo % 60)
		milisegundos = int((tiempo - int(tiempo)) * 1000)

		if minutos < 1:
			if segundos < 10:
				time =  "{:01d}.{:03d}".format(segundos, milisegundos)
			else:
				time = "{:01d}.{:03d}".format(segundos, milisegundos)
		else:
			time = "{:02d}:{:02d}.{:03d}".format(minutos, segundos, milisegundos)
		
	def select_scramble(self, event):
		seleccion = self.combo_sup.get()
		if seleccion == '2x2x2':
			scramble = scrambler222.get_WCA_scramble()
		elif seleccion == '3x3x3':
			scramble = scrambler333.get_WCA_scramble()

		self.text_scramble.config(text=f"scramble: {scramble}")

	def reset_scramble(self):
		seleccion = self.combo_sup.get()
		if seleccion == '2x2x2':
			scramble = scrambler222.get_WCA_scramble()
		elif seleccion == '3x3x3':
			scramble = scrambler333.get_WCA_scramble()

		self.text_scramble.config(text=f"scramble: {scramble}")

	def iniciar_cronometro(self):
		self.corriendo = True
		self.tiempo_inicio = time.time()
		self.actualizar_tiempo()

	def detener_cronometro(self):
		self.corriendo = False

	def actualizar_tiempo(self):
		if self.corriendo:
			self.tiempo_transcurrido = time.time() - self.tiempo_inicio
		tiempo_formateado = self.formatear_tiempo(self.tiempo_transcurrido)
		self.text_timer.config(text=tiempo_formateado)
		if self.corriendo:
			self.root.after(10, self.actualizar_tiempo)  # Actualizar cada 10 milisegundos

	def formatear_tiempo(self, tiempo):
		minutos = int(tiempo // 60)
		segundos = int(tiempo % 60)
		milisegundos = int((tiempo - int(tiempo)) * 1000)

		if minutos < 1:
			if segundos < 10:
				return "{:01d}.{:03d}".format(segundos, milisegundos)
			else:
				self.text_timer.place(x=240, y=250)
				return "{:01d}.{:03d}".format(segundos, milisegundos)
		else:
			self.text_timer.place(x=230, y=300)
			return "{:02d}:{:02d}.{:03d}".format(minutos, segundos, milisegundos)

	def tecla_presionada(self, evento):
		if evento.char == ' ':
			if self.corriendo:
				self.detener_cronometro()
				self.reset_scramble()
			else:
				self.iniciar_cronometro()

root = tk.Tk()
app = qqtimer(root)
root.mainloop()
