from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from  .forms  import ServiceRequestForm


@login_required
def create_request(request):
  
    if request.method == 'POST':
        form= ServiceRequestForm(request.POST , request.FILES)
        if form.is_valid():
            service_request=form.save(commit=False)
            service_request.customer=request.user
            service_request.save()
            return redirect('track_request')
        else:
            form=ServiceRequestForm()
        return render(request , 'create_request.html',{'form':form})
         
    
@login_required
def track_request(request):
    requests=ServiceRequest.objects.filter(customer=request.user)
    return render(request , 'track_request.html',{'requests': requests})

@login_required
def account_details(request):
    return render(request , 'account_details.html',{'user':request.user})

