#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on ...

@author: Hugo Alejandro Gomez

Descripción:
------------

Generador de señales. En primer lugar serán funciones senoidales con 
sus respectivos parámetros.
vmax    Amplitud máxima de la senoidal
dc      Número de muestras
ff      Frecuencia
ph      Fase (radianes)
nn      Cantidad de muestras digitalizadas
fs      Frecuencia de muestreo


"""

# Importación de módulos que utilizaremos en nuesto testbench:
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#%%  Inicialización

#%%  Testbench: creamos una función que no recibe argumentos para asegurar que siempre encontraremos nuestro espacio de variables limpio.

def mi_funcion_sen (vmax, dc, ff, ph, N, fs):
    
    # Grilla de sampleo temporal
    #tt = np.arange( N/fs, ts)
    tt = np.arange(0.0, N/fs, 1/fs)
    #tt=np.linspace(0,(N-1)/fs,N)
    # Calculo de los valores punto a punto de la senoidal
    xx = vmax * np.sin(tt*2*np.pi*ff + ph) + dc
    
    return tt,xx
    
#%% Presentación gráfica de los resultados
# Inicialización de variables 
N=1000
fs=1000
ts=1/fs


# Invocamos a nuestro testbench exclusivamente: 

tt,xx = mi_funcion_sen( vmax=1, dc=0, ff=1, ph=0, N=N, fs=fs)


    
plt.figure(1)
line_hdls = plt.plot(tt, xx)
plt.title('Señal: Senoidal')
plt.xlabel('Tiempo [segundos]')
plt.ylabel('Amplitud [Volts]')
plt.grid(which='both', axis='both')
plt.show()
    
    


