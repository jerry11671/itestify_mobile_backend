# Generated by Django 4.2.19 on 2025-03-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.CharField(default='8486f1', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
