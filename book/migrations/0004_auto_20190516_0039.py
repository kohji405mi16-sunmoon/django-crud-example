# Generated by Django 2.2.1 on 2019-05-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_isbn10'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn10',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
