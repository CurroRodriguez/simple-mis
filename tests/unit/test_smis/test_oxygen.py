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

from smis import _oxygen as o2


class TestOxygenAuthenticationProxy(unittest.TestCase):

    def setUp(self):
        self.key = 'the_key'
        self.secret = 'the_secret'
        self.subject = OxygenAuthenticationProxyMock(self.key, self.secret, self.login_callback)
        self.callback_invoked = False
        return super(TestOxygenAuthenticationProxy, self).setUp()

    # Unit tests
    #
    def test_requires_key(self):
        self.assertEqual(self.subject.key, self.key)

    def test_requires_secret(self):
        self.assertEqual(self.subject.secret, self.secret)

    def test_requires_login_callback(self):
        self.assertEqual(self.subject.callback, self.login_callback)

    def test_returns_access_toke(self):
        access_token = self.subject.authenticate()

    def test_invokes_login_callback_for_user_authorization(self):
        access_token = self.subject.authenticate()
        self.assertTrue(self.callback_invoked)

    # Helpers
    #
    def login_callback(self, authorization_url):
        self.callback_invoked = True


class OxygenAuthenticationProxyMock(o2.OxygenAuthenticationProxy):

    @property
    def key(self):
        return self._key

    @property
    def secret(self):
        return self._secret

    @property
    def callback(self):
        return self._login_callback

    @property
    def endpoint(self):
        return self._endpoint

    # Overriden to avoid calls to authentication during testing
    #
    def _request_token(self):
        self._resource_owner_key = 'resource_owner_key'
        self._resource_owner_secret = 'resource_owner_secret'

    def _obtain_authorization_url(self):
        self._authorization_url = 'https://authorization.url.com'

    def _obtain_user_authorization(self):
        self._login_callback(self._authorization_url)

    def _access_token(self):
        self._credentials = 'client_token'

if __name__ == '__main__':
    unittest.main()
