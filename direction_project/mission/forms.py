from django import forms
from mission.models import Finished

class FinishedForm(forms.ModelForm):
    class Meta:
        model = Finished
        fields = ('img', )
