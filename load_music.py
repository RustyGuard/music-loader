import glob
import json
import os
from pathlib import Path
from time import sleep

from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

from api.load_audio import load_from_youtube_object
from utils.colors import bcolors


def load_all_music():
    for i, file in enumerate(glob.glob('result/*.json'), 1):
        print(f"{i}) ", end="")
        file = Path(file)
        music_file_path = file.parent / f"{file.stem}.mp3"

        with open(file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        if music_file_path.exists():
            print(bcolors.okblue(f"Трек '{json_data['author']} - {json_data['title']}' уже скачан"))
            continue

        try:
            youtube_id = json_data['links'][0]
            youtube_video_url = f"https://youtu.be/{youtube_id}"
            track = YouTube(youtube_video_url)

            rename_required = json_data.get('rename', False)
            if rename_required:
                json_data['author'] = track.author
                json_data['title'] = track.title
                new_file = file.parent / f"{json_data['author']} - {json_data['title']}.json"
                with open(new_file, 'w', encoding='utf-8') as new_file_writer:
                    json.dump(json_data, new_file_writer)
                file.unlink()
                file = new_file
                music_file_path = file.parent / f"{file.stem}.mp3"

            load_from_youtube_object(track, music_file_path)
            print(bcolors.okgreen(f"Трек '{json_data['author']} - {json_data['title']}' скачан"))
        except AgeRestrictedError:
            print(bcolors.fail(f"{json_data['author']} - {json_data['title']} ограничен по возрасту!"))

        sleep(3)


if __name__ == '__main__':
    load_all_music()
