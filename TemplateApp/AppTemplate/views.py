from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext
from forms import ContactForm
import json


def viewtemplate(request):
    if request.method == 'POST': # If the form has been submitted...
        pass
    else:
        inputvalue = request.GET.get('inputvalue')                
        form = ContactForm({'inputvalue':inputvalue, 'outputvalue':inputvalue })
        
        var_array_tuple = [('a',1), ('e',2), ('b',3), ('d',4), ('c',2)]
        sorted_by_second = sorted(var_array_tuple, key=lambda tup: tup[1],reverse=True)
        string_json = json.dumps(sorted_by_second)
        

    return render(request, 'template.html', {
        'string_json':string_json,
        'form': form,
    })    