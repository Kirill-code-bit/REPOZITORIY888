from django import forms
from .models import Attendance, Score, Course, Schedule, Grade


class SearchForm(forms.Form):
    query = forms.CharField(label='Search',
                            max_length=100)


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'is_present']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'numeric_score', 'date']


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student', 'course', 'date', 'numeric_score']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'start_time', 'end_time']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'credits', 'course_type']
