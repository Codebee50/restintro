# Generated by Django 5.0.7 on 2024-08-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='/defaults/default_book.png', upload_to='book_covers'),
        ),
    ]
