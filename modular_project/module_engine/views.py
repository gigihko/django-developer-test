from django.shortcuts import render, redirect, get_object_or_404
from .models import Module
from django.utils import timezone
from django.core.management import call_command
import os

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_engine/module_list.html', {'modules': modules})

def install_module(request, module_name):
    module = get_object_or_404(Module, name=module_name)
    module.status = 'installed'
    module.installed_at = timezone.now()
    module.save()
    os.utime('manage.py', None)
    return redirect('module_list')

def uninstall_module(request, module_name):
    module = get_object_or_404(Module, name=module_name)
    module.status = 'not_installed'
    module.save()
    os.utime('manage.py', None)
    return redirect('module_list')

def upgrade_module(request, module_name):
    try:
        call_command('makemigrations', module_name)
        call_command('migrate', module_name)
    except Exception as e:
        print(f"Error upgrading module: {e}")
    return redirect('module_list')
