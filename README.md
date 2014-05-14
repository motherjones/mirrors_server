# Mirrors

It's some kind of content store.

## Requirements

- Python 3
- Postgres 9.2+
- Some python packages:
 - Django
 - South
 - django-jsonfield
 - psycopg2
 - Sphinx

If you want to have an easier time of it just run `pip install -r
requirements/apps.txt`. In the future we'll probably make some kind of automated
environment setup.

## Running

Settings file is currently one size fits all and set to mirrors in postgres.
We should improve this

    $ python ./manage.py syncdb
      [...]
    $ python ./manage.py migrate

## Tests
To run the tests just do this:

    $ coverage run --source='.' --omit='*migrations*' manage.py test

Run this to get a plain text coverage report:

    $ coverage report

Run this to get an HTML coverage report:

    $ coverage html
