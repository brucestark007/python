def calculate_average(numbers):
    total = 0
    for i in range(numbers):
        total += i
    average = total / len(numbers)
    return averag

nums = [10, 20, 30, 40, 50]
print("Average is:", calculate_average(num))
