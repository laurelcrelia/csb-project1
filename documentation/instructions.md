## Installation instructions:
(You can skip 1. and 2. if you already have Python 3 and Django libraries installed)
1. Install [Python3](https://www.python.org/downloads/) (3.5 or higher).

2. Install the following packages using pip:  
```python3 -m pip install django "selenium<4" "urllib3<2" beautifulsoup4 requests```

3. Clone this repository into your computer:  
```git clone https://github.com/laurelcrelia/csb-project1.git```    

4. Apply database migrations to create the necessary database tables:  
```python3 manage.py migrate```    

5. Start the Django development server:  
```python manage.py runserver```    

6. To access the running Django app, open a web browser, and go to the server in which it will run on.

---
