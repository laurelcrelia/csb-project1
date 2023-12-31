# Cyber Security Project I
This is a project I for Cyber Security Base 2023 course.
The task was to create a web application that has five different flaws from the OWASP top ten list.

---

## Short description:
This is event countdown timer app. The UI of the app is very basic because it was not the focus of this course. App has a simple authentication. User can register and log in. After successful login, user can create events. One can create an event by giving it a title and date. User’s homepage displays all the events that have been created and shows the remaining time to these events. 

---

## Features: 
- registration
- login
- create a new event
- list of all existing events
- remaining countdown time shown by the event
- delete an event
- logout

---

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

## Security flaws and how to fix them:


### FLAW 1 - Cross-Site Request Forgery (CSRF):
The first flaw is that CSRF protection is not implemented in a form that creates a new event.
By using @csrf_exempt, the createView and deleteEvent in views.py are bypassing CSRF protection.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L47
To fix this, delete the @csrf_exempt so that the ‘create’ and ‘delete’ forms use Django's built-in CSRF protection by including the {% csrf_token %} template tag. Having {% csrf_token %} in the form is a good practice to prevent Cross-Site Request Forgery attacks. In a real-world scenario, using @csrf_exempt is generally discouraged unless there is a valid reason for doing so. Here it is applied only to demonstrate possible security flaws.


### FLAW 2 - Injection (OWASP A1:2017):
Here, the query variable is built by directly initializing the ‘userid’ into the SQL query. The code is vulnerable to SQL injection if ‘userid’ is not appropriately sanitized.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L30

The way to fix this is to use Django ORM to construct the query. ORM stands for Object Relational Mapping and it is an API that Django uses to add, delete, modify and query objects in a more secure way.   
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L37-L44


### FLAW 3 - Cross-Site Scripting (XSS) (OWASP A7:2017)
Third flaw is the cross-site scripting vulnerability. It exists in the ‘create’ form where a user can create a new event. The vulnerability makes it possible to insert malicious inputs like scripts. 
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L56   
Quick fix would be to use the escape() function in the ‘title’ input. It would sanitize the input by altering any special characters in the user’s input string. This would make it safer to render the input in HTML. Although the escape function is a good way to sanitize user input, I chose to use a bit longer formula which adds an additional layer of security. I used a TimerForm approach which exists in the forms.py file. TimerForm uses Django forms that include built-in security features. TimerForm automatically handles security concerns like input validation and sanitization.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L66-L79


### FLAW 4 - Security Misconfiguration (OWASP A6-2017):
In a production environment, it is unsafe to run Django applications in debug mode (DEBUG = True). This mode provides detailed error pages and thus could expose sensitive information to outsiders.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/project1/settings.py#L27  
The fix is very simple. In production settings (settings.py) DEBUG has to be set to False. In addition it would be appropriate to create custom error pages.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/project1/settings.py#L29


### FLAW 5 - Insufficient Logging & Monitoring (OWASP A10-2017):
One of the security flaws is that my app has insufficient logging and monitoring. Attacks might go unnoticed if proper monitoring is not implemented. It would also be convenient to log critical security-related events like failed authentication attempts, access control failures and any other suspicious activity.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L10-L24

To fix this flaw, one could establish different ways to monitor, log and alert application’s events. For example, using Python's logging module or Sentry that integrates with Django and provides detailed error messages. 


---

## Current problems in app logic which I might fix in the future:
- can create an event that has already passed and app shows incorrect countdown
- does not send appropriate error messages (for example when registration fails)
