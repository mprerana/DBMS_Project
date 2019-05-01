from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
from twilio.rest import Client
import requests
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import schedule
import pyodbc
import time
import multiprocessing

con = pyodbc.connect("Driver={SQL Server};Server=localhost\sqlexpress;UID=uidai;PWD=uidai;")
cur = con.cursor()

def backup_db():
	con.autocommit = True
	cur.execute("EXEC back_db;")
	cur.commit()
	con.autocommit = False

def run_back_db_server():
	print("Started backup server.")
	schedule.every().day.at("00:00").do(backup_db)
	while True:
		schedule.run_pending()
		time.sleep(82800)

class ftp_server():

	def __init__(self,uid,pwd,port=1026,cwd="D:/projects/uidai/data/"):
		self.authorizer = DummyAuthorizer()
		self.authorizer.add_user(uid, pwd, cwd, perm="elradfmw")

		self.handler = FTPHandler
		self.handler.authorizer = self.authorizer

		self.ipaddr = socket.gethostbyname(socket.gethostname())
#		self.ipaddr = "10.0.32.146"
		self.server = FTPServer((self.ipaddr, port), self.handler)

	def serve(self):
		self.server.serve_forever()

class qrgenerator(object):

	def __init__(self,data):
		self.data = data

	def generateqr(self,qrname):
		import qrcode
		qrc = qrcode.QRCode(
			version = 1,
			error_correction = qrcode.constants.ERROR_CORRECT_H,
			box_size = 10,
			border = 4,
		)
		qrc.add_data(self.data)
		qrc.make(fit=True)
		img = qrc.make_image()
		img.save(str(qrname)+".jpg")

class smsender():

	def __init__(self):
		self.auth_token = 'HT2wsxjb8XmgJkFoC1uidEQl7KLzRDBfWpcIUvPO06tSZVM9yNSmB26FrJWVpbxOT8DqLo7yCn3UMcva'
		# self.smssid = 'AC454dda9e0468a8be7ed47a7121e44afe'
		# self.smsauth_token = 'b52f1033669b39e26ed3fe9978be015b'
		self.sms_url = "https://www.fast2sms.com/dev/bulk"
		# self.smsclient = Client(self.smssid, self.smsauth_token)
		# self.smsnum = '+18608965907'

	def send_sms(self,data,phno):
		payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers={}".format(data,phno)
		print(payload)
		headers = {
			'authorization': self.auth_token,
			'Content-Type': "application/x-www-form-urlencoded",
			'Cache-Control': "no-cache",
			}
		response = requests.request("POST", self.sms_url, data=payload, headers=headers)
		print(response.text)
		print("sms sent")
#		self.msg = self.smsclient.messages.create(to = '+91'+str(phno), from_= self.smsnum, body = "OTP for aadhar authentiation is "+str(data))

def create_aadhar_enrollment(full_name,gender,father_name,mother_name,dob,birthplace,ph_no,email,res_addr,city,dist, state, country, pincode, eid, etime = time.ctime()):

	logo = "assets/images/aadhartop.jpg"
	doc = SimpleDocTemplate(str(eid)+".pdf",pagesize=letter, rightMargin=72,leftMargin=72, topMargin=72,bottomMargin=18)
	Story=[]
	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

	# ptext = '<font size=24><b><center>Aadhar Enroollment Form</center></b></font>'
	# Story.append(Paragraph(ptext, styles["Normal"])) 
	# Story.append(Spacer(1, 12))
	im = Image(logo, 7*inch, 1*inch)
	Story.append(im)
	Story.append(Spacer(2, 0))

	ptext = "<font size=16><br /><b><u>Enroll Details</u></b>: </font>"
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = '<font size=12><b>Enrollment ID</b>: </font><font size=10>%s</font>' % eid
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))
	
	ptext = '<font size=12><b>Enrollment Time</b>: </font><font size=10>%s</font>' % etime
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=16><br /><b><u>Personal Details</u></b>: </font>"
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = '<font size=12><b>Name</b>: </font><font size=10>%s</font>' % full_name
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Father's name</b>: </font><font size=10>%s</font>" % father_name
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Mother's name</b>: </font><font size=10>%s</font>" % mother_name
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Birth place</b>: </font><font size=10>%s</font>" % birthplace
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Date of birth</b>: </font><font size=10>%s</font>" % dob
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=16><br /><b><u>Contact Details</u></b>: </font>"
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Phone Number</b>: </font><font size=10>%s</font>" % ph_no
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Email</b>: </font><font size=10>%s</font>" % email
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Address</b>: </font><font size=10>%s</font>" % res_addr
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>City</b>: </font><font size=10>%s</font>" % city
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>District</b>: </font><font size=10>%s</font>" % dist
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>State</b>: </font><font size=10>%s</font>" % state
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Country</b>: </font><font size=10>%s</font>" % country
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	ptext = "<font size=12><b>Pincode</b>: </font><font size=10>%s</font>" % pincode
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(0, 12))

	doc.build(Story)

if __name__ == "__main__":
#	s = smsender()
#	s.send_sms("hello world","8639928948")
	ftp_server("uidai","uidai").serve()
#	bdb = multiprocessing.Process(target = run_back_db_server)
#	bdb.start()
#	backup_db()