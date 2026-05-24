import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones as lf

from libreria_funciones_proyecto1 import flujo_caja_neto, precio_venta_final, produccion_real_linea, LoteProduccionTextil

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
    st.subheader("Ejercicio 3 – Uso de funciones desde una librería externa")
    st.markdown("""
    Este módulo conecta funciones de ingeniería de proyectos y manufactura textil con la interfaz gráfica, 
    permitiendo evaluar escenarios de cotización o calcular la productividad real de una línea.
    """)

    if "historico_ejercicio3" not in st.session_state:
        st.session_state.historico_ejercicio3 = []

    st.markdown("---")

    # • Selector de función con las dos opciones de tu rubro
    funcion_seleccionada = st.selectbox(
        "Seleccione una función relacionada con su área de formación o trabajo:",
        ["precio_venta_final", "produccion_real_linea"]
    )

    # ==================== CASO 1: PRECIO DE VENTA ====================
    if funcion_seleccionada == "precio_venta_final":
        st.markdown("### 📊 Parámetros de Cotización Textil")
        costo_base = st.number_input("Costo base de producción:", min_value=0.0, step=10.0, format="%.2f")
        margen_ganancia_pct = st.number_input("Margen de ganancia deseado (%):", min_value=0.0, max_value=100.0, step=5.0)
        descuento_pct = st.number_input("Descuento comercial aplicado (%):", min_value=0.0, max_value=100.0, step=1.0)
        iva_pct = st.number_input("IVA / Impuesto (%):", min_value=0.0, max_value=100.0, step=1.0)

        if st.button("Ejecutar función"):
            if costo_base <= 0:
                st.warning("El costo base debe ser mayor a cero.")
            else:
                resultado = precio_venta_final(costo_base, margen_ganancia_pct, descuento_pct, iva_pct)
                st.write(f"### 💰 Precio de Venta Final: S/. {resultado:,.2f}")
                
                st.session_state.historico_ejercicio3.append({
                    "Función": funcion_seleccionada,
                    "Dato Clave 1": f"Costo: S/. {costo_base}",
                    "Dato Clave 2": f"Margen: {margen_ganancia_pct}%",
                    "Resultado": f"S/. {resultado:,.2f}"
                })
                st.toast("Cálculo guardado.")

    # ==================== CASO 2: PRODUCCIÓN DE LÍNEA ====================
    elif funcion_seleccionada == "produccion_real_linea":
        st.markdown("### ⚙️ Control de Producción en Línea")
        
        # Parámetros solicitados por el ejercicio adaptados a widgets
        min_disponibles = st.number_input("Minutos disponibles por operario (ej. 480 para un turno):", min_value=0.0, step=10.0, format="%.1f")
        eficiencia = st.number_input("Eficiencia de la línea (%):", min_value=0.0, max_value=100.0, value=85.0, step=5.0)
        sam = st.number_input("Tiempo estándar por prenda / SAM (minutos):", min_value=0.01, step=0.5, format="%.2f")
        defectos = st.number_input("Porcentaje de prendas defectuosas / mermas (%):", min_value=0.0, max_value=100.0, value=2.0, step=0.5)
        personas = st.number_input("Cantidad de personas en la línea:", min_value=1, step=1, value=10)

        if st.button("Ejecutar función"):
            if min_disponibles <= 0 or sam <= 0:
                st.warning("Los minutos disponibles y el tiempo estándar deben ser mayores a cero.")
            else:
                # Ejecutar la función matemática de la línea textil
                resultado_prendas = produccion_real_linea(min_disponibles, eficiencia, sam, defectos, personas)
                
                # Mostrar resultado en pantalla
                st.write(f"### 📦 Producción Real Estimada: {resultado_prendas:,.0f} unidades netas")
                
                # Guardar en la tabla histórica compartida
                st.session_state.historico_ejercicio3.append({
                    "Función": funcion_seleccionada,
                    "#Operarios": f"{personas}",
                    "SAM": f"{sam} min",
                    "%Ef.": f"{eficiencia}%",
                    "5Def.": f"{defectos}%",
                    "PRENDAS": f"{resultado_prendas:,.0f} pds"
                })
                st.toast("Cálculo de producción guardado.")

    # • Tabla histórica común para visualizar los resultados obtenidos
    if st.session_state.historico_ejercicio3:
        st.markdown("---")
        st.markdown("### ⏳ Tabla histórica de resultados obtenidos")
        df_historico = pd.DataFrame(st.session_state.historico_ejercicio3)
        st.dataframe(df_historico, use_container_width=True)
        
        if st.button("Limpiar histórico"):
            st.session_state.historico_ejercicio3 = []
            st.rerun()

########################
else:
    st.subheader("Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
    st.markdown("""
    Este módulo implementa un sistema **CRUD** utilizando la clase externa `LoteProduccionTextil`. 
    Permite administrar la programación, el seguimiento de estados y la eliminación de órdenes de producción en planta.
    """)

    if "db_lotes" not in st.session_state:
        st.session_state.db_lotes = {
            "LOTE001": LoteProduccionTextil("LOTE001", "Algodón Pima", "Azul Marino", 1200, "En teñido"),
            "LOTE002": LoteProduccionTextil("LOTE002", "Poliéster", "Negro", 2500, "Programado")
        }

    st.markdown("---")

    # Implementación recomendada con st.tabs() para separar las operaciones CRUD de forma limpia
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["➕ Crear Lote", "📋 Leer / Ver Tabla", "🔄 Actualizar Estado", "❌ Eliminar Lote"])

    # ------------------ C - CREATE (CREAR) ------------------
    with tab_crear:
        st.markdown("### 📝 Registrar Nuevo Lote de Producción")
        id_nuevo = st.text_input("Código de Lote único (Ej: LOTE003):").strip().upper()
        tela_nueva = st.selectbox("Tipo de Tela:", ["Algodón Pima", "Jersey", "Rib", "Polystretch", "Denim"])
        color_nuevo = st.text_input("Color de la tela:")
        metros_nuevos = st.number_input("Cantidad de metros a producir:", min_value=1.0, step=100.0, format="%.2f")
        
        if st.button("Guardar Lote"):
            if id_nuevo == "":
                st.warning("Debe ingresar un código de lote válido.")
            elif id_nuevo in st.session_state.db_lotes:
                st.error("Ese código de lote ya existe. Ingrese uno diferente.")
            elif color_nuevo.strip() == "":
                st.warning("Debe especificar un color para el lote.")
            else:
                # Instanciamos la clase externa con los datos capturados de los widgets
                nuevo_objeto_lote = LoteProduccionTextil(id_nuevo, tela_nueva, color_nuevo, metros_nuevos)
                
                # Lo guardamos en nuestro diccionario de sesión
                st.session_state.db_lotes[id_nuevo] = nuevo_objeto_lote
                st.success(f"✅ ¡Lote {id_nuevo} creado e instanciado con éxito!")
                st.rerun()

    # ------------------ R - READ (LEER) ------------------
    with tab_leer:
        st.markdown("### 📊 Tablero de Control de Lotes en Planta")
        
        if st.session_state.db_lotes:
            # Extraemos los datos de los objetos para formatearlos en un DataFrame de Pandas
            tabla_datos = []
            for lote in st.session_state.db_lotes.values():
                tabla_datos.append({
                    "Código Lote": lote.id_lote,
                    "Material / Tela": lote.tipo_tela,
                    "Color": lote.color,
                    "Metros Programados": lote.cantidad_metros,
                    "Estado Actual": lote.estado
                })
            
            df_lotes = pd.DataFrame(tabla_datos)
            st.dataframe(df_lotes, use_container_width=True)
        else:
            st.info("No hay lotes registrados en este momento.")

    # ------------------ U - UPDATE (ACTUALIZAR) ------------------
    with tab_actualizar:
        st.markdown("### 🔄 Modificar Parámetros de Lote Activo")
        
        if st.session_state.db_lotes:
            id_a_modificar = st.selectbox("Seleccione el lote que desea modificar:", list(st.session_state.db_lotes.keys()))
            lote_seleccionado = st.session_state.db_lotes[id_a_modificar]
            
            st.markdown(f"**Datos actuales del lote:** {lote_seleccionado.tipo_tela} ({lote_seleccionado.color})")
            
            # Formulario de actualización combinando inputs y métodos de la clase
            nuevo_est = st.selectbox("Cambiar Estado Operativo:", ["Programado", "En teñido", "En corte", "En confección", "Terminado"])
            nuevos_met = st.number_input("Corregir metros asignados:", min_value=1.0, value=lote_seleccionado.cantidad_metros, step=50.0)
            
            if st.button("Aplicar Cambios"):
                # Ejecutamos los métodos internos del objeto instanciado
                lote_seleccionado.actualizar_estado(nuevo_est)
                lote_seleccionado.actualizar_cantidad(nuevos_met)
                
                st.success(f"🔄 ¡Lote {id_a_modificar} actualizado exitosamente!")
                st.rerun()
        else:
            st.info("No hay lotes disponibles para actualizar.")

    # ------------------ D - DELETE (ELIMINAR) ------------------
    with tab_eliminar:
        st.markdown("### ❌ Dar de Baja u Ordenar Retiro de Lote")
        
        if st.session_state.db_lotes:
            id_a_eliminar = st.selectbox("Seleccione el lote que desea dar de baja:", list(st.session_state.db_lotes.keys()), key="del_box")
            lote_eliminar = st.session_state.db_lotes[id_a_eliminar]
            
            st.warning(f"⚠️ ¿Está seguro de que desea eliminar permanentemente el lote **{id_a_eliminar}** de {lote_eliminar.tipo_tela}?")
            
            if st.button("Confirmar Eliminación", type="primary"):
                # Eliminamos el registro del diccionario de datos
                del st.session_state.db_lotes[id_a_eliminar]
                st.error(f"💥 El lote {id_a_eliminar} fue removido del sistema.")
                st.rerun()
        else:
            st.info("No hay lotes en el sistema para eliminar.")
