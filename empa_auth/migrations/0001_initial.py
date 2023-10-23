# Generated by Django 4.2.6 on 2023-10-23 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('primer_nombre', models.CharField(max_length=45)),
                ('segundo_nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('primer_apellido', models.CharField(max_length=45)),
                ('segundo_apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=9)),
                ('telefono', models.CharField(max_length=120)),
                ('correo', models.CharField(max_length=120, null=True)),
                ('n_identificacion', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('ciudad_nacimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='persona_nacimiento', to='core.ciudad')),
                ('ciudad_residencia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='persona_residencia', to='core.ciudad')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('tipo_identificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoidentificacion')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'persona',
                'managed': True,
            },
        ),
    ]