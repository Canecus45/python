import threading
import requests
import os

os.mkdir("ok")
os.mkdir("ko")


def download_and_analyze(urls, ok_word, save_dir_ok, save_dir_ko):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if save_dir_ok:
                os.chdir("/percorso/ok")
            else:
                os.chdir("/percorso/ko")
        else:
            data = "ERRORE"
    except Exception as e:
        print(f"Erorre nel download e salvataggio di {url}: {str(e)}")


urls = [
    ("http://elexpo.altervista.org/r.txt", "file1.txt"),
    ("http://https://jsonplaceholder.typicode/users", "file2.txt"),
    ("http://https://jsonplaceholder.typicode/post", "file3.txt"),
]

while True:
    ok_word = input("Inserire il ok o ko:\n>")
    if ok_word == "ok" or ok_word == "ko":
        break
    else:
        print("Inserire ")

if ok_word == "ok":
    save_dir_ok = True
    save_dir_ko = False
else:
    save_dir_ok = False
    save_dir_ko = True

download_and_analyze(
    urls,
    ok_word,
)

print("Download e analisi completati.")
