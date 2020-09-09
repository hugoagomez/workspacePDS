#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on ...

@author: Hugo Alejandro Gomez

Descripción:
------------

Generador de señales. En primer lugar serán funciones senoidales con 
sus respectivos parámetros.


"""

# Importación de módulos que utilizaremos en nuesto testbench:
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#%%  Inicialización


#%%  Testbench: creamos una función que no recibe argumentos para asegurar que siempre encontraremos nuestro espacio de variables limpio.

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
    
# Definición de variables de la señal

sig_props = { 'tipo': 'senoidal', 
              'amplitud':      (1), 
              'valor medio':   (0),
              'frecuencia':    (1),  
              'fase':          (0),
              'muestras':      (1000),
              'frec muestreo': (1000.0)
            } 

# Se agrega descripción para el gráfico, identificando la señal por su frecuencia
sig_props['descripcion'] = [ str(sig_props['frecuencia']) + ' Hz' ]

    
# Invocamos a nuestro testbench exclusivamente: 
mi_funcion_sen( sig_props )
    

