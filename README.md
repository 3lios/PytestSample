# PytestSample
pytest -p no:cacheprovider -v
pytest -p no:cacheprovider -k core -v
pytest -p no:cacheprovider -m core -v --disable-warnings
pytest -p no:cacheprovider -m div -v --disable-warnings
pytest -p no:cacheprovider -k mul -v --disable-warnings

pytest -p no:cacheprovider -n 4 -v --disable-warnings
pytest -p no:cacheprovider -n 4 -v --disable-warnings --excelreport=report.xls
pytest projectA\test_testcase2.py -p no:cacheprovider -v --disable-warnings --excelreport=report.xls
pytest projectA\test_testcase2.py -p no:cacheprovider -v --disable-warnings --html=report.html
