import requests


def get_endpoint(query_params=None):
    requests.get("http://localhost:8000/endpoint", params=query_params)
