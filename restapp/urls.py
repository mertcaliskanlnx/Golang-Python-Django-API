from django.urls import path

from restapp.views import MovieItemViews


urlpatterns = [
    #anasayfa
    path('movie-items/',MovieItemViews.as_view()),
    #movie id yönlendirme
    path('movie-items/<int:id>',MovieItemViews.as_view())
]
