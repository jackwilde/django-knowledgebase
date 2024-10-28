from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, DetailView, UpdateView, ListView
from .forms import ArticleForm
from .models import Article


# Create your views here.
class DashboardView(ListView):
    template_name = 'kbase/dashboard.html'
    login_url = reverse_lazy('sign-in')
    model = Article
    context_object_name = 'articles'


class NewArticleView(CreateView):
    template_name = 'kbase/new.html'
    form_class = ArticleForm
    model = Article
    success_url = reverse_lazy(viewname='dashboard') #TODO change to created article
    next_page = reverse_lazy(viewname='dashboard') #TODO change to created article

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super().form_valid(form)


class ArticleView(DetailView):
    template_name = 'kbase/article.html'
    model = Article
    context_object_name = 'article'



class EditArticleView(UpdateView):
    model = Article
    fields = ['title', 'category', 'content']
    template_name = 'kbase/edit.html'