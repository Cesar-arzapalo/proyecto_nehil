from django.contrib import admin
from django.urls import path

from django.contrib import admin

from disenioNehil import views as local
from posts import views as views_post

from usuarios import views as users_view
from pagina import views as pagina_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('angel/',local.hola_mundo,name='hora'),
    path('posts/',views_post.list_p),
    path('users/login', users_view.login_view , name = 'login'),
    path('users/logout', users_view.logout_view , name = 'logout'),
    path('pagina/', pagina_view.principal, name='pagina'),
    path('users/signup', users_view.signup, name='signup'),
    path('users/signup1', users_view.signup1, name='signup1'),
    path('users/signup2', users_view.signup2, name='signup2'),
]
