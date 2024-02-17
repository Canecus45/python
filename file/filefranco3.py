import threading
import requests
import os


def download_file(url, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            file = open("file_name.txt", "r")
            contenuto = file.read
            if contenuto < 2000:
                os.mkdir("small")
                os.chdir("/file/small")
            elif contenuto < 4000:
                os.mkdir("medium")
                os.chdir("/file/medium")
            else:
                os.mkdir("large")
                os.chdir("/file/large")

        else:
            data = "ERRORE"
            print(f"Download completato per {url} e salvato in {file_name}")
    except Exception as e:
        print(f"Errore nel download di {url}: {str(e)}")


# lista di siti dove si trovano i file da scaricare

urls = [
    ("http://elexpo.altervista.org/r.txt", "file1.txt"),
    ("http://https://jsonplaceholder.typicode/users", "file2.txt"),
    ("http://https://jsonplaceholder.typicode/post", "file3.txt"),
]

# scarico i file
threads = []
for url, file_name in urls:
    t = threading.Thread(target=download_file, args=(url, file_name))
    threads.append(t)

# si fanno partitre i threads
for t in threads:
    t.start()

# si fa partire il download di ogni file
for t in threads:
    t.join()

print("Download completati")
