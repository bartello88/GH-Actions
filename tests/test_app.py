import pytest
from app import Dog

def test_home():
  dog = Dog("Reksio")
  assert dog.name == "Reksio"
