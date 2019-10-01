setup:
	npm install

build:
	python3 setup.py sdist -d docker/dist
	npm run build
	npm run sass
	cp -R eastecho/site/static docker/
	cp -R eastecho/site/templates docker/
	docker build -t eastecho:latest docker
	docker build -t eastecho-nginx:latest docker/nginx

init:
	@ cd docker && docker-compose up -d memcached postgres
	@ cd docker && docker-compose run --rm migrate
	@ cd docker && docker-compose up -d eastecho
