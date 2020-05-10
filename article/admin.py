from django.contrib import admin
from .models import Article,Tags,Category


admin.site.register(Tags)
admin.site.register(Article)
admin.site.register(Category)
