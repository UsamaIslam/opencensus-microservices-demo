from locust import TaskSet, task
import random


class LoadTest(TaskSet):
    products = [
        '0PUK6V6EV0',
        '1YMWWN1N4O',
        '2ZYFJ3GM2N',
        '66VCHSJNUP',
        '6E92ZMYYFZ',
        '9SIQT8TOJO',
        'L9ECAV7KIM',
        'LS4PSXUNUM',
        'OLJCESPC7Z']


    def on_start(self):
        self.index()

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def set_currency(self):
        currencies = ['EUR', 'USD', 'JPY', 'CAD']
        self.client.post("/setCurrency",
                         {'currency_code': random.choice(currencies)})

    @task(10)
    def browse_product(self):
        self.client.get("/product/" + random.choice(self.products))

    @task(3)
    def view_cart(self):
        self.client.get("/cart")

    @task(2)
    def add_to_cart(self):
        product = random.choice(self.products)
        self.client.get("/product/" + product)
        self.client.post("/cart", {
            'product_id': product,
            'quantity': random.choice([1, 2, 3, 4, 5, 10])})

    @task(1)
    def checkout(self):
        self.add_to_cart()
        self.client.post("/cart/checkout", {
            'email': 'someone@example.com',
            'street_address': '1600 Amphitheatre Parkway',
            'zip_code': '94043',
            'city': 'Mountain View',
            'state': 'CA',
            'country': 'United States',
            'credit_card_number': '4432-8015-6152-0454',
            'credit_card_expiration_month': '1',
            'credit_card_expiration_year': '2019',
            'credit_card_cvv': '672',
        })

    # def on_start(self):
    #     """Logins and stuff before starting a user session."""
    #     login()
    # 
    # @task
    # def usd_to_bdt(self):
    #     url = "exchange"
    # 
    #     querystring = {"q": "1.0", "from": "USD", "to": "BDT"}
    # 
    #     headers = {
    #         "x-rapidapi-host": settings.HOST,
    #         "x-rapidapi-key": settings.API_TOKEN,
    #     }
    # 
    #     self.client.get(url, headers=headers, params=querystring)
    # 
    # @task
    # def bdt_to_usd(self):
    #     url = "exchange"
    # 
    #     querystring = {"q": "1.0", "from": "BDT", "to": "USD"}
    # 
    #     headers = {
    #         "x-rapidapi-host": settings.HOST,
    #         "x-rapidapi-key": settings.API_TOKEN,
    #     }
    # 
    #     self.client.get(url, headers=headers, params=querystring)
    # 
    # @task
    # def stop(self):
    #     """TaskSet objects don't know when to hand over control
    #     to the parent class. This method does exactly that."""
    # 
    #     self.interrupt()
    # 
    # @task
    # def on_stop(self):
    #     """Logout and stuff after ending a user session."""
    #     logout()
