import json
import random
from pathlib import Path
from time import sleep

from api.search_results import search_results


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
            'links': [result.video_id for result in result_urls],
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
