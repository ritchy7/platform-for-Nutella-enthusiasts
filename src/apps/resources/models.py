from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    """
    Category model.
    """
    name = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model.
    """
    product_name = models.CharField(max_length=400)
    code = models.CharField(max_length=30)
    img_url = models.CharField(max_length=400, blank=True, null=True)
    url = models.CharField(max_length=400, blank=True, null=True)
    salt = models.CharField(max_length=10, blank=True, null=True)
    fat = models.CharField(max_length=10, blank=True, null=True)
    sugars = models.CharField(max_length=10, blank=True, null=True)
    saturated_fat = models.CharField(max_length=10, blank=True, null=True)
    warehouse = models.CharField(max_length=400, blank=True, null=True)
    allergens = models.CharField(max_length=400, blank=True, null=True)
    nutrition_grades = models.CharField(max_length=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    @classmethod
    def get_substitutes(cls, product_id):
        """
        Get a list of better products than the one chosen.

        Parameters
        ----------
        product_id : int
            Product identifier.

        Returns
        -------
        products: list
            List of products that can replace the selected product.
        """
        # Get products from a category sorted by nutrition grades.
        category_id = int(cls.objects.get(pk=product_id).category.id)
        products = cls.objects\
            .filter(category=category_id)\
            .exclude(id=product_id)\
            .order_by("nutrition_grades")[:12]
        return products


class BackupProduct(models.Model):
    """
    History model.
    """
    product_code = models.CharField(max_length=30)
    category_name = models.CharField(max_length=400)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.product_code
