from django.db import models

# Create your models here.
class UserProfile(models.Model):
    EXPRIENCE_LEVEL= [
        ('Less than a year', 'Less than a year'),
        ('one to three year','1 to 3'),
        ('three to five years','3 to 5 years'),
        ('Five years and more','  5+ years'),
      ]
    SKILL_TYPE= [
        ('Cognitive', 'Cognitive Skills'),
        ('Management','Management Skills'),
        ('Interpersonal','Interpersonal Skills'), 
        ('Other skills','Other skills'),
      ]
   
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=30,  blank=True)
    email = models.CharField(max_length=255)
    bio = models.TextField(max_length=255)
    work_experience = models.TextField(max_length=30, choices=EXPRIENCE_LEVEL)
    profile_image =models.FileField(blank=True)
    address = models.CharField(max_length=100)
    resume = models.FileField(blank=True)
    skills =  models.CharField(max_length=30, blank=True, choices=SKILL_TYPE )
    referees = models.CharField(max_length=255, blank=True)

class Apply(models.Model):
    Relate= models.OneToOneField(UserProfile, null=True, blank=True, on_delete=models.CASCADE, related_name='apply')
    Full_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Contact = models.IntegerField()
    Availability= models.CharField(max_length=255)
    Salary_Expectations = models.CharField(max_length=255)
    


    def save_Apply(self):
        self.save()


    def delete_Apply(self):
        self.delete()