from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
# Create your views here.
from . models import Gamecredsmanagers
from . forms import GameForm


def list(request):
    all_data = Gamecredsmanagers.objects.all()
    return render(request, 'gamemanager/gamemanager_list.html', {'data': all_data})

# def insert_view(request):
#     context ={}
#     print("hello world")
#     form = GameForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()

#     context['form'] =form
#     return render(request, "gamemanager/insert_data.html", context)

# def delete_view(request):
#     context = {}
#     obj = get_object_or_404(Gamemanager, id = id)
#     if request.method == "POST":
#         obj.delete()
#         return HttpResponseRedirect("/")
#     return render(request, "gamemanager/delete_view.html", context)

def home(request):
    return HttpResponse("hello world")
