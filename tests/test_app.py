import pytest
from app import Dog

def test_home():
  dog = Dog("Reksio", None)
  assert dog.name == "Reksio"

def test_age():
  dog = Dog("Pluto", 27)
  assert dog.age == 27
