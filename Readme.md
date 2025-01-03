# Cálculo de Cash Flow Automático

Este programa es una mini aplicación interactiva desarrollada con **Streamlit**, **Pandas** y **Plotly**, diseñada para calcular y visualizar el flujo de caja (Cash Flow) de manera automática a partir de un archivo Excel.

## Características Principales

- **Carga de archivo Excel**: Permite a los usuarios subir un archivo en formato `.xlsx` que contiene los datos necesarios.
- **Procesamiento robusto de datos**:
  - Manejo de nombres de columnas, independientemente de mayúsculas, minúsculas o espacios.
  - Validación de la presencia de las columnas necesarias: `Fecha`, `Ingresos`, y `Egresos`.
- **Cálculos automáticos**:
  - Flujo de caja diario (`Ingresos - Egresos`).
  - Flujo de caja acumulado.
- **Visualización interactiva**:
  - Gráficos dinámicos creados con **Plotly** para representar el flujo de caja diario y acumulado.
  - Tablas dinámicas para mostrar datos procesados.

## Requisitos

- Python 3.8 o superior.
- Bibliotecas necesarias:
  - `pandas`
  - `streamlit`
  - `plotly`

Instala las dependencias utilizando:
```bash
pip install pandas streamlit plotly
```

## Cómo usar

1. Ejecuta la aplicación con el siguiente comando:
```bash
streamlit run app.py
```
2. Carga un archivo Excel con las siguientes columnas:
   - **Fecha**: Fechas en formato adecuado (pueden ser reconocidas automáticamente).
   - **Ingreso**: Valores de ingresos diarios.
   - **Egreso**: Valores de egresos diarios.
3. Observa los resultados procesados y visualízalos en gráficos interactivos.

## Errores comunes

- **Archivo inválido**: Si el archivo no contiene las columnas necesarias o si el formato no es `.xlsx`, la aplicación mostrará un mensaje de error.
- **Datos mal formateados**: Asegúrate de que las columnas `Ingresos` y `Egresos` contengan valores numéricos, y que `Fecha` sea interpretable como fechas.

## Personalización

Si deseas modificar o extender la funcionalidad, puedes editar el archivo `app.py` y personalizar las columnas, cálculos o gráficos según tus necesidades.

---

¡Explora y optimiza tu flujo de caja con esta herramienta interactiva! 😊


