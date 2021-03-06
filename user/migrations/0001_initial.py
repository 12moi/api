# Generated by Django 3.2.7 on 2022-05-10 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('bio', models.TextField(max_length=255)),
                ('work_experience', models.TextField(choices=[('Less than a year', 'Less than a year'), ('one to three year', '1 to 3'), ('three to five years', '3 to 5 years'), ('Five years and more', '  5+ years')], max_length=30)),
                ('profile_image', models.FileField(blank=True, upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(blank=True, upload_to='')),
                ('skills', models.CharField(blank=True, choices=[('Cognitive', 'Cognitive Skills'), ('Management', 'Management Skills'), ('Interpersonal', 'Interpersonal Skills'), ('Other skills', 'Other skills')], max_length=30)),
                ('referees', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Contact', models.IntegerField()),
                ('Availability', models.CharField(max_length=255)),
                ('Salary_Expectations', models.CharField(max_length=255)),
                ('Relate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='user.userprofile')),
            ],
        ),
    ]
