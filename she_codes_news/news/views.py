from django.views import generic
from .models import NewsStory #you import classes from models.py, classes are tables in the database
from django.urls import reverse_lazy
from .forms import StoryForm 
#from django.contrib.auth.decorators import login_required



class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        #ordering by date
        context['user_stories'] = NewsStory.objects.order_by('author')
        #ordering by author, author with pk=1 will show first
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

#@login_required
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
        
# class SortStoryView(generic.DetailView):
#     model = NewsStory
#     template_name = 'news/sort.html'
#     context_object_name = 'sort'
