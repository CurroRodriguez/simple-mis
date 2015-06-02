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

import smis._client as misclient
from smis import _utils as utils

class TestClient(unittest.TestCase):

    def setUp(self):
        self.service = ServiceMock('https://some.endpoint.autodesk.com')
        self.client = misclient.Client(self.service)
        return  super(TestClient, self).setUp()

    def test_client_url_is_service_endpoint(self):
        self.assertEqual(self.client.url, self.service.endpoint)

    def test_returns_correct_response(self):
        self.service.response = 'hello'
        self.get_resource(self.client).expect_response(self.service.response)

    def test_correct_relative_path_is_requested(self):
        self.get_resource(self.client).expect_invoked_path('')

    def test_can_access_direct_resource(self):
        self.given_resource(self.client.models).expect_url('models')

    def test_correct_url_is_invoked_on_child_resource(self):
        self.service.response = 'child response'
        self.get_resource(self.client.models).expect_response(self.service.response)

    def test_can_access_identifiable_resource(self):
        model_id = '100'
        self.given_resource(self.client.models.item(model_id)).expect_url('models', model_id)

    def test_can_access_sub_resource(self):
        self.given_resource(self.client.models.proposals).expect_url('models', 'proposals')

    # Test Utilities
    #
    def given_resource(self, resource):
        self.resource = resource
        return self

    def expect_url(self, *args):
        expected_url = utils.url_join(self.service.endpoint, *args)
        self.assertEqual(self.resource.url, expected_url)
        return self

    def get_resource(self, resource):
        self.resource = resource
        self.response = self.resource.get()
        return self

    def expect_invoked_path(self, *args):
        expected_path = utils.url_join(*args)
        self.assertEqual(self.service.requested_url, expected_path)
        return self

    def expect_response(self, response):
        self.assertEqual(self.response, response)
        return  self





class ServiceMock(object):

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.response = None
        self.requested_url = None

    def get(self, url):
        self.requested_url = url
        return self.response

if __name__ == '__main__':
    unittest.main()
