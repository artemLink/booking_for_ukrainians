from django.contrib import admin
from .models import AddCard

# id int
# title varchar
# descript - varchar
# Content - text
# photo - img
# grade - float
# published - DateTime
class card_admin(admin.ModelAdmin):
    list_display = ['id', 'title','description', 'content', 'photo', 'grade', 'published']
    search_fields = ['id', 'title', 'grade']

admin.register(AddCard, card_admin)
# Register your models here.
