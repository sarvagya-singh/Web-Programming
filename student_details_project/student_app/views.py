from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']
            email_id = form.cleaned_data['email_id']
            english_marks = form.cleaned_data['english_marks']
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']

            total_marks = english_marks + physics_marks + chemistry_marks
            percentage = (total_marks / 300) * 100

            student_details = f"""
                Name: {name}
                Date of Birth: {date_of_birth}
                Address: {address}
                Contact Number: {contact_number}
                Email ID: {email_id}
                English Marks: {english_marks}
                Physics Marks: {physics_marks}
                Chemistry Marks: {chemistry_marks}
                """

            return render(request, 'student_app/student_form.html', {
                'form': form,
                'student_details': student_details,
                'percentage': round(percentage, 2)
            })
    else:
        form = StudentForm()
    return render(request, 'student_app/student_form.html', {'form': form})
