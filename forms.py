from django import forms
from lemmatizer.models import lem_model

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class PostText(forms.ModelForm):
	class Meta:
		model = lem_model
		fields = ['title', 'content']

