from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get("hello_world_input")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'

    # def get_object(self):
    #     object = get_object_or_404(User, id=self.kwargs['id'])
    #
    #     return object


