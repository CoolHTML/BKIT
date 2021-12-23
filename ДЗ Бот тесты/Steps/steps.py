from behave import *
from main import *

@given ('Bot')
def step_impl(context):
    return 0
@when('I solve this equation')
def step_impl(context):
    context.roots = send_number()
@then('I expect to get 4')
def step_impl(context):
    result = 4
    assert context.roots == result

