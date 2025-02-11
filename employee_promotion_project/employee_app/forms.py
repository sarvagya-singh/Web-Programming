from django import forms
from .models import Employee
from datetime import date

class PromotionForm(forms.Form):
    employee_id = forms.ModelChoiceField(queryset=Employee.objects.all(), label="Employee ID")
    date_of_joining = forms.DateField(label="Date of Joining", widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        date_of_joining = cleaned_data.get('date_of_joining')
        if date_of_joining:
            today = date.today()
            experience = today.year - date_of_joining.year - ((today.month, today.day) < (date_of_joining.month, date_of_joining.day))
            if experience < 0:
                raise forms.ValidationError("Date of Joining cannot be in the future.")
        return cleaned_data
