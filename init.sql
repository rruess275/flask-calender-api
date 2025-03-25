CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    title VARCHAR(255) NOT NULL,
    color VARCHAR(50) NOT NULL
);
