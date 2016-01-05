# Check to see if User model has any records yet and invoke
# initial database population script if it doesn't.  It only
# checks to see if the 'anonymous' user has been added to the
# User model's table yet.

import sys,os
import django
from django.core.exceptions import ObjectDoesNotExist
from os.path import join, abspath, dirname


sys.path.append(abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fae2.settings')
from django.conf import settings

django.setup()

from django.contrib.auth.models import User


print("\nChecking if database needs to be populated...")

if not User.objects.filter(username='anonymous').exists():
  print("    invoking database population\n\n")
  populate_path = join(abspath(dirname(__file__)),'..','populate')
  saved_path = os.getcwd()
  os.chdir(populate_path)
  sys.path.append(populate_path)
  import pop_all
  os.chdir(saved_path)
  print("\n\n    database population complete")
else:
  print("    already populated")

print("")
