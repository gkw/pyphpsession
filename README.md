# pyphpsession

How to read session vaiables (string, integer only) 

* python program can read PHP session variabled if we know PHP session id.

Preconditions:

In php.ini
  session.save_path="tcp://127.0.0.1:11211";

My testing environment:
  Ubuntu 12.04 LTS 64bit
  nginx + php5-fpm + flask + uwsgi + memcache
