# Generated by Django 3.1.7 on 2021-04-13 13:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(max_length=900, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_before', models.PositiveIntegerField(null=True)),
                ('total_after', models.PositiveIntegerField(null=True)),
                ('percent', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('items', models.ManyToManyField(to='food_shop.Dish')),
            ],
        ),
    ]
