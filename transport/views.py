from django.http import HttpResponse
from django.shortcuts import redirect, render
from instruments.models import Malfunction
 
# this function is for the first delivery afther the costumer make a order the mail man need to go to the place he insert to the web and take the phone 
def main_page_tran(request):
    Customers = Malfunction.objects.filter(status = 'await for mail man')
    context = {
        'customers' :Customers,
        'action' : 'mailman'
    }
    return  render(request,'firsttable.html',context)
     
def first_change(request,data):
    Data = data.split(',')
    if Data[1] == "await for mail man": 
        Customers = Malfunction.objects.filter( user_id = data[0], status = Data[1]).update(status = 'in process' )
        return redirect('transport:mainpage')
    
    Customers = Malfunction.objects.filter( user_id = data[0], status = Data[1] ).update(status = 'phone ready mailman will arrive soon' )
    return redirect('transport:secondpage')

#this function is for the second delivery the mail man take the phone from the technician and deliver the phone back to the cosumer
def second_page_tran(request):
    Customers = Malfunction.objects.filter(status = 'phone ready for delivery')
    context = {
        'customers' :Customers,
        'action' : 'mailman'
    }
    return  render(request,'firsttable.html',context)

