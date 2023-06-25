from django.shortcuts import render, HttpResponse
from hello.prefix import infix_to_prefix
from hello.postfix import infix_to_postfix


from hello.prefix import convert_to_prefix
from hello.postfix import convert_to_postfix

from home.forms import ConversionForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')



# def convert_expression(request):
#     if request.method == 'POST':
#         expression = request.POST['expression']
#         conversion_type = request.POST['conversion']
#         if conversion_type == 'postfix':
#             converted_expression = infix_to_postfix(expression)

#         elif conversion_type == 'prefix':
#             converted_expression = infix_to_prefix(expression)

#         else:
#             converted_expression = ''  # Handle invalid conversion type here
        
#         return render(request, 'index.html', {'converted_expression': converted_expression})
    
#     return render(request, 'index.html')
def convert_expression(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            conversion_type = form.cleaned_data['conversion']
            if conversion_type == 'postfix':
                converted_expression = convert_to_postfix(expression)
            elif conversion_type == 'prefix':
                converted_expression = convert_to_prefix(expression)
            else:
                converted_expression = ''  # Handle invalid conversion type here
            
            return render(request, 'index.html', {'form': form, 'converted_expression': converted_expression})
    else:
        form = ConversionForm()

    return render(request, 'index.html', {'form': form})