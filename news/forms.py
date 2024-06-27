from .models import News

from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class NewsForm(ModelForm):
    class Meta:
         model = News
         fields = '__all__'
         widgets = {
             "title": TextInput(attrs={'class': 'text-form',
                                       'placeholder': 'Название статьи'}),
             'content': Textarea(attrs={'class': 'text-form', 'placeholder': 'Введите текст'}),
             'date': DateTimeInput(attrs={'class': 'text-form', 'type': 'date'})
         }