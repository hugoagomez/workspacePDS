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

# Ejecutado desde consola utiliza las gráficas de QT
mpl.use('Qt5Agg')


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
    
#%% Parametros de consola
import argparse as ap

parser = ap.ArgumentParser(description='Ejemplo de testbench utilizado en la materia Procesamiento Digital de Señales.')

parser.add_argument( 'signal_vmax', 
                     metavar='Amplitud_maxima', 
                     default= 1, 
                     type=float, 
                     help='Amplitud máxima de la señal')

parser.add_argument( 'signal_dc', 
                     metavar='Valor_medio', 
                     default= 0, 
                     type=float, 
                     help='Valor medio de la señal')

parser.add_argument( 'signal_ff', 
                     metavar='Frecuencia', 
                     default=1, 
                     type=float, 
                     help='Frecuencia de la señal')

parser.add_argument( 'signal_ph', 
                     metavar='Fase', 
                     default=0, 
                     type=float, 
                     help='Fase')

parser.add_argument( 'signal_N', 
                     metavar='Muestras', 
                     default=1000, 
                     type=int, 
                     help='Cantidad de muestras')

parser.add_argument( 'signal_fs', 
                     metavar='Frecuencia_muestreo', 
                     default=1000, 
                     type=float, 
                     help='Frecuencia de muestreo')

args = parser.parse_args()
           

#%% Presentación gráfica de los resultados
# Inicialización de variables 
# N=1000
# fs=1000
# ts=1/fs


# Invocamos a nuestro testbench exclusivamente: 

tt,xx = mi_funcion_sen( vmax=args.signal_vmax, dc=args.signal_dc, ff=args.signal_ff, ph=args.signal_ph, N=args.signal_N, fs=args.signal_fs)


    
plt.figure(1)
line_hdls = plt.plot(tt, xx)
plt.title('Señal: Senoidal')
plt.xlabel('Tiempo [segundos]')
plt.ylabel('Amplitud [Volts]')
plt.grid(which='both', axis='both')
plt.show()
    
    


