from django.shortcuts import render, redirect
from .models import Project, Skill, Message, Endorsement, ProjectLanguage
from .form import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm, CommentForm1
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.conf import settings
import os



# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    project1 = ProjectLanguage.objects.all()
    skills = Skill.objects.all()
    endorsement = Endorsement.objects.filter(approved=True)
    context = {'projects': projects, 'skills': skills, 'endorsement': endorsement, 'project1': project1

               }
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    counts = project.comment_set.count()
    comments = project.comment_set.all().order_by('-created')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            form.save()
            messages.success(request, 'Your comment was successfully sent!')
    context = {'project': project, 'counts': counts, 'comments': comments, 'form': form}
    return render(request, 'base/project.html', context)


def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    UnreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'UnreadCount': UnreadCount}
    return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/messages.html', context)


def addSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, 'Your skill was successfully added')
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/skill_form.html', context)


def addEndorsement(request):
    endorsement = EndorsementForm()
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request, 'Your endorsement was successfully added')
        return redirect('home')

    context = {'endorsement': endorsement}
    return render(request, 'base/endorsement_form.html', context)


def projectPage1(request, pk):
    project1 = ProjectLanguage.objects.get(id=pk)
    counts = project1.comment1_set.count()
    comments = project1.comment1_set.all().order_by('-created')

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm1(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project1
            form.save()
            messages.success(request, 'Your comment was successfully sent!')
    context = {'project1': project1, 'counts': counts, 'comments': comments, 'form': form}
    return render(request, 'base/project1.html', context)


def editProject1(request, pk):
    project = ProjectLanguage.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def contactMe(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/Contact_form.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404
