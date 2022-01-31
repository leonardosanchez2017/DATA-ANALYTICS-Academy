import pandas as pd
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

df = pd.DataFrame()
df["Mes"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
df["Ventas"] = [30500, 35600, 28300, 33900, 42500]
df["Gastos"] = [22000, 23450, 18100, 35700, 32450]
df["Gastos/Ventas"] = df["Gastos"] / df["Ventas"]*100
print(df)