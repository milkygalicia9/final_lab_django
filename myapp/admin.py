from django.contrib import admin
from .models import (
    Author,
    Book,
    Publisher,
    Magazine,
    Reader,
    Review,
    
)


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Magazine)
admin.site.register(Reader)
admin.site.register(Review)

