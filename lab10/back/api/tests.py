from django.shortcuts import render
from api.models import *
from api.serializer import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def getCompany(request):
    companies = Company.objects.all()
    if(request.method == 'GET'):
        companies = CompanySerializer(companies, many=True)
        return JsonResponse(companies.data, safe=False)
    
@api_view(['POST'])
def postCompany(request):
    
    if(request.method == 'POST'):
        
        companies = CompanySerializer(data = request.data)
        if companies.is_valid:
            companies.create()
            return Response(companies.data, status=status.HTTP_201_CREATED)
        return Response(companies.errors, status=status.HTTP_400_BAD_REQUEST)
    
def getVacancy(request):
    vacancies = Vacancy.objects.all()
    # [:10]->top 10
    if(request.method == 'GET'):
        vacancies = VacancySerializer(vacancies, many=True)
        return JsonResponse(vacancies.data, safe=False)
def getVacancyByCompany(request, id):
    
    vacancies = Vacancy.objects.filter(company = id)
    if(request.method == 'GET'):
        vacancies = VacancySerializer(vacancies, many=True)
        return JsonResponse(vacancies.data, safe=False)