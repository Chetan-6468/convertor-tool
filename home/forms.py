from django import forms

class ConversionForm(forms.Form):
    expression = forms.CharField(label='Infix Expression', max_length=100)
    conversion = forms.ChoiceField(label='Select Conversion', choices=[('postfix', 'Postfix'), ('prefix', 'Prefix')])
