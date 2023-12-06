#################
# This Script guides us out of the Notebook interface into actual production-level code.
import random
from faker import Faker

SAMPLE_PRODUCT_LIST = ['Nokia Smart Phone, with Caller ID',
'Motorola Smart Phone, Cordless',
'Sharp Wireless Fax, High-Speed',
'Samsung Smart Phone, with Caller ID',
'Novimex Executive Leather Armchair, Adjustable',
'Chromcraft Conference Table, Fully Assembled',
'Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind',
'Accos Rubber Bands, Assorted Sizes',
'Xerox Memo Slips, Recycled',
'Fellowes Shelving, Single Width',
'Green Bar Message Books, 8.5 x 11',
'Stockwell Clamps, 12 Pack',
'Avery Removable Labels, Alphabetical',
'Kleencut Box Cutter, High Speed',
'Tenex Box, Industrial',
'netTALK DUO VoIP Telephone Service',
'Brother Fax Machine, High-Speed',
'KitchenAid Stove, White',
'Hon Computer Table, with Bottom Storage',
'Apple iPhone 5S',
'SAFCO Executive Leather Armchair, Black']


# Create an instance of the Faker class
fake_gen = Faker()

# Generate synthetic orders data for our workflow
def generate_order(fake=fake_gen):
    """ This Function generates a single order and returns it as a json object.
    :param fake: An instance of the Faker class.
    :return: A dictionary containing the order data.
    :rtype: dict
    
    :Example:
    >>> generate_order()
    {'order_number': '12345678', 'product': 'Xerox Memo Slips, Recycled', 'quantity': 3, 'price': 8.99, 'customer_name': 'John Doe', 'customer_email': 'XXXXXXXXXXXXXXXXXXXX', 'order_date': '2022-03-04T13:34:00+00:00'}
    
    :Example:
    >>> generate_order(fake=Faker())
    {'order_number': '12345678', 'product': 'Xerox Memo Slips, Recycled', 'quantity': 3, 'price': 8.99, 'customer_name': 'John Doe', 'customer_email': 'XXXXXXXXXXXXXXXXXXXX', 'order_date': '2022-03-04T13:34:00+00:00'}
    
    :Example:
    >>> generate_order(fake=Faker("en_US"))
    
    """
    order_number = fake.unique.random_number(digits=8)
    product = fake.random_element(SAMPLE_PRODUCT_LIST)
    quantity = random.randint(1, 10)
    price = round(random.uniform(10.0, 100.0), 2)
    customer_name = fake.name()
    customer_email = fake.email()
    order_date = fake.date_time_between(start_date="-1y", end_date="now").isoformat() 

    return {
        "order_number": order_number,
        "product": product,
        "quantity": quantity,
        "price": price,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "order_date": order_date,
    }
