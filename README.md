PYOADFE Hello -- оформляем свой пакет для Python
================================================

1. Составляем файл `pyproject.toml`. Можно воспользоваться [документацией по оформлению `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
   на официальном сайте.
2. После этого пакет можно установить
   - локально `pip install -e .`
   - из git, например `pip install git+https://github.com/pyoadfe/pyoadfe-hello.git`
3. Загрузим пакет на [PyPI](https://pypi.org/), где хранится индекс пакетов для Python, которым пользуется команда `pip install`.
   - соберём архив: `python -m build --sdist`
   - [инструкция по регистрации настройке тестового индекса PyPI](https://packaging.python.org/en/latest/guides/using-testpypi/)
   - отправим в [тестовый индекс PyPI](https://test.pypi.org):`twine upload --repository testpypi dist/pyoadfe_hello-2024.0.tar.gz`
   - проверим возможность установки из тестового индекса: `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/  pyoadfe-hello`
