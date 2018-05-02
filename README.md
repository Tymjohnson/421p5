# 421p5
Project 5 for CSCI 421
TO RUN
  Ensure you are using the Security Lab machine, running Linux.
  Ensure GUI.py and dnsSpoof.py are in the same directory
  Execute GUI.py using "python GUI.py"
  Press the "start" button
  Visit or ping any web site, you should see an IP response
    If the IP is not showing as (10.0.0.X), launch Wireshark and filter for udp port 53 traffic
    You should see packets from 8.8.8.8, then 10.10.10.X, this means that Google's DNS servers are repsonding faster than the     program, but the program is "working" just fine.
