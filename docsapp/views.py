from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Document
from .forms import DocumentForm

def docs_public(request):
    docs = Document.objects.filter(access='public').order_by('title')
    return render(request, 'docsapp/docs_public.html', {'docs': docs})

@login_required
def docs_manage(request):
    user = request.user
    role = 'client'
    profile = getattr(user, 'profile', None)
    if profile:
        role = profile.role
    elif user.is_superuser:
        role = 'admin'

    if role not in ['admin', 'manager']:
        return HttpResponseForbidden('Доступ запрещён.')

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('docsapp:docs_manage')
    else:
        form = DocumentForm()

    docs = Document.objects.all().order_by('-created_at')
    return render(request, 'docsapp/docs_manage.html', {'docs': docs, 'form': form})
