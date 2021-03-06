# Generated by Django 3.0.5 on 2020-05-07 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BOOK', '0003_book_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment_text', models.TextField(blank=True, null=True)),
                ('comment_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BOOK.Book')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
