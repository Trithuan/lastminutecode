from django.shortcuts import render, redirect, HttpResponse

def mathieu(request):
	return render(request, 'mathieu/index.html')

def cv_mathieu(request):
	return render(request, 'mathieu/cv.html')