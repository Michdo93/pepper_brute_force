#!/usr/bin/python
import os
import nmap
import sys
import qi

if __name__ == "__main__":

    ip_range = "192.168.0."
    port = 9559
   
    # instantiate a PortScanner object
    scanner = nmap.PortScanner()
    
    for ip in range(0,256):
        ip_addr = ip_range + str(ip)
        
        # scan the target port
        res = scanner.scan(ip_addr,str(port))
   
        # the result is a dictionary containing 
        # several information we only need to
        # check if the port is opened or closed
        # so we will access only that information 
        # in the dictionary
        res = res['scan'][ip_addr]['tcp'][port]['state']        
        
        if res == "open":
            print("trying to connect to: " + ip_addr)

            session = qi.Session()
            try:
                session.connect("tcp://" + ip_addr + ":" + str(9559))
                system_service = system_service = session.service("ALSystem")
                system_service.shutdown()
            except RuntimeError:
                print ("Can't connect to Naoqi at ip \"" + ip_addr + "\" on port " + str(port) +".\n"
                       "Please check your script arguments. Run with -h option for help.")
