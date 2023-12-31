from django.contrib import admin
from django.urls import path
from store.Views.login import login
from store.Views.tech_form import AddPatient, SearchPatient, Logoutview, UploadView
from store.Views.dashboard import Dashboard
from store.Views.UpdatePatient import UpdatePatient, DeletePatient


urlpatterns = [
    path('', login.as_view(), name='login'),
    path('dashboard', Dashboard.as_view(), name="dashboard"),
    path('form', AddPatient.as_view(), name="form"),
    path('update_patient/<int:customer_id>/', UpdatePatient.as_view(), name='update_patient'),
    path('delete_patient/<int:customer_id>/', DeletePatient.as_view(), name='delete_patient'),
    path('search', SearchPatient.as_view(), name='search'),
    path('logout', Logoutview.as_view(), name='logout' ),
    path('upload', UploadView.as_view(), name='upload' )


]
