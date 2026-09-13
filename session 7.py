#  Session – 7

#Task 1: The Secure Vault Gateway

# Analogy: A vault requires a primary key and an optional secondary biometric override.
# Requirement: Define a function access_vault with one mandatory positional argument  user_id and two 
# keyword-onlyarguments (using the * separator): pincode and biometric_id (defaulting to None).
# Technical Goal: Master the use of Keyword-Only Arguments to prevent accidental
#  credential leaking through positional placement.

def access_vault(user_id,*,pincode,biometric_id=None):
    if biometric_id is not None:
        return f"vault accessed by user {user_id} using pin and biometric_id."
    else:
        return f" vault accessed by user {user_id} using pin."

print(access_vault(101, pincode=1234))
print(access_vault(102, pincode=5678, biometric_id="BIO123"))


#Task 2: The Bulk Transfer Processor
# Analogy: A corporate client wants to send different amounts to various subsidiaries in one go.
# Requirement: Define a function execute_bulk_transfer that accepts a sender_account (positional) 
# and a variable number of amounts using *args.
# Side Effect vs. Return: The function must print a ledger line for every transfer (side effect)
#  but return the final remaining balance after subtracting all amounts from a starting balance of 10,000.

def execute_bulk_transfer(sender_account, *amounts):
    balance = 10000

    for amount in amounts:
        balance -= amount
        print(f"Transfer of ₹{amount} made from account {sender_account}")

    return balance


# Calling the function
remaining_balance = execute_bulk_transfer("ACC101", 2000, 1500, 500, 1000)

print(f"Final remaining balance: ₹{remaining_balance}")



#Task 3: Dynamic Fee Policy
# Analogy: Different countries have different tax/fee keys.
# Requirement: Define a function calculate_net_amount that uses **kwargs to accept various
#  tax rates (e.g., vat=0.15, service_fee=0.05).
# Logic: The function should take a base_amount and iterate through the kwargs to apply
#all taxes dynamically, returning the final figure.

def calculate_net_amount(base_amount, **kwargs):
    final_amount = base_amount

    for fee_name, fee_rate in kwargs.items():
        fee = final_amount * fee_rate
        final_amount -= fee

    return final_amount


# Example
net_amount = calculate_net_amount(
    10000,
    vat=0.15,
    service_fee=0.05
)

print(f"Final amount: ₹{net_amount:.2f}")


#Task 4: The Currency Arbitrage Scanner
# Analogy: A trader needs to know the Buy price, Sell price, and the Spread (difference) simultaneously.
# Requirement: Create a function get_market_rates(ticker). It must return a Tuple containing 
# three floats: (buy_price, sell_price, spread).
# Technical Goal: Demonstrate Multiple Return Values and show how the caller can use"Under-score ignoring"
#  (e.g., buy, _, spread = get_market_rates('USD')) if they don't need the sell price.


def get_market_rates(ticker):
    buy_price = 83.50
    sell_price = 84.20
    spread = sell_price - buy_price

    return buy_price, sell_price, spread


# Get all three values
buy, sell, spread = get_market_rates("USD")

print("Buy Price:", buy)
print("Sell Price:", sell)
print("Spread:", spread)


#Task 5: Account Validation Wrapper
# Analogy: Before a transaction, a system checks if the account is active and if the 
# KYC (Know Your Customer) is complete.
# Requirement: Write a function validate_account_status(account_id).
# Return Logic: It must return a Nested Tuple: (status_code, (is_active,kyc_complete)).
# Challenge: The candidate must write a calling script that uses Nested Unpacking to
#extract kyc_complete in a single line

def validate_account_status(account_id):
    status_code = 200
    is_active = True
    kyc_complete = True

    return status_code, (is_active, kyc_complete)


# Nested unpacking
status_code, (is_active, kyc_complete) = validate_account_status("ACC101")

print("Status Code:", status_code)
print("Account Active:", is_active)
print("KYC Complete:", kyc_complete)


# Extract only KYC status
_, (_, kyc_complete) = validate_account_status("ACC101")

print("KYC Complete:", kyc_complete)

#Task 6: The Auditor’s Google-Style Docstring
# Analogy: Regulators require every financial calculation to be perfectly documented for audits.
# Requirement: Take a complex function that calculates Compound Interest. Write a
#complete Google-Style Docstring.
# Criteria: Must include Args:, Returns:, and a Yields: section (if applicable) or
#Raises: section for ValueError on negative interest rates.

def calculate_compound_interest(principal, annual_rate, years, compounds_per_year):
    """Calculate the final amount using compound interest.

    Args:
        principal (float): The initial amount of money invested.
        annual_rate (float): The annual interest rate as a decimal.
            For example, 5% should be provided as 0.05.
        years (int): The number of years the money is invested.
        compounds_per_year (int): The number of times interest is
            compounded per year.

    Returns:
        float: The final amount after compound interest is applied.

    Raises:
        ValueError: If annual_rate is negative.
        ValueError: If principal, years, or compounds_per_year is
            less than or equal to zero.

    """
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")

    if years <= 0:
        raise ValueError("Years must be greater than zero.")

    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be greater than zero.")

    final_amount = principal * (
        1 + annual_rate / compounds_per_year
    ) ** (compounds_per_year * years)

    return final_amount


# Calling the function
amount = calculate_compound_interest(10000, 0.05, 5, 12)

print(f"Final Amount: ₹{amount:.2f}")



#Task 7: NumPy-Style Scientific Schema
# Analogy: The Risk Assessment team uses NumPy-style documentation for their mathematical models.
# Requirement: Define a function calculate_risk_score(data_points,sensitivity). Write the docstring 
# using NumPy formatting (using underlines forsections). Ensure types like array-like or float  
# are correctly specified.

def calculate_risk_score(data_points, sensitivity):
    """
    Calculate a risk score from a set of data points.

    Parameters
    ----------
    data_points : array-like
        Collection of numerical data points used to calculate
        the risk score.

    sensitivity : float
        Sensitivity factor used to adjust the calculated risk score.

    Returns
    -------
    float
        The calculated risk score.

    Raises
    ------
    ValueError
        If sensitivity is negative.
    """
    if sensitivity < 0:
        raise ValueError("Sensitivity cannot be negative.")

    average = sum(data_points) / len(data_points)
    risk_score = average * sensitivity

    return float(risk_score)


# Example
data = [10, 20, 30, 40, 50]

score = calculate_risk_score(data, 0.8)

print("Risk Score:", score)


#Task 8: The "Print vs. Return" Audit
# Requirement: Provide a code snippet where a function uses print() inside its body to
#show a result, but forgets the return statement.
# Task: The candidate must debug why the variable result = my_function() evaluatesto None and explain 
# the architectural danger of using print as a substitute for data flow in a production pipeline.

def calculate_total(price, tax):
    total = price + (price * tax)
    print("Total:", total)


result = calculate_total(1000, 0.18)

print("Result variable:", result)


#Task 9: Functional Pipeline Design
# Requirement: Create three small functions: clean_input(), apply_discount(), and format_currency().
# Task: Write a "Master" function process_invoice that pipes data through all three.
# Evaluation: The candidate must justify why using Tuples to pass data between these
#functions is safer than using Global Variables.

def clean_input(invoice_data):
    """Clean the invoice data."""
    customer, amount = invoice_data

    customer = customer.strip()
    amount = float(amount)

    return customer, amount


def apply_discount(invoice_data):
    """Apply a 10% discount to the invoice amount."""
    customer, amount = invoice_data

    discount = amount * 0.10
    final_amount = amount - discount

    return customer, final_amount


def format_currency(invoice_data):
    """Format the invoice amount as currency."""
    customer, amount = invoice_data

    formatted_amount = f"₹{amount:.2f}"

    return customer, formatted_amount


def process_invoice(invoice_data):
    """Process an invoice through all pipeline stages."""
    data = clean_input(invoice_data)
    data = apply_discount(data)
    data = format_currency(data)

    return data


# Example
invoice = ("  Deepika  ", "5000")

result = process_invoice(invoice)

print(result)



#Task 10: The Fail-Safe Dispatcher
# Analogy: If a transaction fails, the system shouldn't crash; it should return a "Fail State"and a reason.
# Requirement: Create a function dispatch_payment that returns a Tuple(Success_Bool, Error_Message_Or_None).
# Logic: If Success_Bool is False, the second element must be a string. If True,
#  the second element must be None.
# Documentation: Write a docstring explaining this specific "Result Pattern" 
# (similar to Rust or Go error handling).

def dispatch_payment(amount):
    """
    Process a payment and return its result using the Result Pattern.

    This function follows a Result Pattern similar to error handling
    in languages such as Rust or Go.

    Returns:
        tuple:
            A tuple containing:

            - bool: True if the payment succeeds, otherwise False.
            - str or None: An error message when the payment fails.
              None when the payment succeeds.

    Result Pattern:
        (True, None)
            Indicates successful payment.

        (False, "error message")
            Indicates failed payment and provides the reason.

    The caller can check the first value to determine whether the
    operation succeeded and use the second value only when an error
    occurred.
    """

    if amount <= 0:
        return False, "Payment amount must be greater than zero."

    if amount > 10000:
        return False, "Payment exceeds the maximum allowed limit."

    # Payment processing would happen here
    return True, None


# Successful payment
success, error = dispatch_payment(5000)

if success:
    print("Payment successful.")
else:
    print("Payment failed:", error)


# Failed payment
success, error = dispatch_payment(15000)

if success:
    print("Payment successful.")
else:
    print("Payment failed:", error)




    