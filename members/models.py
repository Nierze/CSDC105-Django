from django.db import models

class Member(models.Model): 
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # 
    def __repr__(self):
        return self.firstname +  " " + self.lastname


    