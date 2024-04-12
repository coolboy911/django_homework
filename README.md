install prerequisition

`pip install django`

---
to start server:

while in django_project_hw directory, type in console `python manage.py runserver`

---

# 2nd homework

all database operations are made using manage.py commands in `django_project_hw/myapp2/management/commands/`

# 3nd homework

to get data on products that client bought recently without duplicating products, enter this url format:

`http://127.0.0.1:8000/orders/<client_id>/<last_week/last_month/last_year>`

example: http://127.0.0.1:8000/orders/1/last_week

# 4th homework

product upload page on `http://127.0.0.1:8000/orders/add_product`  (view and url located in myapp3)

in myapp2 only Product class in models.py was updated
