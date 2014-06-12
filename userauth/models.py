from django.db import models
from core.models import RontalModel
from hashlib import sha1
from django.utils import timezone
from random import random


class Group(RontalModel):
	"""Group akun rontal"""
	
	name = models.CharField(max_length=64, unique=True)
	description = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name


class UserStatus(RontalModel):
	"""Status akun rontal"""
	
	status = models.CharField(max_length=64, unique=True)
	description = models.CharField(max_length=255)
	
	class Meta:
		verbose_name_plural = 'user statuses'
	
	def __unicode__(self):
		return self.status
	

class User(RontalModel):
	"""Akun Rontal"""
	
	user_status = models.ForeignKey(UserStatus)
	group = models.ForeignKey(Group)
	alias = models.CharField(max_length=20, unique=True)
	email = models.EmailField(max_length=128, unique=True)
	
	def __unicode__(self):
		return self.alias


class UserPassword(RontalModel):
	"""User password"""
	user = models.ForeignKey(User)
	salt = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	
	def __unicode__(self):
		return self.user.alias
		
	def save(self, *args, **kwargs):
		if self.pk is None:
			self.hash_password()
		else:
			user = UserPassword.objects.get(pk=self.pk)
			if user.password != self.password:
				self.hash_password()
				
		return super(UserPassword, self).save(*args, **kwargs)
	
	def hash_password(self):
		self.salt = sha1( "%s%s" %(timezone.now(), random()) ).hexdigest()
		self.password = sha1( "%s%s" % (self.salt, self.password) ).hexdigest()		


class UserHistory(RontalModel):
	"""History untuk akses pengguna Rontal"""
	
	user = models.ForeignKey(User)
	user_log = models.TextField()
	
	class Meta:
		verbose_name_plural = 'user history'
	
	def __unicode__(self):
		return self.user.alias
