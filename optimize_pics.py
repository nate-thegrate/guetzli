from os import listdir, system
from os.path import isfile, join, getsize

filenames = [f for f in listdir("./pics") if isfile(join("./pics", f))]

for file in filenames:
    whitespace = " " * (len(max(filenames, key=len)) - len(file))
    startsize = getsize(f"pics\{file}")
    print(f"starting {file} {whitespace} ({round(startsize / 1024)} KB)", flush=True)

    system(f'.\guetzli_windows_x86-64.exe "pics\{file}" "pics\{file}"')

    endsize = getsize(f"pics\{file}")
    print(f"finished {file} {whitespace} ({round(endsize / 1024)} KB, -{round((1-endsize/startsize)*100)}%)\n", flush=True)