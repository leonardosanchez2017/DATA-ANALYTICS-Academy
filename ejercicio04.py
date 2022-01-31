# coding=utf-8
import pandas as pd
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

df = pd.DataFrame()
tabla = pd.read_csv('/Users/marcosleonardosanchez/Desktop/Proyectos Python/Data - Riesgos (1).csv')
print(tabla)
print('Dimensiones:', tabla.shape)
print('Número de elemntos:', tabla.size)
print('Nombres de columnas:', tabla.columns)
print('Nombres de filas:', tabla.index)
print('Tipos de datos:\n', tabla.dtypes)
print('Primeras 10 filas:\n', tabla.head(10))
print('Últimas 10 filas:\n', tabla.tail(10))
print('Primeras 100 filas:\n', tabla.head(100))