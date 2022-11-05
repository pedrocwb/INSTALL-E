
import openai
import streamlit as st
from PIL import Image
from io import BytesIO
import requests



st.title('INSTALL-E - Instagram Image Generator with DALL-E')

st.info("""
🤓 The Images API is in beta. During this time the API and models will evolve based on your feedback. 
To ensure all users can prototype comfortably, the default rate limit is 10 images per minute, 25 per 5 minutes. 
""")


def create_image(text_prompt: str, n_images: int = 1, size: str = "512x512"):

    with st.spinner("Generating your awesome image"):
        response = openai.Image.create(
            prompt=text_prompt,
            n=1,
            size=size
        )
        image_url = response['data'][0]['url']
        return image_url



try:
    text = st.text_area("Type a text to generate the image")
    image_size_choice = st.selectbox("Select the image size:", ['256x256', '512x512', '1024x1024'])
    clicked = st.button("Generate Instagram Image with DALL-E")

    if clicked:
        assert len(text) > 0, "please insert the text"
        image_url = create_image(text_prompt=text, size=image_size_choice)
        
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        st.image(img)
except Exception as e:
    st.error(e, icon="🚨")





