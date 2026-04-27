BEGIN;

CREATE TABLE continents (
    id smallint GENERATED ALWAYS AS IDENTITY,
    country TEXT NOT NULL,
    continent TEXT NOT NULL
);

INSERT INTO continents (country, continent) VALUES
    ('USA', 'North America'),
    ('Canada', 'North America'),
    ('UK', 'Western Europe'),
    ('Germany', 'Western Europe'),
    ('Netherlands', 'Western Europe'),
    ('Sweden', 'Western Europe'),
    ('Australia', 'Asia-Pacific Developed'),
    ('Singapore', 'Asia-Pacific Developed'),
    ('India', 'South Asia'),
    ('Remote', 'Remote');

COMMIT;