# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os as _os

import httpx
import pytest
from httpx import URL

import openai
from openai import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


def reset_state() -> None:
    openai._reset_client()
    # TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization=None)'
    # openai.organization = None
    # TODO: The 'openai.base_url' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url=None)'
    # openai.base_url = None
    # TODO: The 'openai.timeout' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(timeout=DEFAULT_TIMEOUT)'
    # openai.timeout = DEFAULT_TIMEOUT
    # TODO: The 'openai.max_retries' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(max_retries=DEFAULT_MAX_RETRIES)'
    # openai.max_retries = DEFAULT_MAX_RETRIES
    # TODO: The 'openai.default_headers' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(default_headers=None)'
    # openai.default_headers = None
    # TODO: The 'openai.default_query' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(default_query=None)'
    # openai.default_query = None
    # TODO: The 'openai.http_client' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(http_client=None)'
    # openai.http_client = None
      # type: ignore
    # TODO: The 'openai.azure_endpoint' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(azure_endpoint=None)'
    # openai.azure_endpoint = None
    # TODO: The 'openai.azure_ad_token' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(azure_ad_token=None)'
    # openai.azure_ad_token = None
    # TODO: The 'openai.azure_ad_token_provider' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(azure_ad_token_provider=None)'
    # openai.azure_ad_token_provider = None


@pytest.fixture(autouse=True)
def reset_state_fixture() -> None:
    reset_state()


def test_base_url_option() -> None:
    assert openai.base_url is None
    assert openai.completions._client.base_url == URL("https://api.openai.com/v1/")

    # TODO: The 'openai.base_url' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url="http://foo.com")'
    # openai.base_url = "http://foo.com"

    assert openai.base_url == URL("http://foo.com")
    assert openai.completions._client.base_url == URL("http://foo.com")


def test_timeout_option() -> None:
    assert openai.timeout == openai.DEFAULT_TIMEOUT
    assert openai.completions._client.timeout == openai.DEFAULT_TIMEOUT

    # TODO: The 'openai.timeout' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(timeout=3)'
    # openai.timeout = 3

    assert openai.timeout == 3
    assert openai.completions._client.timeout == 3


def test_max_retries_option() -> None:
    assert openai.max_retries == openai.DEFAULT_MAX_RETRIES
    assert openai.completions._client.max_retries == openai.DEFAULT_MAX_RETRIES

    # TODO: The 'openai.max_retries' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(max_retries=1)'
    # openai.max_retries = 1

    assert openai.max_retries == 1
    assert openai.completions._client.max_retries == 1


def test_default_headers_option() -> None:
    assert openai.default_headers == None

    # TODO: The 'openai.default_headers' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(default_headers={"Foo": "Bar"})'
    # openai.default_headers = {"Foo": "Bar"}

    assert openai.default_headers["Foo"] == "Bar"
    assert openai.completions._client.default_headers["Foo"] == "Bar"


def test_default_query_option() -> None:
    assert openai.default_query is None
    assert openai.completions._client._custom_query == {}

    # TODO: The 'openai.default_query' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(default_query={"Foo": {"nested": 1}})'
    # openai.default_query = {"Foo": {"nested": 1}}

    assert openai.default_query["Foo"] == {"nested": 1}
    assert openai.completions._client._custom_query["Foo"] == {"nested": 1}


def test_http_client_option() -> None:
    assert openai.http_client is None

    original_http_client = openai.completions._client._client
    assert original_http_client is not None

    new_client = httpx.Client()
    # TODO: The 'openai.http_client' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(http_client=new_client)'
    # openai.http_client = new_client

    assert openai.completions._client._client is new_client


import contextlib
from typing import Iterator

from openai.lib.azure import AzureOpenAI


@contextlib.contextmanager
def fresh_env() -> Iterator[None]:
    old = _os.environ.copy()

    try:
        _os.environ.clear()
        yield
    finally:
        _os.environ.update(old)


def test_only_api_key_results_in_openai_api() -> None:
    with fresh_env():

        assert type(openai.completions._client).__name__ == "_ModuleClient"


def test_azure_api_key_env_without_api_version() -> None:
    with fresh_env():
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"

        with pytest.raises(
            ValueError,
            match=r"Must provide either the `api_version` argument or the `OPENAI_API_VERSION` environment variable",
        ):
            openai.completions._client


def test_azure_api_key_and_version_env() -> None:
    with fresh_env():
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"
        _os.environ["OPENAI_API_VERSION"] = "example-version"

        with pytest.raises(
            ValueError,
            match=r"Must provide one of the `base_url` or `azure_endpoint` arguments, or the `AZURE_OPENAI_ENDPOINT` environment variable",
        ):
            openai.completions._client


def test_azure_api_key_version_and_endpoint_env() -> None:
    with fresh_env():
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"

        openai.completions._client

        assert openai.api_type == "azure"


def test_azure_azure_ad_token_version_and_endpoint_env() -> None:
    with fresh_env():
        _os.environ["AZURE_OPENAI_AD_TOKEN"] = "example AD token"
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"

        client = openai.completions._client
        assert isinstance(client, AzureOpenAI)
        assert client._azure_ad_token == "example AD token"


def test_azure_azure_ad_token_provider_version_and_endpoint_env() -> None:
    with fresh_env():
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"
        # TODO: The 'openai.azure_ad_token_provider' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(azure_ad_token_provider=lambda: "token")'
        # openai.azure_ad_token_provider = lambda: "token"

        client = openai.completions._client
        assert isinstance(client, AzureOpenAI)
        assert client._azure_ad_token_provider is not None
        assert client._azure_ad_token_provider() == "token"
