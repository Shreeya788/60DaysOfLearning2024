import time
start_time = time.time()

for i in range(100):
    for j in range(100):
        print(0, end=' ')
    print()
print(round((time.time() - start_time),2))  #Time complexity