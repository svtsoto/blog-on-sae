#!/bin/bash
NAME='hello_app'                                   #应用的名称
DJANGODIR=/webapps/hello_django/hello              #django项目的目录
SOCKFILE=/webapps/hello_django/run/gunicorn.sock   #使用这个sock来通信
USER=hello                                         #运行此应用的用户
GROUP=webapps                                      #运行此应用的组
NUM_WORKERS=3                                      
DJANGO_SETTINGS_MODULE=hello.settings              #django的配置文件
DJANGO_WSGI_MODULE=hello.wsgi                      #wsgi模块
echo "starting $NAME as `whoami`"

#激活python虚拟运行环境
cd $DJANGODIR
source ../bin/activate
export  DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
#如果gunicorn.sock所在目录不存在则创建
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

#启动Django

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=unix:$SOCKFILE

