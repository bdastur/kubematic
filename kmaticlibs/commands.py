#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess


class Commands(object):
    def __init__(self, klogger):
        self.klogger = klogger

    def execute_command(self, cmd, cwd=None, env=None, popen=False):
        """
        Execute a shell command.
        The API uses the python subprocess module to execute shell
        commands.
        """
        if popen:
            cmdoutput = ""
            sproc = subprocess.Popen(cmd,
                                     env=env,
                                     cwd=cwd,
                                     shell=True,
                                     stdout=subprocess.PIPE)
            while True:
                nextline = sproc.stdout.readline()
                cmdoutput += nextline
                if nextline == "" and sproc.poll() is not None:
                    break

                sys.stdout.write(nextline)
                sys.stdout.flush()
            return 0, cmdoutput
        try:
            cmdoutput = subprocess.check_output(cmd,
                                                cwd=cwd,
                                                shell=True,
                                                env=env)
        except subprocess.CalledProcessError as err:
            self.klogger.logger.error("cmd '%s' execution failed. Error: [%s]",
                cmd, err)
            return 1, None

        return 0, cmdoutput
