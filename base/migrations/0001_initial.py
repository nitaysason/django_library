# Generated by Django 5.0.1 on 2024-02-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.DecimalField(decimal_places=2, max_digits=5)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
