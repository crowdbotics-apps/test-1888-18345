from django.contrib import admin

from home.models.faculty import Faculty
from home.models.schedule import Schedule
from home.models.schedule_day import ScheduleDay
from home.models.schedule_item import ScheduleItem
from home.models.teacher import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Simple admin for Teacher."""

    list_display = (
        'id', 'first_name', 'middle_name', 'last_name', 'teaching_subject', 'created', 'modified'
    )


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    """Simple admin for Faculty."""

    list_display = ('id', 'title', 'active', 'created', 'modified')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Simple admin for Schedule."""

    list_display = ('id', 'title', 'faculty', 'year', 'term', 'education_format', 'created', 'modified')


@admin.register(ScheduleDay)
class ScheduleDayAdmin(admin.ModelAdmin):
    """Simple admin for ScheduleDay."""

    list_display = ('id', 'title', 'date', 'created', 'modified')


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    """Simple admin for ScheduleItem."""

    list_display = ('id', 'title', 'start_time', 'end_time', 'type', 'created', 'modified')
