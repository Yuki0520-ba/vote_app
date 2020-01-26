from django import forms  
from .models import Band,Vote


class BandForm(forms.ModelForm):
    band_name=forms.CharField(widget=forms.TextInput(attrs={'size':30}))
    point=forms.DecimalField()
    order=forms.IntegerField()

    class Meta:
        model=Band
        fields=['band_name','point','order']


class VoteForm(forms.ModelForm):
    count=forms.IntegerField()

    class Meta:
        model=Vote
        fields=['count']


