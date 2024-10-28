# Generated by Django 5.1 on 2024-10-20 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyberpolygonApp', '0016_remove_correctanswer_answer_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('answer_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cyberpolygonApp.answer')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cyberpolygonApp.question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cyberpolygonApp.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cyberpolygonApp.test'),
        ),
    ]
