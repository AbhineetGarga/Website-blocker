import platform
import subprocess
import schedule
import time
import os

# Define blocked websites
blocked_websites = ["example.com", "example1.com"] #Donot Add https or www

# Determine the hosts file path based on the operating system
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() in ["Darwin", "Linux"]:
    hosts_path = "/etc/hosts"
else:
    print("Unsupported operating system")
    exit(1)

redirect_ip = "127.0.0.1"

def block_websites():
    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            file.seek(0)
            for website in blocked_websites:
                if f"{redirect_ip} {website}" not in content:
                    file.write(f"{redirect_ip} {website}\n")
                    file.write(f"{redirect_ip} www.{website}\n")  # Block www subdomain
            file.truncate()
        print("Websites blocked")
        # Flush DNS cache
        if platform.system() == "Windows":
            subprocess.run(["ipconfig", "/flushdns"])
        elif platform.system() == "Darwin":
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"])
    except Exception as e:
        print(f"Error blocking websites: {e}")

def unblock_websites():
    try:
        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()
        print("Websites unblocked")
        # Flush DNS cache
        if platform.system() == "Windows":
            subprocess.run(["ipconfig", "/flushdns"])
        elif platform.system() == "Darwin":
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"])
    except Exception as e:
        print(f"Error unblocking websites: {e}")

schedule.every().day.at("20:00").do(block_websites)  # Block websites at 8:00 PM
schedule.every().day.at("02:00").do(unblock_websites)  # Unblock websites at 2:00 AM

while True:
    schedule.run_pending()
    time.sleep(1)