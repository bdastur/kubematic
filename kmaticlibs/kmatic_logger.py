#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


class KmaticLogger(object):
    def __init__(self, name=__name__, logfile="/tmp/kmaticlog.txt"):
        """ Kubematic Logging facility.
        @args:
        :type name: String
        :param name: Name of the module
        :type logfile: String
        :param logfile: path to logfile.
        """
        print "Kmaticlogger Initialize."
        if hasattr(KmaticLogger, 'logger'):
            self.logger = KmaticLogger.logger
            print "Kmatic logger"
            self.logger.debug("Logger already initalized.")
            return

        formatStr = '[%(asctime)s %(levelname)5s' \
            ' %(process)d %(name)s]: %(message)s'
        logging.basicConfig(level=logging.DEBUG,
                            format=formatStr,
                            datefmt='%m-%d-%y %H:%M',
                            filename=logfile,
                            filemode='a')

        # Define a stream handler for critical errors.
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)

        formatter = logging.Formatter(
            '[%(asctime)s %(levelname)5s %(name)s]: %(message)s',
            datefmt="%m-%d-%y %H:%M")
        console.setFormatter(formatter)

        # Add handler to root logger.
        logging.getLogger(name).addHandler(console)
        self.logger = logging.getLogger(name)
        KmaticLogger.logger = self.logger
        print "Kmatic Logger initialized"
