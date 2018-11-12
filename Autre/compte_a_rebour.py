import time


def timer(length):
    start = time.time()
    running = True
    while running:
        if time.time() - start >= length:
            print("Time's up!")
            running = False
        else:
            print("Only %.1f more seconds!") % (length - (time.time() - start))


if __name__ == "__main__":
    timer(30)
