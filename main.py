
OK = 'Main ok - only def'
def U():
    global OK
    OK = 'U ok - only def'
    print(OK)

U()
OK= 'ok'
print(OK)

