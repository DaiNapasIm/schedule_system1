# schedules/forms.py
from django import forms
from .models import Schedule
from .models import Teacher, Group, Room

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']  # Поля, которые вы хотите использовать в форме
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']

class GroupChoiceForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']  # Выберите поле, которое будет отображаться
from django import forms
from .models import Schedule
from django.core.exceptions import ValidationError

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['subject', 'teacher', 'group', 'start_time', 'end_time', 'room']

    def clean_start_time(self):
        start_time = self.cleaned_data['start_time']
        if start_time.weekday() >= 5:  # 5 - суббота, 6 - воскресенье
            raise ValidationError("Выбранная дата является выходным днем. Пожалуйста, выберите будний день.")
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data['end_time']
        if end_time.weekday() >= 5:  # 5 - суббота, 6 - воскресенье
            raise ValidationError("Выбранная дата является выходным днем. Пожалуйста, выберите будний день.")
        return end_time

