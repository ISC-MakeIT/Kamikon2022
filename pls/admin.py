from django.contrib import admin
from .models import Users,Kadai,KadaiAdmin,KadaiQuestion,SelectInfo,TextInfo,FileInfo,Answer

admin.site.register(Users)
admin.site.register(Kadai)
admin.site.register(KadaiAdmin)
admin.site.register(KadaiQuestion)
admin.site.register(SelectInfo)
admin.site.register(TextInfo)
admin.site.register(FileInfo)
admin.site.register(Answer)
# Register your models here.
