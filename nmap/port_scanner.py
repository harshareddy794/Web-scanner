import nmap

target='www.sathyabama.ac.in'
port=443
scanner = nmap.PortScanner()
top_20_ports=[20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]

print(scanner.scan(target,str(port)))
scanner.scaninfo()