import re
from collections import Counter

# Path to the log file you want to analyze
file_path = './auth.log'

# Compile a regular expression to capture the IP address after "from"
# This looks for lines containing:
# "Failed password for ... from <IP>"
# and captures the IPv4 address as group 1.
pattern = re.compile(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)')

# Counter object to count how many times each IP appears
ip_counts = Counter()

# Open the log file in read mode
# encoding='utf-8' and errors='ignore' make it more robust to odd characters
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    # Process the file line by line
    for line in f:
        # Search each line for the pattern
        match = pattern.search(line)
        if match:
            # Extract the IP address from the regex group
            ip = match.group(1)
            # Increment the count for this IP address
            ip_counts[ip] += 1

# Iterate over IPs sorted by their count in descending order
for ip, count in ip_counts.most_common():
    # Print each IP and its number of failed login attempts
    print(f"{ip} ==========> {count} failed attempts")









"""
Prompt that I gave the AI:

I am using python and trying to parse a log file. 
here are the codes that I currently have:
import re 

file_path = './auth.log'

pattern = r''

Here is an example of the log entry that I have in that log file:
Dec 29 21:30:12 websystem sshd[8906]: Failed password for invalid user cmc from 198.38.11.222 port 32145 ssh2

I need you to write a script that can show how many failed attempts the IP address tried to login to our server. 

I want to display the IP address and their number of failed attempts in descending order.

In your response, only give me the codes in a code snippet, and nothing else.

"""


# IP reputation Check: https://www.ipqualityscore.com/ip-reputation-check
# IP details check: https://www.virustotal.com/gui/ip-address/218.92.0.97/details