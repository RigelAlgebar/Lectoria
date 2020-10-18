
"""Home page shown when the user enters the application"""
import streamlit as st
import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
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

    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        #st.markdown("<h1 style='text-align: center; color: black;'>LECTORIA</h1>", unsafe_allow_html=True)
        st.image("src/static/images/baner.png",use_column_width=True)
        #st.title("LECTORIA")
        st.write(
"""

##  Lectoria es una aplicación que le permite a tu empresa superar los procesos manuales ofreciendo la extración y el análisis de documentos escaneados de manera automática.






"""
                )
        st.image("src/static/images/diagrama.png",use_column_width=True)

        st.write(
"""



Dentro de las empresas existe la necesidad de extraer información de estados financieros para su análisis y la toma de decisiones. Para superar estos procesos manuales hemos encontrado la  solución con un lector de imágenes que te permite visualizar únicamente la información que deseas obtener de los estados financieros y adicionalmente provee de un reporte que contiene los analíticos óptimos para generar una síntesis sobre la situación de la empresa analizada.
"""
                    )

        ast.shared.components.video_youtube(
                src="https://www.youtube.com/embed/G7ykOxP2Glg"
            )


    st.title("El equipo de Lectoria")
    st.markdown(
        """##
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.image("https://media-exp1.licdn.com/dms/image/C4D03AQEWjl01HtrIOw/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=i1tgC_RQNnz-oCU2UwHAa12ISroWa97UqLeFNbLF0zs",
        caption='Andrea Monserrat', use_column_width=True)
        st.image("https://media-exp1.licdn.com/dms/image/C4E03AQEuA7kDQxfaQQ/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=R25KbguTcSDw4mrEWKwTj7uOXbvApn2YHnyDswKTlMk", caption='Liliana Argüello',
        use_column_width=True)

    with col2:
        st.image("https://media-exp1.licdn.com/dms/image/C4E03AQG3Xd2E2bYdCA/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=FK05LTdViOsTeg7SQDwrvBPIV0xNtGek4rFtUUHbLN8", caption='César Campuzano',
        use_column_width=True)
        st.image("https://media-exp1.licdn.com/dms/image/C4E03AQEeoadg3Y1JZA/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=ffvQ4mC6hTQocSZ-eLkiV_GqrNiy8_4YIfGKv0sfcw0", caption='Mariana García',
        use_column_width=True)

    with col3:
        st.image("https://media-exp1.licdn.com/dms/image/C4D03AQGPOKVV7xsBww/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=OPhC6yrNIcOlyFca0kOxXJVKdv5YzX-GUNt3C6iG6UI", caption='Claudia Trejo',
        use_column_width=True)
        st.image("https://media-exp1.licdn.com/dms/image/C4E03AQG7YCScE8kvgw/profile-displayphoto-shrink_200_200/0?e=1608163200&v=beta&t=H1kx3ERmNRtnKDSW4fCA_hmpzyzbXDtOSLRmvLfVTS8", caption='Miguel Magaña',
        use_column_width=True)
