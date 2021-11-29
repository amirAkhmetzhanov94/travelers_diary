from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from webapp.models import Diary


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class NotesListView(View):
    def get(self, request, *args, **kwargs):
        notes = Diary.objects.all().order_by("-create_time")
        notes_markup = map(lambda note: render_to_string("note.html", {"note": note}), notes)
        return JsonResponse({"notes": list(notes_markup)})

    def post(self, request, *args, **kwargs):
        country = request.POST.get("country")
        visit_date = request.POST.get("visit_date")
        text = request.POST.get("text")
        new_note = Diary.objects.create(country=country, visit_date=visit_date, text=text)
        note_markup = render_to_string("note.html", {"note": new_note})
        return JsonResponse({"note": note_markup, "status": "created"})