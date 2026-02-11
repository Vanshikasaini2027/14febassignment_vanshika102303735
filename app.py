import streamlit as st
import os

st.title("YouTube Mashup Generator")

singer = st.text_input("Singer Name")
num_videos = st.number_input("Number of Videos (must be >10)", min_value=11)
duration = st.number_input("Duration (must be >20 seconds)", min_value=21)
output_name = st.text_input("Output File Name (example: mashup.mp3)")

if st.button("Generate Mashup"):
    if singer and output_name:
        command = f'python 102303735.py "{singer}" {num_videos} {duration} {output_name}'
        os.system(command)

        if os.path.exists(output_name):
            st.success("Mashup Created Successfully!")
            with open(output_name, "rb") as f:
                st.download_button("Download Mashup", f, file_name=output_name)
        else:
            st.error("Something went wrong.")
    else:
        st.warning("Please fill all fields.")
