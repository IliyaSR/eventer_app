from django.core.validators import MinLengthValidator
from django.db import models
from eventer_app.events.validators import validate_future_date


class EventModels(models.Model):
    CATEGORY_CHOICES = [
        ("Sports", "Sports"),
        ("Festivals", "Festivals"),
        ("Conferences", "Conferences"),
        ("Performing Art", "Performing Art"),
        ("Concerts", "Concerts"),
        ("Theme Party", "Theme Party"),
        ("Other", "Other"),
    ]

    event_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),))
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField(validators=[validate_future_date])
    event_image = models.URLField()
