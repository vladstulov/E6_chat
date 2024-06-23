from django.http import HttpResponse
import json
from django.shortcuts import render
from django.core.cache.backends.locmem import _caches as cache


# get rooms from cache
def rooms_reader():
    rooms = []
    for key in cache['my_cache']:
        rooms.append(key)
    return rooms


# home page
def index(request):
    rooms = rooms_reader()
    return render(request, "appchat/index.html", context={'rooms': rooms})


# get the room_name from the url
def room(request, room_name):
    room_name = room_name.replace(' ', '_')
    return render(request, "appchat/chatbox.html", context={"room_name": room_name})


# refreshes rooms from cache for index.html
def rooms_return(request):
    rooms = rooms_reader()
    jsn = json.dumps(rooms)
    return HttpResponse(jsn)
