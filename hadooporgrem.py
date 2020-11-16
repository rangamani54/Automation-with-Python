#import speech_recognition as sr
import subprocess as sp
#import pyttsx3
import os
print("\t\t\t\tHi, I am Hadoop assistant")
#pyttsx3.speak("Hello, Iam Hadoop assistant,tell me what you want to do")
while True :
		
	print("Press 1 to know the status of Hadoop softwares\nPress 2 to install Hadoop softwares\nPress 3 to setup Namenode\nPress 4 to setup Datanode\nPress 5 to Start Namenode\nPress 6 to Stop Namenode\nPress 7 to Start DataNode\nPress 8 to Stop Datanode\nPress 9 to upload a file in cluster\nPress 10 to read a file in cluster\nPress 11 to remove a file from cluster\nPress 12 to see the Cluster Report\nPress 15 to exit from Hadoop")		
	data=input("Enter the Number:")
	print(data)
	if int(data)==1:
		os.system("rpm -q jdk-8u171-linux-x64.rpm")
		os.system("java -version")
		os.system("rpm -q hadoop-1.2.1-1.x86_64.rpm")
		os.system("hadoop version")
	elif int(data)==2:
		os.system("rpm -i jdk-8u171-linux-x64.rpm")
		os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm")
	elif int(data)==3:
		pwname=input("Enter the path with Directory name: ")
		os.system("mkdir {}".format(pwname))
		print("\t\t\t\t\tDirectory created in respective path {}".format(pwname))
		os.system("""echo -e '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n</configuration>' > /etc/hadoop/hdfs-site.xml""".format(pwname))
		os.system("""echo -e '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n</configuration>' > /etc/hadoop/core-site.xml""")
		#print("formatting the name node")
		os.system("hadoop namenode -format")
		#print("starting namenode")
		os.system("hadoop-daemon.sh start namenode")
		#print("showing status")
		os.system("jps")
		os.system("hadoop dfsadmin -report")
	elif int(data)==4:
		sl=input("Enter the path with Directory name: ")
		os.system("mkdir {}".format(sl))
		print("\t\t\t\t\tDirectory created in respective path {}".format(sl))
		os.system("""echo -e '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n</configuration>' > /etc/hadoop/hdfs-site.xml""".format(sl))
		nnip=input("Enter IP Address of Namenode: ")
		os.system("""echo -e '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>' > /etc/hadoop/core-site.xml""".format(nnip))
		#print("starting namenode")
		os.system("hadoop-daemon.sh start datanode")
		#print("showing status")
		os.system("jps")
		os.system("hadoop dfsadmin -report")
	elif int(data)==5:
		os.system("hadoop-daemon.sh start namenode")
		os.system("jps")
	elif int(data)==6:
		os.system("hadoop-daemon.sh stop namenode")
		os.system("jps")
	elif int(data)==7:
		os.system("hadoop-daemon.sh start datanode")
		os.system("jps")
	elif int(data)==8:
		os.system("hadoop-daemon.sh stop datanode")
		os.system("jps")
	elif int(data)==9:
		file=input("Enter the file name: ")
		os.system("hadoop fs -put {} /".format(file))
		os.system("hadoop fs -ls /")
	elif int(data)==10:
		read=input("Enter File name: ")
		os.system("hadoop fs -cat /{}".format(read))
	elif int(data)==11:
		remove=input("Enter File name: ")
		os.system("hadoop fs -rm /{}".format(remove))
	elif int(data)==12:
		os.system("hadoop dfsadmin -report")
	elif int(data)==15:
		exit()
	else:
		print("can't understand")
	input("Click Enter to continue")
								 

			 