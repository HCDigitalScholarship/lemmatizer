from django import forms
from django.db import models
from django.core.files.storage import FileSystemStorage


from lemmatizer.models import lemmmatizer

class post_text(forms.Form):
    LATIN = 'latin'
    GREEK = 'greek'
    LANGUAGE_CHOICES = ((LATIN, 'Latin'), (GREEK, 'Greek'))
    language = models.CharField(max_length = 5, choices=LANGUAGE_CHOICES, default=LATIN)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True, storage=FileSystemStorage(location='/tmp/'))
    text = models.TextField(default='')
    ALL = 'all'
    ONLY_UN = 'oun'
    LEVEL_CHOICES = ((ALL,'Lemmatize All Forms'),(ONLY_UN,'Only Unambiguous Forms'))
    lem_level = models.CharField(max_length = 22, choices=LEVEL_CHOICES, default=ALL)
    BRIDGE = 'bridge'
    MORPHEUS = 'morpheus'
    FORMAT_CHOICES = ((BRIDGE, 'Bridge'), (MORPHEUS, 'Morpheus'))
    lem_format = models.CharField(max_length = 8, choices=FORMAT_CHOICES, default=BRIDGE)

class PostText(forms.ModelForm):
	class Meta:
		model = lemmmatizer
		fields = ['file','language','out_format','lem_format']
        labels = {
            'file': None
        }