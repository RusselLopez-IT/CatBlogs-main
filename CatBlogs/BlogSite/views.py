from django.shortcuts import get_object_or_404, render, redirect
from BlogSite.models import Cat
from django.http import Http404
from UserAuth.models import Article, Comment, Like
from .forms import ArticleForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def index(request):
    cats = Cat.objects.order_by('?')[:3]
    top_blog = Article.objects.order_by('-num_views').first() 
    recent_blogs = Article.objects.exclude(pk=top_blog.pk) if top_blog else Article.objects.order_by('-date_published')[:9]

    context = {
        'cats': cats,
        'recent_blogs': recent_blogs,
        'top_blog': top_blog
    }
    return render(request, 'extensions/index.html', context)

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article_id=article.id) 
    else:
        form = ArticleForm()
    
    return render(request, 'extensions/createblogs.html', {'form': form})



def article_detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.num_views += 1
        article.save()

        comments = Comment.objects.filter(article=article).order_by('-timestamp')

        context = {
            'article': article,
            'comments': comments,
        }

        return render(request, 'extensions/blog_detail.html', context)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")


@login_required
def like_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = request.user

    already_liked = Like.objects.filter(user=user, article=article).first()

    if already_liked:
        already_liked.delete()
        article.num_likes -= 1
        is_liked = False
    else:
        Like.objects.create(user=user, article=article)
        article.num_likes += 1
        is_liked = True

    article.save()

    response_data = {
        'num_likes': article.num_likes,
        'is_liked': is_liked,
    }
    return JsonResponse(response_data)


@login_required
def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment.objects.create(article=article, user=request.user, content=content)
    if comment:
            article.num_comments += 1
            article.save()    
    
    return redirect('article_detail', article_id=article.id)

def catBreeds(request):
     cats = Cat.objects.all()
     return render(request, 'extensions/cats.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    cats = Cat.objects.all()
    return render(request, 'extensions/cat_details.html', {'cat': cat, 'others': cats})

def blogs(request):
    blogs = Article.objects.all()
    return render(request, 'extensions/blogs.html', {'blogs': blogs})
