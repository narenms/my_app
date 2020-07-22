from os import name
import pandas as pd
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# Create your views here.
from my_app.core.models import SampleUser


@api_view(["GET"])
@permission_classes((AllowAny,))
def sample(request):
    df = pd.read_csv('my_app/core/output.csv')
    for index, row in df.iterrows():
        print(row["name"], row["phone"], row['email'])
        user = SampleUser(
            name=row['name'], phone_no=row['phone'], email_id=row['email'])
        user.save()

    return Response({'message': 'Read data from CSV and updated to model.'}, status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((AllowAny,))
def sample_get(request):
    data = SampleUser.objects.all().values('name', 'phone_no', 'email_id')
    return Response({'message': list(data)}, status=HTTP_200_OK)
