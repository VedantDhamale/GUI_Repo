from io import BytesIO
import streamlit as st
import numpy as np
from PIL import Image, ImageColor
import cv2

# Set page configs
st.set_page_config(page_title="Crater and Boulder Detection", layout="centered")

# -------------Header Section------------------------------------------------

title = '<p style="text-align: center;font-size: 40px;font-weight: 550; "> Automatic Craters & Boulders Detection </p>'
st.markdown(title, unsafe_allow_html=True)

supported_modes = "<html> " \
                  "<body><div> <b>Supported Detection Modes (Change modes from sidebar menu)</b>" \
                  "<ul><li>Image Upload</li><li>Webcam Image Capture</li><li>Webcam Realtime Capture</li></ul>" \
                  "</div></body></html>"
st.markdown(supported_modes, unsafe_allow_html=True)

st.warning("NOTE : Click the arrow icon at Top-Left to open Sidebar menu. ")

# -------------Sidebar Section------------------------------------------------

detection_mode = None
# bounding box thickness
bbox_thickness = 3
# bounding box color
bbox_color = (0, 255, 0)

with st.sidebar:
    st.image("./assets/astral-concept-wallpaper.jpg", width=260)

    title = '<p style="font-size: 25px;font-weight: 550;">Detection System Settings</p>'
    st.markdown(title, unsafe_allow_html=True)

    # choose the mode for detection
    mode = st.radio("Choose Detection Mode", ('Image Upload', 'Webcam Image Capture'), index=0)
    if mode == 'Image Upload':
        detection_mode = mode
    elif mode == "Webcam Image Capture":
        detection_mode = mode

    # Get bbox color and convert from hex to rgb
    bbox_color = ImageColor.getcolor(str(st.color_picker(label="Bounding Box Color", value="#00FF00")), "RGB")

    # Set bbox thickness
    bbox_thickness = st.slider("Bounding Box Thickness", min_value=1, max_value=30,
                               value=bbox_thickness)

    st.info("NOTE : The quality of detection will depend on the bounding box color and thickness. "
            "Try adjusting them as needed to get the most optimal output")

# -------------Image Upload Section------------------------------------------------

if detection_mode == "Image Upload":
    uploaded_file = st.file_uploader("Upload Image (Only PNG & JPG images allowed)", type=['png', 'jpg'])
 
    if uploaded_file is not None:
        with st.spinner("Detecting craters and boulders..."):
            img = Image.open(uploaded_file)

            # To convert PIL Image to numpy array:
            img = np.array(img)

            # Placeholder for custom crater and boulder detection logic using YOLOv8/SAM
            # Example detection code should be replaced with crater detection
            # Load custom crater detection model here

            # Here, we simulate detection logic (You need to replace this with actual detection)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            detections = []  # Placeholder for detected craters/boulders as bounding boxes

            # Simulate detection by creating random bounding boxes (Replace this with actual detection results)
            for i in range(3):  # Replace with actual crater and boulder detection loop
                x, y, w, h = np.random.randint(0, 100, 4)
                detections.append((x, y, w, h))

            if len(detections) == 0:
                st.warning("No craters or boulders detected.")
            else:
                # Draw rectangle around detected craters/boulders
                for (x, y, w, h) in detections:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color=bbox_color, thickness=bbox_thickness)

                # Display the output
                st.image(img)

                if len(detections) > 1:
                    st.success(f"Total of {len(detections)} craters and boulders detected.")
                else:
                    st.success("Only 1 crater or boulder detected.")

                # Convert to PIL Image for download
                img = Image.fromarray(img)
                buffered = BytesIO()
                img.save(buffered, format="JPEG")

                # Center download button
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.download_button(
                        label="Download image",
                        data=buffered.getvalue(),
                        file_name="output.png",
                        mime="image/png")

# -------------Webcam Image Capture Section------------------------------------------------

if detection_mode == "Webcam Image Capture":
    st.info("NOTE : In order to use this mode, you need to give webcam access.")

    img_file_buffer = st.camera_input("Capture an Image from Webcam", disabled=False, key=1)

    if img_file_buffer is not None:
        with st.spinner("Detecting craters and boulders..."):
            img = Image.open(img_file_buffer)

            # To convert PIL Image to numpy array:
            img = np.array(img)

            # Placeholder for crater and boulder detection logic
            # Simulate detection logic
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            detections = []

            # Simulate detection by creating random bounding boxes (Replace with actual detection results)
            for i in range(3):  # Placeholder loop for detected objects
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

                # Download the image
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

# -------------Hide Streamlit Watermark------------------------------------------------
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

























# =========================================================
# from io import BytesIO
# import streamlit as st

# import numpy as np
# from PIL import Image, ImageColor
# from streamlit_webrtc import webrtc_streamer, RTCConfiguration
# import av
# import cv2

# # Set page configs. Get emoji names from WebFx
# st.set_page_config(page_title="Real-time Face Detection", page_icon="./assets/astral-concept-wallpaper.jpg", layout="centered")

# # -------------Header Section------------------------------------------------

# title = '<p style="text-align: center;font-size: 40px;font-weight: 550; "> Automatic Craters & Boulders Detection </p>'
# st.markdown(title, unsafe_allow_html=True)

# supported_modes = "<html> " \
#                   "<body><div> <b>Supported Detection Modes (Change modes from sidebar menu)</b>" \
#                   "<ul><li>Image Upload</li><li>Webcam Image Capture</li><li>Webcam Video Realtime</li></ul>" \
#                   "</div></body></html>"
# st.markdown(supported_modes, unsafe_allow_html=True)

# st.warning("NOTE : Click the arrow icon at Top-Left to open Sidebar menu. ")

# # -------------Sidebar Section------------------------------------------------

# detection_mode = None
# # bounding box thickness
# bbox_thickness = 3
# # bounding box color
# bbox_color = (0, 255, 0)

# with st.sidebar:
#     st.image("./assets/astral-concept-wallpaper.jpg", width=260)

#     title = '<p style="font-size: 25px;font-weight: 550;">Detection System Settings</p>'
#     st.markdown(title, unsafe_allow_html=True)

#     # choose the mode for detection
#     mode = st.radio("Choose file type for Detection Mode", ('Image Upload', 'Webcam Image Capture', 'Webcam Realtime'), index=0)
#     if mode == 'Image Upload':
#         detection_mode = mode
#     elif mode == 'Video Upload':
#         detection_mode = mode
#     elif mode == "Webcam Image Capture":
#         detection_mode = mode
#     # elif mode == 'Webcam Realtime':
#     #     detection_mode = mode

#     # Get bbox color and convert from hex to rgb
#     bbox_color = ImageColor.getcolor(str(st.color_picker(label="Bounding Box Color", value="#00FF00")), "RGB")

#     # Set bbox thickness
#     bbox_thickness = st.slider("Bounding Box Thickness", min_value=1, max_value=30,
#                                help="Sets the thickness of bounding boxes",
#                                value=bbox_thickness)

#     st.info("NOTE : The quality of detection will depend on the bounding box color and thickness."
#             " Try adjusting them as needed to get the most optimal output")

#     # line break
#     st.markdown(" ")

# # -------------Image Upload Section------------------------------------------------

# if detection_mode == "Image Upload":

#     # # Example Images
#     # col1, col2 = st.columns(2)
#     # with col1:
#     #     st.image(image="./assets/example_2.png")
#     # with col2:
#     #     st.image(image="./assets/example_3.png")

#     uploaded_file = st.file_uploader("Upload Image (Only PNG & JPG images allowed)", type=['png', 'jpg'])

#     if uploaded_file is not None:

#         with st.spinner("Detecting ..."):
#             img = Image.open(uploaded_file)

#             # To convert PIL Image to numpy array:
#             img = np.array(img)

#             # Load the cascade
#             face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#             # Convert into grayscale
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             # Detect faces
#             faces = face_cascade.detectMultiScale(gray, 1.1)

#             if len(faces) == 0:
#                 st.warning("No Face Detected in Image. Make sure your face is visible in the camera with proper lighting.")
#             else:
#                 # Draw rectangle around the faces
#                 for (x, y, w, h) in faces:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), color=bbox_color, thickness=bbox_thickness)

#                 # Display the output
#                 st.image(img)

#                 if len(faces) > 1:
#                     st.success("Total of " + str(len(faces)) + " faces detected inside the image.")

#                     # convert to pillow image
#                     img = Image.fromarray(img)
#                     buffered = BytesIO()
#                     img.save(buffered, format="JPEG")

#                     # Creating columns to center button
#                     col1, col2, col3 = st.columns(3)
#                     with col1:
#                         pass
#                     with col3:
#                         pass
#                     with col2:
#                         st.download_button(
#                             label="Download image",
#                             data=buffered.getvalue(),
#                             file_name="output.png",
#                             mime="image/png")
#                 else:
#                     st.success("Only 1 face detected inside the image.")

#                     # convert to pillow image
#                     img = Image.fromarray(img)
#                     buffered = BytesIO()
#                     img.save(buffered, format="JPEG")

#                     # Creating columns to center button
#                     col1, col2, col3 = st.columns(3)
#                     with col1:
#                         pass
#                     with col3:
#                         pass
#                     with col2:
#                         st.download_button(
#                             label="Download image",
#                             data=buffered.getvalue(),
#                             file_name="output.png",
#                             mime="image/png")

# # -------------Webcam Image Capture Section------------------------------------------------

# if detection_mode == "Webcam Image Capture":

#     st.info("NOTE : In order to use this mode, you need to give webcam access.")

#     img_file_buffer = st.camera_input("Capture an Image from Webcam", disabled=False, key=1,
#                                       help="Make sure you have given webcam permission to the site")

#     if img_file_buffer is not None:

#         with st.spinner("Detecting faces ..."):
#             # To read image file buffer as a PIL Image:
#             img = Image.open(img_file_buffer)

#             # To convert PIL Image to numpy array:
#             img = np.array(img)

#             # Load the cascade
#             face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#             # Convert into grayscale
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             # Detect faces
#             faces = face_cascade.detectMultiScale(gray, 1.1)

#             if len(faces) == 0:
#                 st.warning("No Face Detected in Image. Make sure your face is visible in the camera with proper lighting.")
#             else:
#                 # Draw rectangle around the faces
#                 for (x, y, w, h) in faces:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), color=bbox_color, thickness=bbox_thickness)

#                 # Display the output
#                 st.image(img)

#                 if len(faces) > 1:
#                     st.success("Total of " + str(len(faces)) + " faces detected inside the image.")
#                 else:
#                     st.success("Only 1 face detected inside the image.")

#                 # Download the image
#                 img = Image.fromarray(img)
#                 buffered = BytesIO()
#                 img.save(buffered, format="JPEG")
#                 # Creating columns to center button
#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     pass
#                 with col3:
#                     pass
#                 with col2:
#                     st.download_button(
#                         label="Download image",
#                         data=buffered.getvalue(),
#                         file_name="output.png",
#                         mime="image/png")

# # -------------Webcam Realtime Section------------------------------------------------

# # if detection_mode == "Webcam Realtime":

# #     # load face detection model
# #     cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# #     st.warning("NOTE : In order to use this mode, you need to give webcam access. "
# #                "After clicking 'Start' , it takes about 10-20 seconds to ready the webcam.")

# #     spinner_message = "Wait a sec, getting some things done..."

# #     with st.spinner(spinner_message):

# #         class VideoProcessor:

# #             def recv(self, frame):
# #                 # convert to numpy array
# #                 frame = frame.to_ndarray(format="bgr24")

# #                 # detect faces
# #                 faces = cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 3)

# #                 # draw bounding boxes
# #                 for x, y, w, h in faces:
# #                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

# #                 frame = av.VideoFrame.from_ndarray(frame, format="bgr24")

# #                 return frame

# #         webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
# #                         rtc_configuration=RTCConfiguration(
# #                             {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}))

# # -------------Hide Streamlit Watermark------------------------------------------------
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# -------------------------------------------------------------------------------------
