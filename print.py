import getpass
import paramiko
import sys
import time

# User Settings
username = raw_input("Username: ")
password = getpass.getpass()
path     = "/homes/"+username+"/print/"

# Server Settings
host = "bert.student.eecs.qmul.ac.uk"
port = 22

# Body

## Transfering the file to the server
print 'Uploading to server'
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
remotepath = path + time.strftime("%Y-%m-%d-%H:%M") + "-" + sys.argv[1]
localpath  = sys.argv[1]
sftp.put(localpath, remotepath)
sftp.close()
transport.close()
print 'Upload complete'

## Available printers
print 'Finding available printers'
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(host, username = username, password = password)
command = 'lpstat -p | grep "enabled" | cut -d " " -f 2'
(stdin, stdout, stderr) = ssh.exec_command(command)
printers = []
num = 0
for line in stdout.readlines():
    printers.append(line)
    sys.stdout.write("[" + str(num) + "] " + line)
    num += 1
selectedPrinter = raw_input("Select printer> ")

## Printing the file
command = "lpr " + remotepath + " -P " + printers[int(selectedPrinter)]
(stdin, stdout, stderr) = ssh.exec_command(command)
ssh.close()

print 'Printing operation complete, check ' + printers[int(selectedPrinter)]