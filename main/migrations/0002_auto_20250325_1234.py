from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_page',
            field=models.BooleanField(default=False, help_text='Показувати'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(
                blank=True, 
                null=True, 
                on_delete=django.db.models.deletion.CASCADE, 
                related_name='news', 
                to='main.category', 
                verbose_name='Категорія'
            ),
        ),
    ]
