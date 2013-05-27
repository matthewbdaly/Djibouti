# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q


def getSearchResults(request):
    # Get the query data
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    # Query the database
    if query:
        results = Post.objects.filter(Q(text__icontains=query) | Q(title__icontains=query))
    else:
        results = None

    # Add pagination
    pages = Paginator(results, 5)

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display the search results
    return render_to_response('search/post_search_list.html',
                              {'page': returned_page,
                               'posts': returned_page.object_list,
                               'search_query': query})
