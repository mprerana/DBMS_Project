import tkinter as tk
from tkinter import *
import tkinter.filedialog as tkFileDialog
from PIL import ImageTk
from PIL import Image
#from tkcalendar import Calendar, DateText
from twilio.rest import Client
import requests, cv2
from datetime import datetime as dt
import random, os, socket
import pyodbc
from tkcalendar import Calendar
from time import perf_counter
from client import ftp_client
from server import qrgenerator

class enroll_center(object):
	def __init__(self):
		self.enroll_id = 1
		self.enroll_name = "Raja Enrollment center"
		self.cur = self.connecttodb()

	def connecttodb(self):
		self.con = pyodbc.connect("Driver={SQL Server};Server=localhost\sqlexpress;UID=uidai;PWD=uidai;")
		return self.con.cursor()

class person(object):
	def __init__(self):
		# self.first_name = "Amarendra"
		# self.middle_name = ""
		# self.last_name = "Bahubali"
		# self.gender = "Male"
		# self.father_name = "Mahendra Bahubali"
		# self.mother_name = "Devasena"
		# self.brt_plc = "Mahismati"
		# self.dob = "2017-04-28"
		# self.addr = "Mahismati samrajyam"
		# self.phno = "9874563210"
		# self.email = ""
		# self.state = "Tamil Nadu"
		# self.city = "Chennai"
		# self.pincode = 600001
		# self.dist = "Chennai"
		# self.country = "India"
		self.first_name = None
		self.middle_name = None
		self.last_name = None
		self.gender = None
		self.father_name = None
		self.mother_name = None
		self.brt_plc = None
		self.dob = None
		self.addr = None
		self.phno = None
		self.email = None
		self.state = None
		self.city = None
		self.pincode = None
		self.dist = None
		self.country = None
		self.ec = enroll_center()
		self.eid = self.ec.cur.execute("SELECT [dbo].[eid_generate]();").fetchall()[0][0]
		self.success = 0

	def send_to_db(self):
		# try:
			if int(int(self.pincode)/100000) == 6:
				self.ec.cur.execute("use tn_uidai;")
				self.ec.con.commit()
			elif int(int(self.pincode)/100000) == 5:
				self.ec.cur.execute("use uidai;")
				self.ec.con.commit()
			add_entry = self.ec.cur.execute("EXEC add_new_entry @fname = '{}', @mname = '{}', @lname = '{}', @gender = '{}', @faname = '{}', @moname = '{}', @dob = '{}', @birthplace = '{}', @p_no = {}, @email = '{}', @address = '{}', @city = '{}', @district = '{}', @state = '{}', @pincode = {}, @country = '{}', @enloc = '{}', @eid = {};".format(self.first_name, self.middle_name, self.last_name, self.gender, self.father_name, self.mother_name, dt.strptime(str(self.dob), "%Y-%m-%d"), self.brt_plc, self.phno, self.email, self.addr, self. city, self.dist, self.state, self.pincode, self.country, self.ec.enroll_id, self.eid))
			self.ec.con.commit()
			dat = "{}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}".format(self.first_name, self.middle_name, self.last_name, self.gender, self.father_name, self.mother_name, dt.strptime(str(self.dob), "%Y-%m-%d"), self.phno, self.addr, self. city, self.dist, self.state, self.pincode, self.country)
			# suc = qrgenerator(dat)
			# suc.generateqr(self.eid)
			self.success = 1
			
		# except Exception as e:
		# 	print(e)

	def __str__(self):
		return str("""Name: {} {} {}, Father's Name: {}, Mother's name: {}, Date of birth: {}\nAddress: {}\nCity: {}, District: {}, State: {}, Country: {}\nPhone #: {}, Email: {}\n  """.format(self.first_name, self.middle_name, self.last_name, self.father_name, self.mother_name, self.dob, self.addr, self. city, self.dist, self.state, self.country, self.phno, self.email))

class aadhar_enroll(tk.Frame):

	def __init__(self):
		self.new_user = person()
		self.root = Tk()
		self.root.configure(background = 'white')
		self.root.geometry("1400x800")
		self.mscount = 0
		Frame.__init__(self, self.root)
		self.canvas = Canvas(self.root, borderwidth=0, background="#ffffff")
		self.frame = Frame(self.canvas, background="#ffffff")
		self.vsb = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
		self.hsb = Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		self.vsb.pack(side="right", fill="y")
		self.hsb.pack(side="bottom", fill="x")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.photo_flag = None 
		self.addr_flag = None 
		self.brth_flag = None 
		self.canvas.create_window((10,10), window=self.frame, anchor="nw", tags="self.frame")

		self.frame.bind("<Configure>", self.onFrameConfigure)
		self.frame.bind("<MouseWheel>", self.on_mousewheel)
		self.root.title("Aadhar Enrollment")
		img = ImageTk.PhotoImage(Image.open("assets/images/aadhar_logo.png").resize((200,150), Image.ANTIALIAS))
		self.logo = Label(self.frame, image = img, background='white').grid(row=0, column=1)
		self.populateform()
		self.ftp_clnt = ftp_client(hostname="10.0.33.62", uid="uidai", pwd="uidai")
		self.root.mainloop()

	def populateform(self):
		gender = [
				("Male"),
				("Female"),
				("Other")
			]
		Label(self.frame, text="Personal Details:", background='white', fg='red', font=(None, 15)).grid(sticky="W", row=1, column=0, padx=10, pady=10)
		Label(self.frame, text="First Name", background='white').grid(row=2, column=0)
		self.fnm = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.fnm.grid(row=3, column=0, padx=10, pady=5)
		Label(self.frame, text="Middle Name", background='white').grid(row=2, column=1)
		self.mnm = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.mnm.grid(row=3, column=1, padx=10, pady=5)
		Label(self.frame, text="Last Name", background='white').grid(row=2, column=2)
		self.lnm = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.lnm.grid(row=3, column=2, padx=10, pady=5)
		Label(self.frame, text="Gender", background='white').grid(row=2, column=4)
		self.gender = StringVar()
		self.gender.set('Male')
		self.gmen = OptionMenu(self.frame, self.gender, *gender)
		self.gmen.grid(row=3, column=4)
		Label(self.frame, text="Father's Name", background='white').grid(row=4, column=0)
		self.fanm = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.fanm.grid(row=5, column=0, padx=10, pady=5)
		Label(self.frame, text="Mother's Name", background='white').grid(row=4, column=1)
		self.manm = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.manm.grid(row=5, column=1, padx=10, pady=5)
		Label(self.frame, text="Date of Birth", background='white').grid(row=4, column=2)
		self.dob = Button(self.frame, font=("Calibri",12), text="Select Date of birth", command=self.show_calendar, pady=10, padx=10)
		self.dob.grid(row=5, column=2, padx=10, pady=5)
		Label(self.frame, text="Contact Details:", background='white', fg='red', font=(None, 15)).grid(sticky="W", row=6, column=0, padx=10, pady=10)
		Label(self.frame, text="Phone Number", background='white').grid(row=7, column=0)
		self.phno = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.phno.grid(row=8, column=0, padx=10, pady=5)
		Label(self.frame, text="Email", background='white').grid(row=7, column=1)
		self.email = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.email.grid(row=8, column=1, padx=10, pady=5)
		Label(self.frame, text="Birth Place", background='white').grid(row=7, column=2)
		self.bpl = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.bpl.grid(row=8, column=2, padx=10, pady=5)
		Label(self.frame, text="Residential Address", background='white').grid(row=9, column=0)
		self.addrs = Text(self.frame, font=("Calibri",12), height=3, width=40, pady=10, padx=10)
		self.addrs.grid(row=10, column=0, padx=10, pady=5, sticky='E')
		Label(self.frame, text="City", background='white').grid(row=9, column=1)
		self.city = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.city.grid(row=10, column=1, padx=10, pady=5)
		Label(self.frame, text="PINCODE", background='white').grid(row=9, column=2)
		self.pincd = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.pincd.grid(row=10, column=2, padx=10, pady=5, sticky='')
		Label(self.frame, text="State", background='white').grid(row=11, column=0)
		self.state = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.state.grid(row=12, column=0, padx=10, pady=5)
		Label(self.frame, text="District", background='white').grid(row=11, column=1)
		self.dist = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.dist.grid(row=12, column=1, padx=10, pady=5)
		Label(self.frame, text="Country", background='white').grid(row=11, column=2)
		self.country = Text(self.frame, font=("Calibri",12), height=1, width=40, pady=10, padx=10)
		self.country.grid(row=12, column=2, padx=10, pady=5)
		Label(self.frame, text="Photo and Biometrics :", background='white', fg='red', font=(None, 15)).grid(sticky="W", row=13, column=0, padx=10, pady=10)
		self.photo_cap = Button(self.frame, text = 'Capture', command = self.im_capture, background='white')
		self.photo_cap.grid(row=14, column=0, pady=10 )
		Label(self.frame, text="Proofs :", background='white', fg='red', font=(None, 15)).grid(sticky="W", row=19, column=0, padx=10, pady=10)
		Label(self.frame, text="Address proof", background='white').grid(row=20, column=0)
		self.adflebtn = Button(self.frame, text = 'Select file', command = self.address_prf, background='white')
		self.adflebtn.grid(row=21, column=0, pady=10 )
		Label(self.frame, text="Date of Birth proof", background='white').grid(row=20, column=1)
		self.adflebtn = Button(self.frame, text = 'Select file', command = self.birth_prf, background='white')
		self.adflebtn.grid(row=21, column=1, pady=10 )
		self.sbmtbtn = Button(self.frame, text = 'Submit', command = self.submitdetails, background='white')
		self.sbmtbtn.grid(row=22, column=1, pady=10 )

	def on_mousewheel(self, event):
		self.canvas.yview_scroll(-1*event.delta, "units")

	def datepicker(self):
		Label(self.frame, text='Choose date').pack(padx=10, pady=10)
		self.cal = DateText(top, width=12, background='darkblue', foreground='white', borderwidth=2)
		self.cal.pack(padx=10, pady=10)

	def address_prf(self):
		self.adprf = tkFileDialog.askopenfile(parent=self.frame, title="Choose a file")
		self.ftp_clnt.uploadFile(self.adprf.name, str(self.new_user.eid), "address_proof")
		self.addr_flag = 1

	def birth_prf(self):
		self.brthprf = tkFileDialog.askopenfile(parent=self.frame, title="Choose a file")
		self.ftp_clnt.uploadFile(self.brthprf.name, str(self.new_user.eid), "dob_prf")
		self.brth_flag = 1

	def validate_form(self):
		self.frame.bind_all()
		self.new_user.first_name = self.fnm.get('1.0', END).rstrip("\n")
		self.new_user.last_name = self.lnm.get('1.0', END).rstrip("\n")
		self.new_user.middle_name = self.mnm.get('1.0', END).rstrip("\n")
		self.new_user.gender = self.gender.get().rstrip("\n")
		self.new_user.father_name = self.fanm.get('1.0', END).rstrip("\n")
		self.new_user.mother_name = self.manm.get('1.0', END).rstrip("\n")
		self.new_user.phno = self.phno.get('1.0', END).rstrip("\n")
		self.new_user.email = self.email.get('1.0', END).rstrip("\n")
		self.new_user.brt_plc = self.bpl.get('1.0', END).rstrip("\n")
		self.new_user.addr = self.addrs.get('1.0', END).rstrip("\n")
		self.new_user.city = self.city.get('1.0', END).rstrip("\n")
		self.new_user.pincode = self.pincd.get('1.0', END).rstrip("\n")
		self.new_user.state = self.state.get('1.0', END).rstrip("\n")
		self.new_user.dist = self.dist.get('1.0', END).rstrip("\n")
		self.new_user.country = self.country.get('1.0', END).rstrip("\n")
		errors = []
		if self.new_user.first_name == "":
			errors.append('First Name')
		if self.new_user.last_name == "":
			errors.append('Last Name')
		if self.new_user.father_name == "":
			errors.append("Father's Name")
		if self.new_user.dob == None:
			errors.append('Date of Birth')
		if self.new_user.phno == "":
			errors.append('Phone Number')
		if self.new_user.addr == "":
			errors.append('Residential address')
		if self.new_user.city == "":
			errors.append('City')
		if self.new_user.pincode == "":
			errors.append('Pincode')
		if self.new_user.state == "":
			errors.append('State')
		if self.new_user.dist == "":
			errors.append('District')
		if self.new_user.country == "":
			errors.append('Country')
		if self.photo_flag == None:
			errors.append('Photo')
		if self.addr_flag == None:
			errors.append('Address proof')
		if self.brth_flag == None:
			errors.append('Birth proof')

		er = "\n"
		for ind in range(len(errors)):
			er += "{}. {}\n".format(ind+1, errors[ind])

		if len(errors) > 0:
			self.alert = Toplevel()
			eid = Label(self.alert, text = "Please re-check these details. {}".format(er), padx=20, pady=20)
			eid.grid(row=0, column=0)
			return 0
		return 1

	def submitdetails(self):
		if self.validate_form():
			print(self.new_user)
			self.new_user.send_to_db()
			if self.new_user.success == 1:
				self.show_success()

	def show_success(self):
		self.popup = Toplevel()
		eid = Label(self.popup, text = """Hello {}.\nYour enrollment at {} is successful.\nPlease not down your enrollment id for further reference.\nYour eid is {}.""".format(self.new_user.last_name, self.new_user.ec.enroll_name, self.new_user.eid), padx=20, pady=20)
		eid.grid(row=0, column=0)
		self.fnm.delete('1.0', END)
		self.lnm.delete('1.0', END)
		self.mnm.delete('1.0', END)
		self.fanm.delete('1.0', END)
		self.manm.delete('1.0', END)
		self.email.delete('1.0', END)
		self.phno.delete('1.0', END)
		self.addrs.delete('1.0', END)
		self.bpl.delete('1.0', END)
		self.city.delete('1.0', END)
		self.pincd.delete('1.0', END)
		self.state.delete('1.0', END)
		self.country.delete('1.0', END)
		self.dist.delete('1.0', END)
		eid.pack()

	def im_capture(self):
		cam = cv2.VideoCapture(0)
		cv2.namedWindow("Aadhar Photo")

		while True:
			ret, frame = cam.read()
			cv2.imshow("Aadhar Photo", frame)
			if not ret:
				break
			k = cv2.waitKey(1)

			if k%256 == 13:
				img_name = "D:/projects/uidai/enroll/data/images/"+str(self.new_user.eid)+".png"
				cv2.imwrite(img_name, frame)
				break
		cam.release()
		cv2.destroyAllWindows()
		self.ftp_clnt.uploadFile(img_name, str(self.new_user.eid),"images")
		img = ImageTk.PhotoImage(Image.open(img_name).resize((200,200), Image.ANTIALIAS))
		self.photo_flag = 1
		self.ad_pt = Label(self.frame, image = img, background='white').grid(row=14, column=1, sticky='W').pack()

	def onFrameConfigure(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	def show_calendar(self):
		def print_sel():
			root.destroy()
			self.new_user.dob = cal.selection_get()
			self.dob.grid_remove()
			print(dt.strptime(str(self.new_user.dob), "%Y-%m-%d"))
			self.dob = Button(self.frame, font=("Calibri",12), text=self.new_user.dob, command=self.show_calendar, pady=10, padx=10)
			self.dob.grid(row=5, column=2)

		root = Tk()

		cal = Calendar(root,
					font="Arial 14", selectmode='day',
					cursor="hand1", year=2018, month=2, day=5)
		cal.pack(fill="both", expand=True)
		Button(root, text="ok", command=print_sel).pack()


if __name__=="__main__":
	os.system('cls')
	clk = perf_counter()
	aadhar_enroll()
	# show_success()
	# p = person()
	# p.send_to_db()
#	enroll_center()
	print("execution time =",perf_counter()-clk)