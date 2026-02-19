import re

log_entry = "Dec 29 21:30:12 websystem sshd[8906]: Failed password for invalid user cmc from 198.38.11.222 port 32145 ssh2"

pattern = r'^(\w+\s+\d+\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(\w+)\[(\d+)\]:\s+(.*)$'

match = re.match(pattern, log_entry)
if match:
    date_time = match.group(1)
    host_name = match.group(2)
    process_name = match.group(3)
    process_id = match.group(4)
    log_message = match.group(5)

    print("Date and time:", date_time)
    print("Host name:", host_name)
    print("Process Name:", process_name)
    print("Process ID:", process_id)
    print("Log Message:", log_message)


"""
Prompt I give to AI: 

I am using python and trying to parse one single log entry.
Here are the codes that I currently have:
import re 

log_entry = "Dec 29 21:30:12 websystem sshd[8906]: Failed password for invalid user cmc from 198.38.11.222 port 32145 ssh2"

pattern = r''

I need string regular expressions for parsing the log and divided into 5 groups and print the groups:
1. Data and time 
2. Host name 
3. Process Name
4. Process ID
5. Log Message

Make sure that the string regular expression you write is valid and correct.

In your response, only give me the codes in a code snippet, and nothing.

"""