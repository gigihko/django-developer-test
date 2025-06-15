from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseNotAllowed

def group_required(*group_names):
    def in_groups(user):
        return user.is_authenticated and user.groups.filter(name__in=group_names).exists()
    return user_passes_test(in_groups)

@group_required('manager', 'user', 'public')
def product_list(request):
    products = Product.objects.all()
    user_groups = request.user.groups.values_list('name', flat=True)
    user_group = user_groups[0] if user_groups else 'public'
    return render(request, 'example_module/product_list.html', {
        'products': products,
        'user_group': user_group,
    })

@group_required('manager', 'user')
def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'example_module/product_form.html', {'form': form})

@group_required('manager', 'user')
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'example_module/product_form.html', {'form': form})

@group_required('manager')
def product_delete(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product_list')
    return HttpResponseNotAllowed(['POST'])

