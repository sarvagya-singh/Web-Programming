from django.shortcuts import render
from .forms import PromotionForm
from datetime import date

def promotion_view(request):
    eligible = None
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            date_of_joining = form.cleaned_data['date_of_joining']
            today = date.today()
            experience = today.year - date_of_joining.year - ((today.month, today.day) < (date_of_joining.month, date_of_joining.day))
            eligible = "YES" if experience > 5 else "NO"
    else:
        form = PromotionForm()
    return render(request, 'employee_app/employee_form.html', {'form': form, 'eligible': eligible})
