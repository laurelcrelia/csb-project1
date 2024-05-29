# FIX 5 (Insufficient Logging & Monitoring):
# The following code logs failed login attempts, after 3 failed attempts happen in a row.
# Failed attempts are logged to the app.log file.

# from django.contrib.auth.signals import user_login_failed, user_logged_in
# from django.dispatch import receiver

# import logging # Python's module 'logging'
# logging.basicConfig(filename='app.log', level=logging.INFO)

# from django.core.cache import cache

# @receiver(user_login_failed)
# def log_failed_login(sender, credentials, **kwargs):
#     username = credentials.get('username')
#     failed_attempts = cache.get(username, 0) + 1

#     if failed_attempts >= 3:
#         logging.warning(f"3 failed login attempts for username: {username}")
#         failed_attempts = 0

#     cache.set(username, failed_attempts, 60*60)  # store the count for 1 hour

# @receiver(user_logged_in)
# def reset_failed_login_count(sender, user, **kwargs):
#     cache.set(user.username, 0, 60*60)  # reset the count
