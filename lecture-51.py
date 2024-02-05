from multiprocessing import Process,cpu_count
import time
#multiprocessing is a package that supports spawning processes using an API similar to the threading module.

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter,args=(50000000,))
    b = Process(target=counter,args=(50000000,))
    c = Process(target=counter,args=(50000000,))
    d = Process(target=counter,args=(50000000,))
    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    b.join()
    c.join()
    d.join()
    
    print("Finished in: ",time.process_time()," seconds")


if __name__ == "__main__":
    main()