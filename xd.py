import tkinter as tk

class MatrizEscalableGUI:
	def __init__(self, root):
		self.root = root
		self.matriz = []
		self.columnas_max = 4
        
		self.frame = tk.Frame(self.root)
		self.frame.pack()
        
		self.entry = tk.Entry(self.frame)
		self.entry.pack(side="left")
        
		self.agregar_button = tk.Button(self.frame, text="Agregar", command=self.agregar_elemento)
		self.agregar_button.pack(side="left")
        
		self.matriz_frame = tk.Frame(self.root)
		self.matriz_frame.pack()
        
	def agregar_elemento(self):
		elemento = self.entry.get()
		if not self.matriz or len(self.matriz[-1]) == self.columnas_max:
			self.matriz.append([])
        
		self.matriz[-1].append(elemento)
		self.actualizar_matriz()
    
	def actualizar_matriz(self):
		for widget in self.matriz_frame.winfo_children():
			widget.destroy()
        
		for fila in self.matriz:
			for elemento in fila:
				label = tk.Label(self.matriz_frame, text=elemento, borderwidth=1, relief="solid")
				label.grid(sticky="nsew")
        
		self.matriz_frame.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
	root = tk.Tk()
	app = MatrizEscalableGUI(root)
	root.mainloop()
