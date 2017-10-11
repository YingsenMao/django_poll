#!c:\users\daniemao\documents\django_tutorial\django_poll\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django==1.11.6','console_scripts','django-admin'
__requires__ = 'django==1.11.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('django==1.11.6', 'console_scripts', 'django-admin')()
    )
