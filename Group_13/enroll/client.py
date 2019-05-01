from ftplib import FTP
import os

class ftp_client():

	def __init__(self,hostname,uid,pwd,port=1026):
		self.ftp = FTP('')
		self.ftp.connect(host=hostname,port=port)
		self.ftp.login(uid,pwd)
		self.ftp.cwd('')

	def uploadFile(self,filename, name, tp):
		fls = filename.split("/")
		fname = fls[len(fls)-1]
		exet = fname.split(".")[1]
		os.chdir(filename.rstrip(fname))
		self.ftp.storbinary('STOR '+str(tp)+'/'+os.path.basename(str(name)+"."+str(exet)), open(os.path.basename(fname), 'rb'))

if __name__ == "__main__":
	f = ftp_client('10.0.33.62','uidai','uidai')
	f.uploadFile("D:/linkedlist.py", 'loll', "programs")