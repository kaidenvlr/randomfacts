from django.db import models


class Fact(models.Model):
    fact_title = models.TextField(verbose_name='Факт')

    def __str__(self):
        return self.fact_title

    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факты"
