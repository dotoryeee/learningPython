import threading, time
 
def f1(cnt):
    for i in range(1, cnt+1):
        print('f1 thread:', i)
        time.sleep(1)

def f2():
    for i in range(97, 123):
        print('f2:', chr(i))
        time.sleep(1)

def main():
    t1 = threading.Thread(target=f1, args=(10,))
    t1.start()

    t2 = threading.Thread(target=f2, args=())
    t2.start()
 
    for i in range(100, 123):
        print('main:', i)
        time.sleep(1)

main()
