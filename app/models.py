from django.db import models



class Maqola(models.Model):
    nomi = models.CharField(max_length=200, help_text='Maqola nomini kiriting.....')
    rasm = models.ImageField(upload_to='post_image')
    maqola_soni = models.CharField(max_length=100,help_text='Maqola sonini kiriting.....')
    batafsil = models.TextField(help_text="Maqola haqida umumiy ma'lumot")
    sana = models.DateTimeField(auto_now_add=True)
    kurishlar = models.IntegerField(default=1)

    def __str__(self):
        return self.nomi


    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
