# Generated by Django 4.2 on 2024-03-23 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Street',
                'verbose_name_plural': 'Streets',
            },
        ),
        migrations.CreateModel(
            name='VillageCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('location', models.CharField(blank=True, max_length=512, null=True, verbose_name='Location')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'Village Center',
                'verbose_name_plural': 'Village Centers',
            },
        ),
        migrations.CreateModel(
            name='VillageLetterQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('type', models.CharField(choices=[('HOUSEHOLDER', 'Householder'), ('FAMILY_MEMBER', 'Family member'), ('HOME_INFO', 'Home info'), ('SUGGESTION_PROBLEM', 'Suggestion problem')], max_length=20, verbose_name='Type')),
                ('text_question', models.TextField(verbose_name='Text question')),
            ],
            options={
                'verbose_name': 'Village Letter Question',
                'verbose_name_plural': 'Village Letter Questions',
            },
        ),
        migrations.CreateModel(
            name='WorkerPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Worker Position',
                'verbose_name_plural': 'Worker Positions',
            },
        ),
        migrations.CreateModel(
            name='WorkerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('full_name', models.CharField(max_length=512, verbose_name='Full name')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('phone_numbers', models.CharField(blank=True, max_length=512, null=True, verbose_name='Phone numbers')),
                ('work_times', models.CharField(blank=True, max_length=512, null=True, verbose_name='Working times')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mfy.workerposition', verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Worker Info',
                'verbose_name_plural': 'Worker Information',
            },
        ),
        migrations.CreateModel(
            name='VillageLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('home_number', models.CharField(max_length=256, verbose_name='Home number')),
                ('householder', models.TextField(verbose_name='Householder')),
                ('family_member', models.TextField(verbose_name='Family member')),
                ('home_info', models.TextField(verbose_name='Home info')),
                ('suggestions_problems', models.TextField(verbose_name='Suggestions and problems')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mfy.street', verbose_name='Street')),
            ],
            options={
                'verbose_name': 'Village Letter',
                'verbose_name_plural': 'Village Letters',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswerChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('text', models.TextField(verbose_name='Text')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mfy.villageletterquestions', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Question Answer Choice',
                'verbose_name_plural': 'Question Answer Choices',
            },
        ),
    ]
