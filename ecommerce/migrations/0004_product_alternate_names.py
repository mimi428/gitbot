# Generated by Django 5.1.1 on 2024-12-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_chathistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alternate_names',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]