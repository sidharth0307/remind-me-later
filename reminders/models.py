from django.db import models

class Reminder(models.Model):
	REMINDER_METHODS = [
		('email','Email'),
		('sms','SMS'),
	]

	date = models.DateField()
	time = models.TimeField()
	message = models.TextField()
	remind_via = models.CharField(max_length=10, choices=REMINDER_METHODS)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.date} {self.time} - {self.message[:30]} ({self.remind_via})"

