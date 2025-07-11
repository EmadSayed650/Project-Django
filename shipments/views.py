from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Shipment
from .forms import ShipmentForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipments/shipment_list.html', {'shipments': shipments})

@login_required
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.created_by = request.user
            shipment.status = 'pending' 
            shipment.save()
            return redirect('shipments:shipment_list')
    else:
        form = ShipmentForm()
    return render(request, 'shipments/add_shipment.html', {'form': form})

@login_required
def confirm_shipment(request, shipment_id):
    if request.user.role == 'manager':
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.status = 'confirmed'
        shipment.save()
    return redirect('shipments:shipment_list')

@login_required
def edit_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Shipment updated successfully.')
            return redirect('shipments:shipment_list')
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipments/edit_shipment.html', {'form': form})

