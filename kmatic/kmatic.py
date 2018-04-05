#!/usr/bin/env python

import click
import kmaticlibs.kubehelper as kubehelper

def build_kmatci_cli_options(namespace=None,
                             cluster_name="testcluster-1"):
    """Build a dictionary with defaults and user provided options"""
    kmatic_options = {}
    if namespace:
        kmatic_options['namespace'] = namespace
    kmatic_options['cluster_name'] = cluster_name

    return kmatic_options


@click.group()
def cli():
    pass

@cli.group()
def namespace():
    print "namespace"

@cli.group()
def gcloud():
    print "gcloud"


#################################################
# namespace subcommand
#################################################
@namespace.command()
@click.option("--namespace", type=str, help="Namespace name", required=True)
def create(namespace):
    print "create namespace"
    kmatic_options = build_kmatci_cli_options(namespace=namespace)
    khelper = kubehelper.KubeHelper()
    khelper.create_namespace(kmatic_options)


@namespace.command()
@click.option("--namespace", type=str, help="Namespace name", required=True)
def delete(namespace):
    print "Delete namespace"
    kmatic_options = build_kmatci_cli_options(namespace=namespace)
    khelper = kubehelper.KubeHelper()
    khelper.delete_namespace(kmatic_options)

#################################################
# gcloud subcommand
#################################################
@gcloud.command()
@click.option("--cluster-name", type=str, help="Cluster name",
              default="testcluster-1")
def create_cluster(cluster_name):
    print "Create Kubernetes cluster in gcloud: ", cluster_name
    kmatic_options = build_kmatci_cli_options(cluster_name=cluster_name)
    khelper = kubehelper.KubeHelper()
    khelper.gcloud_create_kubecluster(kmatic_options)


@gcloud.command()
@click.option("--cluster-name", type=str, help="Cluster name",
              default="testcluster-1")
def delete_cluster(cluster_name):
    print "Delete kubernetes cluster in gcp ", cluster_name
    kmatic_options = build_kmatci_cli_options(cluster_name=cluster_name)
    khelper = kubehelper.KubeHelper()
    khelper.gcloud_delete_kubecluster(kmatic_options)


def main():
    print "main"
    cli.add_command(namespace)
    cli()


if __name__ == '__main__':
    main()
