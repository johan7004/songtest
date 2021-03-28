from django.shortcuts import render
from .models import Songs
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import SongsSerializer


# Create your views here.
# def home(request):
#   songs = Songs.objects.all()
#  return render(request, 'index.html', {'songs': songs})


def home(request):
    template_name = 'index.html'

    query = request.GET.get('search')
    if query:
        # query example
        songs = Songs.objects.filter(title__icontains=query)
    else:
        songs = []
    return render(
        request, template_name, {'songs': songs})
    
    
class lyricsview(DetailView):
    model = Songs
    template_name = 'lyric-detail.html'
    context_object_name ='song'
  
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        post = Songs.objects.filter(slug=self.kwargs.get('slug'))
        context['time'] = timezone.now()
        
        return context

@api_view(['GET', 'POST'])
def lyrics_list(request):
    if request.method == 'GET':
        data = Songs.objects.all()

        serializer = SongsSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

