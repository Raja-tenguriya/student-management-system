from django.shortcuts import render, redirect
from django.views import View
from .models import student
from .forms import AddstudentForm

class home(View):
    def get(self, request):
        stu_data = student.objects.all()
        return render(request, 'crudapp/home.html',{'studata':stu_data})


class Add_student(View):
    def get(self, request):
        fm = AddstudentForm()
        return render(request, 'crudapp/add-student.html', {'form':fm})

    def post(self, request):
        fm = AddstudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'crudapp/add-student.html', {'form': fm})



class delete_student(View):
    def post(self, request):
        data = request.POST
        roll = data.get('roll')
        studata = student.objects.get(roll=roll)
        print(studata)
        studata.delete()
        return redirect('/')


class Edit_student(View):
    def get(self, request, roll):
        stu = student.objects.get(roll=roll)
        fm = AddstudentForm(instance=stu)
        return render(request, 'crudapp/Edit-student.html', {'form':fm})
    
    def post(self, request, roll):
        stu = student.objects.get(roll=roll)
        fm = AddstudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')              

