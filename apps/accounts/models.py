from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'username',  'phone_number', 'address']

    def __str__(self):
        return self.username


# moved user verification model from main to account cause it is concerned with the account
class UserVerification(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='verification')
    NIN = models.CharField(_("National Identification Number"), max_length=20)
    BVN = models.CharField(_("Bank Verification Number"), max_length=20)
    upload_id = models.ImageField(_("upload id"), upload_to='ids/')
    id_type=models.CharField(_("type of ID"), max_length=500)
    bank_name = models.CharField(_("bank name"), max_length=50)
    account_number = models.CharField( _("bank account number"), max_length=20)
    account_name=models.CharField(_("bank account name"), max_length=50)

    class Meta:

        '''modifies the meta info of the UserVerification model'''

        verbose_name = _("user Verification")
        verbose_name_plural = _("user Verifications")

    def __str__(self):
        return f'{self.user}\'s verification '

    def get_absolute_url(self):
        # Edited according to the new url config
        return reverse("user-verify", kwargs={"pk": self.pk})
