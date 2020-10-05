import os
import platform

from datetime import datetime
net = ["192.168.255.0", "192.168.253.0"]
with open("list_device.txt", "w") as f:
    for _ in net:
        print ("Scanning network: ", _)

        net1= _.split('.')
        a = '.'

        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        st1 = 0
        en1 = 63
        en1 = en1 + 1
        oper = platform.system()

        if (oper == "Windows"):
           ping1 = "ping -n 1 "
        elif (oper == "Linux"):
           ping1 = "ping -c 1 "
        else :
           ping1 = "ping -c 1 "
        t1 = datetime.now()

        for ip in range(st1,en1):
            addr = net2 + str(ip)
            comm = ping1 + addr
            response = os.popen(comm)

            for line in response.readlines():
                if(line.count("ttl")):
                    print (addr, "--> Live")
                    f.write(addr + "\n")

t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: ", str(total))
