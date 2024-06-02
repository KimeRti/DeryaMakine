from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import add_watermark

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='category')
    slug = models.SlugField(max_length=160, unique=True)
    status = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'categories'
        ordering = ['order']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    def get_descendants(self, include_self=True):
        descendants = []
        nodes = [self]
        if include_self:
            descendants.append(self)
        while nodes:
            node = nodes.pop(0)
            children = list(node.children.all())
            descendants.extend(children)
            nodes.extend(children)
        return descendants


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    titleEN = models.CharField(max_length=150, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='product')
    price = models.FloatField()
    amount = models.IntegerField()
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

            for i in range(len(breadcrumb) - 1):
                breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
            return breadcrumb[-1:0:-1]
    
    def get_image_url(self):
        return self.image.url


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='product')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Product)
def add_watermark_to_product_image(sender, instance, **kwargs):
    if instance.image:
        input_image_path = instance.image.path
        watermark_image_path = 'img/derya_logo.png'  # Filigran resminin yolu
        output_image_path = instance.image.path  # Aynı dosyayı yeniden kaydediyoruz
        add_watermark(input_image_path, watermark_image_path, output_image_path, 'center', transparency=0.5, size=(300, 300))

@receiver(post_save, sender=ProductImage)
def add_watermark_to_product_image(sender, instance, **kwargs):
    if instance.image:
        input_image_path = instance.image.path
        watermark_image_path = 'img/derya_logo.png'  # Filigran resminin yolu
        output_image_path = instance.image.path  # Aynı dosyayı yeniden kaydediyoruz
        add_watermark(input_image_path, watermark_image_path, output_image_path, 'center', transparency=0.5, size=(300, 300))
