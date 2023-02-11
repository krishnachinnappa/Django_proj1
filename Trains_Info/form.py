from django import forms
class train_form(forms.Form):
    train_num = forms.IntegerField()
    train_name = forms.CharField()
    origin_city = forms.CharField()
    destination_city = forms.CharField()
    departure_time = forms.TimeField()
    arrival_time = forms.TimeField()