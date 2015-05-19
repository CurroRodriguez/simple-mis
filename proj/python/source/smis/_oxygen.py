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
Temporary documentation
"""
from requests_oauthlib import OAuth1Session as Session

from smis._utils import url_join

_AUTHENTICATION_ENDPOINT = 'https://accounts.autodesk.com'

class OxygenAuthenticationProxy(object):
    """
    Temporary
    """

    def __init__(self, key, secret, login_callback):
        self._key = key
        self._secret = secret
        self._login_callback = login_callback

    def authenticate(self):
        self._request_token()
        self._obtain_authorization_url()
        self._obtain_user_authorization()
        self._access_token()
        return  self._client_token

    def _request_token(self):
        request_token_url = url_join(_AUTHENTICATION_ENDPOINT, 'oauth', 'RequestToken')
        self._session = Session(self._key, client_secret=self._secret)
        fetch_response = self._session.fetch_request_token(request_token_url)
        self._resource_owner_key = fetch_response.get('oauth_token')
        self._resource_owner_secret = fetch_response.get('oauth_token_secret')

    def _obtain_authorization_url(self):
        authorize_url = url_join(_AUTHENTICATION_ENDPOINT, 'oauth', 'Authorize')
        self._authorization_url = self._session.authorization_url(authorize_url)

    def _obtain_user_authorization(self):
        self._login_callback(self._authorization_url)

    def _access_token(self):
        self._session = Session(self._key,
                                client_secret=self._secret,
                                resource_owner_key=self._resource_owner_key,
                                resource_owner_secret=self._resource_owner_secret)
        access_token_url = url_join(_AUTHENTICATION_ENDPOINT, 'oauth', 'AccessToken')
        oauth_tokens = self._session.fetch_access_token(access_token_url)
        self._resource_owner_key = oauth_tokens.get('oauth_token')
        self._resource_owner_secret = oauth_tokens.get('oauth_token_secret')
        self._client_token = Session(self._key,
                                     client_secret=self._secret,
                                     resource_owner_key=self._resource_owner_key,
                                     resource_owner_secret=self._resource_owner_secret,
                                     signature_type='auth_header')