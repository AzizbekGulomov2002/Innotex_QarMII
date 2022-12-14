

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Maqola

'''def main(request):
    if request.method=="POST":
        search = request.GET['qidiruv']
        posts = Maqola.objects.filter(nomi=search)
        return render(request,'blog/search.html',{"posts":posts})
    post = Maqola.objects.all()
    return render(request,'blog/basic.html',{"posts":post})



def post_detail(request,id):
    posts=Maqola.objects.post(id=id)
    posts.kurishlar=posts.kurishlar+1
    posts.save()
    return render(request,'blog/post_detail.html',{"post":posts})'''


class PostListView(ListView):
    model = Maqola
    template_name = 'blog/basic.html'
    context_object_name = "post_list"
    paginate_by = 8


class ProfileSearchView(ListView):
    template_name = 'blog/search.html'
    model = Maqola
    context_object_name = "post_list"

    def get_queryset(self):
        name = self.request.GET.get('search')
        # bu yerda GET requestdan kelgan qidiruv xabari olindi

        if name:
            return self.model.objects.filter(nomi__contains=name)
        else:
            return self.model.objects.all()


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Maqola


class jurnal_haqida(ListView):
    model = Maqola
    template_name = 'blog/jurnal_haqida.html'
    context_object_name = 'jurnal_haqida'


class nizom(ListView):
    model = Maqola
    template_name = 'blog/nizom.html'
    context_object_name = 'nizom'


class tahrir(ListView):
    model = Maqola
    template_name = 'blog/tahrirchi.html'
    context_object_name = 'tahrirchi'


class biz(ListView):
    model = Maqola
    template_name = 'blog/biz.html'
    context_object_name = 'biz'
