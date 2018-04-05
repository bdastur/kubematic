#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kmaticlibs.j2renderer as j2renderer
import kmaticlibs.commands as commands

class KubeHelper(object):
    def __init__(self):
        self.cmd = commands.Commands()

    def create_namespace(self, ns_name):
        """Create a new namespace"""
        print "Create new namespace: ", ns_name

    def gcloud_create_kubecluster(self, kmatic_options):
        """Create a new Kubernetes cluster"""
        if 'cluster_name' not in kmatic_options:
            print "Cluster Name required"
            return
        cluster_name = kmatic_options['cluster_name']
        cmd = """gcloud container clusters create %s \
                 --cluster-version=1.9.4-gke.1 \
                 --disk-size=50 \
                 --labels=tier=regular \
                 --max-nodes-per-pool=100 \
                 --node-labels=tier=regular \
                 --node-version=1.9.4-gke.1 \
                 --num-nodes=3 \
                 --tags=tag1
              """ % cluster_name

        ret, output = self.cmd.execute_command(cmd,
                                               env=None, cwd=None, popen=True)
        if ret != 0:
            print "Failed to run command %s"
            return 1
        print "output: ", output
        return 0

    def gcloud_delete_kubecluster(self, kmatic_options):
        """Delete a GCP kubernetes cluster"""
        if 'cluster_name' not in kmatic_options:
            print "Cluster Name is required"
            return

        cluster_name = kmatic_options['cluster_name']
        cmd = """gcloud container clusters delete %s --quiet""" \
            % cluster_name

        ret, output = self.cmd.execute_command(cmd, popen=False)
        if ret != 0:
            print "Failed to delete cluster %s" % cluster_name
            return

        return 0
