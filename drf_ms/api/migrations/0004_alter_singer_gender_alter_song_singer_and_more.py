# Generated by Django 4.1.5 on 2023-01-13 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_singer_song_remove_studentinfo_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sungby', to='api.singer'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
