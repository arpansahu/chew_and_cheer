from django.contrib.auth import signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, \
    post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # print("----------------------")
    # print("Logged-in Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Request:", request)
    # print("User: ",user)
    # print("User Password", user.password)
    # print(f'kwargs {kwargs}')
    pass


user_logged_in.connect(login_success,sender=User)
@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    # print("----------------------")
    # print("Logged-out Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Request:", request)
    # print("User: ",user)
    # print("User Password", user.password)
    # print(f'kwargs {kwargs}')
    pass


# user_logged_out.connect(logout _success,sender=User)

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    # print("----------------------")
    # print("Login-failed Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Credentials", credentials)
    # print("Request:", request)
    # print(f'kwargs {kwargs}')
    pass


# user_login_failed.connect(login_failed,sender=User)

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    # print("----------------------")
    # print("Pre Save Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Instance", instance)
    # print(f'kwargs {kwargs}')
    pass


# pre_save.connect(at_beginning_save,sender=User)

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    # if created:
    #     print("----------------------")
    #     print("Post Save Signal... Run Intro..")
    #     print("Sender: ",sender)
    #     print("Instance", instance)
    #     print("Created", created)
    #     print(f'kwargs {kwargs}')
    # else:
    #     print("----------------------")
    #     print("Post Save Signal... Run Intro..")
    #     print("Sender: ",sender)
    #     print("Instance", instance)
    #     print("Update", created)
    #     print(f'kwargs {kwargs}')
    pass


# post_save.connect(at_ending_save,sender=User)

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    # print("----------------------")
    # print("Pre Delete Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Instance", instance)
    # print(f'kwargs {kwargs}')
    pass


# pre_delete.connect(at_beginning_delete,sender=User)

@receiver(post_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    # print("----------------------")
    # print("Pre Delete Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Instance", instance)
    # print(f'kwargs {kwargs}')
    pass


# pre_delete.connect(at_beginning_delete,sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    # print("----------------------")
    # print("Post Delete Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Instance", instance)
    # print(f'kwargs {kwargs}')
    pass


# post_delete.connect(at_ending_delete,sender=User)


@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    # print("----------------------")
    # print("Pre Init Signal... Run Intro..")
    # print("Sender: ",sender)
    # print(f'kwargs {args}')
    # print(f'kwargs {kwargs}')
    pass


# pre_init.connect(at_beginning_init,sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    # print("----------------------")
    # print("Post Init Signal... Run Intro..")
    # print("Sender: ",sender)
    # print(f'kwargs {args}')
    # print(f'kwargs {kwargs}')
    pass


# post_init.connect(at_ending_init,sender=User)

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    # print("----------------------")
    # print("Pre Request Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Sender: ",environ)
    # print(f'kwargs {kwargs}')
    pass


# request_started.connect(at_beginning_request,sender=User)

@receiver(request_finished)
def at_starting_request(sender, **kwargs):
    # print("----------------------")
    # print("Post Request Signal... Run Intro..")
    # print("Sender: ",sender)
    # print(f'kwargs {kwargs}')
    pass


# request_finished.connect(at_ending_request,sender=User)

@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    # print("----------------------")
    # print("Post Request Signal... Run Intro..")
    # print("Request: ",request)
    # print(f'kwargs {kwargs}')
    pass


# got_request_exception.connect(at_request_exception)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    # print("----------------------")
    # print("before_install_app Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("App Config: ",app_config)
    # print('Verbosity', verbosity)
    # print("Interactive", interactive)
    # print("Using", using)
    # print("Plan", plan)
    # print("Apps", apps)
    # print(f'kwargs {kwargs}')
    pass


# pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    # print("----------------------")
    # print("at_end_migrate_flush Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("App Config: ",app_config)
    # print('Verbosity', verbosity)
    # print("Interactive", interactive)
    # print("Using", using)
    # print("Plan", plan)
    # print("Apps", apps)
    # print(f'kwargs {kwargs}')
    pass


# post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    # print("----------------------")
    # print("Initial Connection to the database Signal... Run Intro..")
    # print("Sender: ",sender)
    # print("Connection: ",connection)
    # print(f'kwargs {kwargs}')
    pass

# connection_created.connect(conn_db)
