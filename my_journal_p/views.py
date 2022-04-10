from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, 'my_journal_p/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request, 'my_journal_p/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'my_journal_p/topic.html', context)

# Create your views here.
