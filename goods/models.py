from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование товара')
    price = models.IntegerField(verbose_name='стоимость товара')
    firm = models.ForeignKey('Firma', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.firm} - {self.category}'


class Firma(models.Model):
    firm_name = models.CharField(max_length=50, verbose_name='Наименование фирмы')
    adress = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.firm_name} - {self.adress}'


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name