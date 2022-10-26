This repo is to demonstrate https://github.com/pact-foundation/pact-stub-server/issues/53

The `consumer-provider.json` contract is created by running `src/test_consumer.py`.

We then start the pact stub service via `docker-compose up stub-service`.

Then if we `curl http://localhost:8000/endpoint?type=bar` we get the (incorrect)
response of `{"type":"none"}`.

The logs of the stub service are checked in as `docker-logs.txt`, which show the debug
info, including the fact that multiple requests were matched.
