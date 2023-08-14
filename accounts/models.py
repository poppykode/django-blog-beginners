from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User (AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ADMIN = 'admin'
    USER = 'user'
    ROLES =((ADMIN,ADMIN),(USER,USER))
    role = models.CharField(max_length=6, choices=ROLES,default=ADMIN)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username + ' ' +(self.role)
