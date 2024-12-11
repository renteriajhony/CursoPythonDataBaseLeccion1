FROM ubuntu:latest
LABEL authors="jrenteria"

ENTRYPOINT ["top", "-b"]