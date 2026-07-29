# honeypot
a sample honeypot
⚠️ Critical Safety Rules
Isolate it: Run this inside a dedicated Virtual Machine (VM) like Ubuntu Linux or Kali Linux.
Do not expose home networks: If you forward your home router's ports to this script, advanced hackers could exploit your script's code to compromise your actual machine.
Use non-root ports: Ports below 1024 (like real SSH Port 22) require root/administrator privileges. 
Stick to high ports like 2222 or 8080 for safe testing.
