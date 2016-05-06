#!/bin/bash
NAME='hello_app'                                   #Ӧ�õ�����
DJANGODIR=/webapps/hello_django/hello              #django��Ŀ��Ŀ¼
SOCKFILE=/webapps/hello_django/run/gunicorn.sock   #ʹ�����sock��ͨ��
USER=hello                                         #���д�Ӧ�õ��û�
GROUP=webapps                                      #���д�Ӧ�õ���
NUM_WORKERS=3                                      
DJANGO_SETTINGS_MODULE=hello.settings              #django�������ļ�
DJANGO_WSGI_MODULE=hello.wsgi                      #wsgiģ��
echo "starting $NAME as `whoami`"

#����python�������л���
cd $DJANGODIR
source ../bin/activate
export  DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
#���gunicorn.sock����Ŀ¼�������򴴽�
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

#����Django

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=unix:$SOCKFILE

