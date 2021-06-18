# Generated by Django 3.2.3 on 2021-06-18 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        #ロール生成
        migrations.RunSQL('CREATE ROLE tenantuser;', reverse_sql='DROP ROLE tenantuser;'),
        #データアクセス
        migrations.RunSQL('''
            GRANT select, insert, delete ON django_session TO tenantuser;
            GRANT select, insert ON django_admin_log TO tenantuser;
            GRANT select, insert ON django_content_type TO tenantuser;
            GRANT select, insert ON auth_group TO tenantuser;
            GRANT select, insert ON auth_permission TO tenantuser;
        ''',
        reverse_sql='''
            REVOKE select, insert, delete ON django_session FROM tenantuser;
            REVOKE select, insert ON django_admin_log FROM tenantuser;
            REVOKE select, insert ON django_content_type FROM tenantuser;
            REVOKE select, insert ON auth_group FROM tenantuser;
            REVOKE select, insert ON auth_permission FROM tenantuser;
        ''')
    ]