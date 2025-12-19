"""Problem: Implement an exponential backoff strategy that doubles 
the wait time between retries, starting from 1 second, but stops after 5 retries."""
import time 

attempt = 0
wait_time =1
max_attempt =5

while attempt< max_attempt:
    print("Attempt",attempt+1,"wait time",wait_time)
    attempt+=1
    time.sleep(wait_time)
    wait_time *=2
print("All attempts are done")
