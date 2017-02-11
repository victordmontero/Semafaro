import tkinter as tk
from termcolor import *;
import colorama;
from time import sleep;
colorama.init();

class App(tk.Frame):
	"""docstring for App"""
	def __init__(self, master=None):
		super(App, self).__init__()
		self.canvas = tk.Canvas(master)
		self.canvas.grid(row=1,column=0,sticky=tk.N+tk.S+tk.W+tk.E)
		self.crearComponentes()

	def crearComponentes(self):
		self.imgParar = tk.PhotoImage(file="../gfx/stopn.gif")
		self.canvas.create_image(12,50,image=self.imgParar)

	def crearBarra(self):
		self.barra = tk.Frame(self)
		self.barra.grid()
		self.btnParar = tk.Button(barra,image=self.imgParar)
		self.btnParar.grid()

root = tk.Tk()
app = App(root)
app.master.title = "Emulador de Semafaro"
app.mainloop()
