from asyncio import Queue, exceptions
import time


def ping_website(address):
    try:
        request = request.get(address, timeout=10)
        if request.status_code >= 400:
            print(f"indirizzo {address} pingato con status code {request.status_code}")
            raise exceptions
    except:
        print(f"errore nel contattare l’url {address} {request.status_code}")


def worker():
    task_queue = Queue()
    while True:
        address = task_queue.get()
        ping_website(address)
        task_queue.task_done()


siti_web = [
    "https://envato.com",
    "http://amazon.com",
    "http://facebook.com",
    "http://google.com",
    "http://google.fr",
    "http://google.es",
    "http://internet.org",
    "http://gmail.com",
    "http://stackoverflow.com",
    "http://github.com",
    "http://heroku.com",
    "http://really-cool-available-domain.com",
    "http://djangoproject.com",
    "http://rubyonrails.org",
    "http://basecamp.com",
    "http://trello.com",
    "http://yiiframework.com",
    "http://shopify.com",
    "http://another-really-interesting-domain.co",
    "http://airbnb.com",
    "http://instagram.com",
    "http://snapchat.com",
    "http://youtube.com",
    "http://baidu.com",
    "http://yahoo.com",
    "http://live.com",
    "http://linkedin.com",
    "http://yandex.ru",
    "http://netflix.com",
    "http://wordpress.com",
    "http://bing.com",
    "http://jessesteahouse.com",
]
task_queue = Queue()
start_time = time.time()

for url in siti_web:
    ping_website(url)
end_time = time.time()

print("tempo di esecuzione", end_time - start_time)
