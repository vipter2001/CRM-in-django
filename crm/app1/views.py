from django.shortcuts import render,get_object_or_404,redirect
from .models import Detailsform
# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    detail=Detailsform.objects.all()
    context={
        "person":detail
    }
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        
        detail=Detailsform(name=name,email=email,phone=phone,gender=gender,address=address,pincode=pincode)
        detail.save()
        
    return render(request,'index.html',context)
        
def delete(request,id):
    
    obj=get_object_or_404(Detailsform,id=id)
    obj.delete()
        
    return redirect('home')
    
def edit(request,id):
    
    obj=get_object_or_404(Detailsform,id=id)

    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.gender=gender
        obj.address=name
        obj.pincode=pincode
        obj.save()
        return redirect('home')
    
    
    
    
    
    return render(request,'edit.html',{"obj":obj})
    
    # return redirect('home')
    
    