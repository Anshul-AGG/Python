import time

seconds = int(input("Enter the countdown time in seconds: "))

for i in range(seconds, 0, -1):
    print(f'time left : {i} seconds')
    time.sleep(1)

print('times up')