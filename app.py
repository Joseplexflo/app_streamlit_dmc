import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones import flujo_caja_neto

st.title("APLICACIÓN EN STREAMLIT")
st.write("Elaborado por: **Jhonattan Josep Lezma Florida**")

st.sidebar.title("Ejercicios")
item = st.sidebar.selectbox("Seleccione un item:", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
st.sidebar.image("dmc_logo.png", use_container_width=True)

if item == "Home":
    st.write("Módulo 1 – Python Fundamentals")
    st.write("**Profesión:** Ingeniero de proyectos en empresa de exportación textil")
    st.write("**Fecha:** Mayo-2026")
    st.write("Este proyecto es el desarrollo de lo aprendio en el Módulo 1 – Python Fundamentals dictado por DMC")
    st.write("**Tecnologías utilizadas:** librerias `numpy` y `streamlit`")
    st.image("logo_personal.png", width=250)

elif item == "Ejercicio 1":
    st.subheader("Flujo de caja con listas")
    st.markdown("""
    En este ejercicio se desarrolla un módulo para registrar movimientos financieros en una lista vacía.
    Permite el ingreso de un concepto, el tipo de movimiento y su valor para calcular el saldo final del flujo de caja.
    """)

    if "lista_movimientos" not in st.session_state:
        st.session_state.lista_movimientos = []
        
    concepto = st.text_input("Concepto:")
    tipo_movimiento = st.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor:", min_value=0.0, step=1.0, format="%.2f")

    if st.button("Agregar movimiento"):
        if concepto.strip() == "":
            st.warning("Por favor, ingrese un concepto.")
        elif valor <= 0:
            st.warning("El valor debe ser mayor a cero.")
        else:
            st.session_state.lista_movimientos.append({
                "concepto": concepto,
                "tipo de movimiento": tipo_movimiento,
                "valor": valor
            })
            st.toast("Movimiento agregado.")

    # Todo este bloque se ejecuta únicamente si existen movimientos registrados
    if st.session_state.lista_movimientos:
        st.markdown("#### Lista de movimientos registrados")
        df_movimientos = pd.DataFrame(st.session_state.lista_movimientos)
        st.dataframe(df_movimientos, use_container_width=True)

        # Los cálculos se realizan dentro del condicional para evitar errores con listas vacías
        total_ingresos = sum(m["valor"] for m in st.session_state.lista_movimientos if m["tipo de movimiento"] == "Ingreso")
        total_gastos = sum(m["valor"] for m in st.session_state.lista_movimientos if m["tipo de movimiento"] == "Gasto")

        saldo_final = flujo_caja_neto(
            ingresos=total_ingresos, 
            costos_operativos=total_gastos, 
            impuestos=0.0, 
            otros_gastos=0.0
        )

        st.markdown("#### Resultado final del flujo de caja")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Total de Ingresos", value=f"S/. {total_ingresos:,.2f}")
        col2.metric(label="Total de Gastos", value=f"S/. {total_gastos:,.2f}")
        col3.metric(label="Saldo Final", value=f"S/. {saldo_final:,.2f}")

        # Indicación de si el flujo de caja está a favor o en contra con st.success() o st.error()
        if saldo_final >= 0:
            st.success("El flujo de caja está: A FAVOR")
        else:
            st.error("El flujo de caja está: EN CONTRA")
                
        # Botón para limpiar y reiniciar la lista en la interfaz
        if st.button("Reiniciar ejercicio"):
            st.session_state.lista_movimientos = []
            st.rerun()

elif item == "Ejercicio 2":
    st.subheader("Registro con NumPy, arrays y DataFrame")
      
elif item == "Ejercicio 3":
    st.subheader("Uso de funciones desde una librería externa")

else:
    st.subheader("Uso de clases desde una librería externa con CRUD")
