# Generated by Django 5.0.1 on 2024-02-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_librarian_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='image',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
    ]