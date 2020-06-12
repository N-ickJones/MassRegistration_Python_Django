# Generated by Django 2.2.13 on 2020-06-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200609_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parish',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='registration.Parishioner', verbose_name='Owner'),
        ),
    ]