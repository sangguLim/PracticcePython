use role alpha_platform;
use warehouse compute_wh;
use database alpha_platform;
use schema public;

put file://D:\Barra\history_csv\USMED_Rates_20201231.csv @~/copy_USMED_Rates;

--copy into load1 from @%load1/data1/ files=('test1.csv', 'test2.csv', 'test3.csv')

create or replace file format t_csvgz1header
type = csv
compression = gzip
field_delimiter= '|'
skip_header = 1
skip_blank_lines =true
error_on_column_count_mismatch = false;

copy into copy_USMED_Rates from @~/copy_USMED_Rates file_format = (format_name = 't_csvgz1header');
--copy into copy_port_index from @~/copy_port_index file_format = (format_name = 'csvgz1header');

remove @~;