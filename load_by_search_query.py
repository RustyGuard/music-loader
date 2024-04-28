from pathlib import Path

from pytube.exceptions import AgeRestrictedError

from api.load_audio import load_by_video_id
from api.search_results import search_results
from input_helpers.input_int import input_int
from utils.colors import bcolors
from utils.create_result_folder import create_result_folder
from utils.disable_logger import disable_pytube_logger


def main():
    disable_pytube_logger()

    search_query = input("Введите название песни: ")

    results = search_results(search_query)


    while True:
        print("Результаты:")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.title} - {result.author} (https://youtube.com/watch?v={result.video_id})")

        video_to_download = input_int("Введите какой пункт следует скачать: ",
                                      is_correct=lambda x: (1 <= x <= len(results)),
                                      default_value=1)

        selected_result = results[video_to_download - 1]

        destination_path = Path("result") / f"{selected_result.title} - {selected_result.author}.mp3"

        try:
            print("Идёт скачивание...")

            create_result_folder()
            load_by_video_id(selected_result.video_id, destination_path)

            print(bcolors.okgreen(f"Файл сохранён в {destination_path.resolve()}"))

            break
        except AgeRestrictedError:
            print(bcolors.fail("На видео установлено ограничение по возрасту("))
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")


if __name__ == '__main__':
    main()
