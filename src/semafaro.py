
"""
Este Codigo No funciona con Linux
"""

from termcolor import *;
import colorama;
from time import sleep;
from os import system;
import sys;
from msvcrt import kbhit
colorama.init();

Ss = [30,60,90,120];
DURACION_TOTAL = 120

def CambiarSemafaro(sem,offset):
    if(sem <= 0):
        sem = offset;
    else:
        sem = sem - 1;
    return sem;

def Imprimir(S):
    if(S < 30):
        cprint(S,"green");
    else:
        cprint(S,"red");

while (not kbhit()):
    system('cls');
    
    for i in range(len(Ss)):
        Ss[i] = CambiarSemafaro(Ss[i],DURACION_TOTAL);
        Imprimir(Ss[i]);
        
    sleep(0.10);
