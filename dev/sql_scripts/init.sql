CREATE USER developer WITH PASSWORD '123';
ALTER USER developer WITH SUPERUSER;
CREATE DATABASE microservices_playground;
GRANT ALL PRIVILEGES ON DATABASE microservices_playground TO developer;
