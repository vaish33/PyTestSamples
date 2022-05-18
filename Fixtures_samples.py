"""
In testing, a fixture provides a defined, reliable and consistent context for the tests. 
This could include environment (for example a database configured with known parameters) or 
content (such as a dataset).

Fixtures define the steps and data that constitute the arrange phase of a test (see Anatomy of a test). 
In pytest, they are functions you define that serve this purpose. 
They can also be used to define a test’s act phase; this is a powerful technique for 
designing more complex tests.

The services, state, or other operating environments set up by fixtures are accessed by test functions 
through arguments. For each fixture used by a test function there is typically a 
parameter (named after the fixture) in the test function’s definition.

We can tell pytest that a particular function is a fixture by decorating it with @pytest.fixture. 
Here’s a simple example of what a fixture in pytest might look like:
"""


import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)