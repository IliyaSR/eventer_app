from django.core.validators import MinLengthValidator
from django.db import models
from eventer_app.profiles.validators import validate_only_letters, validate_password_contains_digit


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=20, validators=[validate_only_letters])
    last_name = models.CharField(max_length=30, validators=(MinLengthValidator(4),))
    email = models.EmailField(max_length=45)
    profile_picture = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=20, validators=[validate_password_contains_digit, MinLengthValidator(5)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"