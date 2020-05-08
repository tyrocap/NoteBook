# Generated by Django 3.0.5 on 2020-05-04 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BOOK', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note_date', models.DateTimeField(auto_now_add=True)),
                ('note_body', models.TextField(max_length=255)),
                ('note_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BOOK.Book')),
                ('note_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]