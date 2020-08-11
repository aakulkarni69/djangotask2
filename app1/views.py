from django.shortcuts import render,redirect
from app1.models import student

def page1(request):
	if request.method=='POST':
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		ph_no = request.POST.get('ph_no')
		email = request.POST.get('email')
		gender = request.POST.get('gender')
		profile = student(f_name=f_name,l_name=l_name,ph_no=ph_no,email=email,gender=gender)
		profile.save()
		return redirect('page1')
	else:
		return render(request,'page1.html')

def page2(request):
	if request.method=='POST':
		email=request.POST.get('email')
		try:
			profile=student.objects.get(email=email)
			return render(request, 'page3.html', {'profile': profile, 'message': 'Found user!'})
		except student.DoesNotExist:
			return render(request, 'page3.html', {'message': 'Sorry no user with the entered email found'})
	else:
		return render(request,'page2.html')
