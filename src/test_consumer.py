import atexit
import unittest

from pact import Consumer, Provider

from .consumer import get_endpoint

pact = Consumer("Consumer").has_pact_with(
    Provider("Provider"), host_name="localhost", port=8000
)
pact.start_service()
atexit.register(pact.stop_service)


class ConsumerTestCase(unittest.TestCase):
    def test_aaa_with_no_params(self):
        # "aaa" makes this test run first, so this interaction is first in the contract
        (
            pact.given("some state")
            .upon_receiving("a request with no type")
            .with_request("get", "/endpoint")
            .will_respond_with(200, body={"type": "none"})
        )

        with pact:
            get_endpoint()

    def test_with_foo(self):
        (
            pact.given("some state")
            .upon_receiving("a request for type foo")
            .with_request("get", "/endpoint", query="type=foo")
            .will_respond_with(200, body={"type": "foo"})
        )

        with pact:
            get_endpoint({"type": "foo"})

    def test_with_bar(self):
        (
            pact.given("some state")
            .upon_receiving("a request for type bar")
            .with_request("get", "/endpoint", query="type=bar")
            .will_respond_with(200, body={"type": "bar"})
        )

        with pact:
            get_endpoint({"type": "bar"})
