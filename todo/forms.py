
from django.forms import ModelForm
from todo.models import Todo


class TODOForm(ModelForm):
    class Meta:
        model=Todo
        fields=['title','status','priority']
      