#!/usr/bin/env python
from __future__ import absolute_import, print_function
import os
import sys



    



if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweetstock.settings')
        
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
   
   
    
  
  
    



