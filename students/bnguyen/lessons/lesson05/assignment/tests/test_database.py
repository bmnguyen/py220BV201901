"""
grade lesson 5
"""

import os
import pytest

from lesson05.assignment import database as l


# Original test has lower case in prouct_type's value - corrected.
@pytest.fixture
def _show_available_products():
    return {
        'P000001': {'description': 'Chair Red leather', 'product_type': 'Livingroom',
                    'quantity_available': '21'},
        'P000002': {'description': 'Table Oak', 'product_type': 'Livingroom',
                    'quantity_available': '4'},
        'P000003': {'description': 'Couch Green cloth', 'product_type': 'Livingroom',
                    'quantity_available': '10'},
        'P000004': {'description': 'Dining table Plastic', 'product_type': 'Kitchen',
                    'quantity_available': '23'},
        'P000005': {'description': 'Stool Black ash', 'product_type': 'Kitchen',
                    'quantity_available': '12'}
        }


@pytest.fixture
def _show_rentals():
    return {
        'C000001': {'name': 'Shea Boehm', 'address': '3343 Sallie Gateway',
                    'phone_number': '508.104.0644 x4976', 'email': 'Alexander.Weber@monroe.com'},
        'C000003': {'name': 'Elfrieda Skiles', 'address': '3180 Mose Row',
                    'phone_number': '(839)825-0058', 'email': 'Mylene_Smitham@hannah.co.uk'
                    }
        }


@pytest.fixture
def _show_rentals_p():
    return {
        'C000001': {'name': 'Shea Boehm', 'address': '3343 Sallie Gateway',
                    'phone_number': '508.104.0644 x4976', 'email': 'Alexander.Weber@monroe.com',
                    'product_id': 'P000003'},
        'C000003': {'name': 'Elfrieda Skiles', 'address': '3180 Mose Row',
                    'phone_number': '(839)825-0058', 'email': 'Mylene_Smitham@hannah.co.uk',
                    'product_id': 'P000003'
                    }
        }


def test_process_csv_product(_show_available_products):
    """
    This is to test the process_csv with product data and file.
    """
    test_dict, a, e = l.process_csv("product.csv", "product_id")

    assert test_dict['P000001'] == _show_available_products['P000001']
    assert a == 5
    assert e == 0


def test_process_csv_rental(_show_rentals_p):
    """
    This is to test the process_csv with product data and file.
    """
    test_dict, a, e = l.process_csv("rental.csv", "user_id")

    assert test_dict['C000003'] == _show_rentals_p['C000003']
    assert a == 9
    assert e == 0


def test_import_data():
    """ import """

    data_dir = os.path.dirname(os.path.abspath(__file__))
    added, errors = l.import_data(data_dir, "product.csv", "customer.csv", "rental.csv")

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (5, 11, 9)
    assert errors == (0, 0, 0)


def test_show_available_products(_show_available_products):
    """ available products """
    students_response = l.show_available_products()
    assert students_response == _show_available_products


def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = l.show_rentals("P000003")
    assert students_response == _show_rentals

    # clean up for all tests.
    l.drop_db("y")
