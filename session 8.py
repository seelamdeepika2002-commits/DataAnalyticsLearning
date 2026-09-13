#Session – 8

#Task 1: The Multi-Vector Firewall (*args & kwargs)
# Analogy: A security gateway receives packets from various sources. Some send raw IP 
# addresses (positional), while others send detailed security metadata 
# like "encryption_type" or "threat_level" (keyword).
# The Task: Create a function analyze_traffic(source_name, *ips, **metadata) that collects 
# multiple IP addresses and various security tags.
# Input: analyze_traffic("Mainframe_A", "192.168.1.1", "10.0.0.5", "172.16.0.1", 
# threat_level="High", protocol="SSH")
# Expected Output:
#"Source: Mainframe_A | Analyzed 3 IPs | Security Tags: threat_level, protocol"

def analyze_traffic(source_name, *ips, **metadata):
    print(
        f"Source: {source_name} | "
        f"Analyzed {len(ips)} IPs | "
        f"Security Tags: {', '.join(metadata.keys())}"
    )


analyze_traffic(
    "Mainframe_A",
    "192.168.1.1",
    "10.0.0.5",
    "172.16.0.1",
    threat_level="High",
    protocol="SSH"
)


#Task 2: The Instant Payload Decoder (Lambda & Map)
# Analogy: Data packets are encoded in a specific "Shift-Key" format. To inspect them, 
# every byte (integer) in a list must be transformed by a mathematical "security key."
# The Task: Use map() and a Lambda to process a list of integers. The transformation logic
#  is: If the number is even, multiply by 2; if odd, add 5.
# Input: payload = [10, 15, 20, 25]
# Expected Output: [20, 20, 40, 30]

payload = [10, 15, 20, 25]

decoded_payload = list(
    map(lambda x: x * 2 if x % 2 == 0 else x + 5, payload)
)

print(decoded_payload)


#Task 3: The Darknet Traffic Purge (Filter & Scope)
# Analogy: Your engine must filter out traffic originating from blacklisted ports.
#  The "Blacklist" is maintained at the Global level by the agency.
# The Task: Define a Global Variable BLACKLIST_RANGE = range(1000, 2000).
#  Write a function filter_ports(ports) that uses filter() and a Lambda to remove any port
#  found in the global blacklist.
# LEGB Challenge: Inside the function, try to create a Local Variable with the same 
# name BLACKLIST_RANGE containing range(0, 500). Explain which range Python uses for the filter and why.
# Input: ports = [80, 443, 1050, 21, 1500]
# Expected Output: [80, 443, 21]

BLACKLIST_RANGE = range(1000, 2000)


def filter_ports(ports):
    BLACKLIST_RANGE = range(0, 500)

    filtered_ports = list(
        filter(lambda port: port not in BLACKLIST_RANGE, ports)
    )

    return filtered_ports


ports = [80, 443, 1050, 21, 1500]

print(filter_ports(ports))



#Task 4: The Signature Hash Aggregator (Reduce)
# Analogy: To verify a file's integrity, you must combine all individual block signatures
#into a single "Master Hash" by finding the greatest common divisor (GCD) or acumulative sum.
# The Task: Use functools.reduce and a Lambda to find the cumulative product of a
#list of security tokens, but with a fail-safe: if the running product exceeds 1,000,000, the
#lambda should reset the current product to the next token value (to prevent overflow).
# Input: tokens = [10, 100, 5, 200, 2]
# Expected Output: 2000 (Calculation: 101005 = 5000; 5000*200 = 1,000,000. Limit
#reached, next product starts at 2).

from functools import reduce

tokens = [10, 100, 5, 200, 2]

def calculate_product(product, token):
    if product * token >= 1_000_000:
        return token
    return product * token

result = reduce(calculate_product, tokens)

print(result)



#Task 5: The Modular Threat Dispatcher (Higher-Order Functions)
# Analogy: A "Modular Dispatcher" accepts a dataset and a "Detection Strategy" (which is
#another function). This allows the system to swap security protocols without changing the main engine.
# The Task: Define a function security_engine(data_stream, strategy).
#1. The strategy argument must be a function (like a map or filter logic passed as an argument).
#2. Use the engine to apply a "Sensitivity Boost" (multiply all inputs by 1.5) and then
#a "Noise Reduction" (filter out values below 100).
# Input: raw_stream = [50, 80, 120, 200]
# Expected Output: [120, 180, 300] (After 1.5x boost: [75, 120, 180, 300]. After filter
#> 100: [120, 180, 300]).

def security_engine(data_stream, strategy):
    # Apply the detection strategy
    return strategy(data_stream)


# Detection strategy
def detection_strategy(data_stream):
    # Step 1: Sensitivity Boost - multiply every value by 1.5
    boosted = list(map(lambda x: x * 1.5, data_stream))

    # Step 2: Noise Reduction - keep values greater than 100
    filtered = list(filter(lambda x: x > 100, boosted))

    return filtered


# Input
raw_stream = [50, 80, 120, 200]

# Pass the function as an argument
result = security_engine(raw_stream, detection_strategy)

print(result)

