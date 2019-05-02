from django.db import models

class fileorfolder(models.Model):
	"""
	only for files for now
	"""
	file_name = models.CharField(max_length=100)
	file_hash = models.CharField(max_length=100, primary_key =True)
	file_size = models.IntegerField()
	number_peers = models.IntegerField()

class peer(models.Model):
	#file_hash = models.ForeignKey(fileorfolder, on_delete=models.CASCADE)
	id = models.IntegerField(primary_key=True)
	file_hash = models.CharField(max_length=100)
	peer = models.CharField(max_length=16)

class chunkshashdb(models.Model):
		file_hash = models.ForeignKey(fileorfolder, on_delete=models.CASCADE)
		chunks = models.CharField(max_length=500)
		offset = models.IntegerField()






# from django.db import models
# import datetime
#
# class peer(models.Model):
# 	peer_ip = models.CharField(max_length=15, primary_key=True)
#
#
#
# class hashTable(models.Model):
# 	filename = models.CharField(max_length=50)
# 	filehash =  models.CharField(max_length=50)
# 	shareddate = models.DateField(default=datetime.date.today)
# 	lastuseddate = models.DateField(default=datetime.date.today)
# 	size = models.IntegerField(null=False)
# 	delete_flag = models.BooleanField(default=False)
# 	downloads = models.IntegerField(default=0)
#
#
# class refTable(models.Model):
# 	peer = models.ForeignKey(peer, on_delete=models.CASCADE)
# 	filehash = models.ForeignKey(hashTable, on_delete=models.CASCADE)
# 	downloadswithpeer = models.IntegerField(default=0)
# 	Ratings = models.IntegerField(null=True)
