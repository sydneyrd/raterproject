# Generated by Django 4.0.6 on 2022-08-03 18:59

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('designer', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('number_of_players', models.IntegerField()),
                ('time', models.IntegerField()),
                ('age_rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=400)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='raterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=250)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='GameRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='raterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
            ],
        ),
    ]