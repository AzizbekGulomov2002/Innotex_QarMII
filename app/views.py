from django.shortcuts import render


from app.models import Maqola
from .models import Maqola

def main(request):
    if request.method=="POST":
        search = request.GET['qidiruv']
        posts = Maqola.objects.filter(nomi=search)
        return render(request,'blog/search.html',{"posts":posts})
    post = Maqola.objects.all()
    return render(request,'blog/basic.html',{"posts":post})



# def post_detail(request,id):
#     posts=Maqola.objects.post(id=id)
#     posts.kurishlar=posts.kurishlar+1
#     posts.save()
#     return render(request,'blog/post_detail.html',{"post":posts})



from django.views.generic import DetailView

class post_detail(DetailView):
    template_name = 'blog/post_detail.html'
    model = Maqola



