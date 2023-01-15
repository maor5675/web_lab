from django.db import models
from user.models import User
from enum import Enum



# Phonebrand table represents all the popular phone brands in israel and give us the option to illustrate the web with brand pics 

class Phonebrand(models.Model):
   brand = models.CharField(max_length=100, null=False)
   logo = models.ImageField(null=True, blank=True)
   
   def __str__(self):
      return self.brand


# Phonetype table represents all the popular phone types in israel connected to specific brand and give us the option to illustrate the web with gadget pics 

class Phonetype(models.Model):
   brand = models.ForeignKey(Phonebrand,on_delete=models.CASCADE)
   type = models.CharField(max_length=100, null=False)
   image =  models.ImageField(null=True, blank=True)

   def __str__(self):
      return self.brand.brand +","+  self.type

# represents the popular phone by phone type and brand make the serch more easy to execute 

class Phone(models.Model):
   type= models.ForeignKey(Phonetype,on_delete=models.CASCADE)
   device = models.CharField(max_length=100, null=False)

   def __str__(self):
      return self.device +","+  self.type.type

# here the web owner insert the popular Malfunction types he can ofer

class Malfunction_type(models.Model):
   Malfunction = models.CharField(max_length=100)

   def __str__(self):
      return self.Malfunction


class Price(models.Model):
   phone_device = models.ForeignKey(Phone,on_delete=models.CASCADE)
   Malfunction_type= models.ForeignKey(Malfunction_type,on_delete=models.CASCADE)
   price = models.PositiveIntegerField(null= True, blank = True)

   def __str__(self):
      return self.Malfunction_type.Malfunction +','+self.phone_device.device

class status_order_type(Enum):
   await_for_mail_man = 1
   in_process = 2
   phone_ready_for_delivery = 3
   phone_ready_mailman_will_arrive_soon = 4
   order_done = 5


#that table grouping Phone,Malfunction_type,user for represent the order

class Malfunction(models.Model):
   
   
   class StatusType(models.IntegerChoices):
        await_for_mail_man = 1, "await for mail man"
        in_process = 2, "in process"
        phone_ready_for_delivery = 3, 'phone ready for delivery'
        phone_ready_mailman_will_arrive_soon = 4, 'phone ready mailman will arrive soon'
        order_done = 5, 'order done'


   phone= models.ForeignKey(Phone,on_delete=models.CASCADE)
   Malfunction_type= models.ForeignKey(Malfunction_type,on_delete=models.CASCADE)
   user= models.ForeignKey(User,on_delete=models.CASCADE)
   status = models.PositiveIntegerField(null= True, choices=StatusType.choices)
   request_date = models.DateField(auto_now_add=True)
   price = models.PositiveIntegerField(null = True, blank = True)


   def __str__(self):
         return self.user.username +","+ self.Malfunction_type.Malfunction +","+  self.phone.device +","+ str(self.request_date)

   def get_Type(self):
        for choice in self.StatusType:
            if self.type == choice.value:
                return choice.label
        return 'NO TYPE'


class handled_by(models.Model):
   order= models.ForeignKey(Malfunction,on_delete=models.CASCADE, null=False)
   mail_man_OR_technician=models.ManyToManyField(User,null=False)
   