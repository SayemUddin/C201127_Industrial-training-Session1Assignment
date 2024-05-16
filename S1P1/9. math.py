def compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

# Example usage
principal = 1000  # Initial amount
rate = 0.05       # Annual interest rate (5%)
time = 3          # Time in years
n = 12            # Compounded monthly

# Calculate compound interest
result = compound_interest(principal, rate, time, n)
print("Compound Interest:", result)



import datetime
import time

def print_current_time():
    while True:
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), end="\r")  # \r for overwriting the previous line
        time.sleep(1)
print_current_time()
