from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from utils import handle_uploaded_file
from lemmatizer.forms import PostText, post_text
from lemmatizer import easy_lem

#def lemmatizer(request):
#	return render(request,'lemmatizer.html')

#def lemmatized(request):
#    test = "came from func output_page...interesting"
#    return render(request,'lemmatized.html', test='hi')
#def lemmatize(request):
#	return render(request,'lemmatize.html')
	#return render_to_response('fileupload/upload.html', {'form': c['UploadFileForm']},  RequestContext(request))

 
def lemmatizer(request):
    
    if request.method == 'POST':
        form = PostText(request.POST, request.FILES)
        
        if form.is_valid():

            
            form.save(commit=True)

            '''Here is where we call easy_lem.lemmatize()'''

            return render(request, 'lemmatized.html',{'form':form})#,{'test'='hi1'})
        else:
            print(form.errors)
    else:
        form = PostText()
    return render(request, 'lemmatizer.html',{'form':form}) # {'form': form, 'test':'hi2'})

def lemmatize_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('lemmatize.html')
    else:
        form = UploadFileForm()

    return render(request, 'lemmatized.html', {'form': form,test:'hi4'})
    return render(request, 'lemmatize.html', {'form': form})

