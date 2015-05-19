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
import unittest

from smis._proxy import MISServiceProxy
from smis._proxy import _MIS_ACCEPT_TYPE
from smis._proxy import _MIS_ENDPOINT
from smis._utils import  url_join

class TestMISServiceProxy(unittest.TestCase):

    def setUp(self):
        self.token = 'token'
        self.proxy = MISServiceProxySpy(self.token)
        return  super(TestMISServiceProxy, self).setUp()

    def test_requires_oauth_token(self):
        self.assertEqual(self.proxy.token, self.token)


    def test_provides_endpoint(self):
        self.assertEqual(self.proxy.endpoint, _MIS_ENDPOINT)

    def test_requests_the_full_url_specified(self):
        self.proxy.get('relative/path')
        expected_full_url = url_join(_MIS_ENDPOINT, 'relative', 'path')
        self.assertEqual(expected_full_url, self.proxy.requested_url)

    def test_uses_mis_accept_header(self):
        self.proxy.get('relative/path')
        self.assertEqual(self.proxy.headers.get('Accept'), _MIS_ACCEPT_TYPE)

    def test_send_request_with_specified_access_token(self):
        self.proxy.get('relative/path')
        self.assertEqual(self.proxy.auth, self.token)




class MISServiceProxySpy(MISServiceProxy):

    @property
    def token(self):
        return self._token

    def _do_get(self, url, headers, auth):
        self.requested_url = url
        self.headers = headers
        self.auth = auth


if __name__ == '__main__':
    unittest.main()
