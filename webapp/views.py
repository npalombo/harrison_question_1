from geodata import fetch

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html', {'states': fetch.states})


@login_required
def detail(request, state):
    all_geodata = fetch.get_data_for_state(state)
    return render(request, 'detail.html', {'state': state, 'all_geodata': all_geodata})

