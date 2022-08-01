from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from auth.models.tokens import ExpiringToken
from metrics.models.errorlog import ErrorLog


def token_to_userprofile(request):
    """
    Function for simplifying token to user  association
    """
    # Assigning UserProfile object based on token from request header
    try:
        tok = request.META.get('HTTP_AUTHORIZATION').split()
        cur_token = ExpiringToken.objects.get(key=tok[1])
        has_expired = ExpiringToken.expired(cur_token)
        if not has_expired:
            return cur_token.user
        else:
            return
    except ExpiringToken.DoesNotExist:
        return

def custom_view_exception_handler(exc, context):
    """
    Inherits the default DRF exception handling and adds logging and custom
    exception handling outside of default 500
    """

    # Call DRF default exception handler first
    response = exception_handler(exc, context)

    request = context['request']
    cur_user = token_to_userprofile(request)

    # Checks if the raised exception is of the type you want to handle
    if isinstance(exc, KeyError):
        err_data = {'error': 'Invalid query parameter'}
        response = Response(err_data, status=status.HTTP_400_BAD_REQUEST)

    elif isinstance(exc, ValueError):
        err_data = {'error': 'Invalid request data'}
        response = Response(err_data, status=status.HTTP_400_BAD_REQUEST)

    elif isinstance(exc, ValidationError):
        err_data = {'error': 'Invalid form data, did not meet validation criteria'}
        response = Response(err_data, status=status.HTTP_400_BAD_REQUEST)

    # Create Error log object
    ErrorLog.objects.create(
        user=cur_user, error_traceback=str(exc),
        url_path=request.path, response_code=response.status_code \
            if hasattr(response, 'status_code') else "500"
    )

    return response
