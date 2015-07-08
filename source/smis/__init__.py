# (C) Copyright 2015 Autodesk, Inc.  All rights reserved.
#
# Permission to use, copy, modify, and distribute these source code samples is
# hereby granted, provided that (i) you must clearly identify any modified
# source code files and any resulting binary files as works developed by you,
# and not by Autodesk;  and (ii) you may distribute the resulting binary files
# of the source code samples in works that are commercially distributed
# software applications only if:  (a) such applications require an Autodesk
# product to operate; and (b) such applications contain, subject to Autodesk's
# sole discretion, significant features and functionality in addition to the
# source code samples so that the source code samples are not the primary
# source of value.  In any copy of the source code samples, derivative works,
# and resulting binary files, you must include the copyright notices of
# Autodesk, Inc., the limited warranty and restricted rights notice below, and
# (if modified) the following statement: "This software contains copyrighted
# code owned by Autodesk but has been modified and is not endorsed by Autodesk
# in its modified form".
#
# AUTODESK PROVIDES THIS SOFTWARE "AS IS" AND WITH ALL FAULTS.  AUTODESK MAKES
# NO WARRANTIES, EXPRESS OR IMPLIED, AS TO NON-INFRINGEMENT OF THIRD PARTY
# RIGHTS, MERCHANTABILITY, OR FITNESS FOR ANY PARTICULAR PURPOSE. IN NO EVENT
# WILL AUTODESK BE LIABLE TO YOU FOR ANY CONSEQUENTIAL, INCIDENTAL OR SPECIAL
# DAMAGES, INCLUDING ANY LOST PROFITS OR LOST SAVINGS, EVEN IF AUTODESK HAS
# BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, OR FOR ANY CLAIM BY ANY
# THIRD PARTY. AUTODESK DOES NOT WARRANT THAT THE OPERATION OF THE SOFTWARE
# WILL BE UNINTERRUPTED OR ERROR FREE.
#
# Use, duplication, or disclosure by the U.S. Government is subject to
# restrictions set forth in FAR 52.227-19 (Commercial ComputerSoftware -
# Restricted Rights) and DFAR 252.227-7013(c)(1)(ii) (Rights in Technical Data
# and Computer Software), as applicable.
#
# You may not export the source code samples or any derivative works,
# resulting binaries, or any related technical documentation,  in violation of
# U.S. or other applicable export control laws.
#
"""
The ``smis`` Python package provides a simple interface to access |mis|, which exposes a REST API to access model data
from |iw|_ models stored in the cloud. The package removes the complexity of authorizing an application to use the
service and simplifies the process of sending HTTP requests to the service to access the resource information.
"""
__author__ = u'Isaac Rodriguez'
__copyright__ = u'(C) Copyright 2015 Autodesk, Inc.'
author_email = u'isaac.rodriguez@autodesk.com'
project = u'smis'
description = u'Simple MIS Library'
long_description=u'A simple library to access Autodesk InfraWorks 360 Model Information Service.'
docs_url=u'http://simple-mis.readthedocs.org/en/latest/'

version_major = u'0'
version_minor = u'0'
version_patch = u'6'

version = u'{major}.{minor}'.format(major=version_major, minor=version_minor)
release = u'{version}.{build}'.format(version=version, build=version_patch)

classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 2.7',
        ]

from requests import codes
from _oxygen import OxygenAuthenticationProxy
from _proxy import MISServiceProxy
from _client import Client

def connect(key, secret, login_callback):
    """
    This function authorizes the application to access.
    
    :param key: Consumer key for an authorized application.
    :param secret: Consumer secret for an authorized application.
    :param login_callback: Login callback to authenticate user.
    :return: Client object that provides interface to access the service
    """
    auth_proxy = OxygenAuthenticationProxy(key, secret, login_callback)
    auth_token = auth_proxy.authenticate()
    mis_service_proxy = MISServiceProxy(auth_token)
    return Client(mis_service_proxy)
