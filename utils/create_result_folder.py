from pathlib import Path


def create_result_folder():
    Path("result").mkdir(exist_ok=True)
