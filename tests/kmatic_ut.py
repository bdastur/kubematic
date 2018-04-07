#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import kmaticlibs.kmatic_logger as logger

class KmaticUt(unittest.TestCase):
    def test_logger_basic(self):
        """Test basic logging api"""
        print "log test"
        klog = logger.KmaticLogger(logfile="../.tempdir/kmatic_log.txt")
        klog.logger.debug("This is s a test")
        klog.logger.error("This is a test")
