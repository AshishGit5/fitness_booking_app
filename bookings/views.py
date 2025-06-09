from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils.timezone import localtime

@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.all()
    for cls in classes:
        cls.date_time = localtime(cls.date_time)
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    try:
        class_id = request.data['class_id']
        client_name = request.data['client_name']
        client_email = request.data['client_email']
    except KeyError:
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({'error': 'Fitness class not found'}, status=status.HTTP_404_NOT_FOUND)

    if fitness_class.available_slots <= 0:
        return Response({'error': 'No available slots'}, status=status.HTTP_400_BAD_REQUEST)

    Booking.objects.create(
        fitness_class=fitness_class,
        client_name=client_name,
        client_email=client_email
    )

    fitness_class.available_slots -= 1
    fitness_class.save()

    return Response({'message': 'Booking successful'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    if not email:
        return Response({'error': 'Email parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
