from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def index_view(request):
	# Renderiza el index
	return render_to_response('index.html', context=RequestContext(request))
