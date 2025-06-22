import re
import pandas as pd

log_path = 'failed_ssh.log'

pattern = r'Failed password for (invalid user )?(\w+) from ([\d.:a-fA-F]+) port (\d+)'

results = []

with open(log_path, 'r') as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            username = match.group(2)
            ip = match.group(3)
            timestamp = line[:15]
            results.append({'timestamp': timestamp, 'username': username, 'ip_address': ip})

df = pd.DataFrame(results)
df.to_csv('failed_logins.csv', index=False)

print(f"[+] Parsed {len(df)} failed login attempts.")
