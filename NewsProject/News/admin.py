from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at',  'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ('is_published', 'category')
    fields = ('title', 'content', 'photo', 'get_photo', 'created_at', 'updated_at', 'is_published')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src=" {obj.photo.url}" width="75">')
        else:
            return '<p>Нет фото</p>'

    get_photo.description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title= 'Страница администратора'
admin.site.site_header = 'Страница администратора'


