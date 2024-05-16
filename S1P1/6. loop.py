temperatures = [25, 28, 30, 32, 29, 27]
threshold = 30
exceeded_temperatures = []

for temp in temperatures:
    if temp > threshold:
        exceeded_temperatures.append(temp)
        print(f"Warning: Temperature {temp} exceeds threshold!")
    else:
        print(f"Temperature {temp} is within the acceptable range.")

print("All temperatures processed.")
if exceeded_temperatures:
    print("Temperatures that exceeded the threshold:", exceeded_temperatures)
else:
    print("No temperatures exceeded the threshold.")



products = {
    "apple": {"stock": 10, "threshold": 5},
    "banana": {"stock": 3, "threshold": 2},
    "orange": {"stock": 7, "threshold": 4}
}

for product, details in products.items():
    stock = details["stock"]
    threshold = details["threshold"]
    
    if stock <= threshold:
        print(f"Alert: Stock of {product} is low ({stock} remaining). Please restock.")
    else:
        print(f"{product} stock is sufficient ({stock} remaining).")

