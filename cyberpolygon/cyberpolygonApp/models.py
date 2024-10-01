from django.contrib.auth.models import AbstractUser
import jsonfield
from django.db import models
from django.db.models import Model, OneToOneField
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if not username:
            raise ValueError("Username shouldn't be empty")
        if not password:
            raise ValueError("Password shoudn't be empty")
        
        user = self.model(**extra_fields)
        if email:
            email = self.normalize_email(email)
            user.email = email
        user.set_password(password)
        userRole = Role.objects.create(role_name = "user")
        user.id_role = userRole
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        user = self.model(**extra_fields)
        if email:
            email = self.normalize_email(email)
            user.email = email
        user.set_password(password)
        adminRole = Role.objects.create(role_name="admin")
        user.id_role = adminRole
        user.save(using=self.db)
        return user


class User(AbstractUser):
    user_data = jsonfield.JSONField()
    id_role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
    telegram_id = models.CharField(max_length=50, unique=True, null=True)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

class Role(models.Model):
    role_name = models.TextField(max_length=50, default="user")
    description = models.TextField()


class Category(models.Model):
    name = models.TextField(max_length=50)


class Task(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    title = models.TextField(max_length=100)
    description = models.TextField()
    points = models.IntegerField
    flag = models.TextField(max_length=100)
    is_active = models.BooleanField()
    created_at = models.DateField()


class Comments(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    task_id = models.ForeignKey('Task', on_delete=models.PROTECT)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.IntegerField()


class UserAvatar(models.Model):
    user_id = OneToOneField('User', on_delete=models.PROTECT)
    image_path = models.TextField(max_length=255)
    image_hash = models.TextField(max_length=255)
    created_at = models.DateField()
# Create your models here.

