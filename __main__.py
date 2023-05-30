from os import listdir
from os.path import getsize
from pathlib import Path
from subprocess import run

guetzli_folder = Path(__file__).parent.resolve()
pics_folder = guetzli_folder.joinpath("pics/")
filenames = [(f, pics_folder.joinpath(f)) for f in listdir(pics_folder) if pics_folder.joinpath(f).is_file()]
longest_filename = len(max(filenames, key=len))

for file, path in filenames:
    whitespace = " " * (longest_filename - len(file))
    startsize = getsize(path)
    print(f"starting {file} {whitespace} ({round(startsize / 1024)} KB)", flush=True)

    run(str(x) for x in [guetzli_folder.joinpath("guetzli_windows_x86-64.exe"), path, path])

    endsize = getsize(path)
    print(f"finished {file} {whitespace} ({round(endsize / 1024)} KB, -{round((1-endsize/startsize)*100)}%)\n", flush=True)