#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import kmaticlibs.j2renderer as j2renderer
import kmaticlibs.commands as commands

class KubeHelper(object):
    def __init__(self, klogger):
        self.cmd = commands.Commands(klogger)
        self.klogger = klogger

    def create_namespace(self, kmatic_options):
        """Create a new namespace"""
        if 'namespace' not in kmatic_options:
            self.klogger.error("Namespace required")
            return
        namespace = kmatic_options['namespace']

        j2obj = j2renderer.J2Renderer()
        templatefile = "namespace.json.j2"
        searchpath = "./templates"
        obj = {}
        obj['namespace'] = {}
        obj['namespace']['name'] = namespace
        obj['namespace']['name_label'] = namespace
        rendered_data = j2obj.render_j2_template(templatefile, searchpath, obj)
        tempFile = j2obj.generate_rendered_template(
        templatefile, searchpath, obj)
        j2renderer.display_rendered_template(tempFile, rendered_data)

        cmd = """kubectl create -f %s""" % tempFile
        #cmd = """kubectl create namespace %s""" % namespace
        ret, output = self.cmd.execute_command(cmd,
                                               cwd=None,
                                               env=None, popen=False)
        if ret != 0:
            self.klogger.logger.error("Failed to create namespace %s",
                                       namespace)
            return

        print output
        return 0

    def delete_namespace(self, kmatic_options):
        """Create a new namespace"""
        if 'namespace' not in kmatic_options:
            print "Namespace is required."
            return
        namespace = kmatic_options['namespace']
        print "Delete namespace: ", namespace
        cmd = """kubectl delete namespace %s""" % namespace
        ret, output = self.cmd.execute_command(cmd,
                                               cwd=None,
                                               env=None, popen=False)
        if ret != 0:
            print "Failed to delete namespace %s" % namespace
            return

        print output
        return 0

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
