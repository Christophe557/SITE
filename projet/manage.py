#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')

    ############ AFFICHAGE DU PYTHONPATH ET DES VARIABLES D'ENVIRONNEMENT #############

    print(" --- PYTHON PATH ---")
    for path in sys.path:
        print(f' -> {path}')
    print(" -------------------")
    print()

    print(f" --- Variables d'environnement: {len(os.environ)} ---")
    for key, val in os.environ.items():
        print(f' -> {key :.<30} : {val[:80]}', '...'*(len(val) > 80))
    print(" ---------------------------------")
    print()
    ###################################################################################

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
