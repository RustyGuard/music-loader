import glob
import json
import os
from pathlib import Path
from time import sleep

from pytube import YouTube
from pytube.exceptions import AgeRestrictedError


def load_from_youtube_object(youtube_track: YouTube, destination_path: Path):
    output = youtube_track.streams.get_audio_only().download()
    os.rename(output, destination_path)


def load_track(youtube_id: str, destination_path: Path, rename_required: bool = False):
    # this try statement will run if the mp3 url is filled
    youtube_video_url = f"https://youtu.be/{youtube_id}"
    try:
        # creating the YouTube object and passing the the on_progress function
        audio = YouTube(youtube_video_url)

        # extracting and downloading the audio file
        output = audio.streams.get_audio_only().download()
        # this splits the audio file, the base and the extension
        base, ext = os.path.splitext(output)
        # this converts the audio file to mp3 file
        # this renames the mp3 file
        os.rename(output, destination_path)
        # popup for dispalying the mp3 downlaoded success message
        # ressetting the progress bar and the progress label
        # progress_label.config(text='')
        # progress_bar['value'] = 0
        # the except will run when an expected error occurs during downloading

    except:
        raise
        # showerror(title='Download Error', message='An error occurred while trying to ' \
        #                                           'download the MP3\nThe following could ' \
        #                                           'be the causes:\n->Invalid link\n->No internet connection\n' \
        #                                           'Make sure you have stable internet connection and the MP3 link is valid')
        # ressetting the progress bar and the progress label
        # progress_label.config(text='')
        # progress_bar['value'] = 0


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def header(msg):
        return bcolors.HEADER + msg + bcolors.ENDC

    @staticmethod
    def okblue(msg):
        return bcolors.OKBLUE + msg + bcolors.ENDC

    @staticmethod
    def okgreen(msg):
        return bcolors.OKGREEN + msg + bcolors.ENDC

    @staticmethod
    def warning(msg):
        return bcolors.WARNING + msg + bcolors.ENDC

    @staticmethod
    def fail(msg):
        return bcolors.FAIL + msg + bcolors.ENDC


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
