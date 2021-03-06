# Generated by Django 3.0.4 on 2020-03-26 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название приложения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания на сайте')),
            ],
            options={
                'verbose_name': 'Приложения',
                'verbose_name_plural': 'Приложение',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Компания')),
                ('destination', models.CharField(max_length=100, verbose_name='Расположение')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название элемента')),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название паттерна')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(db_index=True, default=0, verbose_name='Номер версии')),
                ('published', models.DateField(blank=True, null=True, verbose_name='Дата релиза')),
                ('description', models.TextField(verbose_name='Описание изменений')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Application', verbose_name='Приложение')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название экрана')),
                ('main', models.BooleanField(db_index=True, default=False, verbose_name='Главный экран')),
                ('screen', models.ImageField(blank=True, upload_to='', verbose_name='Снимок экрана')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Version', verbose_name='Приложение')),
                ('elements', models.ManyToManyField(to='main.Element', verbose_name='Элементы')),
                ('pattern', models.ManyToManyField(to='main.Pattern', verbose_name='Паттерн')),
            ],
            options={
                'verbose_name': 'Экран приложения',
                'verbose_name_plural': 'Экраны приложений',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='categories',
            field=models.ManyToManyField(to='main.Category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='application',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Developer', verbose_name='Разработчик'),
        ),
    ]
