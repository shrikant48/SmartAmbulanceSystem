# Generated by Django 3.2 on 2022-10-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_auto_20221010_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookambulance',
            name='tambulance',
            field=models.CharField(choices=[('1', 'Basic Ambulance'), ('2', 'Advance Ambulance'), ('3', 'Mortuary Ambulance'), ('4', 'Patient Transport Vehicle'), ('5', 'Air Ambulance')], default='1', max_length=20),
        ),
    ]
