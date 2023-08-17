from django import forms
from eventer_app.events.models import EventModels


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModels
        fields = ['event_name', 'category', 'description', 'event_date', 'event_image']


class EventDeleteForm(EventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
