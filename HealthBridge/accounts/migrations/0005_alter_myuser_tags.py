# Generated by Django 4.2.3 on 2023-07-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_alter_post_tags'),
        ('accounts', '0004_alter_myuser_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Post.tag'),
        ),
    ]
