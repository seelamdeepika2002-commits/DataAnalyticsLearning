#Task 1: The "Safe Lookup" Dictionary Engine
#Objective: Master Key-Value manipulation and the importance of the .get() method for error-free data retrieval.
#1. Data Setup: Create a dictionary named inventory with the following initial data: "sku_01": 50,
#  "sku_02": 150, "sku_03": 75.
inventory={"sku_01":50,"sku_02":150,"sku_03":75}
print(inventory)
#2. Operations:
# Use the .update() method to add a new item "sku_04" with a value of 200.
# Retrieve the value for "sku_02" using direct bracket notation.
# Use the .get() method to search for "sku_05". Provide a default
#  return value of 0 to handle the missing key safely.
inventory.update({"sku_04":200})
print("updated _inventory:",inventory)
sku_02_value =inventory["sku_02"]
print("value of sku_02:",sku_02_value)
sku_05_value=inventory.get("sku_05",0)
print("value of sku_05:",sku_05_value)
#3. Analysis: Use .keys() and .values() to 
# print the list of all IDs and the list of all stock counts respectively.
ids=list(inventory.keys())
stock_counts=list(inventory.values())
print('all ids are:',ids)
print("all values are:",stock_counts)
#4. Transformation: Print the dictionary as a list of tuples using the .items() method.
inventory_list=list(inventory.items())
print("inventory as list of tuples:",inventory_list)
#Task 2: Deep Access in Nested JSON-like Structures
#Objective: Navigate multi-layered data structures (List of Dicts and Dict of Lists) without using loops.
#1. Data Setup: Create a variable named api_response that mimics a JSON object:
#Python
#api_response = {
#"status": "success",
#"data": [
#{"id": 1, "info": {"email": "user1@work.com", "tags": ["admin", "dev"]}},
#{"id": 2, "info": {"email": "user2@work.com", "tags": ["guest"]}}]}
api_response= {
"status": "success",
"data": [
{"id": 1, "info": {"email": "user1@work.com", "tags": ["admin", "dev"]}},
{"id": 2, "info": {"email": "user2@work.com", "tags": ["guest"]}}]}
print("the api_response:",api_response)
#2. Extraction Challenge: * Access the email of the first
#  user in the list and store it in user_1_email.
# Access the second tag of the first user ("dev") and store it in user_1_secondary_tag.
# Retrieve the ID of the last user in the list using negative indexing.
user_1_email=api_response["data"][0]["info"]["email"]
print("user_1_email is:",user_1_email)
user_1_secondary_tag= api_response ["data"][0]["info"]["tags"][1]
print("user_1_secondary_tag is:",user_1_secondary_tag)
last_user_id=api_response["data"][-1]["id"]
print("last user id is:",last_user_id)
#3. Observation: Print the type() of api_response["data"] and api_response["data"][0]["info"].
print(type(api_response["data"]))
print(type(api_response["data"][0]["info"]))
#Task 3: String Sanitization & Cleaning Pipeline
#Objective: Perform industrial-strength string cleaning 
#using .strip(), .replace(), and .find().
#1. Raw Data: Create a string: raw_log = " ERROR_CODE: 404 | STATUS: NOT_FOUND | SOURCE: SERVER_01 "
raw_data="ERROR_CODE:404|STATUS:NOT_FOUND|SOURCE:SERVER_01"
print("Raw Data is:",raw_data)
#2. The Pipeline:
# Remove the leading and trailing whitespace using .strip().
# Replace all underscores (_) with spaces.
# Use the .find() method to locate the index of the vertical bar |.
# Convert the entire string to lowercase for uniform processing.
cleaned_data=raw_data.strip()
print("cleaned_data:",cleaned_data)
replaced_data=cleaned_data.replace("|","  ")
print("replacing data is:",replaced_data)
bar_index=cleaned_data.find("|")
print("index of the vertical bar is:",bar_index)
cleaned_log=cleaned_data.lower()
print("converted the entire string into lower case is:",cleaned_log)
#3. Verification: Print the final "cleaned" version of the log.
print('cleaned_log is:',cleaned_log)
#Task 4: The CSV-to-Python Parser (Split & Join)
#Objective: Convert raw CSV-style strings into Python structures and back again.
#1. Deconstruction: You are given a CSV row: csv_data = "Apple,iPhone,1200,Silver".
# Use .split(",") to turn this into a list called product_details.
#2. Modification: Change the price (at index 2) to "1300".
#3. Reconstruction: Use the .join() method to convert the list 
# back into a single string, but use a semicolon (;) as the new separator.
#4. Header Generation: Create a header string "BRAND;MODEL;PRICE;COLOR"
#  and concatenate it with your reconstructed string, separated by a newline character (\n).
CSV_data="Apple,iphone,1200,silver"
product_details=CSV_data.split(",")
print("product details is:",product_details)
product_details[2]="1300"
print( 'modification data is:',product_details)
reconstructed_data = ";".join(product_details)
print("Reconstructed Data:", reconstructed_data)
header="BRAND;MODEL;PRICE;COLOR"
final_output=header+"\n"+reconstructed_data
print("final output is:",final_output)
#Task 5: Atomic Dictionary Merging & Popping
#Objective: Advanced dictionary methods for data management.
#1. Merging: Create two dictionaries: personal_info = {"name": "John", "age": 30} 
# and job_info = {"salary": 5000, "role": "Analyst"}.
# Use the Dictionary Union Operator (|) to merge them into a new dictionary called full_profile.
#2. Extraction: Use the .pop() method to remove the "age" key from
#  full_profile and store the removed value in a variable called removed_age.
#3. Clearing: Use the .clear() method on the personal_info dictionary. Print its 
# length to prove it is now empty.
personal_info = {"name": "John", "age": 30} 
job_info = {"salary": 5000, "role": "Analyst"}
full_profile=personal_info | job_info
print("full profile of a person is:",full_profile)
removed_age=full_profile.pop("age")
print("after removed age full profile is:",removed_age)
cleared_data=personal_info.clear()
print("length of the personal info is:",len(personal_info))




