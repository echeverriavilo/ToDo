from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    age = models.IntegerField(verbose_name=_("Age"))
    email = models.EmailField(verbose_name=_("Email Address"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"))     
    
    def __str__(self):
        return self.user.username  
        
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
