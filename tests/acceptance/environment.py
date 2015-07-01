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
import ConfigParser as cp
import os.path
import sys
import twill.commands as browser


this_dir = os.path.dirname(__file__)
rel_path_source = os.path.join(this_dir, '..', '..', 'source')
abs_path_source = os.path.abspath(rel_path_source)
sys.path.append(abs_path_source)
import smis

def before_all(context):
    connect_to_mis(context)


def connect_to_mis(context):
    user_profile_dir = os.path.expanduser('~')
    credentials_file = get_credentials_file_at(user_profile_dir)
    credentials = get_credentials_from(credentials_file)
    credentials_key = 'smis'
    key = credentials.get(credentials_key, 'consumer_key')
    secret = credentials.get(credentials_key, 'consumer_secret')
    user = credentials.get(credentials_key, 'user_name')
    password = credentials.get(credentials_key, 'password')
    logger = OxygenLogger(user, password)
    context.valid_client = smis.connect(key, secret, logger)


def get_credentials_file_at(location):
    as_txt = os.path.join(location, 'smis.txt')
    if os.path.exists(as_txt):
        return as_txt
    as_ini = os.path.join(location, 'smis.ini')
    if os.path.exists(as_ini):
        return as_ini
    raise RuntimeError('Credentials file not found.')


def get_credentials_from(credentials_file):
    parser = cp.ConfigParser()
    parser.read(credentials_file)
    return parser


class OxygenLogger(object):

    def __init__(self, user, password):
        self._user = user
        self._password = password

    def __call__(self, url):
        browser.go(url)
        browser.showforms()
        browser.fv('2', 'UserName', self._user)
        browser.fv('2', 'password', self._password)
        browser.submit('5')
