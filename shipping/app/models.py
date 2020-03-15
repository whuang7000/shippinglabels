from django.db import models
from django.conf import settings

class Shipment(models.Model):
	label_url = models.URLField(max_length=200)
	tracking_number = models.CharField(max_length=200)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']