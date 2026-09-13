#Session – 9
#Task 1: Library Inventory Reader (File Reading)
#Scenario (Analogy): Imagine a librarian scanning through an archive of books. A file books.txt contains the library’s inventory, one book per line with the format Title,Author,Year. You must process this file in two ways: first, read it line-by-line; second, read the entire file at once. This task emphasizes different reading methods (read() vs. iterating lines).
#Requirements:
# Use a with open("books.txt", "r") as f: block to open the file safely (automatic close).
# Part A: Loop over the file object (for line in f:) to count and print how many books were 
# published after 2015.
# Part B: Re-open the file (new with block) and use f.read() to get the entire text as one string. 
# From this string, compute and print the oldest (minimum) publication year in the file.
# Make sure to handle the case where books.txt does not exist by catching FileNotFoundError 
# and displaying an error message.
# Do not write any extra output; print only the required numbers or messages.
#Sample Data: File books.txt (each line: Title,Author,Year)
#Data Science 101,John Doe,2018
#Python Unleashed,Jane Roe,2014
#Machine Learning,John Doe,2021
#Algo Magic,Jane Roe,2017
#Expected Output (for the sample data):
#Books after 2015: 3
#Oldest book year: 2014
#(Explanation: There are 3 books from years 2018, 2021, 2017; the minimum year is 2014.)

try:
    # Part A: Read the file line by line
    with open("books.txt", "r") as f:
        count = 0

        for line in f:
            parts = line.strip().split(",")
            year = int(parts[2])

            if year > 2015:
                count += 1

        print("Books after 2015:", count)

    # Part B: Read the entire file at once
    with open("books.txt", "r") as f:
        text = f.read()

        years = []

        for line in text.strip().splitlines():
            parts = line.split(",")
            years.append(int(parts[2]))

        print("Oldest book year:", min(years))

except FileNotFoundError:
    print("Error: books.txt not found")




#Task 2: Sales Data Logger (File Writing and Appending )
#Scenario (Analogy): Think of this as maintaining a growing sales journal for a store. You have a log file sales_log.txt that accumulates daily sales figures. Each line in the file is a single number (the sales amount for one day). You need to append a new sales entry and then report on the updated log. This task practices write/append modes ("w" vs "a") and reading after writing.
#Requirements:
# Prompt the user to enter today’s sales amount (assume an integer).
# Open sales_log.txt in append mode ("a") using a with block. Write the entered sales amount on a new line. (Append mode "a" will create the file if it doesn’t exist and will preserve existing entries.)
# After appending, open sales_log.txt in read mode ("r") with a new with block. Read all lines and print:
# The total number of entries (lines) in the file.
# The most recent (last) entry in the file.
# Use try/except to catch FileNotFoundError when reading (though append mode creates the file, just in case of issues).
# Only the requested information should be printed, in a clear format as shown below.
#Sample Data (initially in sales_log.txt):
#120
#250
#75
#Sample Input: (user runs the program and inputs)
#180
#Expected Output: (after adding 180)
#Total entries: 4
#Latest entry: 180
#(Explanation: The log now has 4 lines [120, 250, 75, 180)

try:
    # Get today's sales amount
    sales = int(input())

    # Append the new sales amount
    with open("sales_log.txt", "a") as f:
        f.write(str(sales) + "\n")

    # Read all sales entries
    with open("sales_log.txt", "r") as f:
        lines = f.readlines()

    # Print the required information
    print("Total entries:", len(lines))
    print("Latest entry:", lines[-1].strip())

except FileNotFoundError:
    print("Error: sales_log.txt not found")


#Task 4: Robust Transaction Processor (Exception Handling)
#Scenario (Analogy): A cashier processes transactions but occasionally encounters bad inputs or
#  missing records. There is a file transactions.txt with lines in the format action amount, where
#  action is either "deposit" or "withdraw". Example lines: deposit 100 or withdraw 50. 
# Your program should compute the final balance (starting at 0), but be resilient to errors. 
# This involves catching FileNotFoundError and ValueError, and using finally to signal completion.
#Requirements:
# Attempt to open transactions.txt with with open("transactions.txt","r") as f: inside a try block. 
# If the file does not exist, catch the exception and print "Error: transactions.txt not found." and exit.
# If opened successfully, read the file line by line. For each line, split into action and amount.
# Use try/except around the conversion int(amount) to catch non-integer amounts (raising ValueError).
#  If a line is invalid (e.g. withdraw abc), print a message like 
# "Line X: invalid amount 'abc'; skipping." and skip it.
# Update the balance: add amount on "deposit", subtract on "withdraw". (Assume the file is well-formed
#  otherwise.)
# After processing all lines, print the final balance as Final balance: <value>.
# Use a finally block to print "Transaction processing completed." after all try/except handling,
#  regardless of errors.
# No other output should be printed.
#Sample Data (transactions.txt):
#deposit 100
#withdraw 30
#deposit abc
#withdraw 20
#Expected Output:
#Line 3: invalid amount 'abc'; skipping.
#Final balance: 50
#Transaction processing completed.
#(Explanation: 100 - 30 + (skip invalid) - 20 = 50.)


try:
    with open("transactions.txt", "r") as f:
        balance = 0

        for line_number, line in enumerate(f, start=1):
            action, amount = line.strip().split()

            try:
                amount = int(amount)
            except ValueError:
                print(
                    f"Line {line_number}: invalid amount '{amount}'; skipping."
                )
                continue

            if action == "deposit":
                balance += amount
            elif action == "withdraw":
                balance -= amount

        print(f"Final balance: {balance}")

except FileNotFoundError:
    print("Error: transactions.txt not found.")

finally:
    print("Transaction processing completed.")


#Task 5: Functional Context Manager for Safe File Operations
#Scenario (Analogy)
#Instead of building a "machine" (a class), you are writing a process script (a generator) 
#that pauses and resumes. You will create a custom context manager using a function to handle 
#file access. This ensures that the file is opened, the work is done, and the file is automatically closed, 
#even if something goes wrong.
#Requirements
# Import the Decorator: Use from contextlib import contextmanager.
# Define the Generator Function: Create a function safe_file_manager(filename, mode).
# Setup (The "Enter" phase): * Inside a try block, open the file.
# Use the yield keyword to "hand over" the file object to the with block.
# Teardown (The "Exit" phase):
# Use a finally block to ensure file.close() is called. This guarantees the file closes 
#regardless of errors.
# Print a confirmation message (e.g., "File closed successfully.") inside this block.
# Error Handling: Include a specific except FileNotFoundError block to catch issues if the 
#file cannot be accessed or created.
# Execution: * Use your function in a with ... as ... statement.
# Write the text "Confidential data" to a file named secure.txt.
#Logic Flow Comparison
#Feature
#Class-Based (Original)
#Function-Based (New)
#Setup
#__enter__ method
#Code before the yield
#Passing the File
#return self.file
#yield file_object
#Teardown
#__exit__ method
#Code after the yield (in finally)
#Sample Run & Output
#After running your code, the file secure.txt should contain:
#Confidential data
#And the program console should print:
#File closed successfully.
#Submission Instructions

from contextlib import contextmanager


@contextmanager
def safe_file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file

    except FileNotFoundError:
        print(f"Error: {filename} not found.")

    finally:
        file.close()
        print("File closed successfully.")


with safe_file_manager("secure.txt", "w") as f:
    f.write("Confidential data")



#Task 3: Merging Monthly Reports (Context Managers & Multi-file I/O )
#Scenario (Analogy): Two teams submit their monthly performance reports, and you must combine
#  them as if fitting two puzzle pieces together. There are two files, data1.txt and data2.txt, each containing a list of numbers (one per line). Using a single with statement, open both files and read their contents. Create a new file sum_data.txt where each line is the sum of corresponding lines from data1.txt and data2.txt. Assume both files have the same number of lines. This task requires using multiple files in one with context and writing output.
#Requirements:
# Use one combined with statement to open all three files:
# with open("data1.txt","r") as f1, open("data2.txt","r") as f2, open("sum_data.txt","w") as fout:
# ...
#This ensures all files are properly managed and closed automatically.
# Read lines from f1 and f2 simultaneously (e.g., using zip) and for each pair of lines, 
# convert to integers and write their sum to fout (followed by a newline).
# Print the contents of sum_data.txt after writing, or indicate that it has been written.
#  (For this assignment, show the output content explicitly as below.)
# Handle any unexpected errors (e.g. non-integer content) with try/except, printing an error and
#  stopping if conversion fails.
#Sample Data: File data1.txt:
#1
#2
#3
#File data2.txt:
#4
#5
#6
#Expected sum_data.txt content (and output):
#5
#7
#9
#(Explanation: 1+4=5, 2+5=7, 3+6=9)

try:
    with open("fruits.txt", "r") as f1, \
         open("data.txt", "r") as f2, \
         open("sum_data.txt", "w") as fout:

        for line1, line2 in zip(f1, f2):
            num1 = int(line1.strip())
            num2 = int(line2.strip())

            total = num1 + num2

            fout.write(str(total) + "\n")

except ValueError:
    print("Error: File contains non-integer data.")



        