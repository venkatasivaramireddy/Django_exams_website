from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from app.form import QuizForm


def show(request):
    return render(request, 'qtemplate.html', {'form': QuizForm()})

def main(request):

    return render(request,'main.html')

# def loginPage(request):
#     try:
#         value=request.session["email"]
#     except KeyError:
#         student = StudentForm()
#         return render(request, "reg.html", {"form": student})
#     else:
#         return homepage(request)
#
#
# def homepage(request):
#     try:
#         value = request.session["email"]
#     except KeyError:
#         messages.success(request, "Please login")
#         return redirect("main")
#     else:
#         return render(request,"welcome.html",{"email":value})
#
# def savedetails(request):
#     try:
#         n=request.POST["name"]
#         e=request.POST["email"]
#         p=request.POST["password"]
#         i=request.FILES["photo"]
#         StudentModel(name=n,email=e,password=p,photo=i).save()
#         messages.success(request,"registered Successfully, Please Login To access Dashboard")
#         return redirect("main")
#     except:
#         messages.success(request, "Email Already Exstised Please login")
#         return redirect("main")
#
# def verityuser(request):
#     e = request.POST["email"]
#     p = request.POST["password"]
#     try:
#         res=StudentModel.objects.get(email=e,password=p)
#     except StudentModel.DoesNotExist:
#         messages.success(request, "Details Not Match Please register")
#         return redirect("main")
#     else:
#         request.session["email"] = e
#         return redirect("welcome")
#
#
# def profile(request):
#     try:
#         value = request.session["email"]
#     except KeyError:
#         messages.success(request, "Please login")
#         return redirect("main")
#     else:
#         value = StudentModel.objects.get(email=value)
#         return render(request,"profile.html",{"profile":value})

# def forgotpassword(request):
#     student = StudentForm()
#     return render(request, "forgotpassword.html", {"form": student})
#
# def updatedpassword(request):
#     e = request.POST["email"]
#     try:
#         res=StudentModel.objects.get(email=e)
#     except StudentModel.DoesNotExist:
#         messages.success(request, "Please Enter valid Email or Register ")
#         return redirect("main")
#     else:
#         res.password= request.POST["password"]
#         res.save()
#         messages.success(request, "PassWord Updated Succesfully, Please login")
#         return redirect("main")
#
# def logout(request):
#     try:
#         del request.session["email"]
#     except KeyError:
#         return redirect('main')
#     else:
#         return redirect('main')
def enterquestion(request):

    return render(request,"enterquestion.html")


def data(request):
    request.POST.get('')
    return None