import subprocess as sp
import os
while True:
		#form = cgi.FieldStorage()
		print("Press 1 to launch docker container\nPress 2 to start docker services\nPress 3 to see status of docker services\nPress 4 to attach docker container\nPress 5 to configure web server on running docker container\nPress 6 to setup python3 on running docker container\nPress 7 to know the IP Address of running docker container\nPress 8 to start docker container\nPress 9 to kill dokcer container\nPress 10 to know status of all docker containers\nPress 11 to see the running docker containers\nPress 12 to copy files from base os to docker container\nPress 13 to see docker images\nPress 14 to download docker os images\nPress 15 to install docker\nPress 16 to remove stopped docker conatiner\nPress 17 to remove all stopped containers\nPress 20 to exit")
		choice = input("\n\n\nEnter your choice: ")
		if int(choice)==1:

			osname = input("Enter the osname: ")
			osimage = input("Enter os image: ")
			#print(osname)


			cmd = "docker run -d -i -t --name {0} {1}".format(osname,osimage)


			output = sp.getstatusoutput(cmd)

			status = output[0]
			out = output[1]


			if status == 0:
			    print("Your required {1} launched named {0}".format(osname,osimage))
			else:
			    print("Error occured : {}".format(out))
		elif int(choice)==2:
			os.system("systemctl stop firewalld")
			os.system("setenforce 0")
			os.system("systemctl start docker")
		elif int(choice)==3:
			os.system("systemctl status docker")
		
		elif int(choice)==4:
			idname=input("Enter os name or container id: ")
			os.system("docker attach {}".format(idname))
		elif int(choice)==5:
			idname=input("Enter os name or container id: ")
			os.system("docker exec {} yum install httpd -y".format(idname))
			os.system("docker exec {} /usr/sbin/httpd".format(idname))
		elif int(choice)==6:
			idname=input("Enter os name or container id: ")
			os.system("docker exec {} yum install python3 -y".format(idname))
		elif int(choice)==7:
			idname=input("Enter os name or container id: ")
			os.system("docker inspect {} | grep \"IPAddress\"".format(idname))
		elif int(choice)==8:
			idname=input("Enter os name or container id: ")
			os.system("docker start {}".format(idname))
		elif int(choice)==9:
			idname=input("Enter os name or container id: ")
			os.system("docker kill {}".format(idname))
		elif int(choice)==10:
			os.system("docker ps -a")
		elif int(choice)==11:
			os.system("docker ps")
		elif int(choice)==12:
			idname=input("Enter os name or container id: ")
			sourcpath=input("Enter the file name with path which you want to copy: ")
			destpath=input("Enter the path in docker container: ")
			os.system("docker cp {} {}:{}".format(sourcpath,idname,destpath))
		elif int(choice)==13:
			os.system("docker images")
		elif int(choice)==14:
			down=input("Enter the os image name: ")
			os.system("docker pull {}".format(down))
		elif int(choice)==15:
			dock=os.system("""echo '[docker]\nname=docker package\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0' >> /etc/yum.repos.d/docker.repo""")
			os.system("yum repolist")
			os.system("yum install docker-ce --nobest -y")
			os.system("systemctl start docker")
		elif int(choice)==16:
			rem=input("Enter os name or container id: ")
			os.system("docker rm {}".format(rem))
		elif int(choice)==17:
			os.system("docker rm `docker ps -aq`")
		elif int(choice)==20:
			exit()
		else:
			print("can't understand")
		input("click Enter to continue")
		