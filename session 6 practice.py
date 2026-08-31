#Phase 1: Application & Analysis
#Task 1: The Secure Data Scrubber (String Iteration)
# Context: You are cleaning a database of usernames.
# Task: Take a string of characters. Iterate through it to create a new string that removes all special characters and numbers, keeping only alphabets.
# Requirement: Use a for loop and the .isalpha() method. If a character is a space, use pass to maintain the gap.
# SampleData : Input: "Alpha_User 101! #Beta$ & Gamma_99"

sample_data = "Alpha_User 101! #Beta$ & Gamma_99"

cleaned_data = ""

for char in sample_data:
    if char.isalpha():
        cleaned_data += char
    elif char == " ":
        pass
        cleaned_data += char

print("Original Data:", sample_data)
print("Cleaned Data:", cleaned_data)
#Task 2: Financial Threshold Monitor (List Iteration)
# Context: Monitoring a list of stock prices: prices = [120.5, 118.2, 122.0, 115.5, 125.0].
# Task: Iterate through the prices. Calculate the percentage change between the first price and every subsequent price.
# Action: If a price drops by more than 5% from the starting price, print 
# a "SELL ALERT" and the index of that price.
prices = [120.5, 118.2, 122.0, 115.5, 125.0]

starting_price = prices[0]

for index, price in enumerate(prices):
    percentage_change = ((price - starting_price) / starting_price) * 100

    print(f"Index {index}: Price = {price}, Change = {percentage_change:.2f}%")

    if percentage_change < -5:
        print(f"SELL ALERT at index {index}")
#Task 3: The API Response Validator (Dict Iteration)
# Context: You receive a dictionary of service statuses: {"Auth": "200 OK", "Cache": "500 Error", "Database": "200 OK", "Proxy": "404 Not Found"}.
#Task: Iterate through the dictionary using .items().
# Logic: For any status containing "200", print "Service Healthy". 
# For any other status, print "Service Critical" and use the continue keyword
#  to skip any further logging for that specific service.
service_status = {
    "Auth": "200 OK",
    "Cache": "500 Error",
    "Database": "200 OK",
    "Proxy": "404 Not Found"
}

for service, status in service_status.items():

    if "200" in status:
        print(service, "Service Healthy")
    else:
        print(service, "Service Critical")
        continue

    print(service, "Further logging completed")
    #Task 4: The Smart Search Optimizer (For + Break)
# Context: You are searching a massive list for a "target_id".
# Task: Create a list of 20 random integers. Ask the user for a search value.
# Action: Iterate through the list. Print "Analyzing index [i]...". Use
#  break to stop the search the moment the value is found.
# Analysis: After the loop, print a message indicating whether
#  the search was efficient (stopped before the end) or exhaustive (checked every element).
import random

# Create a list of 20 random integers
numbers = [random.randint(1, 50) for _ in range(20)]

print("Generated List:", numbers)

# Ask the user for a search value
target_id = int(input("Enter the value to search: "))

found = False

# Search through the list
for i in range(len(numbers)):
    print(f"Analyzing index {i}...")

    if numbers[i] == target_id:
        print(f"Target {target_id} found at index {i}.")
        found = True
        break

# Analysis after the loop
if found and i < len(numbers) - 1:
    print("Search was efficient: stopped before the end.")
elif found:
    print("Search was exhaustive: checked every element.")
else:
    print("Search was exhaustive: target was not found.")
#Task 5: Infinite Command-Line Interface (While + Exit)
# Context: Building a system utility menu.
# Task: Create an infinite while True loop.
# Action: Prompt user for commands: status, reset, or exit.
# Logic: Use a match-case (from Module 5) inside the while loop
#  to handle the commands. Only the exit command should trigger the break keyword.
while True:
    command = input("Enter command (status/reset/exit): ").lower()

    match command:
        case "status":
            print("System status: Healthy")

        case "reset":
            print("System reset successfully.")

        case "exit":
            print("Exiting the system...")
            break

        case _:
            print("Invalid command. Please enter status, reset, or exit.")
#Task 6: The Multi-Dimensional Grid Mapper (Nested Loops)
# Context: Generating a coordinate system for a game board (5x5).
# Task: Use nested for loops to print coordinates in the format (row, col).
# Requirement: Skip the "center" coordinate (2, 2) using the continue keyword in the inner loop.
for row in range(5):
    for col in range(5):

        # Skip the center coordinate (2, 2)
        if row == 2 and col == 2:
            continue

        print(f"({row}, {col})")
#Task 7: Resource Management Simulator (Control Keywords)
# Context: A battery charging simulator.
# Task: Start a while loop at battery = 0. Increment by 5.
# Logic: When battery reaches 20, 40, and 60, use print to
#show "Charging...". When it reaches 80, use pass (placeholder for "Slow Charge Mode").
#When it hits 100, use break to stop and print "Fully Charged".
battery = 0

while True:
    battery += 5

    if battery == 20 or battery == 40 or battery == 60:
        print("Charging...")

    elif battery == 80:
        pass  # Placeholder for "Slow Charge Mode"

    elif battery == 100:
        print("Fully Charged")
        break
#Task 8: The "Dirty Data" Integrator
# Scenario: You are processing a sensor log: logs = [22, 25, "TIMEOUT", 28, 0, "ERROR", 30].
# Problem: You need the average temperature, but "TIMEOUT" 
# should be ignored, 0 should be ignored as a false reading, and "ERROR" indicates a
#  catastrophic failure where no further data should be processed.
# Challenge: Write a loop that calculates the sum and count of valid temperatures.
#  Use continue for "TIMEOUT" and 0, and break for "ERROR". Print the final average
#  of the data processed up to the error.
logs = [22, 25, "TIMEOUT", 28, 0, "ERROR", 30]

total = 0
count = 0

for data in logs:

    if data == "TIMEOUT" or data == 0:
        continue

    if data == "ERROR":
        break

    total += data
    count += 1

average = total / count

print("Sum of valid temperatures:", total)
print("Count of valid temperatures:", count)
print("Average temperature:", average)
#Task 9: The Prime Number Architect
# Challenge: Write a script to find all prime numbers between 2 and 50.
# Logic: You must use a nested loop structure. The outer loop picks the number,
#  and the inner loop tests for divisibility.
# Evaluation: Optimize your loop using a break keyword so 
# that as soon as a factor is found, the inner loop stops checking. Explain in 
# a comment why this is more "efficient" than checking every number.
for number in range(2, 51):
    is_prime = True

    # Inner loop checks if the number is divisible by another number
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break  # Stop immediately when a factor is found

    # If no factor was found, the number is prime
    if is_prime:
        print(number)
#Task 10: State-Machine Transaction Logic Scenario: A vending machine script.
#  balance = 50. items = {"Soda": 15, "Chips": 10, "Candy": 5}.
#Task: Create a loop that allows a user to buy items until
#  their balance is too low or they type "finished".
#Constraint: 1. If the user picks an item they can't afford,
#  use continue to let them pick something else.
#2. If the balance reaches 0, use break automatically.
# Critical Thinking: Add a pass statement in a section where you
#  would theoretically "Refund" money, then explain in the submission 
# why you chose that structure for future scalability. 
# Task 10: State-Machine Transaction Logic

balance = 50

items = {
    "Soda": 15,
    "Chips": 10,
    "Candy": 5
}

while balance > 0:

    print("\nAvailable Items:")
    for item, price in items.items():
        print(item, "-", price)

    choice = input("Choose an item or type 'finished': ").strip().title()

    # Stop if the user wants to finish
    if choice == "Finished":
        break

    # Check if the item exists
    if choice not in items:
        print("Invalid item. Please choose again.")
        continue

    price = items[choice]

    # If the user cannot afford the item
    if price > balance:
        print("Insufficient balance. Choose another item.")
        continue

    # Purchase the item
    balance -= price
    print(f"{choice} purchased successfully.")
    print("Remaining balance:", balance)

    # The refund feature can be implemented in the future
    if False:
        pass  # Placeholder for Refund functionality

    # Automatically stop when balance reaches 0
    if balance == 0:
        print("Balance is 0. Transaction finished.")
        break

print("Final balance:", balance)       
