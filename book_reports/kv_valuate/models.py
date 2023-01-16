from django.db import models

# Create your models here.



class kv_report(models.Model):


    zoho_user_name = models.EmailField()
    zoho_user_pwd = models.TextField(max_length=30)
    zoho_org_id = models.PositiveBigIntegerField()
    zoho_org_domain = models.TextField(max_length=10, default='.in')



    def __str__(self) -> str:
        
        return self.zoho_user_name


    