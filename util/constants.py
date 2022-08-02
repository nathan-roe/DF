class Constants:
    class EmailVerificationType:
        RECIPIENT_VERIFICATION = 1
        SUBSCRIBER_VERIFICATION = 2

    class LoginConstants:
        MAX_LOGIN_REQUESTS = 3
        LOGIN_THROTTLE = 90
        MAX_FAILED_LOGINS = 10
