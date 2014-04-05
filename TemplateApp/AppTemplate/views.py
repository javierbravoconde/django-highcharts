from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template import RequestContext
from forms import ContactForm
import json


def viewtemplate(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            inputvalue = form.cleaned_data['inputvalue']
            form = ContactForm({'inputvalue':inputvalue, 'outputvalue':inputvalue })
            
            
    else:
        inputvalue = request.GET.get('inputvalue')                
        form = ContactForm({'inputvalue':inputvalue, 'outputvalue':inputvalue })
        
        var_array_tuple = [('a',1), ('b',2)]
        string_json = json.dumps(var_array_tuple)
        

    return render(request, 'template.html', {
        'string_json':string_json,
        'form': form,
    })    