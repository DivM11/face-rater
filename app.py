#!/usr/bin/env python

import base64
from PIL import Image
import streamlit as st

from detect import FaceRater

def get_img_obj(img_path):
    return base64.b64encode(open(img_path, "rb").read()).decode()

def add_icon(icon_paths):
    st.markdown(
            f"""
            <p float="left">
            <img src="data:image/png;base64,{get_img_obj(icon_paths[0])}" width="100" />
            <img src="data:image/png;base64,{get_img_obj(icon_paths[1])}" width="100" /> 
            </p>
            """,
            unsafe_allow_html=True
        )
    # st.markdown(
    #     f"""
    #     <div class="container">
    #         <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    #         <p class="logo-text">{icon_text}</p>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

def add_rating_icons(rating):
    md = """<p float="center">\n"""
    md += f"""<img src="data:image/png;base64,{get_img_obj("./icons/star.png")}" width="100" />\n"""*int(rating//1)
    rem = rating%1
    if rem > 0.25 and rem < 0.75:
        md += f"""<img src="data:image/png;base64,{get_img_obj("./icons/half-star.png")}" width="100" />\n"""
    elif rem >= 0.75:
        md += f"""<img src="data:image/png;base64,{get_img_obj("./icons/star.png")}" width="100" />\n"""
    md += "</p>"
    st.markdown(md,unsafe_allow_html=True)

def main():
    add_icon(icon_paths=["icons/man.png","icons/woman.png"])
    st.title("Face Rater")
    img_opt = st.selectbox("Image",options=["Camera","Upload"])
    if img_opt=="Camera":
        img_file_buffer = st.camera_input("Upload Your Photo")
    else:
        img_file_buffer = st.file_uploader("Upload Your Photo")
    if img_file_buffer is not None:
        pred_flag = st.button("Predict Beauty Score")
        if pred_flag is not None:
            img = Image.open(img_file_buffer)
            mod, rating = FaceRater.detect_face(pil_img=img)
            st.image(mod)
            add_rating_icons(rating)

main()