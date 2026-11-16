from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLES = (
            ('admin','admin'),
            ('student','student'),
            ('trainer','trainer')
             )

    phone = models.CharField(max_length=12,unique=True)

    role = models.CharField(max_length=10,choices=ROLES,default='student')

class StudentProfile(models.Model):

    qualification = models.CharField(max_length=100,null=True)

    skills = models.CharField(max_length=200,null=True)

    linkedin_url = models.URLField(null=True)

    github_url = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')

class TrainerProfile(models.Model):

    qualification = models.CharField(max_length=200,null=True)

    experience = models.PositiveIntegerField(null=True)

    specialization = models.CharField(max_length=200,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    trainer = models.OneToOneField(User,on_delete=models.CASCADE,related_name='trainer_profile')


from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,**kwargs):

    if created and instance.role == 'student':

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)


def create_trainer_profile(sender,instance,created,**kwargs):

    if created and instance.role == 'trainer':

        TrainerProfile.objects.create(trainer=instance)

post_save.connect(create_trainer_profile,sender=User)