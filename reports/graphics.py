import altair as alt
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_vega_lite import vega_lite_component, altair_component
import chart_studio.plotly as plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from plotly import tools
import plotly.express as px
from plotly.subplots import make_subplots
import base64
#from io import BytesIO
import os


st.title('Lectoria')

def read_dataframe():
  d = {'Fecha': ["09/01/2020"], 'Unidades en las que se mide': [25],
       'Caja y bancos': [1345], 'Total activos': [120],
       'Total pasivo': [1550], 'Total patrimonio': [20500],
       'Ventas': [100], 'Costo de ventas': [300],
       'Utilidad bruta': [150], 'Utilidad operacional': [140],
       'Utilidad antes de impuestos': [120], 'Utilidad neta': [130]}
  df=pd.DataFrame(data = d )
  return df

#df = read_dataframe()

###########################################
def read_dataframe_more():
  d = {'Fecha': ["09/01/2020", "10/01/2020", "11/01/2020","12/01/2020", "13/01/2020"], 'Unidades en las que se mide': [25, 40,35,60,35],
       'Caja y bancos': [1345, 1400,1500,1750,1860], 'Total activos': [120, 112,133,122,144],
       'Total pasivo': [1550, 2300,1750,1420,1110], 'Total patrimonio': [20500, 20400,20300,1500,1250],
       'Ventas': [100, 200,300,200,100], 'Costo de ventas': [300, 400,500,150,250],
       'Utilidad bruta': [150, 220,170,180,166], 'Utilidad operacional': [300, 140,150,160,130],
       'Utilidad antes de impuestos': [120, 120,125,133,124], 'Utilidad neta': [130, 140,133,114,155]}
  df=pd.DataFrame(data = d )
  return df
########################################################################

def update_df(df):
   for name,value in df.iteritems():
       for  i in range(0,len(value)):
          if type(value[i]) == np.int64:
              value[i] = value[i]/100
   return df

def update_dolar(df):
   for name,value in df.iteritems():
       for  i in range(0,len(value)):
          if type(value[i]) == np.int64:
              value[i] = value[i]*21.13
   return df

def unidades(df):
    option = st.selectbox('¿Cómo quieres consultar tus datos?',
        ('Original', 'Miles', 'Dólar'))

    if option == 'Dólar':
            data = update_dolar(df)
            st.write(data)
    elif option =="Miles":
            data = update_df(df)
            st.write(data)
    else:
        data = df
        st.write(data)
    return option
######################################

##################################

##################################

def endeudamiento_fig(df):
    df['Endeudamiento']=df['Total pasivo']/df['Total patrimonio']
    scales = ['<b>Endeudamiento</b>']
    scale1 = ['Muy <br> sana ', 'Sana',
               'Neutral ',
              'Endeudada',
              'Muy <br> endeudada ']
    scale_labels = [scale1]

    traces = []
    for i in range(len(scales)):
        traces.append(go.Scatter(
            x=[0.65], # Pad the title - a longer scale title would need a higher value
            y=[6.25],
            text=scales[i],
            mode='text',
            hoverinfo='none',
            showlegend=False,
            xaxis='x'+str(i+1),
            yaxis='y'+str(i+1)
        ))

    # Create Scales
    ## y0  y y1:5 (depende del número de -)
    shapes = []
    for i in range(len(scales)):
        shapes.append({'type': 'rect',
                       'x0': .02, 'x1': 1.2,
                       'y0': 0, 'y1': 5,
                       'xref':'x'+str(i+1), 'yref':'y'+str(i+1)})

    x_domains = [[0,.25 ]] # Split for 4 scales
    chart_width = 350


    # Define X-Axes
    xaxes = []
    for i in range(len(scales)):
        xaxes.append({'domain': x_domains[i], 'range':[0, 1.2],
                      'showgrid': False, 'showline': False,
                      'zeroline': False, 'showticklabels': False})

    ## for more information see: https://plotly.com/python/reference/#layout-yaxis-ticklen
    yaxes = []
    for i in range(len(scales)):
        yaxes.append({'anchor':'x'+str(i+1), 'range':[0,1.2],
                      'showgrid': False, 'showline': False, 'zeroline': False,
                      'ticks':'inside', 'ticklen': chart_width/20,
                      'ticktext':scale_labels[i], 'tickvals':[1.2,.90,.65,.35,0]
                     })

    # Put all elements of the layout together
    layout = {'shapes': shapes,
              'xaxis1': xaxes[0],
              'yaxis1': yaxes[0],
              'autosize': True,
              'width': chart_width,
              'height': 500
    }

    ratings = [df['Endeudamiento'][0]]

    for i in range(len(ratings)):
        traces.append(go.Scatter(
                x=[0.5], y=[ratings[i]],
                xaxis='x'+str(i+1), yaxis='y'+str(i+1),
                mode='markers', marker={'size': 16, 'color': '#29ABD6'},
                text=ratings[i], hoverinfo='text', showlegend=False
        ))

    fig = dict(data=traces, layout=layout)
    fig = go.Figure(data=traces,
                    layout=layout)
    return fig


def solvencia_fig(df):
    df['Solvencia']=df['Total activos']/df['Total pasivo']
    scales = ['<b>Solvencia</b>']
    scale1 = ['Muy <br> sana ', 'Solvente',
               'Neutral ',
              'Insolvente',
              'Muy <br> insolvente ']

    scale_labels = [scale1]

    traces = []
    for i in range(len(scales)):
        traces.append(go.Scatter(
            x=[0.65], # Pad the title - a longer scale title would need a higher value
            y=[6.25],
            text=scales[i],
            mode='text',
            hoverinfo='none',
            showlegend=False,
            xaxis='x'+str(i+1),
            yaxis='y'+str(i+1)
        ))
    shapes = []
    for i in range(len(scales)):
        shapes.append({'type': 'rect',
                       'x0': .02, 'x1': 2.0,
                       'y0': 0, 'y1': 5,
                       'xref':'x'+str(i+1), 'yref':'y'+str(i+1)})

    x_domains = [[0,.25 ]] # Split for 4 scales
    chart_width = 350
    xaxes = []
    for i in range(len(scales)):
        xaxes.append({'domain': x_domains[i], 'range':[0, 2.0],
                      'showgrid': False, 'showline': False,
                      'zeroline': False, 'showticklabels': False})

    yaxes = []
    for i in range(len(scales)):
        yaxes.append({'anchor':'x'+str(i+1), 'range':[0,2.0],
                      'showgrid': False, 'showline': False, 'zeroline': False,
                      'ticks':'inside', 'ticklen': chart_width/20,
                      'ticktext':scale_labels[i], 'tickvals':[ 2.0, 1.50, .75, .25, 0]
                     })

    layout = {'shapes': shapes,
              'xaxis1': xaxes[0],
              'yaxis1': yaxes[0],
              'autosize': True,
              'width': chart_width,
              'height': 500
    }

    ratings = [df['Solvencia'][0]]

    for i in range(len(ratings)):
        traces.append(go.Scatter(
                x=[0.5], y=[ratings[i]],
                xaxis='x'+str(i+1), yaxis='y'+str(i+1),
                mode='markers', marker={'size': 16, 'color': '#29ABD6'},
                text=ratings[i], hoverinfo='text', showlegend=False
        ))

    fig = dict(data=traces, layout=layout)
    fig = go.Figure(data=traces,
                    layout=layout)
    return fig
    #st.plotly_chart(fig11)

def get_plotly_subplots(data):
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(st.plotly_chart(endeudamiento_fig(data)),
        col=None,row=None,)
    fig.add_trace(st.plotly_chart(solvencia_fig(data)),
        col=1,row=2,)
    return fig

#####################################################################

# def ventas_plot(df):
#     source = df
#     source.index = source.Fecha
#     fig1 = st.line_chart(df["Ventas"])
#     #st.write(fig1)
#     return fig1

#if st.checkbox("Visualizar utilidades"):
def visual_utilidades(df):
    source = df
    source.index = source.Fecha
    source.drop(['Fecha','Unidades en las que se mide', 'Caja y bancos',
       'Total activos', 'Total pasivo', 'Total patrimonio', 'Ventas',
       'Costo de ventas'], axis='columns', inplace=True) #'Endeudamiento','Solvencia',
    #source.drop(['Fecha'], axis='columns', inplace=True)
    source = source.reset_index().melt('Fecha', var_name='Categoria', value_name='Totales')

    # Create a selection that chooses the nearest point & selects based on x-value
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                            fields=['Fecha'], empty='none')

    # The basic line
    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x=('Fecha'),
        y=('Totales'),
        color='Categoria:N'
    )

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(source).mark_point().encode(
        x=('Fecha'),
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'Totales:Q', alt.value(' '))
    )

    # Draw a rule at the location of the selection
    rules = alt.Chart(source).mark_rule(color='gray').encode(
        x=('Fecha')
    ).transform_filter(
        nearest
    )

    # Put the five layers into a chart and bind the data
    fig2 = alt.layer(
        line, selectors, points, rules, text
    ).properties(
        width=600, height=300
    )
    #st.altair_chart(fig2, use_container_width=True)
    return fig2


def visual_totales(data):
    source = data
    source.index = source.Fecha
    source.drop(['Fecha', 'Unidades en las que se mide', 'Caja y bancos', 'Ventas',
       'Costo de ventas','Utilidad bruta', 'Utilidad operacional',
       'Utilidad antes de impuestos', 'Utilidad neta'], axis='columns', inplace=True)
    source = source.reset_index().melt('Fecha', var_name='Categoria', value_name='Totales')
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                            fields=['Fecha'], empty='none')
    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x=('Fecha'),
        y=('Totales'),
        #y = 'Totales:Q',
        color='Categoria:N'
    )

    selectors = alt.Chart(source).mark_point().encode(
        x=('Fecha'),
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'Totales:Q', alt.value(' '))
    )
    rules = alt.Chart(source).mark_rule(color='gray').encode(
        x=('Fecha'),
    ).transform_filter(
        nearest
    )
    fig3 = alt.layer(
        line, selectors, points, rules, text
    ).properties(
        width=600, height=300
    )

    #st.altair_chart(fig3, use_container_width=True)
    return fig3

############################
def margen_frame(source):
    df=pd.DataFrame(columns=("Fecha","Empresa","Ventas","Margen neto","Margen bruto"))
    for i in range(0,len(source)):
        Empresa = i
        Fecha = source["Fecha"][i]
        Utilidad = source["Utilidad neta"][i]
        Ventas = source["Ventas"][i]
        Coste = source["Costo de ventas"][i]
        Margen_neto = Utilidad/Ventas
        Margen_bruto = (Ventas-Coste)/Ventas
        df.loc[len(df)]=[Fecha,Empresa,Ventas,Margen_neto,Margen_bruto]
    df.index = df.Fecha
    return df

def margen_one(source, Empresa):
    key = Empresa
    Utilidad = source["Utilidad neta"][key]
    Ventas = source["Ventas"][key]
    Coste = source["Costo de ventas"][key]
    Margen_neto = Utilidad/Ventas
    Margen_bruto = (Ventas-Coste)/Ventas
    return Margen_neto, Margen_bruto
#if st.checkbox("Margen neto"):
def margen_neto(df):
    source = margen_frame(df)
    brush = alt.selection(type='interval')
    points = alt.Chart(source).mark_point().encode(
            x='Ventas',
            y=('Margen neto'),
            color=alt.condition(brush,'Empresa:N', alt.value('lightgray')),
            ).add_selection(brush)

    bars = alt.Chart(source).mark_bar().encode(
        y='Ventas:N',
        color='Ventas',
        x='count(Ventas):Q'
    ).transform_filter(
        brush
    )

    fig4 = points & bars
    st.altair_chart(fig4, use_container_width=True)
    return fig4

#if st.checkbox("Margen bruto"):
def margen_bruto(df):
    source = margen_frame(df)
    brush = alt.selection(type='interval')
    points = alt.Chart(source).mark_point().encode(
            x='Ventas',
            y=('Margen bruto'),
            color=alt.condition(brush,'Empresa:N', alt.value('lightgray')),
            ).add_selection(brush)

    bars = alt.Chart(source).mark_bar().encode(
        y='Ventas:N',
        color='Ventas',
        x='count(Ventas):Q'
    ).transform_filter(
        brush
    )

    fig5 = points & bars
    st.altair_chart(fig5, use_container_width=True)
    return fig5
######################################################

def option_graphics(option):
    if option == 'Archivo':
        data = read_dataframe()
        Empresa = 0
        Margen_neto, Margen_bruto = margen_one(data, Empresa)
        st.subheader('Información encontrada')
        st.write(unidades(data))
        st.header("Graficador")
        st.markdown("Un solo archivo")
        st.plotly_chart(endeudamiento_fig(data))
        st.write("Margen neto % "+ str(Margen_neto))
        st.plotly_chart(solvencia_fig(data))
        st.write("Margen bruto % "+ str(Margen_bruto))
        #st.write(get_plotly_subplots(data))
        return data

def option_graphics_various(option):
    if option == 'Varios archivos':
        data = read_dataframe_more()
        st.write(unidades(data))
        st.header("Graficador")
        st.markdown("Varios archivos")
        st.altair_chart(visual_utilidades(data),use_container_width=True)
        data_update = read_dataframe_more()
        st.altair_chart(visual_totales(data_update),use_container_width=True)
        return data

files_names=["archivo1","archivo2","archivo3"]
if len(files_names)== 1:
    option = 'Archivo'
    vista = option_graphics(option)
else:
    if st.checkbox("Varios archivos", value = False):
        option = "Varios archivos"
        vista = option_graphics_various(option)
    for file in files_names:
        if st.checkbox(file,value = False):
            option = 'Archivo'
            vista = option_graphics(option)
