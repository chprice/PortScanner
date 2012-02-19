import socket, sys
def scan(address, port):
    s = socket.socket()
    s.settimeout(1.0)
    try:
        s.connect((address, port))
        return True 
    except socket.error:
        return False
    except socket.timeout:
        return False
    s.close()

def scanRange(ip, numComputers, portList):
    count =0
    master =[]
    addr = ip
    while count < numComputers:
        print("Scanning: "+addr)
        for port in portList:
            if(scan(addr, port)):
                master.append([addr, port])
        count=count+1
        addr = incr(addr.split("."))
    return master


def incr(ip):
    d = int(ip[3])+1
    c = int(ip[2])
    b = int(ip[1])
    a = int(ip[0])
    if(d==256):
        c = c+1
        d=0
        if(c==256):
            b= b+1
            c=0
            if(b==256):
                a=a+1
                b=0
                if(a==256):
                    print("Fuck you >__>")
    return str(a) +"."+ str(b) +"."+ str(c) +"."+ str(d)


def listDump(name, ipList):
    try:
        filehandle = open(name, "w")
    except IOError:
        print("Can't dump ips")
        return
    for ip in ipList:
        filehandle.write(ip[0]+" "+str(ip[1])+"\n")
    filehandle.close()

def scanner(ip, num, ports):
    listDump(ip+str(num)+".txt", scanRange(ip, num, ports))

print("Welcome to the port scanner I wrote in like 15 minutes.")
I = input("Input a starting ip address ")
N = int(input("Input the number of computers you want to scan "))
tempP = input("Input a list of ports you want to be scanned seperated by a comma (but no spaces, I'm lazy) ").split(",")
P=[]
for eh in tempP:
    P.append(int(eh))
fileName = input("Input a filename you want me to dump the results to (or - to use standard output) (just hit return to default) ")
data = scanRange(I, N, P)
if(fileName == "-"):
    for line in data:
        print(line[0]+" "+int(line[1]))
if(fileName == ""):
    listDump(I+str(N)+".txt", data)
else:
    listDump(fileName, data)
    
