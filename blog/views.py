# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from blog.models import Post, Category
from django.contrib.syndication.views import Feed

def getCategory(request, slug, page=1):
    # Get specified category
    posts = Post.objects.filter(categories__slug__contains=slug)

    # Paginate it
    pages = Paginator(posts, 5)

    # Get category
    category = Category.objects.filter(slug=slug)[0]

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the posts
    return render_to_response('blog/category.html', {'posts': returned_page.object_list, 'page': returned_page, 'category': category})


class PostsFeed(Feed):
    title = "My blog posts"
    link = "feeds/posts/"
    description = "Posts from my blog"

    def items(self):
        return Post.objects[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
