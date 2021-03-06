# Generated by Django 2.1.7 on 2019-03-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_auto_20190319_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acta',
            name='Asistentes',
            field=models.TextField(help_text='Cada asistente en una línea separada', max_length=200),
        ),
        migrations.AlterField(
            model_name='acta',
            name='Conclusiones',
            field=models.TextField(help_text='Cada conclusión en una línea separada'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='Temas',
            field=models.TextField(help_text='Cada tema en una línea separada', max_length=200),
        ),
    ]
