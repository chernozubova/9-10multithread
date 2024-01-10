import time
import threading
from random import randint

value = 0
name_of_person = 0
locker = threading.Lock()

def inc_value():
    global value, name_of_person
    while True:
        with locker:
            name_of_person = randint(10000, 99999)
            value += 1
            print(f"{name_of_person} - {value}")
        time.sleep(0.5)

for _ in range(10):
    threading.Thread(target=inc_value).start()
