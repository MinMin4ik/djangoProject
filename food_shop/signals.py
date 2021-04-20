from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from food_shop.models import Kit
from food_shop.models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def create_kit(instance, **kwargs):
    if kwargs["action"] == 'post_add':
        if instance.items.count() < 2:
            raise ValidationError(f'You cant assign less than two regions, now {instance.items.count()}')
    total = 0
    for item in instance.items.all():
        total += item.price
    instance.total_before = total

    instance.total_after = total * (total * instance.percent) / 100
    instance.total_before = total
    instance.save()

    instance.save()


m2m_changed.connect(create_kit, sender=Kit.items.through)

##########################################################################################################
def save(self, *args, **kwargs):
    discount = self.discount
    price = self.price
    if discount > 0:
      recount_of_discount = (discount / 100)
      print(recount_of_discount)
      multiplay_sum_on_coef = float(price) * float(recount_of_discount)
      print(multiplay_sum_on_coef)
      from_sum_minus_percent = float(price) - float(multiplay_sum_on_coef)
      print (float(from_sum_minus_percent))
    super(Product, self).save(*args, **kwargs)