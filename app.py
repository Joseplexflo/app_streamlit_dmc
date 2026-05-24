import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones import flujo_caja_neto
from libreria_funciones_proyecto1 import flujo_caja_neto, precio_venta_final

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

########################
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
            costos_operativos=total_gastos
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

########################
elif item == "Ejercicio 2":
    # Una breve descripción del ejercicio
    st.subheader("Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
    st.markdown("""
    Este módulo permite registrar información de productos mediante un formulario. 
    Los datos ingresados se almacenan temporalmente en arreglos de NumPy y luego 
    se convierten en un DataFrame de Pandas para mostrar la tabla actualizada.
    """)

    if "lista_registros" not in st.session_state:
        st.session_state.lista_registros = []

    st.markdown("---")

    # El formulario de ingreso de datos
    st.markdown("### 📝 Ingreso de productos")
    
    nombre_producto = st.text_input("Nombre del producto:")
    categoria = st.selectbox("Categoría:", ["Electrónica", "Abarrotes", "Limpieza", "Ropa", "Otros"])
    precio = st.number_input("Precio:", min_value=0.0, step=1.0, format="%.2f")
    cantidad = st.number_input("Cantidad:", min_value=1, step=1)

    if st.button("Agregar registro"):
        if nombre_producto.strip() == "":
            st.warning("Debe ingresar el nombre del producto.")
        elif precio <= 0:
            st.warning("El precio debe ser mayor a 0.")
        else:
            total = precio * cantidad

            st.session_state.lista_registros.append([nombre_producto, categoria, precio, cantidad, total])
            st.success("Registro agregado exitosamente.")

    if st.session_state.lista_registros:
        st.markdown("---")
        st.markdown("### 📦 Datos registrados")
        
        arreglo_numpy = np.array(st.session_state.lista_registros, dtype=object)
        
        nombres_columnas = ["Nombre del producto", "Categoría", "Precio", "Cantidad", "Total"]
        df_registros = pd.DataFrame(arreglo_numpy, columns=nombres_columnas)
        
        st.dataframe(df_registros, use_container_width=True)

        if st.button("Reiniciar tabla"):
            st.session_state.lista_registros = []
            st.rerun()

########################
elif item == "Ejercicio 3":
    # Una breve descripción del ejercicio
    st.subheader("Ejercicio 3 – Uso de funciones desde una librería externa")
    st.markdown("""
    Este módulo conecta una función de negocio con la interfaz gráfica. Evaluando el rol de 
    **Ingeniero de proyectos en exportación textil**, se ha seleccionado la función `precio_venta_final` 
    para determinar el precio de salida de mercancías aplicando márgenes, descuentos e impuestos.
    """)

    if "historico_precios" not in st.session_state:
        st.session_state.historico_precios = []

    st.markdown("---")

    funcion_seleccionada = st.selectbox(
        "Seleccione una función relacionada con su área de formación o trabajo:",
        ["precio_venta_final"]
    )

    if funcion_seleccionada == "precio_venta_final":
        st.markdown("### 📊 Parámetros de Cotización Textil")
        
        # • Widgets para ingresar parámetros (st.number_input)
        costo_base = st.number_input("Costo base de producción (USD o S/.):", min_value=0.0, step=10.0, format="%.2f")
        margen_ganancia_pct = st.number_input("Margen de ganancia deseado (%):", min_value=0.0, max_value=100.0, step=5.0)
        descuento_pct = st.number_input("Descuento comercial aplicado (%):", min_value=0.0, max_value=100.0, step=1.0)
        iva_pct = st.number_input("IVA / Impuesto de exportación (%):", min_value=0.0, max_value=100.0, step=1.0)

        if st.button("Ejecutar función"):
            if costo_base <= 0:
                st.warning("El costo base debe ser mayor a cero para realizar el cálculo.")
            else:
                resultado_precio = precio_venta_final(costo_base, margen_ganancia_pct, descuento_pct, iva_pct)
                
                st.write(f"### 💰 Precio de Venta Final: S/. {resultado_precio:,.2f}")
                
                st.session_state.historico_precios.append({
                    "Función Ejecutada": funcion_seleccionada,
                    "Costo Base": costo_base,
                    "Margen (%)": margen_ganancia_pct,
                    "Descuento (%)": descuento_pct,
                    "IVA (%)": iva_pct,
                    "Resultado Final": resultado_precio
                })
                st.toast("Cálculo guardado en el histórico.")

        if st.session_state.historico_precios:
            st.markdown("---")
            st.markdown("### ⏳ Tabla histórica de resultados obtenidos")
            df_historico = pd.DataFrame(st.session_state.historico_precios)
            st.dataframe(df_historico, use_container_width=True)
            
            if st.button("Limpiar histórico"):
                st.session_state.historico_precios = []
                st.rerun()

########################
else:
    st.subheader("Uso de clases desde una librería externa con CRUD")
