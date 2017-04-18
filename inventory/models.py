from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#-------------PARANO--------------------
class Parano(models.Model):
    created_by = models.ForeignKey(
        'Member',
        verbose_name="Créé par",
        related_name="%(app_label)s_%(class)s_creator",
        null=True,
        blank=True,
    )
    modified_by = models.ForeignKey(
        'Member',
        verbose_name="Modifié par",
        related_name="%(app_label)s_%(class)s_modificator",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Créé le",
        null=True,
        blank=True,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name="Modifié le",
        null=True,
        blank=True,
        auto_now=True
    )
    class Meta:
        abstract = True
        app_label = "inventory"
        
#-----------------MEMBER-----------------
class Member(models.Model):
    user = models.OneToOneField(
        User,
        related_name="member" #facultatif dans un OneToOneField puisque fait direct le lien symétrique
    )
    class Meta:
        app_label="inventory"
        ordering=["user__date_joined"]

    def __str__(self):
        return str(self.user.username)


#-------------PRODUCT-----------------
class Product(Parano, models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name="Name",
        null=True,
        blank=False
    )

    brand = models.CharField(
        max_length=60,
        verbose_name="Brand",
        null=True,
        blank=True
    )

    gender_choices = (
        ('Men', 'Men'),
        ('Women', 'Women')
    )
    gender = models.CharField(
        max_length=20, 
        choices=gender_choices,
        null=True
    )

    type_choices = (
         ('Pant', 'Pant'),
         ('Shirt', 'Shirt'),
         ('Dress', 'Dress'),
         ('Shoes', 'Shoes')
    )
    type = models.CharField(
        max_length=50, 
        choices=type_choices,
        null=True
    )

    quantity = models.IntegerField(
        null = True,
        blank = False,
        verbose_name = "Quantity"
    )
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )

    # stock = models.BooleanField(
    #     verbose_name="En stock ?",
    #     default=False,
    #     blank=True
    # )

    class Meta:
        app_label = "inventory"
        #ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    #def disponible(self):
    #    return False


    def get_absolute_url(self):
        return '/'+str(self.id)+'/'
    #     return reverse_lazy('inventory:tasks:retrieve', kwargs={'pk': self.id})