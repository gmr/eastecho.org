Contributing
============

Development Setup
-----------------

Setup the Python development environment and install the dependencies:

```bash
python3.7 -m venv env
source env/bin/activate
python setup.py develop
```

Setup the nodejs environment used to compile JavaScript and Sass:

```bash
npm install
```

Prepare the Django site to be run locally for development:

```bash
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

Compiling static assets (js, css) in development environment:

```bash
npm run-script dev-build
npm run-script dev-sass
```

Running a local web server for development:

```bash
./manage.py runserver
```
