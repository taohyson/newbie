@ECHO OFF
rem ARP /?

ARP -A
ARP -D 192.168.160.255
ARP -S 192.168.160.255 ff-ff-ff-ff-ff-ff