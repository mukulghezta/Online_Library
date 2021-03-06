# Generated by Django 3.0.1 on 2021-02-21 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_cds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDReserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('cd_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books_cds.CD')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookReserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('book_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books_cds.Book')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
