# from dotenv import load_dotenv,dotenv_values


# load_dotenv()
# values_env_openai = dotenv_values(".env")

# key = values_env_openai['key']
# location = values_env_openai['location']
# endpoint = values_env_openai['endpoint']
# deployment_id_gpt4=values_env_openai['deployment_id_gpt4']  


# STREAMLIT CONFIGURATION
import streamlit as st

key = st.secrets["key"]
location = st.secrets["location"]
endpoint = st.secrets["endpoint"]
deployment_id_gpt4 = st.secrets["deployment_id_gpt4"]