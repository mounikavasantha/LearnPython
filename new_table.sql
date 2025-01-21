create table north_american_cities(city VARCHAR(255),
    country VARCHAR(255),
    population INT,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6))


INSERT INTO north_american_cities (city, country, population, latitude, longitude) VALUES
('Guadalajara', 'Mexico', 1500800, 20.659699, -103.349609),
('Toronto', 'Canada', 2795060, 43.653226, -79.383184),
('Houston', 'United States', 2195914, 29.760427, -95.369803),
('New York', 'United States', 8405837, 40.712784, -74.005941),
('Philadelphia', 'United States', 1553165, 39.952584, -75.165222),
('Havana', 'Cuba', 2106146, 23.05407, -82.345189),
('Mexico City', 'Mexico', 8555500, 19.432608, -99.133208),
('Phoenix', 'United States', 1513367, 33.448377, -112.074037),
('Los Angeles', 'United States', 3884307, 34.052234, -118.243685),
('Ecatepec de Morelos', 'Mexico', 1742000, 19.601841, -99.050674),
('Montreal', 'Canada', 1717767, 45.501689, -73.567256),
('Chicago', 'United States', 2718782, 41.878114, -87.629798);


select city,population from north_american_cities
select city,population from north_american_cities where country='Canada'

SELECT city, country, population, latitude, longitude
FROM north_american_cities
WHERE country = 'United States'
ORDER BY latitude DESC;

SELECT city, longitude FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;

select city,population from north_american_cities where country = 'Mexico'
order by population desc limit 2

select city,population from north_american_cities where country like 'United States'
order by population desc limit 2 offset 2
