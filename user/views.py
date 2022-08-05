from datetime import datetime
from typing import Dict
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View

from .models import Author
from .forms import AuthorRegistrationForm
import logging
logger = logging.getLogger(__name__)


def register(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html, status=200)


class UserRegisterView(View):
    form_class = AuthorRegistrationForm
    initial: Dict = {}
    template_name = 'user/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            user = form.save()
            bio = form.cleaned_data.get('bio')
            author = Author(bio=bio, user=user)
            author.save()

            return redirect('post_list')

        return render(request, self.template_name, {'form': form})
