#!/usr/bin/env python

import click
import kmaticlibs.j2renderer

@click.group()
def cli():
    pass

@cli.group()
def namespace():
    print "namespace"


@namespace.command()
def create():
    print "create namespace"


def main():
    print "main"
    cli.add_command(namespace)
    cli()


if __name__ == '__main__':
    main()
