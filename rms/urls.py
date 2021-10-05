from django.urls import include, path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = [

	path('', views.ma, name='ma'),
    path('engine/', views.ai_search, name='engine'),
    path('rms/', views.index, name='rms'),
    path('report/', views.download_file, name='report'),
    path('doc/', views.doc_insight, name='doc'),
    path('cv/', views.cv_insight, name='cv'),
    path('media/', views.media_check, name='media_check'),
    path('loletter/', views.LOutgoingLetter.as_view(), name='loletter'),
    path('liletter/', views.LIcomingLetter.as_view(), name='liletter'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage-files/<int:pk>', views.crudAdmin.found, name='found'),
    path('save-data/', views.save_data, name='save_data'),
    path('letter/', views.save_letter, name='save_letter'),
    path('addfile/', views.add_file, name='addfile'),
    path('addletter/', views.add_letter, name='addletter'),
    path('save_file/', views.save_file, name='savefile'),
    path('outletter/', views.out_letter, name='outletter'),
    path('search/', views.search_ai, name='search'),
    path('usearch/', views.usearch, name='usearch'),
    path('sentletter/', views.outing_letter, name='sentletter'),
    path('manage-files/', views.ManageFileView.as_view(), name='manage_files'),
    path('search/', views.search_view, name='search'),
    path('lsearch/', views.search_letter, name='search_letter'),
    path('test/', views.test, name='test'),
    path('r_admin_list/<int:pk>/update_file/', views.update_file, name='update_file'),
    path('list-files/', views.FileListView.as_view(), name='list_file'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('r_admin_list/<int:pk>', views.AdminListReadView.as_view(), name='r_admin_list'),
    path('al_update/<int:pk>', views.AlUpdateView.as_view(), name='al_update'),
    path('u_update/<int:pk>', views.UserUpdateView.as_view(), name='u_update'),
    path('admin_list_delete/<int:pk>', views.ListItDeleteView.as_view(), name='admin_list_delete'),
    path('delete_user/<int:pk>', views.DeleteUserView.as_view(), name='delete_user'),
    path('users/', views.UserView.as_view(), name='users'),
    path('r_admin_truck/<int:pk>', views.AListTruckReadView.as_view(), name='r_admin_truck'),
    path('login/', auth_views.LoginView.as_view(template_name='crow/login.html'), name='login'),



]
