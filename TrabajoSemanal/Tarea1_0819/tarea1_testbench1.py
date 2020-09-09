#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on ...

@author: Hugo Alejandro Gomez
Descripción:
------------

Generador de señales. En primer lugar serán funciones senoidales con 
sus respectivos parámetros.
Este testbench sigue con el ejemplo del "testbench0" pero agrega la funcionalidad
 de ejecutarlo a través de la consola, haciendo el parseo de argumentos.
 Mandando en orden:
     Amplitud máxima de la senoidal
     Valor medio
     Frecuencia
     Fase
     Cantidad de muestras digitalizadas por el ADC
     Frecuencia de muestreo del ADC

"""

# Ejemplificaremos el uso de las herramientas que utilizaremoos frecuentemente 

# Importación de módulos que utilizaremos en nuesto testbench:
# Una vez invocadas estas funciones, podremos utilizar los módulos a través del identificador que indicamos luego de "as". 
# Por ejemplo np.linspace() -> función linspace dentro e NumPy
import numpy as np
#import scipy.signal as sig
import matplotlib as mpl
# la siguiente línea solo afecta en caso que lo quisiéramos correr desde la línea de comandos
mpl.use('Qt5Agg')

import matplotlib.pyplot as plt




#%%  Inicialización de librerías

# Setup inline graphics
mpl.rcParams['figure.figsize'] = (10,10)

#%%  Testbench: creamos una función que no recibe argumentos para asegurar que siempre encontraremos nuestro espacio de variables limpio.
# Prestar atención al indentado, ya que Python interpreta en función del indentado !!


def mi_funcion_sen( sig_type ):
    
    # Datos generales de la simulación
    fs = sig_type['frec muestreo'] # frecuencia de muestreo (Hz)
    N = sig_type['muestras']   # cantidad de muestras
    
    ts = 1/fs # tiempo de muestreo
    
    # grilla de sampleo temporal
    tt = np.arange(0.0, N/fs, ts)

    # Concatenación de matrices:
    # guardaremos las señales creadas al ir poblando la siguiente matriz vacía
    xx = np.array([], dtype=np.float).reshape(N,0)
    
    
    # estructuras de control de flujo
    if sig_type['tipo'] == 'senoidal':
    
        
        # Cálculo punto a punto de la señal
        aux = sig_type['amplitud'] * np.sin( 2*np.pi*sig_type['frecuencia']*tt + sig_type['fase'] ) + sig_type['valor medio']
        # para concatenar horizontalmente es necesario cuidar que tengan iguales FILAS
        xx = np.hstack([xx, aux.reshape(N,1)] )
        
     
    
    else:
        
        print("Tipo de señal no implementado.")        
        return
        
    #%% Presentación gráfica de los resultados
    
    plt.figure(1)
    line_hdls = plt.plot(tt, xx)
    plt.title('Señal: ' + sig_type['tipo'] )
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [Volts]')
    plt.grid(which='both', axis='both')
    
# Presentar una leyenda para cada tipo de señal
    axes_hdl = plt.gca()
    
    axes_hdl.legend(line_hdls, sig_type['descripcion'], loc='upper right'  )
    
    plt.show()
    
#%% Comienzo de nuestro script
    ##########################
    
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

parser.add_argument( 'signal_nn', 
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
           


# Definición de variables de la señal

sig_props = { 'tipo': 'senoidal', 
              'amplitud':      (args.signal_vmax), 
              'valor medio':   (args.signal_dc),
              'frecuencia':    (args.signal_ff),  
              'fase':          (args.signal_ph),
              'muestras':      (args.signal_nn),
              'frec muestreo': (args.signal_fs)
            } 

# Se agrega descripción para el gráfico, identificando la señal por su frecuencia
sig_props['descripcion'] = [ str(sig_props['frecuencia']) + ' Hz' ]

    
# Invocamos a nuestro testbench exclusivamente: 
mi_funcion_sen( sig_props )

