import threading
import requests

# con questa funzione dico chiedo di installare i file
# tramite il link che provvedo


def download_file(url, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
        else:
            data = "ERRORE"
        # faccio aprire il file in scrittura binaria
        with open(file_name, "wb") as file:
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
