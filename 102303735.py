# Name: Vanshika Saini
# Roll Number: 102303735
# Assignment: Mashup Program 1

import sys
import os
import yt_dlp
from pydub import AudioSegment

def download_videos(singer, num_videos):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    search_url = f"ytsearch{num_videos}:{singer} songs"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_url])

def convert_and_trim(duration):
    output_files = []

    for file in os.listdir("downloads"):
        if file.endswith(('.mp3', '.m4a', '.webm')):
            file_path = os.path.join("downloads", file)
            audio = AudioSegment.from_file(file_path)
            trimmed = audio[:duration * 1000]

            output_name = file.split('.')[0] + "_trimmed.mp3"
            trimmed.export(output_name, format="mp3")
            output_files.append(output_name)

    return output_files

def merge_audios(audio_files, output_file):
    combined = AudioSegment.empty()

    for file in audio_files:
        audio = AudioSegment.from_mp3(file)
        combined += audio

    combined.export(output_file, format="mp3")

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
    output_file = sys.argv[4]

    if num_videos <= 10:
        print("Number of videos must be greater than 10")
        sys.exit(1)

    if duration <= 20:
        print("Duration must be greater than 20 seconds")
        sys.exit(1)

    try:
        print("Downloading videos...")
        download_videos(singer, num_videos)

        print("Converting and trimming...")
        audio_files = convert_and_trim(duration)

        print("Merging files...")
        merge_audios(audio_files, output_file)

        print("Mashup created successfully!")

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
