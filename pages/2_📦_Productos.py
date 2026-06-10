import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Productos", page_icon="📦")

st.title("📦 Catálogo de Productos")

# Imagen desde Unsplash
st.image(
    "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=800&q=80",
    caption="Catálogo de Productos",
    use_container_width=True,
)

# DataFrame con productos
data = {
    "Nombre": [
        "Laptop Pro 15",
        "Mouse Inalámbrico",
        "Teclado Mecánico",
        "Monitor 27\"",
        "Auriculares BT",
        "Webcam HD",
        "Hub USB-C",
    ],
    "Categoría": [
        "Computadores",
        "Accesorios",
        "Accesorios",
        "Computadores",
        "Audio",
        "Accesorios",
        "Accesorios",
    ],
    "Precio": [3500000, 85000, 220000, 950000, 180000, 130000, 95000],
    "Stock": [12, 45, 30, 8, 25, 17, 40],
}

df = pd.DataFrame(data)

# Filtro por categoría
categorias = df["Categoría"].unique().tolist()
seleccion = st.multiselect(
    "Filtrar por categoría:",
    options=categorias,
    default=categorias,
)

df_filtrado = df[df["Categoría"].isin(seleccion)]

st.dataframe(df_filtrado, use_container_width=True)

# Métrica total de productos
st.metric("Total de productos", len(df_filtrado))

# Gráfico de barras precio por producto
st.subheader("Precio por producto")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df_filtrado["Nombre"], df_filtrado["Precio"], color="#4F8BF9")
ax.set_xlabel("Producto")
ax.set_ylabel("Precio (COP)")
ax.set_title("Precio por producto")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
st.pyplot(fig)