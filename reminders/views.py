from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReminderSerializer
from rest_framework.generics import ListAPIView, DestroyAPIView
from .models import Reminder

class ReminderCreateAPIView(APIView):
	def post(self, request):
		serializer = ReminderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message':'Reminder saved successfully.'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReminderListAPIView(ListAPIView):
	queryset = Reminder.objects.all()
	serializer_class = ReminderSerializer

class ReminderDeleteAPIView(DestroyAPIView):
	queryset = Reminder.objects.all()
	serializer_class = ReminderSerializer
	lookup_field = 'id'