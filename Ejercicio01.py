import numpy as np
import pandas as pd
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

print ("Cuales han sido las ventas de los ultimos 5 dias")
df = pd.DataFrame()
df["Dia de la semana"] = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
df["Articulo"] = ['pan', 'arroz', 'carne de res', 'pollo', 'huevo']
df["Precio Unitarios"] = [10, 20, 30, 40, 60]
df["Cantidad"] = [7, 8, 8, 8, 34]
df["Precio Total"] = df["Precio Unitarios"]*df["Cantidad"]
df["Descuento"] = (0.5 * df["Precio Total"]/100)
print(df)
