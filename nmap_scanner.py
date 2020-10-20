import nmap3
scann1 = nmap3.PortScanner()
ns.scan("192.168.100.6", "1-1024", "-v")
print(scann1.scaninfo())
print(scann1.csv())

