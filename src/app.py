import streamlit as st
import pandas as pd 

st.image('./data/neuron.webp', width=350)

st.title("¡Hola neurona! - ALEJANDRO FR")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
   st.subheader("Una neurona con una entrada y un peso")
   w = st.slider("Peso", min_value=0.00, max_value=5.00, step=0.01, key="tab1_w")
   x = st.number_input('Introduzca el valor de la entrada', key="tab1_x")

   if st.button("Calcular la salida", key="tab1_button"):
       y = x * w
       st.text(f"La salida de la neurona es: {y}")

with tab2:
    col1, col2, = st.columns([1,1])

    with col1:
        w0 = st.slider("Peso $w_0$", min_value=0.00, max_value=5.00, step=0.01, key="tab2_w0")
        x0 = st.number_input('Entrada $x_0$', key="tab2_x0")

    with col2:
        w1 = st.slider("Peso $w_1$", min_value=0.00, max_value=5.00, step=0.01, key="tab2_w1")
        x1 = st.number_input('Entrada $x_1$', key="tab2_x1")

    if st.button("Calcular la salida", key="tab2_button"):
       y = x0 * w0 + x1 * w1
       st.text(f"La salida de la neurona es: {y}")

with tab3:
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        w0 = st.slider("Peso $w_0$", min_value=0.00, max_value=5.00, step=0.01, key="tab3_w0")
        x0 = st.number_input('Entrada $x_0$', key="tab3_x0")

    with col2:
        w1 = st.slider("Peso $w_1$", min_value=0.00, max_value=5.00, step=0.01, key="tab3_w1")
        x1 = st.number_input('Entrada $x_1$', key="tab3_x1")

    with col3:
        w2 = st.slider("Peso $w_2$", min_value=0.00, max_value=5.00, step=0.01, key="tab3_w2")
        x2 = st.number_input('Entrada $x_2$', key="tab3_x2")
    
    b = st.number_input('Introduzca el valor del sesgo', key="tab3_b")
        
    if st.button("Calcular la salida"):
       y = x0 * w0 + x1 * w1 + x2 * w2 + b
       st.text(f"La salida de la neurona es: {y}")

    