from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from utils import handle_uploaded_file
from lemmatizer.forms import PostText



def lemmatizer(request):
	return render(request,'lemmatizer.html')

def output_page(request):
    return render(request,'lemmatized.html')
#def lemmatize(request):
#	return render(request,'lemmatize.html')
	#return render_to_response('fileupload/upload.html', {'form': c['UploadFileForm']},  RequestContext(request))

 
def lemmatize_text(request):
    if request.method == 'POST':
        form = PostText(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'lemmatized.html')
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'lemmatized.html', {'form': form})

def lemmatize_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('lemmatize.html')
    else:
        form = UploadFileForm()
    return render(request, 'lemmatize.html', {'form': form})

