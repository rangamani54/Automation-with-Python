import os 
print("Your available Hard Disks")
os.system("fdisk -l")
disk1 = input("Enter the name of disk 1: ")
disk2 = input("Enter the name of disk 2: ")
os.system("pvcreate {}".format(disk1))
os.system("pvcreate {}".format(disk2))
os.system("pvdisplay")
volgrp = input("Enter volume group name: ") 
os.system("vgcreate {0} {1} {2}".format(volgrp,disk1,disk2))
logvol=input("Enter the name for logical volume: ")
size = input("Enter the size for Logical Volume: ")
os.system("lvcreate --size {0}G --name {1} {2}".format(size,logvol,volgrp))
os.system("mkfs.ext4 /dev/{0}/{1}".format(volgrp,logvol))
mountdir = input("Enter the path of directory to mount: ")
os.system("mount /dev/{0}/{1} {2}".format(volgrp,logvol,mountdir))
os.system("df -h")
input("click enter to continue")
exit()