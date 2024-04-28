import json
from pathlib import Path

from pytube import Playlist


def get_playlist_songs(playlist_url: str):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        song_id = video_url.split('?v=', 1)[-1]
        print(song_id)
        result_file_path = Path("result") / f"{song_id}.json"
        with open(result_file_path, "w", encoding='utf-8') as result_file:
            result_file_contents = {
                "rename": True,
                'links': [song_id],
            }
            json.dump(result_file_contents, result_file)


if __name__ == '__main__':
    get_playlist_songs("https://youtube.com/playlist?list=PL9amtKqWY8ajIjSWZFrm7ZPlHY_sSyWMK&si=1gOEV7tqMxQ94eFP")
