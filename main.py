from io import BytesIO
import streamlit as st
import numpy as np
from PIL import Image, ImageColor
import cv2

st.set_page_config(page_title="Crater and Boulder Detection", layout="centered")

title = '<p style="text-align: center;font-size: 40px;font-weight: 550; "> Automatic Craters & Boulders Detection </p>'
st.markdown(title, unsafe_allow_html=True)

supported_modes = "<html> " \
                  "<body><div> <b>Supported Detection Modes (Change modes from sidebar menu)</b>" \
                  "<ul><li>Image Upload</li><li>Webcam Image Capture</li></ul>" \
                  "</div></body></html>"
st.markdown(supported_modes, unsafe_allow_html=True)

detection_mode = None
bbox_thickness = 3
bbox_color = (0, 255, 0)

with st.sidebar:
    st.image("./assets/astral-concept-wallpaper.jpg", width=260)

    title = '<p style="font-size: 25px;font-weight: 550;">Detection System Settings</p>'
    st.markdown(title, unsafe_allow_html=True)

    mode = st.radio("Choose Detection Mode", ('Image Upload', 'Webcam Image Capture'), index=0)
    if mode == 'Image Upload':
        detection_mode = mode
    elif mode == "Webcam Image Capture":
        detection_mode = mode

    bbox_color = ImageColor.getcolor(str(st.color_picker(label="Bounding Box Color", value="#00FF00")), "RGB")

    bbox_thickness = st.slider("Bounding Box Thickness", min_value=1, max_value=30,
                               value=bbox_thickness)

    # st.info()

if detection_mode == "Image Upload":
    uploaded_file = st.file_uploader("Upload Image (Only PNG & JPG images allowed)", type=['png', 'jpg'])
 
    if uploaded_file is not None:
        with st.spinner("Detecting craters and boulders..."):
            img = Image.open(uploaded_file)

            img = np.array(img)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            detections = []  
            
            for i in range(3):  
                x, y, w, h = np.random.randint(0, 100, 4)
                detections.append((x, y, w, h))

            if len(detections) == 0:
                st.warning("No craters or boulders detected.")
            else:
                for (x, y, w, h) in detections:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color=bbox_color, thickness=bbox_thickness)

                st.image(img)

                if len(detections) > 1:
                    st.success(f"Total of {len(detections)} craters and boulders detected.")
                else:
                    st.success("Only 1 crater or boulder detected.")
                    
                img = Image.fromarray(img)
                buffered = BytesIO()
                img.save(buffered, format="JPEG")

                col1, col2, col3 = st.columns(3)
                with col2:
                    st.download_button(
                        label="Download image",
                        data=buffered.getvalue(),
                        file_name="output.png",
                        mime="image/png")

#for webcam capture
if detection_mode == "Webcam Image Capture":
    st.info("NOTE : In order to use this mode, you need to give webcam access.")

    img_file_buffer = st.camera_input("Capture an Image from Webcam", disabled=False, key=1)

    if img_file_buffer is not None:
        with st.spinner("Detecting craters and boulders..."):
            img = Image.open(img_file_buffer)

            img = np.array(img)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            detections = []

            for i in range(3):  
                x, y, w, h = np.random.randint(0, 100, 4)
                detections.append((x, y, w, h))

            if len(detections) == 0:
                st.warning("No craters or boulders detected.")
            else:
                for (x, y, w, h) in detections:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color=bbox_color, thickness=bbox_thickness)

                st.image(img)

                if len(detections) > 1:
                    st.success(f"Total of {len(detections)} craters and boulders detected.")
                else:
                    st.success("Only 1 crater or boulder detected.")

                img = Image.fromarray(img)
                buffered = BytesIO()
                img.save(buffered, format="JPEG")

                col1, col2, col3 = st.columns(3)
                with col2:
                    st.download_button(
                        label="Download image",
                        data=buffered.getvalue(),
                        file_name="output.png",
                        mime="image/png")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
