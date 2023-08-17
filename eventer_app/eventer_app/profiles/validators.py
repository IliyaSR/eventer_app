from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")


def validate_password_contains_digit(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least 1 digit!")
