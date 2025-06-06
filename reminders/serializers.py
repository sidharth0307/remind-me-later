from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reminder
		fields = ['id','date','time','message','remind_via']