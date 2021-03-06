# Generated by Django 3.2.6 on 2021-08-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_blog', '0002_auto_20210816_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_image',
            field=models.ImageField(default='categories_images/SmartCheap.png', upload_to='topic_title_image/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='body',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
    ]
