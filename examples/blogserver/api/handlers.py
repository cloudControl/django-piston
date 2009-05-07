from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc

from blogserver.blog.models import Blogpost

class AnonymousBlogpostHandler(AnonymousBaseHandler):
    model = Blogpost
    fields = ('title', 'content', 'created_on')

class BlogpostHandler(BaseHandler):
    model = Blogpost
    anonymous = AnonymousBlogpostHandler
    fields = ('title', 'content', ('author', ('username',)), 
              'created_on', 'content_length')
    
    def content_length(self, blogpost):
        return len(blogpost.content)
        
    def create(self, request):
        if request.content_type:
            print request.data
            return { 'foo': 42 }

        attrs = self.flatten_dict(request.POST)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            post = Blogpost(title=attrs['title'], 
                            content=attrs['content'],
                            author=request.user)
            post.save()
            
            return post
        