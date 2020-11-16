import os
p=input("Do you want to do this on Remote[R],Local[L],AWS Instance[I]: ")
if p=="L": 
		print("Your available Hard Disks")
		os.system("fdisk -l")
		disk1 = input("Enter the name of disk 1: ")
		disk2 = input("Enter the name of disk 2: ")
		os.system("pvcreate {}".format(disk1))
		os.system("pvcreate {}".format(disk2))
		os.system("pvdisplay")
		volgrp = input("Enter volume group name: ") 
		os.system("vgcreate {0} {1} {2}".format(volgrp,disk1.disk2))
		os.system("vgdisplay")
		logvol=input("\n\n\nEnter the name for logical volume: ")
		size = input("Enter the size for Logical Volume in GB: ")
		os.system("lvcreate --size {0}G --name {1} {2}".format(size,logvol,volgrp))
		os.system("lvdisplay")
		os.system("mkfs.ext4 /dev/{0}/{1}".format(volgrp,logvol))
		mountdir = input("Enter the path of directory to mount: ")
		os.system("mount /dev/{0}/{1} {2}".format(volgrp,logvol,mountdir))
		os.system("df -h")
elif p=="R":
		ip = input("Enter Ip Address: ")
		os.system("scp -r lvmorgrem.py root@{}:/".format(ip))
		os.system(r"ssh root@{} python3 /lvmorgrem.py".format(ip))
elif p=="I":
		ip = input("Enter Ip Address: ")
		os.system("scp -i hadoopkey.pem -r lvmorgrem.py ec2-user@{}:~".format(ip))
		os.system("ssh -i hadoopkey.pem -l ec2-user {} sudo python3 lvmorgrem.py".format(ip))
	 
else:
		print("can't understand")
		

