from django.shortcuts import render
from .forms import updateAddressForm,captcha
from django.http import HttpResponse
from django.db import connection
import requests
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from bs4 import BeautifulSoup
import random
import pyodbc

uidai_con = pyodbc.connect("DRIVER={SQL Server};SERVER=10.0.33.62,1433;DATABASE=uidai;UID=uidai;PWD=uidai")
uidai_cur = uidai_con.cursor()
"""
class Sms:

	def __init__(self, mobileNo, password):

		'''
		Takes mobileNo and password as parameters for constructors and try to log in
		'''

		self.base_url = "http://www.way2sms.com/"
		self.login_url = self.base_url + "re-login"
		self.msg_url=  self.base_url + "smstoss"
		self.future_msg_url = self.base_url + "schedulesms"
		self.logout_url = self.base_url + "Logout"

		self.session = requests.Session()	# Session because we want to maintain the cookies
		self.session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
		self.session.get(self.base_url)		# once do a http GET to get the cookies

		#self.session.headers['Referer'] = self.base_url
		#self.session.headers['Host'] = self.base_url
		self.session.headers['X-Requested-With'] = 'XMLHttpRequest'
		#self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
		#self.session.headers['Content-Length'] = '43'
		self.set_cookies_header()

		self.payload = {'mobileNo': mobileNo, 'password': password, 'CatType' : ''}
		self.q = self.session.post(self.login_url, data=self.payload)		# POST the payload
		self.logged_in = False				# a variable of knowing whether logged in or not

		if self.q.status_code == 200 and self.q.text == "send-sms":	# http status 200 == OK
			print("Successfully logged in..!")
			self.logged_in=True
		else:
			print("Can't login, once check credential..!")
			self.logged_in=False

		self.jsid = self.session.cookies.get_dict()['JSESSIONID'][4:]	    # JSID is the main KEY as JSID are produced every time a session satrts

	def set_cookies_header(self):
		self.session.headers['Cookie'] = "JSESSIONID=" + self.session.cookies.get_dict()['JSESSIONID']

	def msgSentToday(self):

		'''
		Returns number of SMS sent today as there is a limit of 100 messages everyday..!
		'''

		if self.logged_in == False:
			print("Can't perform since NOT logged in..!")
			return -1

		self.msg_left_url='http://www.way2sms.com/sentSMS?Token='+self.jsid
		self.q=self.session.get(self.msg_left_url)
		self.soup=BeautifulSoup(self.q.text,'html.parser')		#we want the number of messages sent which is present in the
		self.t=self.soup.find("div",{"class":"hed"}).h2.text		# div element with class "hed" -> h2
		self.sent=0

		for self.i in self.t:
			if self.i.isdecimal():
				self.sent=10*self.sent+int(self.i)
		return self.sent

	def send(self,mobile_no,msg):

		'''
		Sends the message to the given mobile number
		'''

		if self.logged_in == False:
			print("Can't perform since NOT logged in..!")
			return False

		if len(msg)>139 or len(str(mobile_no))!=10 :	#checks whether the given message is of length more than 139 and mobile numnber is valid
			return False

		self.payload = {
						'ssaction':'ss',
						'Token':self.jsid,					#inorder to visualize how I came to these payload,
			        	'toMobile':mobile_no,			#must see the NETWORK section in Inspect Element
       				 	'message':msg,						#while messagin someone from your browser
       			    }

		self.q=self.session.post(self.msg_url,data=self.payload)

		if self.q.status_code==200 and self.q.text == '0':
			return True
		else:
			return False

	def send_later(self, mobile_no, msg, date, time):				#Function for future SMS feature.
											#date must be in dd/mm/yyyy format
											#time must be in 24hr format. For ex: 18:05

		if self.logged_in == False:
			print("Can't perform since NOT logged in..!")
			return False

		if len(msg)>139 or len(mobile_no)!=10 or not mobile_no.isdecimal():
			return False

		dateparts = date.split('/')			#These steps to check for valid date and time and formatting
		timeparts = time.split(':')
		if int(dateparts[0])<1 or int(dateparts[0])>32 or int(dateparts[1])>12 or int(dateparts[1])<1 or int(dateparts[2])<2017 or int(timeparts[0])<0 or int(timeparts[0])>23 or int(timeparts[1])>59 or int(timeparts[1])<0:
			return False
		date = dateparts[0].zfill(2) + "/" + dateparts[1].zfill(2) + "/" + dateparts[2]
		time = timeparts[0].zfill(2) + ":" + timeparts[1].zfill(2)

		self.payload = {'Token' : self.jsid,
						'toMobile' : mobile_no,
						'sdate' : date,
						'stime' : time,
						'message' : msg,
					}

		self.q = self.session.post(self.future_msg_url, data=self.payload)
		if self.q.status_code == 200:
			return True
		else:
			return False

	def logout(self):
		self.session.get(self.logout_url)
		self.session.close()								# close the Session
		self.logged_in=False
"""
class smsender():



    def __init__(self):

        self.auth_token = '3BwxGQMoVlPuay1EW9iksqOhrFKSnt8HzCD0m7IRZ45pAbfeXL2DosgtX1fTIJB8knv6LYhRA0e9plGb'

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

def update_address(request):
	if request.method == 'POST':
		form = captcha(request.POST)
		if form.is_valid():
			aadhar_num = request.POST['aadhar_num']
			uidai_cur.execute("SELECT phone from details WHERE aadhar_num = {}".format(aadhar_num))
			phone_num=uidai_cur.fetchall()
			print(phone_num)
			#a = Sms('9121587454','Shiva@01')
			smss = smsender()
			otp=random.randint(100000,999999)
			phone_num=phone_num[0][0]
			print(phone_num)
			print(type(phone_num))
			#send(phone_num,str(otp))
			smss.send_sms(otp, phone_num)
			print(phone_num)
			print(otp)
			uidai_cur.execute("INSERT INTO verify_otp(aadhar_num, phone_num, otp) VALUES ({},{},{});".format(aadhar_num,phone_num,otp))
			uidai_cur.commit()
			return render(request,"update/enter_otp.html",{'phone_num': phone_num})
	else:
		form = captcha()
	return render(request,"update/enter_aadharnum.html",{'form':form})


def verify_otp(request):
	if request.method == 'POST':
		otp = request.POST['otp']
		phone_num = request.POST['phone_num']
		uidai_cur.execute("SELECT otp,aadhar_num FROM verify_otp WHERE phone_num={}".format(phone_num))
		real_otp = uidai_cur.fetchone()
		if int(otp) == int(real_otp[0]) :
			uidai_cur.execute("DELETE FROM verify_otp WHERE phone_num={}".format(phone_num))
			uidai_cur.commit()
			return render(request,"update/data_update_req.html",{'aadhar_num':real_otp[1]})
		else:
			return HttpResponse('NO')

def data_update_req(request):
	if request.method == 'POST':
		form = updateAddressForm()
		aadhar_num = request.POST['aadhar_num']
		return render(request,"update/contact_details.html",{'form':form,'aadhar_num':aadhar_num})

def data_modify(request):
	if request.method == 'POST':
		form = updateAddressForm(request.POST)
		aadhar_num = request.POST['aadhar_num']
		co = form.data['co']
		house = form.data['house']
		street = form.data['street']
		landmark = form.data['landmark']
		area = form.data['area']
		pincode = form.data['pincode']
		town = form.data['town']
		postoffice = form.data['po']
		dist = form.data['district']
		state = form.data['state']
		uidai_cur.execute("INSERT INTO update_req VALUES ({},'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}')".format(aadhar_num,co,house,street,landmark,area,pincode,town,postoffice,dist,state))
		uidai_cur.commit()
		#cursor.execute("INSERT INTO update_req VALUES ({},'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}')".format(aadhar_num,co,house,street,landmark,area,pincode,town,postoffice,dist,state))
		#cursor.commit()
		return render(request,"update/modify_details.html",{'form':form,'aadhar_num':aadhar_num})
	else:
		return HttpResponse('get')

def proceed(request):
	if request.method == 'POST':
		aadhar_num = request.POST['aadhar_num']
		return render(request,"update/document_upload.html",{'aadhar_num':aadhar_num})

def submit_document(request):
	if request.method == 'POST':
		aadhar_num = request.POST['aadhar_num']
		proof_type = request.POST['type']
		"""if 'proof' in request.FILES and request.POST:
			filename = request.FILES['proof'].name
			return HttpResponse(filename)
		else:
			return HttpResponse('no')"""
		image = request.FILES['proof']
		fs_img = FileSystemStorage(
		        location = settings.FS_IMAGE_UPLOADS,
		        base_url= settings.FS_IMAGE_URL
		    )
		imageName = fs_img.save(image.name,image)
		uploaded_image_url = fs_img.url(imageName)
		image_url = uploaded_image_url
		print(image_url)
		uidai_cur.execute("INSERT INTO document VALUES ({},'{}','{}')".format(aadhar_num,proof_type,image_url))
		uidai_cur.commit()
		return render(request,'update/thanku.html')
