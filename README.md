Habit Rainbow - Tracker Personal de Hábitos y Metas

Descripción

Habit Rainbow es un proyecto desarrollado en Python para el Parcial 1 de Fundamentos de Programación.

La aplicación permite crear metas personales, registrar actividades diarias y visualizar el progreso mediante gráficas interactivas. Su objetivo es convertir hábitos cotidianos como leer, estudiar, hacer ejercicio o ahorrar en estadísticas fáciles de entender y analizar.

Librería principal: Plotly

Plotly es una librería de Python que permite crear gráficas interactivas y visualizar datos de una forma más clara.

Yo utilicé Plotly Express ya que es mucho más fácil de implementar, acorta las funciones a una sola línea de código y se puede usar directamente con las tablas de Pandas.

Para este proyecto utilicé estas funciones:

px.bar() es una gráfica de barras que sirve para comparar el progreso de las diferentes metas de forma vertical, dependiendo de si se quiere ver por semana, mes o año.
px.line() la utilicé para visualizar el progreso a lo largo del tiempo, mostrando las horas registradas y si se cumplió la meta o no.
px.pie() la utilicé para mostrar la distribución del cumplimiento de las metas y poder ver de una forma más visual la comparación entre todas.


Streamlit

Streamlit la utilicé para crear la interfaz del proyecto, y en ella se realizó la mayoría de las funciones, ya que hace que editar y personalizar sea más fácil.

En mi código permite:

Mostrar las pantallas de la aplicación.
Agregar metas.
Registrar actividades diarias.
Navegar entre fechas.
Mostrar las gráficas generadas por Plotly.
Pandas

Pandas permite trabajar con datos en forma de tablas. La utilicé para organizar toda la información y para que después Plotly pudiera usar esos datos y generar las gráficas.

En este proyecto se utiliza para:

Leer y guardar información en archivos CSV.
Organizar metas y registros.
Filtrar información por fechas.
Preparar los datos antes de enviarlos a Plotly.
Datetime

Datetime permite trabajar con fechas y calendarios.

En este proyecto se utiliza para:

Obtener la fecha actual.
Calcular semanas, meses y años.
Navegar entre días anteriores y posteriores.
Realizar los cálculos de porcentaje según el período seleccionado.
Funcionalidades
Crear metas personalizadas.
Registrar actividades diarias.
Consultar progreso semanal.
Consultar progreso mensual.
Consultar progreso anual.
Visualizar estadísticas mediante gráficas interactivas.
Comparar todas las metas o analizar una meta específica.



Instalación
1. Clonar el repositorio
git clone https://github.com/tu-usuario/parcial1-habitos-.git
2. Instalar dependencias
pip install streamlit pandas plotly
3. Entrar a la carpeta del proyecto
cd "/Ruta/De/Tu/Carpeta/parcial1-habitos-"
4. Ejecutar la aplicación
streamlit run Trackerpersonal.py

La aplicación se abrirá automáticamente en:

http://localhost:8501
Autor

Desarrollado con ❤️ por Camila Ortíz.

Proyecto Final - Parcial 1 de Programación.
