import os
from pathlib import Path

from pytube import YouTube


def load_by_video_id(video_id: str, destination_path: Path):
    youtube_video_url = f"https://youtu.be/{video_id}"

    audio = YouTube(youtube_video_url)

    load_from_youtube_object(audio, destination_path)


def load_from_youtube_object(youtube_track: YouTube, destination_path: Path):
    output = youtube_track.streams.get_audio_only().download()
    os.rename(output, destination_path)