from django.db import models


class Diary(models.Model):
    country = models.CharField(max_length=40, null=False, blank=False)
    text = models.TextField(max_length=2000, null=False, blank=False)
    visit_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.country} ({self.visit_date})'

    class Meta:
        verbose_name_plural = "Diaries"
        verbose_name = "Diary"
