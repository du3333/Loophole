import re
import os
import sys
def dns_zone_tranfer_finder(domain):
    #print('[+] Nslookup %s' % domain)
    #cmd_res = os.popen('nslookup -type=ns ' + domain).read()
    #dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
   # if len(dns_servers) == 0:
        #print('[+] No DNS Server Found!\n')
       # exit(0)
    #for singledns in dns_servers:
        #print('[+] Using @%s' % singledns)
        singledns="vulhub.org"
        cmd_res = os.popen('dig @%s axfr %s' % (domain, singledns)).read()
        #print( cmd_res)

        if cmd_res.find('XFR size:') > 0:
            print('[+] Vulnerable dns server found:', singledns)
            print (cmd_res)
            print("1")
            return 1
        else:
            print('[+] No Vulnerable found')
            print("0")
            return 0

def usage():
    print('[+] Usage: python DZT-tester.py [domain]\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    elif '-h' in sys.argv[1]:
        usage()
    else:
        domain = sys.argv[1]
        print('[+] Test %s' % domain)
        dns_zone_tranfer_finder(domain)
        print('[+] Finished!')