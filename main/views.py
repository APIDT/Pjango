from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView, ListView, DateDetailView
from main.models import Article
from main.models import Category

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# app_blog/views.py
# class MainPageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)


class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        try:
            context['images'] = context['item'].images.all()
        except Exception:
            pass
        return context


class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        try:
            context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        except Exception:
            context['category'] = None
        return context

    def get_queryset(self, *args, **kwargs):
        return Article.objects.all()


class ArticleCategoryList(ArticleList):
    def get_queryset(self, *args, **kwargs):
        return Article.objects.filter(category__slug__in=[self.kwargs['slug']]).distinct()


class MainPageView(ListView): 
    model = Article
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:5]
        return context

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()
