from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView
from django.utils.http import urlencode
from django.shortcuts import render, redirect
import hashlib
from .forms import ProfileForm, UserCreationMultiForm
from .models import  Profile


def gitlab_auth(request):
    print(request.POST)

    return render(request, 'base.html')


def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=(urlencode({'d': default, 's': str(size)}))
    )
    return url


class UserSignupView(CreateView):
    form_class = UserCreationMultiForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            # We need to save the user before we can save the profile
            user = form['user'].save()
            profile = form['profile'].save(commit=False)
            profile.user = user
            profile.save()
            return redirect(self.get_success_url())
        return render(self.request, self.template_name, self.get_context_data())


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            return super(UserLoginView, self).form_valid(form)

        return render(self.request, self.template_name, self.get_context_data())


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'view_account.html'
    success_url = reverse_lazy('view_account')

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_avatar(self, instance):
        if instance.profile.use_gravatar:
            return gravatar(user=instance.profile.user)

        return ''
    get_avatar.short_description = 'Current Avatar'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.profile.save()
        user.save()

        return redirect('view_account')
