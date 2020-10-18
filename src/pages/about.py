"""Home page shown when the user enters the application"""
import streamlit as st
import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
	"""Used to write the page in the app.py file"""
	with st.spinner("Loading About ..."):
		st.title("The Team")
		st.markdown(
		"""## Members
		Inlcude a picture, name, position and social media of every member in this section.
		Get some HTML and CSS code for a cool design. 
		""", unsafe_allow_html=True)

	col1, col2, col3 = st.beta_columns(3)

	with col1:
		st.image("https://media-exp1.licdn.com/dms/image/C4D03AQEWjl01HtrIOw/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=i1tgC_RQNnz-oCU2UwHAa12ISroWa97UqLeFNbLF0zs", 
		caption='Member 1', 
		use_column_width=True)
		st.image("https://media-exp1.licdn.com/dms/image/C4E03AQEuA7kDQxfaQQ/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=R25KbguTcSDw4mrEWKwTj7uOXbvApn2YHnyDswKTlMk", caption='Member 4', 
		use_column_width=True)

	with col2:
		st.image("https://media-exp1.licdn.com/dms/image/C4E03AQG3Xd2E2bYdCA/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=FK05LTdViOsTeg7SQDwrvBPIV0xNtGek4rFtUUHbLN8", caption='Member 2', 
		use_column_width=True)
		st.image("https://media-exp1.licdn.com/dms/image/C4E03AQEeoadg3Y1JZA/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=ffvQ4mC6hTQocSZ-eLkiV_GqrNiy8_4YIfGKv0sfcw0", caption='Member 5', 
		use_column_width=True)

	with col3:
		st.image("https://media-exp1.licdn.com/dms/image/C4D03AQGPOKVV7xsBww/profile-displayphoto-shrink_800_800/0?e=1608163200&v=beta&t=OPhC6yrNIcOlyFca0kOxXJVKdv5YzX-GUNt3C6iG6UI", caption='Member 3', 
		use_column_width=True)
		st.image("https://media-exp1.licdn.com/dms/image/C4E03AQG7YCScE8kvgw/profile-displayphoto-shrink_200_200/0?e=1608163200&v=beta&t=H1kx3ERmNRtnKDSW4fCA_hmpzyzbXDtOSLRmvLfVTS8", caption='Member 6', 
		use_column_width=True)