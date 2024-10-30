import re
from django.utils import timezone


def check_response(response, request):
    if response is None or request.session.get('role') is None:
        request.session.clear()
        check_session(request.session)
        return True


def check_session(session):
    if (session.get('role') is None):
        session.clear()
        session['role'] = ''
        session['user'] = ''
        session['cart'] = []
        session['counter'] = None
        session.save()


def addCounterInfo(session, origin):
    counter_page = session.get('counter_origin')
    counter = session.get('counter')
    if (counter_page is not None and counter is not None and counter_page == origin):
        return
    session['counter_origin'] = origin
    session['counter'] = int(timezone.now().timestamp())
    session.save()


def number_validator(value, t, form):
    try:
        num = t(value)
        if num < 0 or (t == float and num == 0):
            form.add_error(None,
                           f'Wrong {"price" if t == float else "amount"} format')
    except:
        form.add_error(None,
                       f'Wrong {"price" if t == float else "amount"} format')


def phone_validator(value, form):
    pattern = r'^\+37529\d{7}$'
    if not re.match(pattern, value):
        form.add_error(
            None, 'Phone number must matches `+37529xxxxxxx`!')


def password_validator(value, form):
    if (len(value) < 8):
        form.add_error(None, 'Password min length is 8!')
    if not any(char.isdigit() for char in value):
        form.add_error(
            None, 'Password must contain at least 1 digit!')

    if not any(char.isupper() for char in value):
        form.add_error(
            None, 'Password must contain at least 1 capital letter!')
