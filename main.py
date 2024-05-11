import requests
import io
import numpy as np
from PIL import Image
import streamlit as st
def comicgen(text):
    try:
        image_bytes = C_query({
            "inputs": text,
        })
	if(md_index==0) or (md_index==2):
		image = Image.open(io.BytesIO(image_bytes))
		image_byt = io.BytesIO(image_bytes)
		print(type(image))
		print(type(image_byt))
		st.image(image, caption='Generated Image')
	else:
		image_byt = io.BytesIO(image_bytes)
		print(type(image))
		print(type(image_byt))
		st.image(image, caption='Generated Image')
        st.download_button(label="Download File", data=image_byt, file_name="Anime.jpeg")
    except Exception as e:
        print(e)
        st.error(f"Error occured while displaying the image {e}")
def C_query(payload):
	response = requests.post(C_API_URL[md_index], headers=headers, json=payload)
	return response.content


C_API_URL = ["https://api-inference.huggingface.co/models/ogkalu/Comic-Diffusion","https://api-inference.huggingface.co/models/GraydientPlatformAPI/comicbabes2","https://api-inference.huggingface.co/models/Stelath/textual_inversion_comic_strip_turbo"]
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
st.write("## Comic")
mdl_Comic = st.radio(" **Select the model** ",["Comic-Diffusion","comicbabes2","textual_inversion_comic_strip_turbo"],key="Model-selection-1")
check1 = st.button(label="Submit", key="Model-selection-4")
prompt = st.text_input(label="Enter your prompt here",key="Model-selection-7")
if check1==True:
  if mdl_Comic=="Comic-Diffusion":
    md_index=0
  elif mdl_Comic=="comicbabes2":
    md_index=1
  elif mdl_Comic== "textual_inversion_comic_strip_turbo":
    md_index=2
  comicgen(prompt)
