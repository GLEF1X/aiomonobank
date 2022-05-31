from datetime import datetime
from typing import Dict, Any

import pytest
from pydantic import ValidationError

from aiomonobank.client import GetClientInfo, GetBankStatement, SetWebhook
from aiomonobank.core.abc.api_method import Request
from aiomonobank.utils.dates import convert_to_unix_time

datetime_for_testing = datetime(2020, 1, 1, 0, 0, 0)


def test_get_client_info_method():
    method = GetClientInfo()
    request = method.build_request()
    assert request.endpoint == "https://api.monobank.ua/personal/client-info"
    assert request.http_method == "GET"


@pytest.mark.parametrize(
    "method_payload,expected_request",
    [
        [
            {"from_date": datetime_for_testing},
            Request(
                endpoint=f"https://api.monobank.ua/personal/statement/0/{convert_to_unix_time(datetime_for_testing)}")
        ],

        pytest.param({
            "account": -1,
        }, Request(endpoint=""),
            marks=pytest.mark.xfail(raises=ValidationError, reason="account must be positive integer")),

        [
            {"from_date": datetime_for_testing, "to_date": datetime_for_testing},
            Request(
                endpoint=f"https://api.monobank.ua/personal/statement/0/{convert_to_unix_time(datetime_for_testing)}/{convert_to_unix_time(datetime_for_testing)}")
        ]

    ]
)
def test_get_bank_statement_method(method_payload: Dict[str, Any], expected_request: Request):
    method = GetBankStatement(**method_payload)
    assert method.build_request() == expected_request


@pytest.mark.parametrize(
    "method_payload,expected_request",
    [
        [
            {"webhook_url": "https://example.com/webhook"},
            Request(endpoint="https://api.monobank.ua/personal/webhook", http_method="POST",
                    data={"webHookUrl": "https://example.com/webhook"})
        ],
        pytest.param(
            {"webhook_url": "some string that not a http url"},
            Request(endpoint=""),
            marks=pytest.mark.xfail(raises=ValidationError, reason="webhook_url must be a valid http url")
        )
    ]
)
def test_set_webhook_method(method_payload: Dict[str, Any], expected_request: Request):
    method = SetWebhook(**method_payload)
    assert method.build_request() == expected_request

