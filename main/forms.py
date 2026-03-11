from django import forms
from django.core.validators import RegexValidator
from .models import AdmissionApplication, ContactForm

class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'additional_notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'pincode': 'PIN Code',
            'previous_school': 'Previous School',
            'grade_applying_for': 'Grade Applying For',
            'parent_name': "Parent's/Guardian's Name",
            'parent_occupation': "Parent's/Guardian's Occupation",
            'parent_email': "Parent's/Guardian's Email",
            'parent_phone': "Parent's/Guardian's Phone",
            'additional_notes': 'Additional Notes',
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }

class AdmissionForm(forms.Form):
    # Student Information
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'})
    )
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'})
    )

    # Contact Information
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    phone = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': 'required'})
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    pincode = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{6}$', 'Enter a valid 6-digit PIN code.')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )

    # Academic Information
    previous_school = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    grade_applying_for = forms.ChoiceField(
        choices=[
            ('Nursery', 'Nursery'),
            ('LKG', 'LKG'),
            ('UKG', 'UKG'),
            ('1', 'Grade 1'),
            ('2', 'Grade 2'),
            ('3', 'Grade 3'),
            ('4', 'Grade 4'),
            ('5', 'Grade 5'),
            ('6', 'Grade 6'),
            ('7', 'Grade 7'),
            ('8', 'Grade 8'),
            ('9', 'Grade 9'),
            ('10', 'Grade 10'),
            ('11', 'Grade 11'),
            ('12', 'Grade 12'),
        ],
        widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'})
    )

    # Parent/Guardian Information
    parent_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    parent_occupation = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    parent_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    parent_phone = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'})
    )

    # Additional Information
    additional_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    ) 