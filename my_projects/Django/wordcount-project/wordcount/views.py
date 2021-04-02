from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    word_count_dictionary = {}
    
    wordlist = fulltext.split()

    word_count_dictionary
    
    for word in wordlist:
        if word in word_count_dictionary:
            #Increase
            word_count_dictionary[word] += 1
        
        else:
            #add to the dictionary 
            word_count_dictionary[word] = 1

            sortedwords = sorted(word_count_dictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render (request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
