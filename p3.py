import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Día 5: FLORES PERRO')

# Ejemplo 1: Texto y emojis
st.write('Hola, *Mundo!* :sunglasses: rocket:')

# Ejemplo 2: Números
st.write(1234)

# Ejemplo 3: Tablas (DataFrames)
df = pd.DataFrame({
     'primera columna': [1, 2, 3, 4],
     'segunda columna': [10, 20, 30, 40]
     })
st.write(df)

# Ejemplo 4: Mezclar argumentos
st.write('Abajo hay una tabla:', df, 'Y arriba texto.')

# Ejemplo 5: Gráficos complejos
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

grafico = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(grafico)
