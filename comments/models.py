from django.db import models

# Create your models here.
class Reviews(models.Model):
    email=models.EmailField()
    name=models.CharField('Имя',max_length=100)
    text=models.TextField('Сообщение',max_length=5000)
    parent=models.ForeignKey(
        'self',verbose_name='review',on_delete=models.SET_NULL,blank=True,null=True
    )
    order_id = models.PositiveIntegerField(default=1)     # whose review
    def __str__(self):
        return f"{self.name}-{self.id}"

    def get_reviews(self):
        return self.objects.filter(parent=Null)

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'