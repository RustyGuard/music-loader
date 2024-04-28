from pathlib import Path

from pytube import YouTube

from api.load_audio import load_from_youtube_object
from utils.colors import bcolors
from utils.create_result_folder import create_result_folder


def main():
    youtube_url = input("Вставьте url youtube видео: ")

    youtube_object = YouTube(youtube_url)

    destination_path = Path("result") / f"{youtube_object.title} - {youtube_object.author}.mp4"
    print("Идёт скачивание...")

    create_result_folder()
    load_from_youtube_object(youtube_object, destination_path)

    print(bcolors.okgreen(f"Файл сохранён в {destination_path.resolve()}"))


if __name__ == '__main__':
    main()
