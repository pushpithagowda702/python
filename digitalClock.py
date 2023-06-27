import time

def digital_clock():
    while True:
        print("\033c", end="")
        current_time = time.strftime("%H:%M:%S")
        print(current_time, end="", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()
