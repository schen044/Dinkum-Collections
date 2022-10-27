from django.forms import ModelForm
from .models import Fish

class FishForm(ModelForm):
    class Meta:
        model = Fish
        fields = ['name', 'location', 'time_active', 'season', 'price']