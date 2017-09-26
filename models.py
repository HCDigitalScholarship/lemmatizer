from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.

class lemmmatizer(models.Model):
	LATIN = 'latin'
	GREEK = 'greek'
	LANGUAGE_CHOICES = ((LATIN, 'Latin'), (GREEK, 'Greek'))

	language = models.CharField(max_length = 5, choices=LANGUAGE_CHOICES, default=LATIN)
	
	created_at = models.DateTimeField(auto_now_add=True)

	file = models.FileField(blank=True, storage=FileSystemStorage(location='/tmp/lematizer_temp_file.txt'))
	
	text = models.TextField(default='', blank=True)

	ALL = 'all'
	ONLY_UN = 'oun'
	LEVEL_CHOICES = ((ALL,'Lemmatize All Forms'),(ONLY_UN,'Only Unambiguous Forms'))

	lem_level = models.CharField(max_length = 22, choices=LEVEL_CHOICES, default=ALL)

	BRIDGE = 'bridge'
	MORPHEUS = 'morpheus'
	FORMAT_CHOICES = ((BRIDGE, 'Bridge'), (MORPHEUS, 'Morpheus'))

	lem_format = models.CharField(max_length = 8, choices=FORMAT_CHOICES, default=BRIDGE)

	CSV = 'csv'
	EXCEL = 'Excel'
	FORMAT_CHOICES = ((CSV, 'csv'), (EXCEL, 'Excel'))

	out_format = models.CharField(max_length = 5, choices=FORMAT_CHOICES, default=CSV)
    


    # i would think you would add something about the language here... 
    # later on if lemmatizer.language == 'latin': is asked   
