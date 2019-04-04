from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

import django_tables2 as tables
from django_tables2.paginators import  LazyPaginator
from django_tables2 import RequestConfig
# Create your views here.
from .models import Post,PostTable,Product
from .filters  import ProductFilter


def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,"blog/home.html",context)



def about(request):
    return render(request,"blog/about.html",{'title':'about'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TableView(tables.SingleTableView):
    table_class = PostTable
    queryset = Post.objects.all()
    paginator_class = LazyPaginator
    template_name = "blog/post_list.html"


def tab(request):
    table = PostTable(Post.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'blog/post_table.html', {'table': table})



# class MyFormView(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    # template_name = 'form_template.html'
# 
    # def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
# 
    # def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        # if form.is_valid():
            # # <process form cleaned data>
            # return HttpResponseRedirect('/success/')
# 
        # return render(request, self.template_name, {'form': form})

def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'blog/filter.html', {'filter': f})