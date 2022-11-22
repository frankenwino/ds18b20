from ds18b20.ds18b20 import DS18B20

def test_celsius():
    # Arrange
    t = DS18B20()
    # Act
    celsius = t.celsius()
    # Assert
    assert isinstance(celsius, float)

def test_farenheit():
    # Arrange
    t = DS18B20()
    # Act
    farenheit = t.farenheit()
    # Assert
    assert isinstance(farenheit, float)
    
def test_now():
    # Arrange
    n = DS18B20()
    # Act
    current_time = n.now()
    # Assert
    assert isinstance(current_time, str)