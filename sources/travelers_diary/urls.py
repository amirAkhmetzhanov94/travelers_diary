"""travelers_diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views as webview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webview.IndexView.as_view(), name="index"),
    path('notes-list/', webview.NotesListView.as_view(), name="notes_list"),
    path('notes-details/<int:pk>/', webview.NoteDetailsView.as_view(), name="note_details")
]
