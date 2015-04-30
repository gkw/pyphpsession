# pyphpsession

How to read session vaiables (string, integer) Not intended for class or any complex data structure.
Preconditions:

In php.ini
  session.save_path="tcp://127.0.0.1:11211";

Testing environment:
  Ubuntu 12.04 LTS 64bit
  nginx + php5-fpm + flask + uwsgi
