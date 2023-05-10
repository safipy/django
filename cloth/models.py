from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=100, verbose_name="Surname")
    last_name = models.CharField(max_length=100, verbose_name="Name", blank=True)
    phone = models.CharField(max_length=100, verbose_name="Number")
    email = models.EmailField(verbose_name="mail", blank=True)

    def __srt__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("На обработке", "На обработке"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.product.name
