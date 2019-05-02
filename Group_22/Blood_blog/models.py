from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

Blood_Groups = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

States = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('karnataka', 'karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Goa', 'Goa'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)

Hospitals = (
    ('Andhra Pradesh', ('Yashodha','Apollo')),
    ('Arunachal Pradesh',('Yashodha','Apollo')),
    ('Assam',('Yashodha','Apollo')),
    ('Bihar',('Yashodha','Apollo')),
    ('Goa', ('Yashodha','Apollo')),
    ('Haryana', ('Yashodha','Apollo')),
    ('Himachal Pradesh', ('Yashodha','Apollo')),
    ('Jammu and Kashmir', ('Yashodha','Apollo')),
    ('Jharkhand', ('Yashodha','Apollo')),
    ('karnataka', ('Yashodha','Apollo')),
    ('Kerala', ('Yashodha','Apollo')),
    ('Madhya Pradesh', ('Yashodha','Apollo')),
    ('Maharashtra', ('Yashodha','Apollo')),
    ('Manipur', ('Yashodha','Apollo')),
    ('Meghalaya', ('Yashodha','Apollo')),
    ('Mizoram', ('Yashodha','Apollo')),
    ('Nagaland', ('Yashodha','Apollo')),
    ('Odisha', ('Yashodha','Apollo')),
    ('Punjab', ('Yashodha','Apollo')),
    ('Rajasthan', ('Yashodha','Apollo')),
    ('Sikkim', ('Yashodha','Apollo')),
    ('Tamil Nadu', ('Yashodha','Apollo')),
    ('Goa', ('Yashodha','Apollo')),
    ('Telangana', ('Yashodha','Apollo')),
    ('Tripura', ('Yashodha','Apollo')),
    ('Uttar Pradesh', ('Yashodha','Apollo')),
    ('Uttarakhand', ('Yashodha','Apollo')),
    ('West Bengal', ('Yashodha','Apollo')),
)

class Comments(models.Model):
    user_comment = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(blank = True)
    blog_id = models.PositiveIntegerField()

    def __str__(self):
        return self.comment


class Donate_blood(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Patient_name = models.CharField(max_length=100)
    blood = models.CharField(max_length=10, choices=Blood_Groups, blank=False)
    phone_number = models.CharField(max_length=10,
                                    validators=[
                                        RegexValidator(
                                            regex='^[1-9]{1}[0-9]{9}$',
                                            message='Enter a valid phone number',
                                            code='invalid_cell'
                                        ),
                                    ]
                                    )
    gender = models.CharField(max_length=10,default='Male')
    state = models.CharField(max_length=30, choices=States, blank=False)
    Amount_blood = models.PositiveIntegerField(default = 0)
    reason = models.TextField(blank=False, null=False, max_length=500)
    date = models.DateField(default=timezone.now)
    verified = models.CharField(max_length= 5,default = "F")
    img = models.ImageField(default = "/home/hemanth/Pictures/profile_pic1.jpeg",upload_to='blog_pics')

    def __str__(self):
        return self.Patient_name

    def checkingrequestor(self):
        return '%s' % (self.user)

    def get_absolute_url(self):
        return reverse('Blog-detail',kwargs = {'id' : self.id })
