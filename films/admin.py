from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
    prepopulated_fields = {'url': ("name",)}

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    prepopulated_fields = {'slug': ("name",)}


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ("movie", "name", "email", "parent", "text")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    list_editable = ("draft",)
    prepopulated_fields = {'url': ("title",)}


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie")
    list_display_links = ("name",)
    readonly_fields = ("movie", "name", "email", "parent", "text")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name",)
    prepopulated_fields = {'url': ("name",)}

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "ip")

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("image", "movie")



admin.site.register(RatingStar)

admin.site.site_title = 'Django Фильмы'
admin.site.site_header = 'Django Фильмы'