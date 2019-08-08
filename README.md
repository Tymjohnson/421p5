Requirements: Primary OS <br /> 
VM of Linux (Any distro, I used RedHat). <br />
Python 3 installed <br />
Scapy installed <br />
Wireshark installed on Main OS <br />
TO RUN <br /> 
  Have a VM running Linux and a primary OS up and running<br />
  Ensure GUI.py and dnsSpoof.py are in the same directory on the VM<br />
  Execute GUI.py using "python GUI.py"
  Press the "start" button
  Visit or ping any web site, you should see an IP response
    If the IP is not showing as (10.0.0.X), launch Wireshark and filter for udp port 53 traffic
    You should see packets from 8.8.8.8, then 10.0.0.X, this means that Google's DNS servers are repsonding faster than the     program, but the program is "working" just fine.
