from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Order, Response
from django.utils import timezone
from django.db.models import Avg


def index(request):
    context = {" ": " "}
    template = loader.get_template("quiz/index.html")
    return HttpResponse(template.render(context, request))

def dashboard(request):
    context = {" ": " "}
    template = loader.get_template("quiz/dashboard.html")
    return HttpResponse(template.render(context, request))

def feedbackform(request):
    context = {" ": " "}
    template = loader.get_template("quiz/feedbackform.html")
    return HttpResponse(template.render(context, request))


def submitfeedback(request):
    if request.method == 'POST':
        new_order = Order(order_name="Order at " + timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
        new_order.save()
        
        new_response = Response(
            order=new_order,
            delivery_time_rating=request.POST.get('delivery_time_rating'),
            package_condition_rating=request.POST.get('package_condition_rating'),
            courier_behavior_rating=request.POST.get('courier_behavior_rating'),
            created_at=timezone.now()
        )
        new_response.save()
        
        return redirect('index')
    else:
        template = loader.get_template("quiz/feedbackform.html")
        return HttpResponse(template.render(request))


def dashboard(request):
    responses = Response.objects.all()
    
    if responses.exists():
        total_responses = responses.count()
        avg_delivery_time = responses.aggregate(Avg('delivery_time_rating'))['delivery_time_rating__avg']
        avg_package_condition = responses.aggregate(Avg('package_condition_rating'))['package_condition_rating__avg']
        avg_courier_behavior = responses.aggregate(Avg('courier_behavior_rating'))['courier_behavior_rating__avg']
    else:
        total_responses = 0
        avg_delivery_time = 0
        avg_package_condition = 0
        avg_courier_behavior = 0

    context = {
        'total_responses': total_responses,
        'avg_delivery_time': avg_delivery_time,
        'avg_package_condition': avg_package_condition,
        'avg_courier_behavior': avg_courier_behavior
    }

    template = loader.get_template("quiz/dashboard.html")
    return HttpResponse(template.render(context, request))
