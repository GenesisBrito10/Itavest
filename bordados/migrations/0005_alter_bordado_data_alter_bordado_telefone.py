# Generated by Django 4.1.13 on 2024-02-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bordados', '0004_alter_bordado_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bordado',
            name='Data',
            field=models.DateTimeField(default='2024-02-02 14:39', editable=False),
        ),
        migrations.AlterField(
            model_name='bordado',
            name='Telefone',
            field=models.CharField(help_text='<span style="font-size: larger;">Não coloque o 9 no inicio</span>', max_length=15),
        ),
    ]
