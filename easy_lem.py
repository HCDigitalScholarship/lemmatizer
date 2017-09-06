import os
path = os.path.dirname(os.path.realpath(__file__))

#Use autoLemma.py to create lemma sheet
def lemmatize(language,filename):
    try: 
    
        os.system('python3 autoLemma.py {0} {1}'.format(language, filename))   
    
        #convert lemma format to Bridge
        os.system('python3 convert_lemmata_format.py {0} import morpheus-bridge.xlsx'.format(language))   

        new_filename = filename.split('.')[0] + '.xlsx'
        
        os.system('python3 convert_lemmata_format.py {0} convert {1} morpheus bridge'.format(language,new_filename))
        
        #clean up spreadsheet for import into bridge
        os.system('python3 format_lemmatized_text.py {0}'.format(new_filename))
        
    except:
        print ('Unable to lemmatize file.')        
lemmatize('latin','latin_text.txt')
