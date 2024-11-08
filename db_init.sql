CREATE DATABASE invoicedb;
CREATE USER invoiceadmin WITH PASSWORD 'invoicesafepass';
ALTER ROLE invoiceadmin SET client_encoding TO 'utf8';
ALTER ROLE invoiceadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE invoiceadmin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE invoiceadmin TO invoicedb;