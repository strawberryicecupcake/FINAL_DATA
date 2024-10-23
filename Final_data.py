import pandas as pd

# Cargar el CSV
df = pd.read_csv('DATA_TURISMO.csv')

# 1era Regla: Reemplazar valores vacíos con "sin datos"
df.fillna('sin datos', inplace=True)

# 2da Regla: En las columnas 'VISITAS_E1', 'VISITAS_E2A3', 'VISITAS_E3A30', si es "0", reemplazar por "no data"
columnas_visitas = ['VISITAS_E1', 'VISITAS_E2A3', 'VISITAS_E3A30']
df[columnas_visitas] = df[columnas_visitas].replace('0', 'no data')

# Guardar el DataFrame transformado en el mismo archivo CSV
df.to_csv('archivo.csv', index=False)


