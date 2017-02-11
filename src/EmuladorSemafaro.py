#!/usr/bin/env python

import tkinter as tk
from termcolor import *;
import colorama;
from time import sleep;
colorama.init();

class Semafaro(object):
    def __init__(self,Semafaros,DurTotal=120,vel=0.1,callback=None,callback2=None):
        self.Ss = Semafaros
        self.DURACION_TOTAL = DurTotal
        self.parado = False
        self.velocidad = vel
        self.dibujarSemafaro=callback
        self.CambiarSemafaro=callback2

    def CambiarSemafaro(self,sem,offset):
        for i in range(len(sem)):
            if(sem[i] <= 0):
                sem[i] = offset;
            else:
                sem[i] = sem[i] - 1;
            print(sem[i])
    
    def Imprimir(self,S):
        if(S < 10):
            cprint(S,"green");
        else:
            cprint(S,"red");

    def IniciarEmulacion(self,parar):
        while (not parar):
            for i in range(len(self.Ss)):
               self.Ss[i] = self.CambiarSemafaro(self.Ss[i],self.DURACION_TOTAL);
               self.dibujarSemafaro(self.Ss[i])
               #self.Imprimir(self.Ss[i])
            sleep(self.velocidad);


class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.crearComponentes(master)
        self.lienzo
        self.btnPausar
        self.crearSemafaros()

    def crearComponentes(self,master):
        top = tk.Frame(master)
        top.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        imgParar = tk.PhotoImage(file="../gfx/stopn.gif")
        self.btnPausar = tk.Button(top,image=imgParar)
        self.btnPausar.image = imgParar
        self.btnPausar.grid()
        self.btnPausar.bind('<Button-1>',self.onClick)
        self.btnPausar.bind('<ButtonRelease-1>',self.onClick)
        self.lienzo = tk.Canvas(top)
        self.lienzo.grid(row=1,column=0,columnspan=3)

    def actualizar(self,semafaro):
        if(semafaro < 30):
            print(str(semafaro)+" V")
        else:
            print(str(semafaro)+" R")
        
    def crearSemafaros(self):
        imgParar = tk.PhotoImage(file="../gfx/stopn.gif")
        self.semafaro = Semafaro([30,60,90,120],120,0.1,callback=self.actualizar)
        self.lienzo.create_image(5,5,image=imgParar)
        self.lienzo.grid(row=1,column=0,columnspan=3)
        self.after(100 ,self.semafaro.CambiarSemafaro,self.semafaro.Ss,self.semafaro.DURACION_TOTAL)

    def onClick(self,event):
        self.semafaro.IniciarEmulacion(False)
        print(event.type)
        


app = Application()
app.master.title('Emulador de Semafaro')
app.mainloop()
