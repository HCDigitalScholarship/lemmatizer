from django import forms
from lemmatizer.models import lemmmatizer

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class PostText(forms.ModelForm):
	class Meta:
		model = lemmmatizer
		fields = ['content']

