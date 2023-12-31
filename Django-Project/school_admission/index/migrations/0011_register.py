# Generated by Django 4.2.2 on 2023-08-15 16:08

from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_alter_tuitionfee_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.IntegerField()),
                ('Ref', models.CharField(max_length=30)),
                ('Photo', models.CharField(max_length=255)),
                ('First_Name_Kh', models.CharField(max_length=255)),
                ('Last_Name_Kh', models.CharField(max_length=255)),
                ('First_Name_En', models.CharField(max_length=255)),
                ('Last_Name_En', models.CharField(max_length=255)),
                ('Village_POB', models.CharField(max_length=255)),
                ('Commune_POB', models.CharField(max_length=255)),
                ('District_POB', models.CharField(max_length=255)),
                ('Province_POB', models.CharField(max_length=255)),
                ('DOB', models.DateField()),
                ('Village_Current', models.CharField(max_length=255)),
                ('Commune_Current', models.CharField(max_length=255)),
                ('District_Current', models.CharField(max_length=255)),
                ('Province_Current', models.CharField(max_length=255)),
                ('Nationality', models.CharField(max_length=255)),
                ('Father_Name', models.CharField(max_length=255)),
                ('Father_Tel', models.CharField(max_length=20)),
                ('Mother_Name', models.CharField(max_length=255)),
                ('Mother_Tel', models.CharField(max_length=20)),
                ('Emergency_Contact_Name', models.CharField(max_length=255)),
                ('Emergency_Contact_Tel', models.CharField(max_length=20)),
                ('Tel', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=100)),
                ('Diploma_Certificate', models.CharField(max_length=255)),
                ('Student_ID', models.CharField(max_length=255)),
                ('Khmer_ID', models.CharField(max_length=255)),
                ('Submit_Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=10, verbose_name=index.models.Status)),
                ('Decided_By', models.CharField(max_length=30, null=True)),
                ('Decided_Date', models.DateTimeField()),
                ('Reason', models.TextField(null=True)),
                ('Apply_For', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.level')),
                ('Emergency_Contact_Relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.relationship')),
                ('Major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.major')),
                ('Marital_Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.married')),
                ('Payment_Method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.payment')),
                ('Sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.sex')),
                ('Shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.shift')),
            ],
        ),
    ]
