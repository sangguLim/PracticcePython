use role alpha_platform;
use warehouse compute_wh;
use database alpha_platform;
use schema public;

put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft0_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft1_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft2_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft3_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft4_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft5_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom0_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom1_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom2_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom3_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom4_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom5_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv0_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv1_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv2_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv3_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv4_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv5_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq0_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq1_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq2_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq3_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq4_daily.csv @~/copy_port_const;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq5_daily.csv @~/copy_port_const;

put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft0_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft1_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft2_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft3_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft4_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\qrft5_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom0_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom1_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom2_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom3_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom4_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\amom5_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv0_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv1_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv2_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv3_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv4_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\hdiv5_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq0_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq1_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq2_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq3_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq4_index.csv @~/copy_port_index;
put file://C:\Users\USER\qraft\alphaplatform-db\etf_migration\legacy_csv_format_change\daily_data\nvq5_index.csv @~/copy_port_index;


create or replace file format csvgz1header
type = csv
compression = gzip
skip_header = 1
skip_blank_lines =true
error_on_column_count_mismatch = false;

copy into copy_port_const from @~/copy_port_const file_format = (format_name = 'csvgz1header');
copy into copy_port_index from @~/copy_port_index file_format = (format_name = 'csvgz1header');

remove @~;