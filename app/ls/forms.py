from django import forms
from .models import Comments

class ContactForm(forms.Form):
    from_name = forms.CharField(label='Имя', required=True)
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)
    
class CommentFormAdd(forms.Form):
    from_name = forms.CharField(label='Имя', required=True)
    from_email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)
