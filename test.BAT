echo daily_file_to_csv RunStart: %date% %time% >> C:\\Users\\USER\\Desktop\\task\\testCode\\test_log.txt
python "C:\\Users\\USER\\Desktop\\task\\testCode\\test_date_range.py" >> C:\\Users\\USER\\Desktop\\task\\testCode\\test_log.txt
echo test_date_range RunEnd: %date% %time% >> C:\\Users\\USER\\Desktop\\task\\testCode\\test_log.txt