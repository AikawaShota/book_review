from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


@login_required
def close_account(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return render(request, 'registration/close_account.html')


@login_required
def close_account_confirm(request):
    return render(request, 'registration/close_account_confirm.html')


@login_required
def account(request):
    return render(request, 'accounts/account.html')
