import threading
# Definizione di risorse
resource_a=threading.Lock()
resource_b=threading.Lock()

#Funzione per l'esecuzione del primo thread
def thread_a():
    # Acquisizioen del lock sulal risorsa A
    resource_a.acquire()
    print("Thread A ha acquisito il lock sulal risorsa A")

    # Tentativo di acquisizione sulla risorsa B
    print("Thread A tetna di acquisire il lock sulla risorsa A")
    resource_b.acquire()
    print("Thread A ha acquisito il lock sulla risorsa B")

    # Rilascio delle risorse
    resource_b.release()
    resource_a.release()

# Funzione per l'esecuzione del secondo thread
def thread_b():
    # Acquisizione del lock sulla risorsa B
    resource_b.acquire()
    print("Thread B ha acquisito il lock sulla risorsa B")
    
    # Tentativo di acquisizione del lock sulla risorsa A
    print("Thread B tenta di acquisire il lock sulla risorsa A")
    resource_a.acquire()
    print("Thread B ha acquisito il lock sulla risorsa A")
    # Rilascio delle risosrse
    resource_a.release()
    resource_b.release()

# Creazioen dei thread
thread1=threading.Thread(targhet=thread_a)
thread2=threading.Thread(targhet=thread_b)
# Avvio dei thread
thread1.start()
thread2.start()
# Attesa che i thread terminino
thread1.join()
thread2.join()

print("Fine del programma")