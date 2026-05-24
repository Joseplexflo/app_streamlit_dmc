import streamlit as st
import numpy as np

st.title("APLICACIÓN EN STREAMLIT")
st.sidebar.title("Ejercicios")

st.write("Elaborado por: Jhonattan Josep Lezma Florida")
st.image("logo_personal.png")

st.write("Módulo 1 – Python Fundamentals")

st.write("Ingeniero jefe de proyectos en empresa de exportación textil")

st.write("2026")
st.write("Este proyecto es el desarrollo de lo aprendio en el Módulo 1 – Python Fundamentals dictado por DMC")
st.write("Tecnologías utilizadas: librerias numpy,")


sesion = st.sidebar.selectbox("Seleccione una ejercicios", ["Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if sesion == "Ejercicio 1":
  st.write("Flujo de caja con listas")
  
  
elif sesion == "Ejercicio 2":
  st.write("Registro con NumPy, arrays y DataFrame")
    
  
elif sesion == "Ejercicio 3":
  st.write("Uso de funciones desde una librería externa")
    

else:
  st.write("Uso de clases desde una librería externa con CRUD")
  
