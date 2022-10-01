from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<username>/<filename>
    return 'user_{0}/{1}'.format(instance.username, filename)



class AccountManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields): 
        if not username: raise ValueError( _('Please provide a username !'))

        # first_name=first_name,
        # last_name=last_name
        # email=self.normalize_email(email),
        if extra_fields.get('user_type') != 'vigile':
            user = self.model(
                username=username,
                is_active=True,
                **extra_fields
            )
        else:
            user = self.model(
                username=username,
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
       
        user.is_active      = True
        user.is_staff       = True
        user.is_superuser   = True 
        
        user.save(using=self._db)
        
        return user
        

USER_TYPE = [
    ('PHARMACIST', _('pharmacist')),
    ('VIGILE', _('vigile')),
    ('ADMIN', _('admin')),
]

username_validator = UnicodeUsernameValidator()

class Account(AbstractBaseUser):
    first_name      = models.CharField(_('First Name'), max_length=100, blank=True, null=True)
    last_name       = models.CharField(_('Last Name'), max_length=100, blank=True, null=True)
    username        = models.CharField(_('Username'), max_length=50, unique=True, validators=[username_validator])
    email           = models.CharField(_('email'), max_length=100, unique=True, blank=True, null=True)
    phone_number    = models.CharField(_('phone number'), max_length=50, blank=True, null=True)
    address         = models.CharField(_('address'), max_length=100, blank=True, null=True)
    picture         = models.ImageField(_('Picture'), upload_to=user_directory_path, blank=True, null=True)
    user_type       = models.CharField(_('User Type'), choices=USER_TYPE, max_length=100, default='pharmacist')
    birth_date      = models.CharField(_('Birth Date'), null=True, blank=True, max_length=100)
    

    # required field
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_staff        = models.BooleanField(_('staff'), default=False)
    is_superuser   = models.BooleanField(_('superadmin'), default=False)
    is_active       = models.BooleanField(_('active'), default=False)


    USERNAME_FIELD  = 'username'

    objects = AccountManager()
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('profile-detail', kwargs={'id': self.pk})
    

    
    
    
    


