#parcial 1 
# se importan las librerias 
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Se comienza la interfaz de la pagina

st.set_page_config(page_title="Habit Rainbow", layout="centered") # le pido a la pagina que imprima el nombre  y que lo ponga al centro 

# se pide que el fondo de la interfaz sea colo rosa palo, cambie el tipo de letra para que sea basico y diseñe el titulo principal para que este en el centro
#y pido que todos los botones tengan un color rosado fuerte y cuando se pase el cursor se vuelv mas oscuro.  
# el color de las metas es un color un poco mas blaco para que contraste y se repite para las cajas de el estado de la semana
st.markdown("""
    <style> 
    .stApp {
        background-color: #fff0f3;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
    }
    
    .titulo-principal {
        color: #2c3e50;
        text-align: center;
        font-weight: 700;
        margin-bottom: 20px;
    }
    
    .stButton>button {
        background-color: #ff7695 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold !important;
    }
    
    .stButton>button:hover {
        background-color: #ff4f76 !important;
        color: white !important;
    }
    
    .tarjeta-meta {
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 10px;
    }
    
    .caja-dia {
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True) 

#archivador de  metas para que cuando comience a correr el codigo no este vacia 

if "metas" not in st.session_state:
    st.session_state.metas = {
        "Ejercicio": {"tipo": "Semanal", "medida": "Cantidad", "objetivo_cantidad": 4, "horas": 0, "minutos": 0},
        "Leer": {"tipo": "Mensual", "medida": "Tiempo", "objetivo_cantidad": 0, "horas": 1, "minutos": 30},
        "Ahorrar": {"tipo": "Mensual", "medida": "Cantidad", "objetivo_cantidad": 1, "horas": 0, "minutos": 0}
    }

# si no hay checks en registro diario se agregan checks para que no comience vacia esa parte
if "historial" not in st.session_state:
    hoy_base = datetime.now()
    st.session_state.historial = {
        (hoy_base - timedelta(days=2)).strftime("%Y-%m-%d"): ["Ejercicio"],
        (hoy_base - timedelta(days=1)).strftime("%Y-%m-%d"): ["Ejercicio", "Leer"],
        hoy_base.strftime("%Y-%m-%d"): ["Ejercicio", "Ahorrar"]
    }

# Guarda la fecha del calendario  en registro diario para saber en qué día esta el usuario
if "fecha_actual_calendario" not in st.session_state:
    st.session_state.fecha_actual_calendario = datetime.now().date()

# por default abre siempre en inicio la interfaz y guarda en que pestana del menu estas. 
    st.session_state.pantalla_navegacion = "Inicio"

# Guarda qué semana estamos en la pantalla de inicio 
if "fecha_semana_inicio" not in st.session_state:
    st.session_state.fecha_semana_inicio = datetime.now().date()


#textos en espanol, python usa los dias y meses en ingles etonces hay que traducirlos

MESES = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 
         7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Ponemos el título principal arriba de todo
st.markdown("<h1 class='titulo-principal'>Habit Rainbow</h1>", unsafe_allow_html=True)


#menu donde aparece inicio, registro diario y estadisticas a la par las 3, columnas de navegacion
col_nav1, col_nav2, col_nav3 = st.columns(3)

with col_nav1:
    # si se hace clic en inicio, cambiamos  a inicio y se refresca la pag ,  session state es como la memoria interna del navegador.
    if st.button("Inicio", use_container_width=True):
        st.session_state.pantalla_navegacion = "Inicio" # el session state de pantalla es el que hace que controle la navegacion
        st.rerun()
with col_nav2:
    # si se presiona se mueve a la pantalla donde registro diario
    if st.button("Registro Diario", use_container_width=True):  #usa el boton de registro diario
        st.session_state.pantalla_navegacion = "Registro Diario" 
        st.rerun()
with col_nav3:
    # muestra la pag de los graficos interactivos 
    if st.button("Estadísticas", use_container_width=True): #este usa streamlit con button por los botones de estadoisticas
        st.session_state.pantalla_navegacion = "Estadísticas"
        st.rerun()

st.markdown("---") # linea decorativa entre inicio y la fecha, usa markdown se usa para editar y cambiar 

#PANTALLA 1 
if st.session_state.pantalla_navegacion == "Inicio":
    hoy = datetime.now().date() # usamos la libreria para la fecha real de hoy y la ponemos bien bonita centrada
    texto_fecha_hoy = f"Hoy: {hoy.day} de {MESES[hoy.month]} de {hoy.year}"
    st.markdown(f"<h4 style='text-align: center; color: #7f8c8d;'>{texto_fecha_hoy}</h4>", unsafe_allow_html=True)
    
    st.markdown("##### Estado de la semana")
    
    base_semana = st.session_state.fecha_semana_inicio  #usa la fecha del dia de hoy y le resta la semana para ver cual es la fecha de la semana pasada y tmb  para la proxima semana 
    lunes_visualizado = base_semana - timedelta(days=base_semana.weekday()) 
    domingo_visualizado = lunes_visualizado + timedelta(days=6) 
    
    # muestra las letas o como que imprime la fecha de semana del mes, y año y lo disena 
    texto_rango_semana = f"Semana del {lunes_visualizado.day} de {MESES[lunes_visualizado.month]} al {domingo_visualizado.day} de {MESES[domingo_visualizado.month]}"
    st.markdown(f"<p style='text-align: center; font-weight: bold; color: #2980b9;'>{texto_rango_semana}</p>", unsafe_allow_html=True)
    
    # botones para ir a la semana anterior o siguiente
    col_sem_atras, col_sem_espacio, col_sem_adelante = st.columns([2, 2, 2])
    with col_sem_atras:
        if st.button("⬅ Semana Anterior", key="btn_sem_atras", use_container_width=True):
            # se resta 7 días  a la fecha de la semana y hace refresh
            st.session_state.fecha_semana_inicio = st.session_state.fecha_semana_inicio - timedelta(days=7)
            st.rerun()
    with col_sem_adelante:
        if st.button("Semana Siguiente ➡", key="btn_sem_adelante", use_container_width=True):
            #  se suma 7 días exactos a la fecha de la semana y recargamos
            st.session_state.fecha_semana_inicio = st.session_state.fecha_semana_inicio + timedelta(days=7)
            st.rerun()
            
    # estos colores pastel se usan para poner las fechas del dia de la semana de lunes, martes y asi 
    colores_dias_arcoiris = ["#ffb3ba", "#ffdfba", "#ffffba", "#baffc9", "#bae1ff", "#e8cbff", "#ffc6ff"]
    
    # se divide en columnas para los dias de la semana 
    columnas_dias = st.columns(7)
    for indice in range(7):
      
        dia_evaluado = lunes_visualizado + timedelta(days=indice) #usa la libreria de tiempo para ver el dia 
        dia_evaluado_cadena = dia_evaluado.strftime("%Y-%m-%d")
        nombre_dia_corto = DIAS_SEMANA[indice][:3] #resumimos la letra con los nombres cortos 
        
        # Revisa si en el historial de ese diahay al menos un hábito marcado
        tiene_registros = dia_evaluado_cadena in st.session_state.historial and len(st.session_state.historial[dia_evaluado_cadena]) > 0
        
        # si psuo al menos un habitp en la pag de registros se muestra en la pag de inicio con una x o un cheque  
        simbolo_marca = "✓" if tiene_registros else "✗"
        color_simbolo = "#27ae60" if tiene_registros else "#c0392b" #color de los cheques 
        fondo_dia = colores_dias_arcoiris[indice] # cada dia  tiene un color diferente del arcoitis
        
        # usa cada caja de la fecha con su color con marksown para personalizar
        with columnas_dias[indice]:
            st.markdown(f"""
            <div class='caja-dia' style='background-color: {fondo_dia};'>
                <span style='font-size: 12px; color: #2c3e50; font-weight: bold;'>{nombre_dia_corto}</span><br>
                <span style='font-size: 16px; font-weight: bold; color: #2c3e50;'>{dia_evaluado.day}</span><br>
                <span style='color: {color_simbolo}; font-size: 18px; font-weight: bold;'>{simbolo_marca}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    

    st.markdown("##### Agregar Nueva Meta") # agrega nueva meta 
    # inputs sueltos 
    nombre_nueva_meta = st.text_input("Nombre de la meta:")
    frecuencia = st.selectbox("Frecuencia:", ["Diaria", "Semanal", "Mensual", "Anual"])
    tipo_medicion = st.radio("¿Cómo vas a medir este hábito?", ["Cantidad (Veces)", "Tiempo (Horas y Minutos)"], horizontal=True)
    
    # si se pone cantidad no abre la opcion de casilla del tiempo 
    if tipo_medicion == "Cantidad (Veces)":
        objetivo_veces = st.number_input("Objetivo de veces a cumplir:", min_value=1, value=1, step=1)
        horas_configuradas = 0
        minutos_configurados = 0
    # si quiere tiempo al tocar el boton se dibujan las casillas de horas y min 
    else:
        col_horas, col_minutos = st.columns(2)
        with col_horas:
            horas_configuradas = st.number_input("Horas :", min_value=0, max_value=23, value=1, step=1)
        with col_minutos:
            minutos_configurados = st.number_input("Minutos :", min_value=0, max_value=59, value=30, step=1)
        objetivo_veces = 0
        
    # Cuando se guarda meta  se borra el texto  el texto y guardamos la meta en la memoria mas abajo
    if st.button("Guardar Meta", use_container_width=True):
        nombre_limpio = nombre_nueva_meta.strip()
        if nombre_limpio != "":
            st.session_state.metas[nombre_limpio] = {
                "tipo": frecuencia,
                "medida": "Cantidad" if tipo_medicion == "Cantidad (Veces)" else "Tiempo",
                "objetivo_cantidad": objetivo_veces,
                "horas": horas_configuradas,
                "minutos": minutos_configurados
            }
            st.success(f"Meta '{nombre_limpio}' añadida correctamente.")
            st.rerun() # se refresca para que aparezca abajo en la lista al instante
        else:
            st.warning("Por favor, escribe un nombre válido para la meta.")

    st.markdown("---")

    # lISTA DE METAS 
    st.markdown("##### Mis Metas ")
    colores_arcoiris = ["#ffadad", "#030303", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff", "#bdb2ff"]
    
    #SE LISTA todas las metas que estan guardadas en el codigo mas arriba de memoria siempre que abra la app 
    for posicion, (meta_nombre, datos) in enumerate(st.session_state.metas.items()):
        # se asigna un color del arcoíris a cada tarjeta 
        color_borde = colores_arcoiris[posicion % len(colores_arcoiris)]
        
        # se ajusta el texto que se lee segun cómo configuró el usuario su meta
        if datos["medida"] == "Cantidad":
            texto_meta_detalle = f"{datos['objetivo_cantidad']} vez/veces al periodo ({datos['tipo']})"
        else:
            texto_meta_detalle = f"{datos['horas']}h {datos['minutos']}m al periodo ({datos['tipo']})"
            
        # se crea una columna ancha para los datos y una pequeña para el botón de eliminar 
        col_tarjeta, col_eliminar = st.columns([5, 1])
        with col_tarjeta:
            # se dibuja la tarjeta blanca con un borde izquierdo de color arcoíris pastel
            st.markdown(f"""
                <div class='tarjeta-meta' style='border-left: 6px solid {color_borde};'>
                    <span style='font-weight: bold; color: #2c3e50;'>{meta_nombre}</span><br>
                    <span style='font-size: 13px; color: #7f8c8d;'>Meta: {texto_meta_detalle}</span>
                </div>
            """, unsafe_allow_html=True)
        with col_eliminar:
            st.write("") # Un pequeño espacio para centrar el botón 
            # Si se presiona eliminar, se borra esa meta 
            if st.button("Eliminar", key=f"btn_eliminar_{meta_nombre}"):
                del st.session_state.metas[meta_nombre]
                st.rerun()




# PANTALLA 2


elif st.session_state.pantalla_navegacion == "Registro Diario":
    st.markdown("##### Historial de Cumplimiento") # que si se pone en registro diario siempre aparezca historial
    
    # se crea un calendario   para que el usuario escoja un dia que queira
    fecha_elegida = st.date_input("Ir a una fecha específica:", value=st.session_state.fecha_actual_calendario)
    st.session_state.fecha_actual_calendario = fecha_elegida 
    
    # Botones interactivos para retroceder o avanzar 1 día 
    col_retroceder, col_espacio, col_avanzar = st.columns([2, 2, 2])
    with col_retroceder:
        if st.button("⬅ Día Anterior", use_container_width=True):
            st.session_state.fecha_actual_calendario = st.session_state.fecha_actual_calendario - timedelta(days=1)
            st.rerun()
    with col_avanzar:
        if st.button("Día Siguiente ➡", use_container_width=True):
            st.session_state.fecha_actual_calendario = st.session_state.fecha_actual_calendario + timedelta(days=1)
            st.rerun()
            
    # se transforma la fecha seleccionada en un texto 
    fecha_cadena = st.session_state.fecha_actual_calendario.strftime("%Y-%m-%d")
    mes_nombre_diario = MESES[st.session_state.fecha_actual_calendario.month]
    
    # se muestra la fecha  y estilizada en azul en medio de la pantalla con semana del al 
    st.markdown(f"<h3 style='text-align: center; color: #2980b9;'>{st.session_state.fecha_actual_calendario.day} / {mes_nombre_diario} / {st.session_state.fecha_actual_calendario.year}</h3>", unsafe_allow_html=True)
    
    # Si este día es nuevo y no tiene registros, le preparo una lista vacía para almacenar sus checks
    if fecha_cadena not in st.session_state.historial:
        st.session_state.historial[fecha_cadena] = []
        
    st.markdown("Marque los hábitos que lograste completar en este día:")
    
    if len(st.session_state.metas) == 0:
        st.info("No hay metas creadas en el sistema. Ve a la pestaña 'Inicio' para agregar una.")
    else:
       
        for meta_nombre in st.session_state.metas.keys(): # se genera  un Checkbox donde se pueda poner que si  por cada meta que el usuario tenga creada
            
            marcado_previo = meta_nombre in st.session_state.historial[fecha_cadena]# se busca si el hábito ya estaba marcado previamente en este día
            
            estado_checkbox = st.checkbox(f"Completé: {meta_nombre}", value=marcado_previo, key=f"chk_{meta_nombre}_{fecha_cadena}")            # se dibuja el checkbox en pantalla

            
    
            if estado_checkbox and meta_nombre not in st.session_state.historial[fecha_cadena]:# Si el usuario activa el check y no estaba guardado, lo añadimos a la lista
                st.session_state.historial[fecha_cadena].append(meta_nombre)
           
            elif not estado_checkbox and meta_nombre in st.session_state.historial[fecha_cadena]:            # Si quita el check y estaba guardado, lo removemos de la lista de inmediato

                st.session_state.historial[fecha_cadena].remove(meta_nombre)

# PANTALLA 3: 


elif st.session_state.pantalla_navegacion == "Estadísticas":
    st.markdown("##### Rendimiento y Gráficos Interactivos") # muestra esto al entrar a estadisticas 
    
    if len(st.session_state.historial) == 0 or len(st.session_state.metas) == 0:
        st.info("Necesitas tener metas configuradas y registros marcados para visualizar las estadísticas.")
    else:
       
        col_filtro1, col_filtro2 = st.columns(2) # Filtros superiores para segmentar la información por hábito o por rango de días
        with col_filtro1:
            meta_filtrada = st.selectbox("Selecciona un hábito:", ["Todos los hábitos"] + list(st.session_state.metas.keys()))
        with col_filtro2:
            rango_tiempo = st.selectbox("Rango de análisis:", ["Semanal", "Mensual", "Anual"])
            
        
        lista_temporal_datos = []
        conteo_dias_activos = 0 # Reestructuración de datos: Convertimos el diccionario del historial en una lista limpia
        
        for fecha_key, metas_completadas in st.session_state.historial.items():
            if len(metas_completadas) > 0:
                conteo_dias_activos += 1 # se cuenta cuántos días únicos ha registrado actividad el usuario
            for m in metas_completadas:
               
                lista_temporal_datos.append({"Fecha": pd.to_datetime(fecha_key), "Meta": m, "Veces": 1}) 
                
        if len(lista_temporal_datos) == 0:
            st.warning("No hay datos guardados de hábitos cumplidos todavía.")
        else:
           
            df_base = pd.DataFrame(lista_temporal_datos)
            hoy_pandas = pd.Timestamp(datetime.now().date())# Usamos pandas ya que con los datos se hace una tabla que funciona como excel y asi panda usa una tabla y leugo se conveirte a graficas. 
            
            
            if rango_tiempo == "Semanal":  # este depende del usuario elegir semana o mes o año para poder mostrar las graficas 
                df_filtrado = df_base[df_base["Fecha"] >= (hoy_pandas - pd.Timedelta(days=7))]
            elif rango_tiempo == "Mensual":
                df_filtrado = df_base[df_base["Fecha"] >= (hoy_pandas - pd.Timedelta(days=30))]
            else:
                df_filtrado = df_base[df_base["Fecha"] >= (hoy_pandas - pd.Timedelta(days=365))]

            df_resumen = df_filtrado.groupby("Meta").sum(numeric_only=True).reset_index()            # se agrupa los datos sumando las veces que se repite cada meta

            
            
            gama_colores = px.colors.qualitative.Pastel # se carga una paleta  de Plotly con  colores pastel estilo arcoíris 

            # CASO A: estadísticas globales de todo junto
            if meta_filtrada == "Todos los hábitos":
                st.markdown("###### Desglose General de Cumplimientos")
                
                # gráfico de pastel
                grafico_pastel = px.pie(df_resumen, values="Veces", names="Meta", 
                                        title="Porcentaje de hábitos realizados", 
                                        color_discrete_sequence=gama_colores)
                st.plotly_chart(grafico_pastel, use_container_width=True)

                #  gráfico de barras 
                grafico_barras = px.bar(df_resumen, x="Meta", y="Veces", 
                                        title="Veces totales completadas", 
                                        labels={"Veces": "Cantidad de Veces"},
                                        color="Meta", color_discrete_sequence=gama_colores)
                st.plotly_chart(grafico_barras, use_container_width=True)
                
                total_veces_periodo = df_filtrado.shape[0] # Cuenta cuántas filas totales pasaron el filtro
                
            # CASO B: El usuario eligió analizar un único hábito en específico
            else:
                st.markdown(f"###### Evolución en el tiempo: {meta_filtrada}")
                
                # se filtra  la tabla dejando exclusivamente las filas de ese hábito
                df_unica_meta = df_filtrado[df_filtrado["Meta"] == meta_filtrada]
                df_linea_tiempo = df_unica_meta.groupby("Fecha").sum(numeric_only=True).reset_index().sort_values("Fecha")
                
                if len(df_linea_tiempo) == 0:
                    st.info(f"No tienes registros guardados para '{meta_filtrada}' en el rango seleccionado.")
                    total_veces_periodo = 0
                else:
                    # se dibuja un gráfico de línea temporal con puntitos para ver los picos de constancia
                    grafico_linea = px.line(df_linea_tiempo, x="Fecha", y="Veces", 
                                            title=f"Cumplimiento por día de {meta_filtrada}", 
                                            labels={"Veces": "Veces Cumplidas"},
                                            markers=True)
                    st.plotly_chart(grafico_linea, use_container_width=True)
                    total_veces_periodo = df_unica_meta.shape[0]

            #  TARJETAS METRICAS 
            st.markdown("---")
            st.markdown("##### Resumen de Consistencia")
            
            col_metrica1, col_metrica2 = st.columns(2)
            with col_metrica1:
                # Muestra un cuadro limpio destacando la cantidad de días que usó la app
                st.metric(label="Días con actividad registrada", value=f"{conteo_dias_activos} días")
            with col_metrica2:
                # Muestra las veces totales que cumplió la meta, sonando amigable y motivador
                if meta_filtrada == "Todos los hábitos":
                    st.metric(label="Logros totales acumulados", value=f"{total_veces_periodo} veces")
                else:
                    st.metric(label=f"Veces completado {meta_filtrada}", value=f"{total_veces_periodo} veces")

            # Se desplega un mensaje felicitando
            if total_veces_periodo > 0:
                if meta_filtrada == "Todos los hábitos":
                    st.success(f"¡Excelente progreso general! Has interactuado en la plataforma durante {conteo_dias_activos} días y completado metas individuales un total de {total_veces_periodo} veces.")
                else:
                    st.success(f"¡Gran trabajo enfocado en {meta_filtrada}! Lograste completarlo {total_veces_periodo} veces dentro del rango {rango_tiempo.lower()}.")
