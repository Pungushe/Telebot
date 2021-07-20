from django.db import models


class SmpSlider(models.Model):
    smp_img = models.ImageField(upload_to='sliderimg/')
    smp_title = models.CharField(max_length=200, verbose_name='Заголовок')
    smp_text = models.CharField(max_length=200, verbose_name='Текст')
    smp_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.smp_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
