# Generated by Django 4.2.19 on 2025-03-01 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('A', 'Avancado'), ('i', 'Intermediario'), ('B', 'Basico')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
