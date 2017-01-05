project=$(pwd)
run:
	python $(project)manage.py runserver

migrate:
	python $(project)manage.py migrate

makemigrations:
	python $(project)manage.py makemigrations

createsuperuser:
	python $(project)manage.py createsuperuser

shell:
	python $(project)manage.py shell
