#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import jinja2


class J2Renderer(object):
    def __init__(self):
        """Initialize J2Renderer."""
        pass

    def generate_temporary_filename(self):
        current = datetime.datetime.now()
        tempFilename = "kmatcirendered_%s%s" % \
            (str(current.second), str(current.microsecond))

        if not os.path.exists(".tempdir"):
            tempDir = os.mkdir(".tempdir", mode=0777)

        filename = os.path.join(".tempdir", tempFilename)
        return filename

    def generate_rendered_template(self, templatefile, searchpath, obj):
        """
        Generate a rendered template from the specific j2 template.
        Returns: a file Name
        """
        rendered_data = self.render_j2_template(templatefile, searchpath, obj)
        temp_file = self.generate_temporary_filename()
        with open(temp_file, 'w') as outfile:
            outfile.write(rendered_data)
        return temp_file

    def render_j2_template(self, templatefile, searchpath, obj):
        """
        Returns a rendered string.
        The API returns a rendered string from the j2 template file
        """
        objdata = {}
        template_loader = jinja2.FileSystemLoader(searchpath=searchpath)
        env = jinja2.Environment(loader=template_loader,
                                 trim_blocks=True,
                                 lstrip_blocks=True)
        template = env.get_template(templatefile)
        objdata['data'] = obj
        rendered_data = template.render(objdata)

        return rendered_data
