from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Assets(models.Model):
    name = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


request_status = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected')
)

class AssetRequest(models.Model):
    requestId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assetId = models.ForeignKey(Assets, on_delete=models.CASCADE)
    employeeId = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_date =  models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    requestStatus = models.CharField(choices=request_status, default='Pending', max_length=100)
    description = models.CharField(max_length=150)
