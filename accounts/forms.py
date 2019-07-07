from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    use_gravatar = forms.BooleanField(label='Use avatars from Gravatar?', required=False)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        try:
            self.fields['use_gravatar'].initial = self.instance.profile.use_gravatar
            self.fields['avatar'].initial = self.instance.profile.avatar
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['last_name'].initial = self.instance.last_name
            self.fields['email'].initial = self.instance.email
            self.fields['location'].initial = self.instance.profile.location
        except User.DoesNotExist:
            pass

    class Meta:
        model = Profile
        fields = ['avatar', 'first_name', 'last_name', 'email', 'use_gravatar', 'location', ]
        exclude = ['user']

    def save(self, commit=True):
        super(ProfileForm, self).save(commit)
        self.instance.profile.use_gravatar = self.cleaned_data['use_gravatar']
        if self.cleaned_data['avatar'] is not False:
            self.instance.profile.avatar = self.cleaned_data['avatar']
        else:
            self.instance.profile.avatar = None
        self.instance.profile.location = self.cleaned_data['location']
        self.instance.profile.save()
        self.instance.save()

        return self.instance
