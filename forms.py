from django import forms

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_id = forms.EmailField()
    mobile_no = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})  # This ensures the browser renders a date picker
    )
    address = forms.CharField(widget=forms.Textarea)
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    skills = forms.MultipleChoiceField(
        choices=[
            ('AWS', 'AWS'),
            ('DevOps', 'DevOps'),
            ('QA-Automation', 'QA-Automation'),
            ('Full Stack Developer', 'Full Stack Developer'),
            ('WebServices', 'WebServices'),
        ],
        widget=forms.CheckboxSelectMultiple
    )
