from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import MovieTicket
from .forms import MovieTicketForm
@login_required(login_url='login_url')
def add_movieticket(request):
    template_name = 'crud_app/add.html'
    form = MovieTicketForm()
    if request.method == "POST":
        form = MovieTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request,template_name,context)
@login_required(login_url='login_url')
def show_movieticket(request):
    template_name = 'crud_app/show.html'
    movietickets = MovieTicket.objects.all()
    context = {'movietickets': movietickets}
    return render(request, template_name, context)

def update_movieticket(request,pk):
    template_name = 'crud_app/add.html'
    obj = MovieTicket.objects.get(id=pk)
    form = MovieTicketForm(instance=obj)
    if request.method == "POST":
        form = MovieTicketForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request,template_name,context)

def cancel_movieticket(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = MovieTicket.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')

    return render(request,template_name)


