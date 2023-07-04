from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('new_review', views.CreateView.as_view(), name='new_review'),
    path('delete_review/<int:pk>', views.DeleteView.as_view(), name='delete_review'),
    path('edit_review/<int:pk>', views.EditView.as_view(), name='edit_review'),
    path('about', views.about, name='about'),
    path('how_to_use', views.how_to_use, name='how_to_use'),
    # path('contact', views.ContactView.as_view(), name='contact'),
    path('contact', views.contact, name='contact'),
    path('contact_success', views.ContactResultView.as_view(), name='contact_success'),
]
