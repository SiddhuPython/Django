# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
class UserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError('User must have an email address')
		user = self.model(username = username,
			email = self.normalize_email(email)
			)
		user.set_password(password)
		user.save(using = self._db)
		return user
	def create_superuser(self, username, email, password=None):
		user = self.create_user(username=username, email=email, password=password)
		user.is_admin = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):

	username = models.CharField(max_length = 300, validators = [RegexValidator(regex = USERNAME_REGEX, message='User name must be alpha numeric or contains numbers', code = 'invalid_username')], 
	unique = True
	)
email = models.EmailField(max_length = 255, unique=True, verbose_name = 'email address')
is_admin = models.BooleanField(default=False)
objects = UserManager()
USERNAME_FIELD = 'username'
REQUIRED_FIELDS = ['email']
