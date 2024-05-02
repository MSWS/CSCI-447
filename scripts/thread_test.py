import threading
import time
import random

shared_value = 0
shared_output = []

possibilities = [
    (5,4,5),
    (2,3,2),
    (1,5,1),
    (2,2,3),
    (5,3,6),
    (4,4,6),
    (7,8,9),
]

offsets = []

def getOffsets(ls: tuple) -> tuple:
    return (ls[1] - ls[0], ls[2] - ls[1])

for p in possibilities:
    offsets.append(getOffsets(p))

possible = set()

def thread_a():
    global shared_value, shared_output
    x = shared_value
    #time.sleep(random.random() / 5)
    x += 1
    #time.sleep(random.random() / 5)
    shared_value = x
    # #time.sleep(random.random() / 5)
    shared_output.append(shared_value)

def thread_b():
    global shared_value
    x = shared_value
    #time.sleep(random.random() / 5)
    x -= 2
    #time.sleep(random.random() / 5)
    shared_value = x
    #time.sleep(random.random() / 5)
    shared_output.append(shared_value)

def thread_c():
    global shared_value
    x = shared_value
    #time.sleep(random.random() / 5)
    x += 2
    #time.sleep(random.random() / 5)
    shared_value = x
    #time.sleep(random.random() / 5)
    shared_output.append(shared_value)

def run_simulation():
    # Reset shared value for each simulation
    global shared_value, shared_output
    shared_value = 0
    shared_output = []

    thread1 = threading.Thread(target=thread_a)
    thread2 = threading.Thread(target=thread_b)
    thread3 = threading.Thread(target=thread_c)

    thread1.start()
    thread2.start()
    thread3.start()

    thread2.join()
    thread3.join()
    thread1.join()

    # Return the final value of shared_value
    return shared_output

# Number of simulations to run
num_simulations = 100000

for i in range(num_simulations):
    output = run_simulation() 
    offs = getOffsets(output)

    if offs in offsets:
        ps = possibilities[offsets.index(offs)]
        print(ps, "is possible")
        possible.add(ps)

print("\n".join(map(lambda t: str(t), possible)))