import time
import random

print("Get ready...")
time.sleep(random.randint(2, 5))  # wait randomly

start = time.time()
input("NOW! Press Enter as fast as you can!")
end = time.time()

reaction_time = end - start
print(f"Your reaction time: {reaction_time:.3f} seconds")
