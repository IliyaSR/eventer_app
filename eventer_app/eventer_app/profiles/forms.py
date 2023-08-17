from django import forms
from eventer_app.events.models import EventModels
from eventer_app.profiles.models import ProfileModel


class ProfileBaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ProfileModel
        fields = ['email', 'profile_picture', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'profile_picture', 'password']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'password']


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            EventModels.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class ProfileCreateForm(ProfileBaseForm):
    pass
