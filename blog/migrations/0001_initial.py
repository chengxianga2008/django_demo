# Generated by Django 4.0.6 on 2022-08-05 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.author')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('is_published', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
