import time

# while: 2.424460375
# for-range: 0.932917942
if __name__ == "__main__":

    N = 30000000
    start = time.perf_counter()
    i = 0
    while i < N:
        i += 1
    end = time.perf_counter()
    print("while:", end - start)

    start = time.perf_counter()
    for i in range(N):
        pass
    end = time.perf_counter()
    print("for-range:", end - start)
