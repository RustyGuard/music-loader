# This is a sample Python script.
import json
import random
from pathlib import Path
from time import sleep

from pytube import Search


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def search_results(prompt: str) -> list[str]:
    s = Search(prompt)
    return [video.video_id for video in s.results]


def load_links(author: str, title: str):
    result_file_path = Path("result") / f"{author} - {title}.json"
    if result_file_path.exists():
        print(f"{author} - {title} already exists")
        return
    result_urls = search_results(f"{author} - {title}")
    with open(result_file_path, "w", encoding='utf-8') as result_file:
        result_file_contents = {
            'author': author,
            'title': title,
            'links': result_urls,
        }
        json.dump(result_file_contents, result_file)
    sleep_time = random.randint(5, 10)
    print(f"Sleeping for {sleep_time}...")
    sleep(sleep_time)


def load_all_data():
    import csv
    with open('music_to_load.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|',)
        next(spamreader)
        for author, title in spamreader:
            print(author, title)
            load_links(author, title)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    load_all_data()
    # load_rick_astley()
