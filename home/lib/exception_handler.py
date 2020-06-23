# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    """Returns extra information about some safe errors."""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = drf_exception_handler(exc, context)
    if not response:
        response = Response({'detail': ''}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    response.data['status_code'] = response.status_code
    return response
