shared_x = 0

def get():
    return shared_x

def set(x):
    global shared_x
    shared_x = x

def prin():
    print(shared_x)

a = get()
c = get()
b = get()

a = a + 1

set(a)

prin()

b = b - 2

set(b)

prin()

c = c + 2
set(c)
prin()