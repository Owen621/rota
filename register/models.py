from asyncio.windows_events import NULL
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import random

ROLE_CHOICES = [
    ('KP', 'Kitchen Porter'),
    ('Commis Chef', 'Commis Chef'),
    ('CDP', 'Chef de Partie'),
    ('Sous Chef', 'Sous Chef'),
    ('Head Chef', 'Head Chef'),
]

HOURS_CHOICES = [
    (5, 5),
    (10, 10),
    (15, 15),
    (20, 20),
    (25, 25),
    (30, 30),
    (35, 35),
    (40, 40),
    (45, 45),
    (50, 50),
]

PAY_CHOICES = [
    (5, '£5.00'),
    (5.5, '£5.50'),
    (6, '£6.00'),
    (6.5, '£6.50'),
    (7, '£7.00'),
    (7.5, '£7.50'),
    (8, '£8.00'),
    (8.5, '£8.50'),
    (9, '£9.00'),
    (9.5, '£9.50'),
    (10, '£10.00'),
    (10.5, '£10.50'),
    (11, '£11.00'),
    (11.5, '£11.50'),
    (12, '£12.00'),
    (12.5, '£12.50'),
    (13, '£13.00'),
    (13.5, '£13.50'),
    (14, '£14.00'),
    (14.5, '£14.50'),
    (15, '£15.00'),
]

SHIFT_CHOICES = [
    (' ', ' '),
    ('09:00-22:00', '09:00-22:00'),
    ('09:00-17:00', '09:00-17:00'),
    ('10:00-22:00', '10:00-22:00'),
    ('10:00-17:00', '10:00-17:00'),
    ('11:00-22:00', '11:00-22:00'),
    ('11:00-17:00', '11:00-17:00'),
    ('12:00-22:00', '12:00-22:00'),
    ('12:00-17:00', '12:00-17:00'),
    ('13:00-22:00', '13:00-22:00'),
    ('13:00-17:00', '13:00-17:00'),
    ('14:00-22:00', '14:00-22:00'),
    ('15:00-22:00', '15:00-22:00'),
    ('16:00-22:00', '16:00-22:00'),
    ('17:00-22:00', '17:00-22:00'),
    ('18:00-22:00', '18:00-22:00'),
]





class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    rotaSaved = models.BooleanField(default=False)
    rotaGenerated = models.BooleanField(default=False)

    def companyGenerated(self):
        self.rotaGenerated = True
        self.save()


    def companySave(self):
        self.rotaSaved = True
        self.save()
            
    def companyClear(self):
        self.rotaSaved = False
        self.rotaGenerated = False
        self.save()
            
            
    def companyCheck(self):
        if self.rotaSaved == 0:
            return False
        else:
            return True
    

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=8)
    account = models.CharField(max_length=30)


class Employee(models.Model):
    extended_user = models.OneToOneField(ExtendedUser, on_delete=models.CASCADE, default=NULL)
    birth_date = models.DateField('Birthday')
    manager = models.ForeignKey(
        User, default=NULL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default=False)
    last_name = models.CharField(max_length=30, default=False)
    role = models.CharField(max_length=11, choices=ROLE_CHOICES)
    hours_per_week = models.IntegerField(choices=HOURS_CHOICES)
    hourly_pay = models.FloatField(choices=PAY_CHOICES)
    monday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")
    tuesday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")
    wednesday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")
    thursday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")
    friday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")
    saturday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")
    sunday = models.CharField(choices=SHIFT_CHOICES, max_length=15, default=" ")


    
    def generate(self):
        
        off = self.daysOff()
        days1 = [1] * 7

        for i in range(off):
            number = random.randint(0,6-i)
            k=0
            j=0
            while True:
                if j == number:
                    if days1[k] == 1:
                        days1[k] = 0
                        break
                else:
                    j+=1
                k+=1
        
        if self.hours_per_week % 10 == 5 or self.hours_per_week <= 20:
            days1 = self.randomHours(days1)

        days4 = [" "]*7
        for y in range(7):
            
            if days1[y] == 1:

                days4[y] = "12:00-22:00"

            if days1[y] == 2:

                days4[y] = "12:00-17:00"

            if days1[y] == 3:

                days4[y] = "17:00-22:00"

        return days4

    def SaveShifts(self, days1):
        self.monday = days1[0]
        self.tuesday = days1[1]
        self.wednesday = days1[2]
        self.thursday = days1[3]
        self.friday = days1[4]
        self.saturday = days1[5]
        self.sunday = days1[6]
        self.save()

    def unsave(self):
        self.monday = " "
        self.tuesday = " "
        self.wednesday = " "
        self.thursday = " "
        self.friday = " "
        self.saturday = " "
        self.sunday = " "
        self.save()

        

    def daysOff(self):

        if self.hours_per_week <= 20:
            off = 7 - (self.hours_per_week // 5)
        else:
            off = 7 - (self.hours_per_week // 10)
            if self.hours_per_week % 10 == 5:
                off -=1

        return off

    def randomHours(self, days):
        
        if self.hours_per_week <= 20:
            for x in range(len(days)):
                if days[x] == 1:
                    days[x] = random.randint(2,3) #if less than 20 randomise the shift times
                
            return days

        else:
            off = self.daysOff()
            work = 7-off
            num = random.randint(0,work-1) #otherwise, this subroutine has been called
            i = 0                          #because the hours per week % 10 == 5, therefore
            for x in range(7):             #the program needs to randomise the day which
                if days[x] == 1:           #the employee will work a 5 hour shift
                    if i == num:
                        n = random.randint(2,3)
                        days[x] = n
                    
                    i+=1

            return days