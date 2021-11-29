from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from webapp.models import Diary


class IndexView(View):
    def get(self, request, *args, **kwargs):
        print(Diary.objects.all())
        return render(request, "index.html")


class NotesListView(View):
    def get(self, request, *args, **kwargs):
        notes = Diary.objects.all()
        notes_markup = map(lambda note: render_to_string("note.html", {"note": note}), notes)
        return JsonResponse({"notes": list(notes_markup)})
