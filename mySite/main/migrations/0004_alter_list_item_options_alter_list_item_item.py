# Generated by Django 4.2.3 on 2023-08-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_list_item_delete_goal_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list_item',
            options={'verbose_name_plural': 'items'},
        ),
        migrations.AlterField(
            model_name='list_item',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]