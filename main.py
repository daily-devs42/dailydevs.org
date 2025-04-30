import time
start_time = time.time()
for n in range(1000000):
  print(n)
print("--- %s seconds ---" % (time.time() - start_time))