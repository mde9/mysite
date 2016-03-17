from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Film, CSchedue
from django.template import loader
from django.http import Http404
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'films/index.html'
    context_object_name = 'latest_film_list'

    def get_queryset(self):
        """Return the last five published films."""
        return Film.objects.order_by('-pub_date')
    
class DetailView(generic.DetailView):
    model = Film
    template_name = 'films/detail.html'

       
class ResultsView(generic.DetailView):
    model = Film
    template_name = 'films/results.html'

def reservation(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    try:
        selected_cschedue = film.cschedue_set.get(pk=request.POST['cschedue'])
    except (KeyError, CSchedue.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'films/detail.html', {
            'film': film,
            'error_message': "You didn't select a reservation.",
        })
    else:
        selected_cschedue.reserved_places += 1
        selected_cschedue.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('films:results', args=(film.id,)))
 
# Create your views here.
