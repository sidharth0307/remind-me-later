from django.urls import path
from .views import ReminderCreateAPIView, ReminderListAPIView, ReminderDeleteAPIView

urlpatterns= [
	path('reminders/', ReminderCreateAPIView.as_view(), name='reminder-create'),
	path('reminders/all/', ReminderListAPIView.as_view(), name='reminder-list'),
	path('reminders/<int:id>/', ReminderDeleteAPIView.as_view(), name='reminder-delete'),
]