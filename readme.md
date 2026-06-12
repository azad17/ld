
docker run -d -p 1025:1025 -p 8025:8025 axllent/mailpit

celery -A config  beat -l info

setting up mailpit

docker run -d -p 1025:1025 -p 8025:8025 axllent/mailpitloc

docker run -d --name redis -p 6379:6379 redis  
for redis setup

celery -A config worker -l info --pool=solo
for celery

for testing

coverage run manage.py test


Docker

docker compose build

docker compose up 