"""Home page shown when the user enters the application"""
import streamlit as st
import streamlit.components.v1 as components
import awesome_streamlit as ast
from typing import Dict
import pandas as pd
import numpy as np
import time
import os
import base64

from src.pages.utils import upload_to_aws
from reports.graphics import option_graphics, option_graphics_various
S3BUCKETNAME = "lechatnoir"



df = pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
	})



@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store
    the files uploaded"""
    return {}


def write():
	"""Used to write the page in the app.py file"""
	st.markdown(f"""
	<style>
	.reportview-container .main .block-container{{
		max-width: 1250px;
		padding-top: 2rem;
		padding-right: 2rem;
		padding-left: 2rem;
		padding-bottom: 2rem;
		}}
	.reportview-container .main {{
	color: black;
	background-color: white;
	}}
	</style>
	""",
	unsafe_allow_html=True,
	)


	with st.spinner("Loading the Dashboard ..."):
		st.markdown("<h1 style='text-align: center; color: black;'>Analytics Dashboard</h1>", unsafe_allow_html=True)
		#st.title("Analytics Dashboard")
		st.write(
"""
Esta interfaz le permitirá procesar documentos en una mínima fracción de tiempo comparado con la transcripción manual.
-Inserte uno o varios documentos PDF en el área designada para ello y espere la respuesta.
-No debe demorar más de 1 minuto por archivo.
## Uso
Visualize además de sus resultados obtenidos  a través de OCR con AWS, estadísticas y descripción del estado económico de las empresas evaluadas.
También ofrece resultados para un solo archivo.
"""
				)


		st.write(
		"""
		### Arrastra en la siguiente caja o da click en "Browse files" para
		seleccionar los archivos que deseas procesar.
		"""		)

		static_store = get_static_store()
		uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True, height=500)

		for uploaded_file in uploaded_files:
			if uploaded_file.name not in files_names: files_names.append(uploaded_file.name)
			st.write("Filename:", uploaded_file.name)
			bytes_file = uploaded_file.read()
			f = open("files/"+uploaded_file.name, "wb")
			#f.write(bytes_file)
			f.close()
			upload_to_aws(r"files/"+uploaded_file.name, S3BUCKETNAME, uploaded_file.name)
			os.remove("files/"+uploaded_f)


		components.html("""<hr>""")

		st.write(
		"""
		# Resultados.
		"""		)
		if len(uploaded_files)== 1:
		    option = 'Archivo'
		    vista = option_graphics(option)
		else:
		    if st.checkbox("Varios archivos", value = False):
		        option = "Varios archivos"
		        vista = option_graphics_various(option)
		    for file in uploaded_files:
		        if st.checkbox(file,value = False):
		            option = 'Archivo'
		            vista = option_graphics(option)


		#col1, col2, col3 = st.beta_columns(3)

		#with col1:
		#	static_store = get_static_store()
		#	uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
		#	for uploaded_file in uploaded_files:
		#		st.write("filename:", uploaded_file.name)
		#		upload_to_aws(uploaded_file.name, S3BUCKETNAME, uploaded_file.name)

		#with col3:
		#	st.text("")
		#	st.text("")
		#	st.button("Analisis Basico")
		#	st.text("")
		#	st.button("Analisis Pro")

		# st.write(
		# """
		# ## Tabla generadas a partir de tus archivos.
		# """		)
		# components.html("""<hr>""")

		d = {'Fecha': ["10/01/2020", "10/01/2020", "11/01/2020","11/01/2020", "12/01/2020"], 'Unidades en las que se mide': [25, 40,35,60,35],
		'Caja y bancos': [1345, 1400,1500,1750,1860], 'Total activos': [120, 112,133,122,144],
		'Total pasivo': [1550, 2300,1750,1420,1110], 'Total patrimonio': [20500, 20400,20300,1500,1250],
		'Ventas': [100, 200,300,200,100], 'Costo de ventas': [300, 400,500,150,250],
		'Utilidad bruta': [150, 220,170,180,166], 'Utilidad operacional': [300, 140,150,160,130],
		'Utilidad antes de impuestos': [120, 120,125,133,124], 'Utilidad neta': [130, 140,133,114,155]}

		df=pd.DataFrame(data = d )
		#df.astype(float)


		#st.write(df)

		components.html("""<hr>""")
		left_column, right_column = st.beta_columns(2)

		with left_column:
			chart_data = pd.DataFrame(
				np.random.randn(20, 3),
				columns=['a', 'b', 'c'])


		with right_column:
			map_data = pd.DataFrame(
				np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
				columns=['lat', 'lon'])

		def get_table_download_link(df):
		    """Generates a link allowing the data in a given panda dataframe to be downloaded
		    in:  dataframe
		    out: href string
		    """
		    csv = df.to_csv(index=False)
		    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
		    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'


		if st.button('descarga'):
    			result = get_table_download_link(df)



		#if st.checkbox('Show dataframe'):
		#	chart_data2 = pd.DataFrame(
		#	np.random.randn(20, 3),
		#	columns=['a', 'b', 'c'])

		#	st.line_chart(chart_data2)

		#option = st.selectbox(
		#'Which number do you like best?',
		#df['first column'])
		#'You selected: ', option



		#pressed = left_column.button('Press me?')
		#if pressed:
		#	right_column.write("Woohoo!")

		#expander = st.beta_expander("FAQ")
		#expander.write("Here you could put in some really, really long explanations...")


		# Add a placeholder
		latest_iteration = st.empty()
		bar = st.progress(0)


		#for i in range(100):
  		# Update the progress bar with each iteration.
  		#	latest_iteration.text(f'Iteration {i+1}')
  		#	bar.progress(i + 1)
  		#	time.sleep(0.1)

		#st.write('...and now we\'re done!')
