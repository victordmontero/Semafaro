import tkinter as tk
from time import sleep;

class Semafaro(object):
	CUENTATOTAL = 120
	MINIMO = 30
	def __init__(self,cuenta,imgVerde,imgRojo):
		self.contador = cuenta
		self.verde = imgVerde
		self.rojo = imgRojo
		self.actual = imgRojo

	def Comprobar(self):
		if self.cuenta < self.MINIMO:
			self.actual = self.verde
		else:
			self.actual = self.rojo

class App(tk.Frame):
	"""docstring for App"""
	def __init__(self, master=None):
		super(App, self).__init__()
		self.corriendo = True
		self.crearBarra()
		self.canvas = tk.Canvas(master)
		self.canvas.grid(row=1,column=0,sticky=tk.W+tk.E)
		self.crearComponentes()
		self.actualizar()

	def crearComponentes(self):
		self.semafarosImg = [tk.PhotoImage(file="gfx/SemVerde.gif"),
							 tk.PhotoImage(file="gfx/SemRojo.gif")]
		print(self.canvas.winfo_width())
		self.canvas.create_image(19,120,image=self.semafarosImg[0],tags="W")
		self.canvas.create_image(360,120,image=self.semafarosImg[1],tags="E")
		self.canvas.create_image(190, 50, image=self.semafarosImg[1],tags="N")
		self.canvas.create_image(190, 220, image=self.semafarosImg[1],tags="S")

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
		self.canvas.after(1000,self.actualizar)

	def cambiarSemafaro(self):
		Semafaros = [self.canvas.coords("N"),
					 self.canvas.coords("S"),
					 self.canvas.coords("W"),
					 self.canvas.coords("E")]

	def onClick(self,e):
		print(self.corriendo)
		self.corriendo = not self.corriendo


app = App()
app.master.title("Emulador de Semafaro")
app.mainloop()
