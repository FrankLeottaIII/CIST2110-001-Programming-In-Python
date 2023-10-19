import pytest

def add(a, b):
    """_summary_
    add two numbers together

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)

def main():
    add("Two", 3)
    
if __name__ == "__main__":
    main()
