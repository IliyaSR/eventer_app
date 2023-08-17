from django.shortcuts import render, redirect
from eventer_app.events.forms import EventForm, EventDeleteForm
from eventer_app.events.models import EventModels
from eventer_app.profiles.models import ProfileModel
from eventer_app.profiles.views import create_profile_page


def dashboard_page(request):
    context = {
        'events': EventModels.objects.all(),
        'nav_links': True,
    }

    return render(request, template_name='events/dashboard.html', context=context)


def create_page(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {'form': form,
               'nav_links': True,}

    return render(request, template_name='events/event-create.html', context=context)


def event_details_page(request, pk):
    event = EventModels.objects.get(pk=pk)
    events = EventModels.objects.all()
    context = {
        'event': event,
        'events': events,
        'nav_links': True,
    }

    return render(request, template_name='events/events-details.html', context=context)


def edit_event_page(request, pk):
    event = EventModels.objects.get(pk=pk)
    if request.method == 'GET':
        form = EventForm(instance=event, initial=event.__dict__)
    else:
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form,
               'nav_links': True,}

    return render(request, template_name='events/event-edit.html', context=context)


def delete_event_page(request, pk):
    event = EventModels.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')
    form = EventDeleteForm(initial=event.__dict__)
    context = {
        'form': form,
        'nav_links': True,
    }

    return render(request, template_name='events/events-delete.html', context=context)
