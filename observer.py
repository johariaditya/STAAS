#!/usr/bin/python2

import os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.USER_DGRAM)
s.bind(("",8888)


data=s.recvfrom(20)
d_name=data[0]
d_name=data[0]

data1=s.recvfrom(10)
d_size=data1[0]

cliaddr=data1[1][0]

os.system('lvcreate --name '+d_name+' --size '+d_size+'M adhocvg')

os.system('mkfs.ext4  /dev/adhocvg/' +d_name)

os.system(' mkdir /mnt/' +d_name)

os.system('mount /dev/adhocvg/' +d_name+' /mnt/' +d_name)

os.system('yum install nfs-utils -y')

entry="/mnt/"+d_name+" " +cliaddr+ "(rw,no_root_squash)"

f=open('/etc/exports','a')
f.write(entry)
f.close()

os.system('systemctl restart nfs-server')
os.system('systemctl enable nfs-server')
check=os.system('exportfs -r')
if check == 0:
	s.sendto("done",data1)
else:
	print "Please check your code"

