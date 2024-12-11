from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Schedule, Group
from .forms import TeacherForm, ScheduleForm, GroupForm
# schedules/views.py


# schedules/views.py
def index(request):
    groups = Group.objects.all()  # Получаем все группы
    return render(request, 'schedules/index.html', {'groups': groups})



# Список групп
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'schedules/group_list.html', {'groups': groups})

# Добавление группы
def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'schedules/add_group.html', {'form': form})

# Выбор группы для расписания
def select_group(request):
    groups = Group.objects.all()
    return render(request, 'schedules/select_group.html', {'groups': groups})

# Выбор преподавателя для расписания
def select_teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'schedules/select_teacher.html', {'teachers': teachers})

# Отображение расписания для группы
def group_schedule(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    schedules = Schedule.objects.filter(group=group).order_by('start_time')
    return render(request, 'schedules/group_schedule.html', {'schedules': schedules, 'group': group})

# Отображение расписания для преподавателя
def teacher_schedule(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    schedules = Schedule.objects.filter(teacher=teacher).order_by('start_time')
    return render(request, 'schedules/teacher_schedule.html', {'schedules': schedules, 'teacher': teacher})

def teacher_list(request):
    teachers = Teacher.objects.all()  # Получаем всех учителей
    return render(request, 'schedules/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем учителя в базе данных
            return redirect('teacher_list')  # Перенаправляем на список учителей
    else:
        form = TeacherForm()
    return render(request, 'schedules/add_teacher.html', {'form': form})

def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'schedules/edit_teacher.html', {'form': form})

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'schedules/delete_teacher.html', {'teacher': teacher})
def edit_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'schedules/edit_group.html', {'form': form})

def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'schedules/delete_group.html', {'group': group})
def schedule_list(request):
    group_id = request.GET.get('group_id')  # Получаем выбранную группу из запроса
    if group_id:
        schedules = Schedule.objects.filter(group_id=group_id)  # Фильтруем расписание по группе
    else:
        schedules = Schedule.objects.all()  # Если группа не выбрана, показываем все расписания

    return render(request, 'schedules/schedule_list.html', {'schedules': schedules})
from django.shortcuts import render, redirect
from .models import Schedule
from .forms import ScheduleForm

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем запись в базе данных
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/add_schedule.html', {'form': form})


def edit_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedules/edit_schedule.html', {'form': form})

def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'schedules/delete_schedule.html', {'schedule': schedule})