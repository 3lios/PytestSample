# PytestSample
pytest -v
pytest -k core -v
pytest -m core -v --disable-warnings
pytest -m div -v --disable-warnings
pytest -k mul -v --disable-warnings

pytest -n 4 -v --disable-warnings
pytest -n 4 -v --disable-warnings --excel-report=report.xls

pytest projectA\test_testcase2.py -v --disable-warnings --excel-report=report.xls
pytest projectA\test_testcase2.py -v --disable-warnings --html=report.html

pytest projectB\test_testcase1.py -m cls -v --disable-warnings