#!/usr/bin/env bash

docker build -t relate-webui:20180818008 -f docker/relate_webui/Dockerfile .

docker build -t relate-staticfiles-webserver:20180524 -f docker/relate_staticfiles_webserver/Dockerfile .