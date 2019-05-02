# from django.db import models
#
#
# # Create your models here.
#
#
# class RegisterDetails(models.Model):
#     UserId = models.IntegerField(primary_key=True, null=False)
#     aadhar_no = models.CharField(max_length=10, null=False)
#     FirstName = models.CharField(max_length=20, null=False)
#     MiddleName = models.CharField(max_length=20)
#     LastName = models.CharField(max_length=20)
#     DateOfBirth = models.CharField(max_length=8, null=False)
#     mobile_no = models.CharField(max_length=10, null=False)
#     Primary_add = models.CharField(max_length=100, null=False)
#     Secondary_add = models.CharField(max_length=100)
#     emailId =
#
#
# class BankDetails(models.Model):
#     UserId = models.ForeignKey('RegisterDetails', on_delete=models.CASCADE)
#     Bank_name = models.CharField(max_length=20)
#     Branch_name = models.CharField(max_length=30)
#     IFSC_code = models.CharField(max_length=10)
#
#
# class KycDetails(models.Model):
#     status = {1: 'Allowed', 2: 'Rejected', 3: 'In Process'}
#     UserId = models.ForeignKey('RegisterDetails', on_delete=models.CASCADE)
#     # KYC_status = models.CharField(max_length=10, choices=status)
#     # KYC_request_date = models.
