# Generated by Django 5.0.4 on 2024-09-05 07:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('info', models.TextField(default='Default info text', help_text="Company's info")),
            ],
            options={
                'db_table': 'about_info_table',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('name', models.TextField(help_text="Author's name")),
                ('surname', models.TextField(help_text="Author's surname")),
            ],
            options={
                'db_table': 'authors_table',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('name', models.TextField(help_text="Genre's name", unique=True)),
            ],
            options={
                'db_table': 'genres_table',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CompanyPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('link', models.TextField(help_text="Companie's web site")),
                ('image', models.ImageField(help_text="Companie's logo", upload_to='app/static/partners')),
            ],
            options={
                'db_table': 'partner_companies_table',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('name', models.CharField(help_text='Name', max_length=50)),
                ('phone', models.CharField(help_text='Phone number', max_length=13, unique=True)),
                ('email', models.EmailField(help_text='Email', max_length=254, unique=True)),
                ('password', models.CharField(help_text='Password', max_length=300)),
            ],
            options={
                'db_table': 'customers_table',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('name', models.CharField(help_text='Name', max_length=50)),
                ('phone', models.CharField(help_text='Phone number', max_length=13, unique=True)),
                ('email', models.EmailField(help_text='Email', max_length=254, unique=True)),
                ('password', models.CharField(help_text='Password', max_length=300)),
                ('is_admin', models.BooleanField(help_text='Admin\\Employee')),
            ],
            options={
                'db_table': 'employees_table',
                'ordering': ['-is_admin', 'name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('title', models.CharField(help_text='News title', max_length=50)),
                ('text', models.TextField(help_text='News summary')),
                ('img', models.ImageField(help_text='News photo', upload_to='app/static/news')),
            ],
            options={
                'db_table': 'news_table',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('question', models.TextField(help_text='Question')),
                ('answer', models.TextField(help_text='Answer')),
            ],
            options={
                'db_table': 'qa_table',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SaleCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('code', models.CharField(help_text='Sale code', max_length=50)),
                ('is_active', models.BooleanField(help_text='Is code active')),
            ],
            options={
                'db_table': 'sale_codes_table',
                'ordering': ['is_active', 'code'],
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('name', models.CharField(help_text="Vacancy's name", max_length=50)),
                ('description', models.TextField(help_text="Vacancy's description")),
            ],
            options={
                'db_table': 'vacancies_table',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('title', models.TextField(help_text="Book's title")),
                ('price', models.FloatField(help_text="Book's price")),
                ('amount', models.PositiveIntegerField(help_text='Amount of copies in the shop')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
                ('genre', models.ForeignKey(default='Роман', on_delete=django.db.models.deletion.SET_DEFAULT, to='app.bookgenre')),
            ],
            options={
                'db_table': 'books_table',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('rate', models.PositiveSmallIntegerField(help_text='Rate (0-5)')),
                ('text', models.TextField(help_text="Review's text")),
                ('user', models.ForeignKey(help_text='Reviewer', on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
            options={
                'db_table': 'customer_reviews_table',
                'ordering': ['rate'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('img', models.ImageField(help_text='Employees photo', upload_to='app/static/info')),
                ('description', models.TextField(help_text='Employees work description')),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
            options={
                'db_table': 'employees_info_table',
                'ordering': ['employee_id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
            options={
                'db_table': 'orders_table',
                'ordering': ['customer_id'],
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('status', models.CharField(default='0', help_text="Order's status", max_length=1)),
                ('sale', models.PositiveSmallIntegerField(default=0, help_text="Order's sale")),
                ('delivery_date', models.DateTimeField(help_text='Delivery date & time')),
                ('delivery_address', models.TextField(default='Minsk, ', help_text='Delivery address')),
                ('order_price', models.FloatField(help_text="Order's price")),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
            options={
                'db_table': 'orders_info_table',
                'ordering': ['delivery_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('quantity', models.PositiveIntegerField(default=1, help_text='Quantity of books in the order')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
            options={
                'db_table': 'order_items_table',
                'unique_together': {('order', 'book')},
            },
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ManyToManyField(help_text='Goods list', related_name='orders', through='app.OrderItem', to='app.book'),
        ),
    ]