#import speech_recognition as sr
import subprocess as sp
#import pyttsx3
import os
print("\t\t\t\tHi, Iam AWS assistant")
#pyttsx3.speak("Hi, Iam AWS assistant,tell me what you want to do")
login=input("Local [L] , Remote [R] : ")
if login=="L":
	while True :
	#r=sr.Recognizer()
	#with sr.Microphone() as source:
		#pyttsx3.speak("please say something")
		#print("\t\t\t\tstart say")
		#audio = r.listen(source)
		#print("\t\t\t\tspeech done")
		#pyttsx3.speak("Ok working on it")
		#data = r.recognize_google(audio)
			print("Press 1 to open see available key pairs\nPress 2 to create key pair\nPress 3 to create security group\nPress 4 to see available instances\nPress 5 to launch instance\nPress 6 to create EBS volume\nPress 7 to attach EBS volume\nPress 8 to start instance\nPress 9 to stop instance\nPress 10 to terminate instance\nPress 11 to create S3 bucket [public option available]\nPress 12 to add image into S3 bucket [public,Cloud Front options available]\nPress 13 to create Partition\nPress 14 to configure Web server\nPress 15 to start web services\nPress 16 to see status of web services\nPress 17 to stop web services\nPress 18 to create Cloud Front Distribution\nPress 20 to exit")
			data=input("Enter the Number: ")
			print(data)
			publicip="aws ec2 describe-instances  --filter \"Name=instance-state-name,Values=running\" --query \"Reservations[].Instances[].[PublicIpAddress, Tags[?Key==\'Name\'].Value|[0]]\" --output json"
			
			if int(data)==1:
				os.system("aws ec2 describe-key-pairs --key-name")
				#pyttsx3.speak("These are your available key pairs")
				#print(akey)
			elif int(data)==2:
				p=input("Enter Key pair name:")
				os.system("aws ec2 create-key-pair --key-name {}".format(p))
				#print(ckey)
				#pyttsx3.speak("key pair named {} created".format(p))
				#print("\t\t\t\tkey pair named {} created".format(p))
			elif int(data)==3:
				q=input("Enter security group name:")
				os.system("aws ec2 create-security-group --group-name {0} --description {0}".format(q))
				#print(o)
				#pyttsx3.speak("security group named {} created".format(q))
				#print("\t\t\t\tsecurity group named {} created".format(q))
			elif int(data)==4:
				#pyttsx3.speak("These are your available instances")
				os.system("aws ec2 describe-instances --instance-ids")
			elif int(data)==5:
				#pyttsx3.speak("Enter the instance type")
				itype=input("Enter the instance type: ")
				#pyttsx3.speak("Enter the number of instances")
				noi=input("Number of instances: ")
				#pyttsx3.speak("Enter key pair name")
				koi=input("Enter key pair name: ")
				#pyttsx3.speak("Enter security group id")
				soi=input("Enter security group id: ")
				os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type {0} --count {1} --subnet-id subnet-c40108ac --security-group-ids {3} --key-name {2}".format(itype,noi,koi,soi))
				#print(launchi)
				#pyttsx3.speak("instance launched")
				#print("\t\t\t\tinstance launched")
			elif int(data)==6:
				size=input("Enter the size(GB): ")
				os.system("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {}".format(size))
				#print(cvol)		
				#pyttsx3.speak("EBS volume created")
				#print("\t\t\t\tEBS volume created")
			elif int(data)==7:
				print("Available instances are: ")
				os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==\'Name\']|[0].Value}\" --output json")			
				insid=input("Enter instance id: ")
				print("Available Volumes are: ")
				os.system("aws ec2 describe-volumes --filters Name=tag:status,Values=available Name=availability-zone,Values=ap-south-1a")			
				volid=input("Enter volume id: ")		
				os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(volid,insid))
				#print(avol)
				#pyttsx3.speak("volume attached")
				#print("\t\t\t\tvolume attached")
			elif int(data)==8:
				print("Available instances are: ")
				os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==\'Name\']|[0].Value}\" --output json")	
				#pyttsx3.speak("Enter instance-id")
				starti=input("Enter instance-id:  ")
				os.system("aws ec2 start-instances --instance-ids {}".format(starti))
				#print(si)
				#pyttsx3.speak("instance {} started successfully".format(starti))
				#print("instance {} started successfully".format(starti))
			elif int(data)==9:
				print("Available instances are: ")
				os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==\'Name\']|[0].Value}\" --output json")	
				#pyttsx3.speak("Enter instance-id")
				stopi=input("Enter instance-id:  ")
				os.system("aws ec2 stop-instances --instance-ids {}".format(stopi))
				#print(sti)
				#pyttsx3.speak("instance {} stopped successfully".format(stopi))
				#print("instance {} stopped successfully".format(stopi))
			elif int(data)==10:
				print("Available instances are: ")
				os.system("aws ec2 describe-instances --filters Name=tag-key,Values=Name --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==\'Name\']|[0].Value}\" --output json")	
				#pyttsx3.speak("Enter instance-id")
				terminatei=input("Enter instance-id:  ")
				surei=input("Are you sure to terminate instance {} [Y/N] : ".format(terminatei))
				if "Y" == surei:
					os.system("aws ec2 terminate-instances --instance-ids {}".format(terminatei))
					#print(ti)
					#pyttsx3.speak("instance {} stopped successfully".format(terminatei))
					#print("instance {} stopped successfully".format(terminatei))
				else:
					print("stopped termination")
			elif int(data)==11:
				bucketname=input("Enter the bucket name: ")
				os.system("aws s3api create-bucket --bucket {0} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1".format(bucketname))
				sbp=input("Do you want to make this bucket public [Y/N]: ")
				if sbp =="Y":
					pr=os.system("aws s3api put-bucket-acl --acl public-read --bucket {}".format(bucketname))
					
				else:
					print("Your bucket is created but not publicy accessible")
			elif int(data)==12:
				obbs=input("Enter the S3 bucket name: ")
				pob=input("Enter the location of file in your system: ")
				fname=input("Enter the object file name: ")
				#foldn=input("Enter the folder name: ")
				os.system("aws s3 sync \"{2}\" s3://{0}".format(obbs,fname,pob))
				obp=input("Do you want to make this object file publicly accessible [Y/N]: ")
				if obp == "Y":
					os.system("aws s3api put-object-acl --bucket {0} --key {1} --acl public-read".format(obbs,fname))
					#print("Now your object file {} publicly accessible".format(fname))
				else:
					print("Your object file {0} is added but not publicy accessible".format(fname))
				cfd=input("Do you want to create cloud front distribution for this object file [Y/N]: ")
				if cfd == "Y":
					os.system("aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com ".format(obbs))
					#print("Now your object file {} cloud-front enabled".format(fname))
				else:
					print("Your object file {} is not enabled for cloud front".format(fname)) 				
			elif int(data)==13:
				print("Available instances with public IPv4 address: ")
				os.system(publicip)
				eip=input("Enter IPv4 Address:  ")
				print("\t\t\t\t\n\nShowing the status of storage devices")
				os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo fdisk -l".format(eip))
				edev=input("\n\n\nEnter the device name: ")
				os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo fdisk {1} ".format(eip,edev))
				print("\n\n\nLoading the driver please wait")
				os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo udevadm settle".format(eip))
				print("\t\t\t\t\t\n\nSuccessfully loaded the driver")
				print("\n\n\nShowing the status of storage devices")
				os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo fdisk -l".format(eip))
				fpar=input("\n\n\nTo format the partition,enter the partition name: ")
				os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo mkfs.ext4 {1}".format(eip,fpar))
				#print("\t\t\t\t\t\n\nSuccessfully formatted the {}".format(fpar))
				mpar=input("\n\nTo mount this partition, enter the directory name[default webserver directory,enter Y]: ")
				if mpar == "Y":
					os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo mount {1} /var/www/html".format(eip,fpar))
					#print("\t\t\t\t\tpartition {0} successfully mounted on /var/www/html".format(fpar))
				else:
					os.system("ssh -i hadoopkey.pem -l ec2-user {0} sudo mount {1} {2}".format(eip,fpar,mpar))
					#print("\t\t\t\t\tpartition {0} successfully mounted on {1}".format(fpar,mpar)) 
			elif int(data)==14:
				print("Available instances with public IPv4 address: ")
				os.system(publicip)			
				ipadd=input("Enter IPv4 Address of the system: ")
				os.system("ssh -i hadoopkey.pem -l ec2-user {} sudo yum install httpd -y".format(ipadd))
			elif int(data)==15:
				print("Available instances with public IPv4 address: ")
				os.system(publicip)
				ipadd=input("Enter IPv4 Address of the system: ")			
				os.system("ssh -i hadoopkey.pem -l ec2-user {} sudo systemctl start httpd".format(ipadd))
			elif int(data)==16:
				print("Available instances with public IPv4 address: ")
				os.system(publicip)
				ipadd=input("Enter IPv4 Address of the system: ")
				os.system("ssh -i hadoopkey.pem -l ec2-user {} sudo systemctl status httpd".format(ipadd))
			elif int(data)==17:
				print("Available instances with public IPv4 address: ")
				os.system(publicip)
				ipadd=input("Enter IPv4 Address of the system: ")
				os.system("ssh -i hadoopkey.pem -l ec2-user {} sudo systemctl stop httpd".format(ipadd))
			elif int(data)==18:
				disbtion=input("Enter Domain name: ")
				os.system("aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com ".format(disbtion))		
			elif int(data)==20:
				exit()
			else:
				#pyttsx3.speak("can't understand")
				print("can't understand")
elif login=="R":
			ipremote=input("Enter IP Address: ")
			os.system("scp -r awsorgrem.py root@{}:/".format(ipremote))
			os.system(r"ssh root@{} python3 /awsorgrem.py".format(ipremote))
			
else:
			#pyttsx3.speak("can't understand")
			print("can't understand")
			
input("\t\t\t\t\tClick Enter to continue")  
