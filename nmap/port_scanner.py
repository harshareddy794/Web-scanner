import socket
target = '127.0.0.1'
target_IP = socket.gethostbyname(target)

top_20_ports=[20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
for port in top_20_ports: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    socket.setdefaulttimeout(1) 
        
    # returns an error indicator 
    result = s.connect_ex((target_IP,port)) 
    if result ==0: 
        print("Port {} is open".format(port)) 
    s.close() 



