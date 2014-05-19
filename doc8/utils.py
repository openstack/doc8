# -*- coding: utf-8 -*-

# Copyright (C) 2014 Ivan Melnikov <iv at altlinux dot org>
#
# Author: Joshua Harlow <harlowja@yahoo-inc.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import fnmatch
import os


def find_files(paths, patterns):
    for path in paths:
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            for root, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    if any(fnmatch.fnmatch(filename, pattern)
                           for pattern in patterns):
                        yield os.path.join(root, filename)
        else:
            raise IOError('Invalid path: %s' % path)


def filter_document(document, filter_func):
    for n in document.traverse(include_self=True):
        if filter_func(n):
            yield n