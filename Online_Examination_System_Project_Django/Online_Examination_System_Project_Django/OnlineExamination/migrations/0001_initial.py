

import OnlineExamination.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('no_of_ques', models.CharField(max_length=20)),
                ('total_marks', models.CharField(max_length=20)),
                ('time_duration', models.DurationField(default='00:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('marks', models.PositiveIntegerField(default=0)),
                ('question', models.TextField(max_length=500)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(choices=[('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4')], max_length=1)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.Exams')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the define format', regex='^\\+?1?\\d{9,12}$')])),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=OnlineExamination.models.upload_image, width_field='width_field')),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('stream', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
