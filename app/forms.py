from django import forms
from . models import Student

game_choices = [
    ('Batsman','🏏 Batsman'),
    ('Bowler','⚾ Bowler'),
    ('All-Rounder','🎯 All-Rounder')
]

gender_choices = [
    ('Male',"Male"),
    ('Female',"Female"),
    ('Other',"Other"),
]

class studentForm(forms.ModelForm):
    game_type = forms.ChoiceField(choices=game_choices,widget=forms.RadioSelect)
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    class Meta:
        model = Student
        exclude = []
        widgets = {
            'birthdate' : forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'Enter DOB'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full name'}),
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter mobile number'}),
            'game_type' : forms.Select(attrs={'class':'form-control'}),
        }