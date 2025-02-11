from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea, label="Address")
    contact_number = forms.CharField(max_length=15, label="Contact Number")
    email_id = forms.EmailField(label="Email ID")
    english_marks = forms.IntegerField(label="English Marks")
    physics_marks = forms.IntegerField(label="Physics Marks")
    chemistry_marks = forms.IntegerField(label="Chemistry Marks")
