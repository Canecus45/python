import threading
import time


class MonitorBuffer:
    def __init__(self) -> None:
        self.condition = threading.Condition
        self.buffer = None

    # Metodo produttore:
    def produce(self, data) -> None:
        with self.condition:  # Inizia la mutua esclusione
            while self.buffer is not None:
                self.condition.wait()

            print(f"Produttore ha generato {data}")
            self.buffer = data  # Il buffer Viene riempito
            self.condition.notify()  # Il metodo consume() viene notificato che può consumare

    def consume(self) -> None:
        with self.condition:
            while self.buffer is None:
                self.condition.wait()

            print(f"Consumatore ha prelevato {self.buffer}")
            self.buffer = None  # I dati nel buffer vengono prelevati
            self.condition.notify()  # Il metodo produce() viene notificato che può produrre


# Funzioni che simulano produttore e consumatore
def producer(monitor) -> None:
    while True:
        data = "Dati casuali"
        monitor.produce(data)
        time.sleep(2)


def consumer(monitor) -> None:
    while True:
        monitor.consume()
        time.sleep(3)


# Creiamo il monitor
monitor = MonitorBuffer()

# Avviamo il thread produttore e consumatore
prod_thread = threading.Thread(target=producer, args=(monitor,))
cons_thread = threading.Thread(target=consumer, args=(monitor,))

# Join dei due thread

prod_thread.join()
cons_thread.join()