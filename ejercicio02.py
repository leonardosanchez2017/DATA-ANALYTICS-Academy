import pandas as pd

def ingresos(ingresosMensuales):
    ingresosMensuales = pd.Series(ingresosMensuales)
    montos = pd.Series([ingresosMensuales.min(), ingresosMensuales.max(), ingresosMensuales.mean()],
                       index=['Min', 'Max', 'Media'])
    return montos
ingresosMensuales = {'marcos': 9000, 'Dicent': 6040, 'carmen': 4000, 'pedro': 8005, 'tomas': 5000}
print(ingresos(ingresosMensuales))
