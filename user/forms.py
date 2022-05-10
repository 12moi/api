
from django import forms

from user.models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'