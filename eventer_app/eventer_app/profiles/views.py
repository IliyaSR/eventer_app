from django.shortcuts import render, redirect
from eventer_app.profiles.forms import ProfileForm, ProfileEditForm, ProfileDeleteForm, ProfileCreateForm
from django.contrib.auth.decorators import login_required
from eventer_app.profiles.models import ProfileModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def create_profile_page(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,

    }

    return render(request, template_name='profiles/profile-create.html', context=context)


def profile_details_page(request):
    profile = get_profile()
    events_count = EventModels.objects.count()

    context = {
        'profile': profile,
        'nav_links': True,
        'events_count': events_count,

    }

    return render(request, template_name='profiles/profile-details.html', context=context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form,
               'nav_links': True, }
    return render(request, template_name='profiles/profile-edit.html', context=context)


def delete_profile_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'nav_links': True,
    }

    return render(
        request,
        'profiles/profile-delete.html',
        context,
    )
