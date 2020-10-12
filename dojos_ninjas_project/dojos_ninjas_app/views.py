from django.shortcuts import render, redirect
from dojos_ninjas_app.models import Ninja, Dojo

# Create your views here.
def index(request):
    context = {
        # 'all_dojos' : Dojo.objects.all()
        'all_dojos' : Dojo.objects.all().order_by("city")#makes sure it is in alphabetical order
    }

    return render(request, 'index.html', context)

def process_add(request):
    if ( request.POST['which_form'] == "add_dojo"):
        Dojo.objects.create(name = request.POST['dojo_name'], city = request.POST['dojo_city'], state = request.POST['dojo_state'])

    if ( request.POST['which_form'] == "add_ninja"):
        Ninja.objects.create(first_name = request.POST['ninja_first'], last_name = request.POST['ninja_last'], dojo = Dojo.objects.get(city=request.POST['dojo']))

    return redirect('/')

def delete(request, dojo_id):
    delete_dojo = Dojo.objects.get(id= dojo_id)
    delete_dojo.delete()

    return redirect('/')

