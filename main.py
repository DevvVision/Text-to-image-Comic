import requests
import io
import numpy as np
from PIL import Image
import streamlit as st
def AnimeGen(text,index):
    try:
        image_bytes = A_query({
            "inputs": text,
        },index)
        image = Image.open(io.BytesIO(image_bytes))
        # Convert PIL Image to bytes in PNG format
        image_png_bytes = io.BytesIO()
        image.save(image_png_bytes, format='PNG')
        st.image(image_png_bytes, caption='Generated Image', use_column_width=True)
        st.download_button(label="Download File",data = image_png_bytes,file_name="Comic.png")
    except Exception as e:
        print(e)
        st.error(f"Error occured while displaying the image {e}")
def A_query(payload):
	response = requests.post(API_URL[md_index], headers=headers, json=payload)
	return response.content


API_URL = ["https://api-inference.huggingface.co/models/ogkalu/Comic-Diffusion","https://api-inference.huggingface.co/models/GraydientPlatformAPI/comicbabes2","https://api-inference.huggingface.co/models/Stelath/textual_inversion_comic_strip_turbo"]
headers = {"Authorization": "Bearer "+st.secrets["API-KEY"]}

st.set_page_config(
    page_title="text-to-image",
    page_icon=":santa",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.write("# **Text to Image Generator**:wave:")
# prompt = st.text_input(label="Enter your prompt here")

tab1 = st.tabs(["**Comic**"])
with tab1:
    st.write("## Comic")
    mdl_Comic = st.radio(" **Select the model** ",["Comic-Diffusion","comicbabes2","textual_inversion_comic_strip_turbo"],key="Model-selection-1")
    check1 = st.button(label="Submit", key="Model-selection-4")
prompt = st.text_input(label="Enter your prompt here",key="Model-selection-7")
if check1==True:
  if mdl_comic=="Comic-Diffusion":
    md_index=0
  elif mdl_comic=="comicbabes2":
    md_index=1
  elif mdl_comic== "textual_inversion_comic_strip_turbo":
    md_index=0
  AnimeGen(prompt,"Comic")
