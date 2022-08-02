import base64
import requests
from df_auth.models.tokens import EmailVerificationToken
from util.constants import Constants
from util.functions import get_env


def get_client_ip(request):
    """Helper function for retrieving an returning the client's ip address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def verify_user(request, user_data):
    """Verifies a recaptcha key and email address sent from the client"""
    # try:
    #     if(User.objects.filter(email_address=user_data['email_address']).count() > 0):
    #         raise

    #     resp = requests.post(
    #         'https://www.google.com/recaptcha/api/siteverify',
    #         data={
    #             'secret': get_env('RECAPTCHA_SECRET_KEY'),
    #             'response': user_data['recaptcha_key'],
    #             'remoteip': get_client_ip(request)
    #         }
    #     )
    #     return resp.json()['success']
    # except KeyError as ke:
    #     raise NotAcceptable() from ke
    return True


def send_verificiation_email(user, type):
    """
    Function used to send a verification email to the appropriate user subclass
    """

    # Create a an email verification token to be sent to the user
    verification_token = EmailVerificationToken.objects.update_or_create(user=user)[0].key
    # Send correct email based on user type
    # TODO: Add email logic
    if type == Constants.EmailVerificationType.RECIPIENT_VERIFICATION:
        return verification_token
    elif type == Constants.EmailVerificationType.SUBSCRIBER_VERIFICATION:
        return verification_token
    else:
        raise ValueError



def send_email(passcode, email, webUrl, templateName, subject, vars):
    # verifyUrl = webUrl + passcode
    # apiKey = get_env("MAILCHIMP_API_KEY")
    # url = get_env("MAILCHIMP_URL")
   
    # headers = {
    #     'Content-Type': 'application/json',
    #     'Authorization': 'Basic ' + base64.b64encode(apiKey.encode("utf-8")).decode("utf-8"),
    #     'Content-Accept': 'application/json'
    # }

    # json = {
    #       "key": apiKey,
    #       "template_name": templateName,
    #       "template_content": [
    #           {
    #               "name": "example name",
    #               "content": "example content"
    #           }
    #       ],
    #       "message": {
    #           "subject": subject,
    #           "from_email": get_env("CONTACT_EMAIL"),
    #           "to": [
    #               {
    #                   "email": email
    #               }
    #           ],
    #           "merge_vars": [
    #               {
    #                     "rcpt": email,
    #                     "vars": [
    #                         *vars,
    #                         { "name": "EVLINK", "content": verifyUrl }
    #                     ]
    #               }
    #           ],
    #           "tags": [
    #               "validate"
    #           ]
    #       }
    #     }


    # resp = requests.post(url, headers=headers, json=json)
    # return resp
    return True
