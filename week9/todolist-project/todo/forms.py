from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text for todo', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))
