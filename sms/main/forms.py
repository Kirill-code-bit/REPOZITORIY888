from django import forms
from .models import Attendance, Course, Schedule, GradeForm


class SearchForm(forms.Form):
    query = forms.CharField(label='Search',
                            max_length=100)


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'is_present']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'start_time', 'end_time']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'credits', 'course_type']
