from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    CMname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
        label=""
    )
    CMemail=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}),
        label="")
    CMsubject=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
        label="")
    CMmessage = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message'}),
        label=""
    )
    class Meta:
        model = ContactMessage
        fields = ['CMname', 'CMemail', 'CMsubject', 'CMmessage']
