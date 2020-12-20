
def run_django():
    import sys
    sys.dont_write_bytecode = True

    # Django specific settings
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    import django
    django.setup()