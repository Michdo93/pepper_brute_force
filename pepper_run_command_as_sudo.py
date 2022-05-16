#!/usr/bin/python
import os
import sys
import qi

if __name__ == "__main__":

    ip_range = "192.168.0."

    for ip in range(0,256):
        ip_addr = ip_range + str(ip)
        print("trying to connect to: " + ip_addr)

        session = qi.Session()
        try:
            session.connect("tcp://" + ip_addr + ":" + str(9559))
            if sudo:
                root = ["/usr/bin/sudo"]
            else:
                root = ["/bin/su", "--command"]
            command = root + [ sys.argv[0] ]
            system_service = system_service = session.service("ALSystem")
            system_service.shutdown()
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + ip_addr + "\" on port " + str(9559) +".\n"
                   "Please check your script arguments. Run with -h option for help.")
