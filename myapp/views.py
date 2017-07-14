from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoBord


def myapp_index(request):
    msg = request.POST.get('words')
    delete_text = request.POST.getlist('delete_text')
    image_file = request.FILES.get('files')

    if delete_text:
        TodoBord.objects.filter(id__in=delete_text).delete()

    if not msg and not image_file:
        data_list = TodoBord.objects.order_by('-id')
        contexts = {
            'result_list': data_list,
        }
        return render(request, 'myapp/index.html', contexts)
    else:
        message_data = TodoBord()
        message_data.new_message = msg
        if image_file:
            message_data.image_url = image_file
        message_data.save()

        data_list = TodoBord.objects.order_by('-id')
        contexts = {
            'result_list': data_list,
        }
        return render(request, 'myapp/index.html', contexts)
