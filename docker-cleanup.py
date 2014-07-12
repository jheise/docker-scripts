#!/usr/bin/env python

import docker

conn = docker.Client("unix:///var/run/docker.sock")

for container in conn.containers(all=True):
    if "Up" not in container["Status"]:
        print "deleting", container["Names"]
        conn.remove_container(container["Names"][0][1:])
