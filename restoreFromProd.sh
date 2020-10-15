#!/bin/bash
echo "reloading $HCAT_DB from production"
# Database
scp tuatara@tuatara.data.humancellatlas.org:/home/tuatara/hourly-backup/hcat.sql.gz .
gunzip hcat.sql.gz
# edit db name
cat hcat.sql | egrep -v '(^CREATE DATABASE|^USE)' > hcat.edited.sql
rm hcat.sql
hgsql -e "drop database if exists $HCAT_DB"
hgsql -e "create database $HCAT_DB"
hgsql $HCAT_DB < hcat.edited.sql
# Media
echo "reloading $HCAT_MEDIA from production"
scp tuatara@tuatara.data.humancellatlas.org:/home/tuatara/hourly-backup/hcatMedia.tar.gz .
pushd $HCAT_MEDIA
tar xfz $HOME/hca-tuatara/hcatMedia.tar.gz
popd
