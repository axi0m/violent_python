# author: axi0m
# purpose: banner grabber
# usage: ftp_banner_grabber.py <vuln banner file>
# changelog: 02/21/18 - initial creation
#            02/23/18 - minor updates and rename file
#            02/26/18 - adding vuln_banners.txt file to read in and iterate over, also changed name of script, had typo

import socket
import sys
import os

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return str(banner)
    except:
        return

def checkVulns(banner):
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("[+] Server is vulnerable: " + banner.strip('\n'))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] " + filename + " does not exist!")
            exit(0)
        if not os.access(filename, os.R_OK):
            print("[-] " + filename + " access denied.")
            exit(0)
        else:
            print("[+] Reading Vulnerabilities From: " + filename)
            portList = [21, 22, 25, 80, 110, 443]
            for x in range(1, 10):
                ip = '192.168.1.' + str(x)
                for port in portList:
                    banner = retBanner(ip, port)
                    if banner:
                        print('[+] ' + ip + ': ' + banner.strip('\n'))
                        checkVulns(banner)

if __name__ == '__main__':
    main()