from threading import Thread, Lock

lock = Lock()

def calculate_squares_parallel(start, end):
    for i in range(start, end):
        with lock:
            print(f"{i} * {i} = {i*i}")

if __name__ == "__main__":
    threads = []
    num_threads = 4
    total = 100
    chunk = total // num_threads
    for t in range(num_threads):
        start = t * chunk
        end = (t + 1) * chunk if t != num_threads - 1 else total
        thread = Thread(target=calculate_squares_parallel, args=(start, end))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("End Main")
