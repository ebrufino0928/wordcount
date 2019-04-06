from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()
    word_count = len(word_list)
    # process entered_text into a word_dictionary list
    # for the purpose of counting occurrence of each word
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sorted_word_dictionary = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'entered_text':entered_text,
                                          'word_count':word_count,
                                          'sorted_word_dictionary':sorted_word_dictionary})

def about(request):
    return render(request, 'about.html')