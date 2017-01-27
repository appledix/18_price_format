# Price Formatter

Данный скрипт обрабатывает переданное ему в виде числа или строки значение цены и приводит его к красивому виду. 

Он имеет два интерфейса:
* Программный - для использования в сторонней программе
* Command Line Interface - для запуска в ручном режиме из консоли

В случае передачи на обработку отрицательного значения, или некорректной строки (которую не удалось преобразовать в число) - скрипт выбрасывает исключение `ValueError`.

### Использование
* В терминале: `python3.5 format_price.py <обрабатываемое значение>`
* В сторонней программе:
    ```python
        from format_price import format_price 
        
        print(format_price(price))
    ```
### Примеры работы
* `3245.000000` -> `3 245`
* `12345678` -> `12 345 678`
* `1234.5678` -> `1 234.57`
* `1234,5678` -> `1 234.57`
* `0.00` -> `0`

### Установка скрипта 
В терминале: `git clone https://github.com/appledix/18_price_format.git`

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
