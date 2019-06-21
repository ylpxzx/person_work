from django import forms
from .models import Memo
from DjangoUeditor.forms import UEditorField
class MemoForm(forms.ModelForm):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",
                               upload_settings={"imageMaxSize": 120400000},
                               settings={})
    class Meta:
        model=Memo
        fields=(
            'title','content','category','image2'
        )


