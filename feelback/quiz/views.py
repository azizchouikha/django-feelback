from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Answers, Questions, Title, Orders, Forms
from django.db.models import Avg
from django.utils import timezone


def index(request):
    context = {" ": " "}
    template = loader.get_template("quiz/index.html")
    return HttpResponse(template.render(context, request))


def submitfeedback(request):
    if request.method == 'POST':

        form_instance, created = Forms.objects.get_or_create(
            defaults={'form_name': 'Default Form Name', 'created_at': timezone.now()}
        )
        
        order_name = f"Order at {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}"
        order = Orders(order_name=order_name, form=form_instance)
        order.save()

        questions = Questions.objects.all()

        for question in questions:
            answer_value = request.POST.get(f'question_{question.id}')
            if answer_value:  
                answer = Answers(
                    value=int(answer_value),  
                    question=question
                )
                answer.save()

        return redirect('index') 
    
    else:
        questions = Questions.objects.all()
        return render(request, 'quiz/feedbackform.html', {'questions': questions})

def dashboard(request):
    titles = Title.objects.all()
    questions = Questions.objects.all().order_by('id')
    total_responses = Answers.objects.count() // 3  

    question_stats = []
    for question, title in zip(questions, titles):
        avg_response = Answers.objects.filter(question=question).aggregate(Avg('value'))['value__avg']
        if avg_response is None:
            avg_response = 0  
            
        question_stats.append({
            'title': title.title_name,
            'average': avg_response
        })

    context = {
        'total_responses': total_responses,
        'question_stats': question_stats
    }

    return render(request, "quiz/dashboard.html", context)
