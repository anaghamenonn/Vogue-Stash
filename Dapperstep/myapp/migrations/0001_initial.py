# Generated by Django 4.2.7 on 2024-01-12 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category')),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=200, null=True, unique=True)),
                ('Password', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='unknown', max_length=100)),
                ('img', models.ImageField(null=True, upload_to='product')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('desc', models.TextField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('available', models.BooleanField(blank=True, default=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
