import streamlit as st
import pandas as pd
import plotly.express as px

from PIL import Image

logo = Image.open('graphmagnifier_117961.png')

st.set_page_config(page_title="Calculadora de Cash Flow", page_icon=logo, layout='wide')

def pagina_inicio():

    st.title('Cálculo de Cash Flow Automático')

    # Subir archivo Excel
    archivo_subido = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

    if archivo_subido is not None:
        # Leer el archivo Excel
        df = pd.read_excel(archivo_subido)

        # Manejar nombres de columnas para mayor robustez
        columnas_originales = df.columns
        columnas_normalizadas = [col.lower().strip() for col in columnas_originales]
        df.columns = columnas_normalizadas

        # Verificar que las columnas necesarias estén presentes
        columnas_necesarias = {'fecha', 'ingresos', 'egresos'}
        if not columnas_necesarias.issubset(set(columnas_normalizadas)):
            st.error("El archivo no contiene las columnas necesarias: Fecha, Ingresos y Egresos.")
        else:
            # Mostrar datos cargados
            st.write("Datos cargados de tu archivo Excel:")
            st.dataframe(df)

            try:
                # Convertir la columna de fecha a datetime
                df['fecha'] = pd.to_datetime(df['fecha'])

                # Ordenar por fecha
                df = df.sort_values(by='fecha')

                # Calcular el flujo de caja
                df['cash flow'] = df['ingresos'] - df['egresos']

                # Calcular flujo de caja acumulado
                df['cash flow acumulado'] = df['cash flow'].cumsum()

                # Mostrar tabla procesada
                st.write("Datos procesados con el cálculo de Cash Flow:")
                st.dataframe(df)

                # Crear gráfico de Cash Flow
                fig = px.line(df, x='fecha', y=['cash flow', 'cash flow acumulado'], 
                            title='Flujo de Caja y Flujo Acumulado',
                            labels={'value': 'Monto', 'variable': 'Tipo'})

                # Mostrar el gráfico
                st.plotly_chart(fig)

                st.write("Listo!! Ya tienes tu Cash Flow Calculado. Ahora puedes hacer lo que desees. Puedes descargar la información e interactuar con ella solo desde aquí si prefieres.")

            except Exception as e:
                st.error(f"Error al procesar los datos: {e}")
    else:
        st.write("Sube un archivo Excel para comenzar.")


if __name__ == '__main__':
    pagina_inicio()