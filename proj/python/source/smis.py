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
Python library that provides a simple interface to Autodesk InfraWorks 360 Model Information Service.
"""
import _utils as utils

class Client(object):
    """
    Model Information Service client application.

    This class is provided as entry point for all interfaces that communicate with the Autodesk InfraWorks 360 Model
    Information Service. The class is instantiated with a ``service`` proxy that knows how to communicate with
    the on-line service REST API.

    Client applications should not instantiate this class directly, and they should use the ``connect()`` method
    instead to access the ``Client`` object.
    """

    def __init__(self, service):
        self._service = service
        self._root_resource = _Resource('', self._service)

    @property
    def url(self):
        """
        Provides the end-point URL of the Autodesk InfraWorks 360 Model Information Service.

        :return:
            A string containing the URL to the Autodesk InfraWorks 360 Model Information Service.
        """
        return self._service.endpoint

    def get(self):
        """
        Access information about the service end-point.

        :return:
            Returns the response from the service end-point.

        ..  todo::
            Complete documentation for this method.
        """
        return self._root_resource.get()

    def __getattr__(self, item):
        return _Resource(item, self._service, self._root_resource)



class _Resource(object):
    """
    Temporary ``_Resource`` class documentation
    """

    def __init__(self, url_token, service, parent=None):
        self._url_token = url_token
        self._service = service
        self._parent = parent

    @property
    def url(self):
        """
        Provides the full URL to the resource.

        :return:
            A string containing the full URL to the resource.
        """
        return utils.url_join(self._service.endpoint, self.path)

    @property
    def path(self):
        """
        Provides the relative path to the resource from the base end-point.

        :return:
            Returns a string containing the relative path to the resource.
        """
        return utils.url_join(self._parent.path, self._url_token) if self._parent else self._url_token

    def get(self):
        """
        Provides the resource representation.

        :return:
            Returns the resource representation.
        """
        return self._service.get(self.path)

    def item(self, identity):
        """
        Temporary ``item()`` method documentation.
        :param identity:
        :return:
        """
        return _Resource(identity, self._service, self)

    def __getattr__(self, item):
        return self.item(item)
