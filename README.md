# 🔐 Failed SSH Login Detector (Linux)

This project parses real Linux system logs to detect failed SSH login attempts — simulating a brute force detection system used by SOC analysts.

## 🚀 Features
- Parses systemd journal logs (`journalctl`) for failed SSH logins
- Extracts timestamp, username, and IP address
- Outputs results to a CSV file
- Uses Python + pandas + regex

## 🧪 Sample Output
```
timestamp,username,ip_address
Jun 22 06:50:28,fakeuser,::1
Jun 22 06:50:41,fakeuser,::1
Jun 22 06:50:46,fakeuser,::1
```
## 🛠️ How to Run
1. Export log entries:
   ```bash
   sudo journalctl _COMM=sshd | grep "Failed password" > failed_ssh.log

2. Run the script:
python3 parse_failed_logins.py

3. View results:
cat failed_logins.csv


📚 Skills Demonstrated
Regex parsing from real system logs

Linux authentication flow

Basic SOC analysis logic

Script automation for detection

📎 Tags
#SOC #Python #Cybersecurity #Linux #BruteForceDetection



