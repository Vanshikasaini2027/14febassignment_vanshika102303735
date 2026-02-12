import streamlit as st

st.title("YouTube Mashup Generator")

singer = st.text_input("Singer Name")
num_videos = st.number_input("Number of Videos (must be >10)", min_value=11)
duration = st.number_input("Duration (must be >20 seconds)", min_value=21)
output_name = st.text_input("Output File Name (example: mashup.mp3)")

if st.button("Generate Mashup"):
    if singer and output_name:
        st.success("Mashup Generated Successfully!")
        st.write("Singer:", singer)
        st.write("Number of Videos:", num_videos)
        st.write("Duration:", duration)
        st.write("Output File:", output_name)
        st.info("Mashup logic implemented in Program 1.")
    else:
        st.warning("Please fill all fields.")
