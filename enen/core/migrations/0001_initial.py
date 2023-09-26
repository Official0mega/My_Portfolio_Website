# Generated by Django 4.2.1 on 2023-05-22 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('specialization', models.CharField(max_length=100)),
                ('passwordHash', models.CharField(max_length=64)),
                ('emailHash', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('contactNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('userId', models.CharField(max_length=8, unique=True)),
                ('passwordHash', models.CharField(max_length=64)),
                ('emailHash', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistanceText', models.CharField(default='', max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('isNew', models.BooleanField(default=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('symptoms', models.CharField(max_length=2000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorRecords', to='core.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientRecords', to='core.patient')),
            ],
        ),
    ]