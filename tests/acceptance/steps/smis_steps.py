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
from behave import *
import nose.tools as verify
import smis

@given('we provide valid credentials and callback')
def we_provide_valid_credentials_and_callback(context):
    print('IN SCENARIO OUTLINE')
    context.client = context.valid_client


@given('a models collection resource')
def a_models_collection_resource(context):
    context.resource = context.client.models


@given('a model resource')
def a_model_resource(context):
    context.resource = context.client.models.item('32553')


@given('a proposal resource')
def a_proposal_resource(context):
    context.resource = context.client.models.item('32553').proposals.item('master')


@given('an object collection resource')
def an_object_collection_resource(context):
    context.resource = context.client.models.item('32553').proposals.item('master').roads


@given('an object resource')
def step_imp(context):
    context.resource = context.client.models.item('32553').proposals.item('master').roads.item('6')


@when('we call get in client')
def we_call_get_in_client(context):
    context.response = context.client.get()


@when('we get resource')
def we_get_resource(context):
    context.response = context.resource.get()


@then('the result is ok')
def the_result_is_ok(context):
    verify.eq_(context.response.status_code, smis.codes.ok)
