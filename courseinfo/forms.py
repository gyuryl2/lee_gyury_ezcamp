from django import forms
from courseinfo.models import Counselor, Cabin, Course, Session, Camper, Registration


class CounselorForm(forms.ModelForm):
    class Meta:
        model = Counselor
        fields= '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class CabinForm(forms.ModelForm):
    class Meta:
        model = Cabin
        fields= '__all__'

    def clean_cabin_name(self):
        return self.cleaned_data['cabin_name'].strip()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields= '__all__'

    def clean_course_number(self):
        return self.cleaned_data['course_number'].strip()

    def clean_course_name(self):
        return self.cleaned_data['course_name'].strip()


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields= '__all__'


class CamperForm(forms.ModelForm):
    class Meta:
        model = Camper
        fields= '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields= '__all__'