# Generated by Django 5.0 on 2024-01-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_genre_alter_book_created_at_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(
                to='myapp.genre',
                on_delete=models.SET_NULL,
                null=True,
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]