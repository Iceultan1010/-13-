from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Тақырыбы')),
                ('content', models.TextField(verbose_name='Мазмұны')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='notes',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Авторы'
                )),
            ],
            options={
                'verbose_name': 'Жазба',
                'verbose_name_plural': 'Жазбалар',
                'ordering': ['-created_at'],
            },
        ),
    ]
