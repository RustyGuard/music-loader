import glob
import shutil
from pathlib import Path


def separate():
    for file in glob.glob('result/*.mp3'):
        shutil.copyfile(file, Path("neon_white") / Path(file).name)


if __name__ == '__main__':
    separate()
