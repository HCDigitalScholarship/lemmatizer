import os
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from django.core.files.base import ContentFile
from utils import handle_uploaded_file
from lemmatizer.forms import PostText, post_text
from lemmatizer import easy_lem
import tempfile
from django.utils.encoding import smart_str


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
            
            #class is InMemoryUploadedFile
            with tempfile.NamedTemporaryFile(suffix='.txt', dir='/tmp/', delete=True) as f:
                
                #write the uploaded file to a temporary file on the server in /tmp
                f.write(form['file'].value().read())

                #TODO: Handle data from textfield
                #f.write(form['text'].value().read())
                #with .read() gives'unicode' object has no attribute 'read'
                #without gives 'ascii' codec can't encode character u'\u2014' in position 182: ordinal not in range(128)


                #language, filename and format variables from form to pass to easy_lem
                language = str(form['language'].value())

                filename = f.name

                lem_format = str(form['lem_format'].value()) 
            
                #pass variables to lemmatize function and Bret's scripts
                print (language,filename,lem_format)
                easy_lem.lemmatize(language,filename,lem_format)

                #uncomment to save form data to db
                #form.save(commit=True)

                #Here we send the output file to lemmatized.html (tmpEDoVlX_Input.xlsx)
                if lem_format == 'bridge':
                    output_file = str(f.name).split('.')[0] + '_Input.xlsx'
                    output_file = output_file.split('/')[2]

                elif lem_format == 'morpheus':
                    output_file = str(f.name).split('.')[0] + '.xlsx'
                    output_file = output_file.split('/')[2]


            return render(request, 'lemmatized.html',{'form':form, 'output_file':output_file})#,{'test'='hi1'})
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

