from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='advertisements')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('status', models.CharField(
                    choices=[('NEW', 'NEW'), ('IN PROGRESS', 'IN PROGRESS'),
                             ('CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLETED')], default='NEW',
                    max_length=15)),
                ('receipted_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('response_time', models.DateTimeField(null=True)),
                ('was_notified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('image', models.ImageField(upload_to='profits')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Профит',
                'verbose_name_plural': 'Профит',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='services')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='sites')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('PROCESSED', 'PROCESSED')],
                                            default='NEW', max_length=10)),
                ('receipted_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('response_time', models.DateTimeField(null=True)),
                ('was_notified', models.BooleanField(default=False)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='services', to='code.service')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
            },
        ),
    ]
