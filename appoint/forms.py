from django.forms import ModelForm
from .models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['age','mobNum','profilePicture','speciality','city','availability','author']