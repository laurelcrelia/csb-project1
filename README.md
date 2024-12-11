# :lock: Cyber Security Project I

This repository contains Project I for the [Cyber Security Base](https://cybersecuritybase.mooc.fi/) 2023 course. The goal of the project was to develop a web application that intentionally includes five different security vulnerabilities from the OWASP [Top Ten list](https://owasp.org/www-project-top-ten/).

The application is an event countdown timer. While the app’s user interface is kept basic, this aligns with the course's focus on demonstrating and understanding security flaws.

## :books: What I learned
- understanding common security vulnerabilities from the OWASP Top Ten list.
- best practices for securing web applications
- identifying potential security risks in code

### Technologies
- Python
- Django
- HTML

## 🔗 [Features](documentation/features.md)
## 🔗 [Installation](documentation/instructions.md)

---

## :bomb: Intentional Security Flaws

Here is the description and fix for each security flaw that was included in the code.


### FLAW 1 - Cross-Site Request Forgery (CSRF):
The first flaw is that CSRF protection is not implemented in a form that creates a new event.
By using @csrf_exempt, the createView and deleteEvent in views.py are bypassing CSRF protection.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L47
To fix this, delete the @csrf_exempt so that the ‘create’ and ‘delete’ forms use Django's built-in CSRF protection by including the {% csrf_token %} template tag. Having {% csrf_token %} in the form is a good practice to prevent Cross-Site Request Forgery attacks. In a real-world scenario, using @csrf_exempt is generally discouraged unless there is a valid reason for doing so. Here it is applied only to demonstrate possible security flaws.


### FLAW 2 - Injection (OWASP A1:2017):
Here, the query variable is built by directly initializing the ‘userid’ into the SQL query. The code is vulnerable to SQL injection if ‘userid’ is not appropriately sanitized.  
https://github.com/laurelcrelia/csb-project1/blob/1f48329b42fb315149830b376429a2f21158af34/countdown_app/views.py#L13-L14

The way to fix this is to use Django ORM to construct the query. ORM stands for Object Relational Mapping and it is an API that Django uses to add, delete, modify and query objects in a more secure way.   
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/countdown_app/views.py#L37-L44


### FLAW 3 - Cross-Site Scripting (XSS) (OWASP A7:2017)
Third flaw is the cross-site scripting vulnerability. In templates/index.html there is a template filter ‘safe’ that marks a string as safe for rendering, meaning it won't be auto-escaped. The vulnerability makes it possible to insert malicious inputs like HTML or Javascript scripts into the title, which would then be executed when the page is rendered.
https://github.com/laurelcrelia/csb-project1/blob/bd52954721ace609c39199d5617fe7233349b990/countdown_app/templates/index.html#L17
Fix for this is simple, just remove the filter to let Django's templating engine to auto-escape.
https://github.com/laurelcrelia/csb-project1/blob/bd52954721ace609c39199d5617fe7233349b990/countdown_app/templates/index.html#L18-L19


### FLAW 4 - Security Misconfiguration (OWASP A6-2017):
In a production environment, it is unsafe to run Django applications in debug mode (DEBUG = True). This mode provides detailed error pages and thus could expose sensitive information to outsiders.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/project1/settings.py#L27  
The fix is very simple. In production settings (settings.py) DEBUG has to be set to False. In addition it would be appropriate to create custom error pages.  
https://github.com/laurelcrelia/csb-project1/blob/79b2f1e9173db2a038bb2a0113b1989118dff504/project1/settings.py#L29


### FLAW 5 - Insufficient Logging & Monitoring (OWASP A10-2017):
One of the security flaws is that my app has insufficient logging and monitoring. Attacks might go unnoticed if proper monitoring is not implemented. It would also be convenient to log critical security-related events like failed authentication attempts, access control failures and any other suspicious activity.  
To fix this flaw, one could establish different ways to monitor, log and alert application’s events. For example, using Python's logging module to catch malicious login attempts. The proposed code logs failed login attempts, after 3 failed attempts happen in a row:
https://github.com/laurelcrelia/csb-project1/blob/174f52620d3e4cf0f9e2e6ed8097d30b84d8d6c7/countdown_app/signals.py#L1-L26


---

## Current problems in app logic which I might fix in the future:
- can create an event that has already passed and app shows incorrect countdown
- does not send appropriate error messages (for example when registration fails)
