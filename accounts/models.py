from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=10, verbose_name='Title',
                             choices=(('dr', 'Dr.'), ('prof', 'Prof.'), ('mr', 'Mr.'), ('mrs', 'Mrs.'),
                                      ('miss', 'Miss.')), blank=True, )
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, default=True, null=True, choices=(('male', 'Male'), ('female', 'Female')))
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['title', 'date_of_birth', 'gender',
                       'street1', 'zip_code',
                       'city', 'country']

    objects = CustomUserManager()
