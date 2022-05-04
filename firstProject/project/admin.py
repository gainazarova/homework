from django.contrib import admin

from project.models import Person, Musician, Album

admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)

from project.models import Students, Teacher, Group, GroupStudents
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Group)
admin.site.register(GroupStudents)


