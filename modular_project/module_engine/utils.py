from django.urls import path, include
from .models import Module

def get_active_module_urls():
    urls = []
    for module in Module.objects.filter(status='installed'):
        try:
            urls.append(path(f'{module.name}/', include(f'{module.name}.urls')))
        except ModuleNotFoundError:
            print(f"Module {module.name} not found or has no urls.py")
    return urls
