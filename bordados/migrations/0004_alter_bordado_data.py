# Generated by Django 4.1.13 on 2024-02-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bordados', '0003_alter_bordado_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bordado',
            name='Data',
            field=models.DateTimeField(default='2024-02-02 14:01', editable=False),
        ),
    ]
