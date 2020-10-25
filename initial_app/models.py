from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class ActivityPeriods(models.Model):
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(null=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now_add=True)


class Profile(User):

	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=300)
	name = models.CharField(max_length=200)
	emp_id = models.CharField(max_length=200)
	timezone = models.CharField(max_length=100)
	activity_periods = models.ManyToManyField(
		ActivityPeriods, blank=True)

	def __str__(self):

		return self.name