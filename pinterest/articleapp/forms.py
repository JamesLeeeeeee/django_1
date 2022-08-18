from django.forms import ModelForm
from .models import Article

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
