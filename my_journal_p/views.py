from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


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

def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        #данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        #Отправлены данные ПОСТ, обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_journal_p:topics')

    #вывести пустую форму или недействительную
    context = {'form': form}
    return render(request, 'my_journal_p/new_topic.html', context)


def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        """Данные не отправлялись, создается пустая форма"""
        form = EntryForm()
    else:
        """Отправлены данные POST; обработать данные"""
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('my_journal_p:topic', topic_id=topic_id)

        #вывести пуустую строку или недействительную форму

    context = {'topic' : topic, 'form' : form}
    return render(request, 'my_journal_p/new_entry.html', context)


def edit_entry(request, entry_id):
    """Редактирует существующую запись"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        #Исходный запрос, форма заполняется данными текущей записи
        form = EntryForm(instance=entry)
    else:
        #Отправка данных POST, обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_journal_p:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'my_journal_p/edit_entry.html', context)
# Create your views here.
