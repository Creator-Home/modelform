# Generated by Django 3.2.6 on 2021-08-14 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0005_auto_20210814_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classrecord',
            name='collegename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='college_set', to='modelform.collegerecord'),
        ),
    ]