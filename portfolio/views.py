from django.shortcuts import render, redirect
from .models import About, ResumeItem, Service, Skill, Project, BlogPost, SiteStatistic
from .forms import ContactForm  
from django.http import FileResponse
import os
from django.conf import settings


def index(request):
    # Process form submission first
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('portfolio:index')
    else:
        form = ContactForm()

    # Now gather the rest of your data
    about = About.objects.first()
    resume_items = ResumeItem.objects.all()
    services = Service.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    count_pro = projects.count()
    blog_posts = BlogPost.objects.order_by('-BPcreated_at')[:3]

    # Update site statistics with the count of projects
    statsed = SiteStatistic()
    statsed.SScomplete_projects = count_pro
    statsed.save()
    stats = SiteStatistic.objects.first()

    # Build context after form is defined
    context = {
        'about': about,
        'form': form,
        'resume_items': resume_items,
        'services': services,
        'skills': skills,
        'projects': projects,
        'blog_posts': blog_posts,
        'stats': stats,
    }
    return render(request, 'index.html', context)



def download_cv(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'CV\IslamNajahCV.pdf')  # Adjust the path as needed.
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='IslamNajahCV.pdf')


