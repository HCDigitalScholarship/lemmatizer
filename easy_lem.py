import os
path = os.path.dirname(os.path.realpath(__file__))

def lemmatize(language,filename,format):
    try: 
    
        os.system('python3 autoLemma.py {0} {1}'.format(language, filename))   
    
        #convert lemma format to Bridge
        if language == 'latin':
            os.system('python3 convert_lemmata_format.py {0} import morpheus-bridge.xlsx'.format(language))   
        elif language == 'greek':
            os.system('python3 convert_lemmata_format.py {0} import Convert-bridge-morpheus-greek.xlsx'.format(language))   

        new_filename = filename.split('.')[0] + '.xlsx'
        if format == 'bridge':
            os.system('python3 convert_lemmata_format.py {0} convert {1} morpheus bridge'.format(language,new_filename))
            os.system('python3 format_lemmatized_text.py {0}'.format(new_filename))

        else:
            pass
         
    except:
        print ('Unable to lemmatize file.')        
lemmatize('greek','greek_text.txt','bridge')
