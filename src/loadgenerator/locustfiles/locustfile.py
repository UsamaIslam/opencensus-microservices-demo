from locust import HttpUser, between

from locustfiles.load_testing_microservice import LoadTest


class PrimaryUser(HttpUser):
    tasks = [LoadTest]
    wait_time = between(1, 3)
