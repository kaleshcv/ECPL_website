from django.db import models

# Create your models here.

class Services(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    icon=models.CharField(max_length=100)

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    testi=models.TextField()

class Contactform(models.Model):
    message = models.TextField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/images')
class Clients(models.Model):
    image=models.ImageField(upload_to='static/logos')

class Careers(models.Model):
    designation=models.CharField(max_length=200)
    project=models.CharField(max_length=200)
    job_location=models.CharField(max_length=200)
    work_timing=models.CharField(max_length=200)
    weekly_off=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    emp_type=models.CharField(max_length=200)
    salary=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    skills=models.CharField(max_length=200)
    requirement=models.TextField()
    interview_type=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    others=models.CharField(max_length=200)

class Candidate(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    resume=models.FileField(upload_to='static/Resume')
