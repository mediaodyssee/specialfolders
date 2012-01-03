#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import specialfolders


project_name = 'specialfolders'
project_url = 'http://www.bitbucket.org/izi/%s/' % project_name
project_desc = '''
%s

%s
''' % (open('README').read(), open('CHANGELOG').read())

setup(
    name=project_name,
    version=specialfolders.VERSION.replace(' ', '-'),
    description=specialfolders.__doc__.strip().replace('\n', ' '),
    long_description=project_desc,
    author=u'Média Odyssée',
    author_email='izimobil@mediaodyssee.com',
    url=project_url,
    download_url='%sdownloads/%s-%s.tar.gz' % (project_name, project_url, specialfolders.VERSION),
    py_modules=['specialfolders'],
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Desktop Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
