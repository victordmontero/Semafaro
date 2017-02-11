from termcolor import *;
import colorama;
from time import sleep;
colorama.init();

class Semafaro(object):
    def __init__(self,Semafaros,DurTotal=120,vel=0.1,callback=None):
        self.Ss = Semafaros
        self.DURACION_TOTAL = DurTotal
        self.parado = False
        self.velocidad = vel
        self.dibujarSemafaro=callback

    def _CambiarSemafaro(self,sem,offset):
        if(sem <= 0):
            sem = offset;
        else:
            sem = sem - 1;
        return sem;
    
    def _Imprimir(self,S):
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
