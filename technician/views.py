from django.shortcuts import redirect, render
from instruments.models import Malfunction

 
def main_page_tech(request):
    Customers = Malfunction.objects.filter(status = 'in process')
    context = {
        'customers' :Customers,
        'action':'technician'
    }
    return  render(request,'firsttable.html',context)

     
def change(request,data): 
    data = data.split(",")
    Customers = Malfunction.objects.filter( user_id = data[0], id = data[1] ).update(status = 'phone ready for delivery' )
    return redirect('technician:mainpage') 
    