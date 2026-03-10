from django.contrib import admin
from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")  # 管理画面で一覧に表示
    list_filter = ("created_at", "user")           # 絞り込み可能
    search_fields = ("title", "description")       # 検索可能