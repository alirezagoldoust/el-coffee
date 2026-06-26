from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField(help_text='قیمت به تومان')
    ingredients = models.TextField()
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False, help_text='پیشنهاد ویژه')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'آیتم منو'
        verbose_name_plural = 'آیتم‌های منو'

    def __str__(self):
        return self.title

    def formatted_price(self):
        return f'{self.price:,}'
