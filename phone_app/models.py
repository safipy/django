from django.db import models

class Phone(models.Model):
    MODEL = (
        ("Простые", "Простые"),
        ("Бюджетные", "Бюджетные"),
        ("Высокого класса", "Высокого класса"),
        ("Премиум класса", "Премиум класса"),
        ("Элитные", "Элитные")
    )

    title = models.CharField("Название телефона", max_length=100)
    description = models.TextField("Характеристики", blank=True, null=True)
    image = models.ImageField("Фото", upload_to='')
    video = models.URLField("Трейлер")
    cost = models.PositiveIntegerField("Стоимость")
    model_phone = models.CharField("Модели телефона", max_length=100, choices=MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    phone_choice_comment = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='comment_object')
    name = models.CharField(max_length=50)
    stars = models.CharField(max_length=100, choices=RATING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценка смартфона'





















