import os
p=input("Do you want to do this on Remote[R],Local[L],AWS Instance[I]: ")
if p=="L": 
		#print("Your available Hard Disks")
		os.system("df -hT")
		
		volgrp = input("Enter volume group name: ") 
		os.system("vgdisplay {0}".format(volgrp))
		logvol=input("Enter the name of logical volume: ")
		size = input("Enter the incremental size(GB): ")
		os.system("lvextend --size +{}G /dev/{}/{}".format(size,volgrp,logvol))
		os.system("resize2fs /dev/{}/{}".format(volgrp,logvol))
		
		os.system("df -h")
elif p=="R":
		ip = input("Enter Ip Address: ")
		os.system("scp -r lvmextendorgrem.py root@{}:/".format(ip))
		os.system(r"ssh root@{} python3 /lvmextendorgrem.py".format(ip))
elif p=="I":
		ip = input("Enter Ip Address: ")
		os.system("scp -i hadoopkey.pem -r lvmextendorgrem.py ec2-user@{}:~".format(ip))
		os.system("ssh -i hadoopkey.pem -l ec2-user {} sudo python3 lvmextendorgrem.py".format(ip))
	 
else:
		print("can't understand")
		
