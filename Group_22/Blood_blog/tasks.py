ot -pfrom templated_email import send_templated_mail
from .models import Donate_blood
import datetime
from django.conf import settings

def timediff(a,b):
    date_format1 = "%Y-%m-%d"
    a_new  = datetime.datetime.strptime(str(a), date_format1)
    b_new = datetime.datetime.strptime(str(b), date_format1)
    diff = a_new - b_new
    return diff.days

def send_invitation():
    curr = datetime.date.today()
    res = curr + datetime.timedelta(days = 5)
    ob1 = BookingListIndi.objects.raw('''select * from ''')
    for object in ob1:
        val = object.date_visit
        if timediff(res,object.date_visit) == 0:
            u_name = object.name_person
            u_visit = object.industry_name
            u_email  = str(object.email)
            u_slottime = object.slot_time
            send_templated_mail(
                        template_name = 'Remainder',
                        from_email = settings.EMAIL_HOST_USER,
                        recipient_list = [u_email],
                        context = {
                                'u_name':u_name,
                                'u_visit':u_visit,
                                'u_slottime':u_slottime,
                                'u_date':val,
                        }
                    )
