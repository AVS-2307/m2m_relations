# Generated by Django 4.1.2 on 2022-10-11 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_category_alter_relations_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relations',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='categories',
        ),
    ]
