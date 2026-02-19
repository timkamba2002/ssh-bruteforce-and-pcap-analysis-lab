import re

file_path = "./auth.log"

pattern = r'^([A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+([^\[\s]+)\[(\d+)\]:\s+(.*)$'

with open(file_path, "r") as f:
    for line in f:
        m = re.match(pattern, line)
        if m:
            date_time = m.group(1)
            host_name = m.group(2)
            process_name = m.group(3)
            process_id = m.group(4)
            log_message = m.group(5)

            print("Date and time:", date_time)
            print("Host name:", host_name)
            print("Process name:", process_name)
            print("Process ID:", process_id)
            print("Log Message:", log_message)
            print("-" * 40)





"""
Prompt that I gave to the AI:

I am using python and trying to parse a log file.
here are the codes that I currently have:
import re

file_path = '/auth.log'

pattern = r''

Here is an example of the log entry that I have in that log file:
Dec 29 21:30:12 websystem sshd[8906]: Failed password for invalid user cmc from 198.38.11.222 port 32145 ssh2

I need string regular expression for parsing each log entry and dividing it into 5 groups and print each of them:
1. Date and time
2. Host name
3. Process name
4. Process ID
5. Log Message

Make sure that the string regular expression you write is valid and correct.

In your response, only give me the codes in a code snippet, and nothing else.
"""