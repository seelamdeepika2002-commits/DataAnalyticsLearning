#Task 1: The "Truthy/Falsy" Validation Suite
#Objective: Understand how Python evaluates non-boolean types in a boolean context.
#1. Variable Setup: Create the following variables:
# val_1 = 0
# val_2 = 0.0
# val_3 = "" (Empty string)
# val_4 = None
# val_5 = "False" (The string "False")
val_1=0
val_2=0.0
val_3=""
val_4=None
val_5="False"
print(val_1)
print(val_2)
print(val_3)
print(val_4)
print(val_5)
print(type(val_1))
print(type(val_2))
print(type(val_3))
print(type(val_4))
print(type(val_5))
#2. Logic Test: Write an if-else block
#  for each variable to check if Python considers it True or False

if val_1:
    print("val_1 is True")
else:
    print("val_1 is False")
if val_2:
    print("val_2 is True")
else:
    print("val_2 is False")
if val_3:
    print("val_3 is True")
else:
    print("val_3 is False")
if val_4:
    print("val_4 is True")
else:
    print("val_4 is False")
if val_5:
    print("val_5 is True")
else:
    print("val_5 is False")
#3. Output: Print a formatted message for each: "Variable [X]
#  with value [Y] is evaluated as [TRUE/FALSE]".  
print(f"Variable val_1 with value {val_1} is evaluated as {str(bool(val_1)).upper()}")
print(f"Variable val_2 with value {val_2} is evaluated as {str(bool(val_2)).upper()}")
print(f"Variable val_3 with value {val_3} is evaluated as {str(bool(val_3)).upper()}")
print(f"Variable val_4 with value {val_4} is evaluated as {str(bool(val_4)).upper()}")
print(f"Variable val_5 with value {val_5} is evaluated as {str(bool(val_5)).upper()}")  
#4. Analysis: In a comment, explain why val_5 evaluates differently than the others
val_5 = "False"
# "False" is a non-empty string, so Python evaluates it as Truthy (True).

#Task 2: Multi-Tiered Logical Branching (The Tax Engine)
#Objective: Implement a professional if-elif-else structure with nested logic.
#1. Input: Prompt a user for their annual_income (float) 
# and residency_status (string: "Resident" or "Non-Resident").

#2. The Logic:
# If annual_income is less than or equal to 30,000, tax is 0%.
# If annual_income is between 30,001 and 80,000:
# Residents pay 10%.
# Non-Residents pay 15%.
# If annual_income is above 80,000, everyone pays 25%.
#3. Calculation: Calculate the tax_amount and the remaining_balance.
#4. Output: Use f-strings to print a summary including the income,
#  the applied tax rate, and the final balance.
# 1. Input
annual_income = float(input("Enter your annual income: "))
residency_status = input("Enter your residency status (Resident or Non-Resident): ")

# 2. Logic
if annual_income <= 30000:
    tax_rate = 0

elif annual_income <= 80000:
    # Nested logic based on residency status
    if residency_status == "Resident":
        tax_rate = 0.10
    elif residency_status == "Non-Resident":
        tax_rate = 0.15
    else:
        print("Invalid residency status")
        tax_rate = 0

elif annual_income > 80000:
    tax_rate = 0.25

# 3. Calculation
tax_amount = annual_income * tax_rate
remaining_balance = annual_income - tax_amount

# 4. Output
print(f"Annual Income: {annual_income:.2f}")
print(f"Residency Status: {residency_status}")
print(f"Applied Tax Rate: {tax_rate * 100:.0f}%")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Final Balance: {remaining_balance:.2f}")
#Task 3: Modern Pattern Matching (match-case)
#Objective: Replace traditional switch-case logic with Python's match-case for cleaner code.
#1. Scenario: You are building a system that processes "HTTP Status Codes."
#2. The Task: Create a variable status_code (int) via user input.
#3. Implementation: Use a match status_code: block to handle:
# 200 -> Print "Success: OK"
# 400 -> Print "Client Error: Bad Request"
# 404 -> Print "Client Error: Not Found"
# 500 -> Print "Server Error: Internal Server Error"
# Wildcard (_): Handle any other code by printing "Unknown Status Code".
# Get HTTP status code from the user
status_code = int(input("Enter HTTP status code: "))

# Match the status code
match status_code:
    case 200:
        print("Success: OK")
    
    case 400:
        print("Client Error: Bad Request")
    
    case 404:
        print("Client Error: Not Found")
    
    case 500:
        print("Server Error: Internal Server Error")
    
    case _:
        print("Unknown Status Code")
#Task 4: Structural Pattern Matching with Combined Patterns
#Objective: Use the pipe operator (|) in match-case to group multiple conditions.
#1. Scenario: A file processing system accepts different extensions.
#2. The Task: Create a variable file_ext (string) via user input (e.g., ".jpg", ".png", ".pdf").
#3. Implementation: Use a match statement to categorize the file:
# If ".jpg", ".jpeg", or ".png" -> Print "File Type: Image"
# If ".pdf", ".docx", or ".txt" -> Print "File Type: Document"
# If ".mp4" or ".mkv" -> Print "File Type: Video"
# Case _ -> Print "File Type: Unsupported"  
file_ext = input("Enter file extension: ")

# Categorize the file using match-case
match file_ext:
    case ".jpg" | ".jpeg" | ".png":
        print("File Type: Image")

    case ".pdf" | ".docx" | ".txt":
        print("File Type: Document")

    case ".mp4" | ".mkv":
        print("File Type: Video")

    case _:
        print("File Type: Unsupported")      
#Task 5: The "Short-Circuit" Logic Challenge
#Objective: Combine if statements with Logical Operators (and, or, not) to manage access.
#1. Scenario: A system requires three flags for "System Override" access:
# is_admin (bool)
# has_security_key (bool)
# system_offline (bool)
#2. The Task: Set these variables using input() and type casting to bool. (Note: In Python, bool(input()) might be tricky—ensure you compare the input string to "True").
#3. Requirement: A user is granted "OVERRIDE ACCESS" only if:
# They are an admin AND have the security_key.
# OR if the system_offline flag is True (regardless of admin status).
#4. Execution: Use one if-else block to determine access and print the result.
is_admin = input("Are you an admin? (True/False): ") == "True"

has_security_key = input("Do you have a security key? (True/False): ") == "True"

system_offline = input("Is the system offline? (True/False): ") == "True"

# Check override access
if (is_admin and has_security_key) or system_offline:
    print("OVERRIDE ACCESS")
else:
    print("ACCESS DENIED")