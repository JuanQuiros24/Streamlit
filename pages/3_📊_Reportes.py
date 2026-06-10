import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Reportes", page_icon="📊")

st.title("📊 Dashboards y Reportes")

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("💰 Ventas totales", "$48.350.000", "+12%")
col2.metric("👥 Clientes activos", "1.284", "+5%")
col3.metric("📦 Productos vendidos", "3.670", "+8%")

st.divider()

# --- Selector de rango de fechas ---
st.subheader("Filtrar por rango de fechas")
col_a, col_b = st.columns(2)
fecha_inicio = col_a.date_input("Fecha inicio", datetime.date(2024, 1, 1))
fecha_fin = col_b.date_input("Fecha fin", datetime.date(2024, 12, 31))

# --- Datos de ventas por mes ---
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ventas = [3200000, 2800000, 4100000, 3900000, 4500000, 5200000,
          4800000, 4300000, 3700000, 4900000, 5800000, 6100000]

df_ventas = pd.DataFrame({"Mes": meses, "Ventas": ventas})

# --- Gráfico de líneas ---
st.subheader("Ventas por mes (2024)")
st.line_chart(df_ventas.set_index("Mes"))

st.divider()

# --- Botón de descarga ---
csv = df_ventas.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Descargar reporte CSV",
    data=csv,
    file_name="reporte_ventas_2024.csv",
    mime="text/csv",
)