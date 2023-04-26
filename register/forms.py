from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from register.models import Company, Employee, ExtendedUser

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ['company_name']

class ExtendedUserForm(ModelForm):

    class Meta:
        model = ExtendedUser
        fields = ['postcode']
        

class AddEmployee(ModelForm):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'birth_date', 'role', 'hours_per_week', 'hourly_pay']
        


class ShiftForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']