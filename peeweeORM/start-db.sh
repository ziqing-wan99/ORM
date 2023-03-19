docker run --name my-postgres -e POSTGRES_PASSWORD=cs5421 -p 5432:5432 -d postgres
createdb mydatabase -h localhost -p 5432 -U postgres