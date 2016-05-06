
from blog.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

            
def blog_list(request):
    blogs = Blog.objects.all().order_by('-publish_time')
                
    return render_to_response('index.html', {"blogs": blogs}, context_instance=RequestContext(request))
def blog_lists(request):
    blogs = Blog.objects.all().order_by('-publish_time')
                
    return render_to_response('bloglist.html', {"blogs": blogs}, context_instance=RequestContext(request))
def blog_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id', '');
        try:
            blog =Blog.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404
        return render_to_response("detail.html", {"blog": blog}, context_instance=RequestContext(request))
    else:
        raise Http404

def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    return render_to_response("blog_filter.html",
        {"blogs": blogs, "tag": tag, "tags": tags})

