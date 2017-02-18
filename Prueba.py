import tkinter as tk

class Semafaro(object):
	CUENTATOTAL = 120
	MINIMO = 30
	def __init__(self,t,cuenta,imgVerde,imgRojo,coords):
		self.tag = t
		self.contador = cuenta
		self.verde = imgVerde
		self.rojo = imgRojo
		self.actual = imgRojo
		self.Coords = coords

	def Comprobar(self):
		if self.contador > 0:
			if self.contador < self.MINIMO:
				self.actual = self.verde
			else:
				self.actual = self.rojo
		else:
			self.contador = self.CUENTATOTAL

class App(tk.Frame):
	"""docstring for App"""
	def __init__(self, master=None):
		super(App, self).__init__()
		self.corriendo = True
		self.semafarosImg = [tk.PhotoImage(file="gfx/SemVerde.gif"),
							 tk.PhotoImage(file="gfx/SemRojo.gif")]
		self.crearBarra()
		self.canvas = tk.Canvas(master)
		self.canvas.grid(row=1,column=0,sticky=tk.W+tk.E)
		self.semafaros = [Semafaro("W",30,self.semafarosImg[0],self.semafarosImg[1],(19,120)),
						  Semafaro("E",90,self.semafarosImg[0],self.semafarosImg[1],(360,120)),
						  Semafaro("N",60, self.semafarosImg[0], self.semafarosImg[1],(190,50)),
						  Semafaro("S",120, self.semafarosImg[0], self.semafarosImg[1],(190,220))]
		self.crearComponentes()
		self.actualizar()

	def crearComponentes(self):
		print(self.canvas.winfo_width())
		for i in self.semafaros:
			self.canvas.create_image(i.Coords[0],i.Coords[1], image=i.actual, tags=i.tag)

	def crearBarra(self):
		self.barra = tk.Frame(self.winfo_toplevel())
		self.barra.grid(row=0,column=0,sticky=tk.W+tk.E)
		self.imgParar = tk.PhotoImage(file="gfx/stopn.gif")
		self.btnParar = tk.Button(self.barra,image=self.imgParar)
		self.btnParar.grid()
		self.btnParar.bind("<ButtonRelease-1>",self.onClick)

	def actualizar(self):
		if self.corriendo:
			print("Corriendo")
			for s in self.semafaros:
				s.contador = s.contador - 1
				s.Comprobar()
				self.cambiarSemafaro()
				print(s.contador)
		self.canvas.after(1000,self.actualizar)

	def cambiarSemafaro(self):
		for i in self.semafaros:
			self.canvas.create_image(i.Coords[0], i.Coords[1], image=i.actual, tags=i.tag)


	def onClick(self,e):
		self.corriendo = not self.corriendo


app = App()
app.master.title("Emulador de Semafaro")
app.mainloop()
