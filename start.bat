@echo on
cd ..
call venv_ecommerce_design\Scripts\activate.bat
cd ecommerce-design\src
python manage.py runserver 0.0.0.0:8005
start http://localhost:8005