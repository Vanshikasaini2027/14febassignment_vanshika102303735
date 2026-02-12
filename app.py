import streamlit as st
import subprocess
import os

st.title("YouTube Mashup Generator")

singer = st.text_input("Singer Name")
num_videos = st.number_input("Number of Videos (>10)", min_value=11)
duration = st.number_input("Duration (>20 seconds)", min_value=21)
output_name = st.text_input("Output File Name (example: mashup.mp3)")

if st.button("Generate Mashup"):
    if singer and output_name:
        command = [
            "python",
            "102303735.py",
            singer,
            str(num_videos),
            str(duration),
            output_name
        ]

        try:
            subprocess.run(command, check=True)

            if os.path.exists(output_name):
                st.success("Mashup Generated Successfully!")
                with open(output_name, "rb") as f:
                    st.download_button("Download Mashup", f, file_name=output_name)
            else:
                st.error("Mashup file not created.")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please fill all fields.")
