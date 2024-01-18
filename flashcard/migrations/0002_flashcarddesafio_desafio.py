# Generated by Django 5.0.1 on 2024-01-18 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashcardDesafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondido', models.BooleanField(default=False)),
                ('acertou', models.BooleanField(default=False)),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='flashcard.flashcard')),
            ],
        ),
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('quantidade_perguntas', models.IntegerField()),
                ('dificuldade', models.CharField(choices=[('D', 'Difícil'), ('M', 'Médio'), ('F', 'Fácil')], max_length=1)),
                ('categoria', models.ManyToManyField(to='flashcard.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('flashcards', models.ManyToManyField(to='flashcard.flashcarddesafio')),
            ],
        ),
    ]
