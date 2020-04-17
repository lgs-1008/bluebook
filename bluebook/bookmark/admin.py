from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

#admin.site.register(Bookmark, BookmarkAdmin)
#만약 위에 @를 안 쓸 시 위 주석처럼 사용가능. @는 데코레이터. 이와 같이 테이블을 새로 만들 시 모델파이와 어드민파이를 같이 수정해야함.
