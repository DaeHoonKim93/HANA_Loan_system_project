from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label="제목")
    contents = forms.CharField(widget=forms.Textarea, label="내용")
