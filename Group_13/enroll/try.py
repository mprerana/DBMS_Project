import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


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

if __name__=="__main__":
	create_aadhar_enrollment("Bandi Surya Manikanta Sowri", "Male", "Bandi Srinivasa Rao", "Bandi Padma Jyothi", "22-06-2000", "lingamparthi", "9490416461", "sowrisurya@outlook.com", "3-75/5, opp Sattammathalli thaadii, near Bnak of Maharashtra, Sarpavaram", "Kakinada", "East Godavari", "Andhra Pradesh", "India", "533005", "12345678901234")