
from rest_framework import serializers
from user.models import Apply


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ['Full_Name', 'Email', 'Contact', 'Salary_Expectations']