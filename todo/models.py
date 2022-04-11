from enum import auto
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#title
#status
#data-current
#user
#priority




class Todo(models.Model):

    status_choices=[


        ('C','Completed'),
        ('P','Pending'),
    ]
    priority_choices=[


        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
        ('10','🔟'),
       
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE) #which means on dlete user all to do will delete
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2,choices=status_choices)
    date=models.DateTimeField(auto_now_add=True) #it will add current date
    priority=models.CharField(max_length=2,choices=priority_choices)