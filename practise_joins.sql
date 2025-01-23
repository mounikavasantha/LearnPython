create table boxoffice

insert into boxoffice (movie_id, rating, domestic_sales, international_sales) VALUES
(5, 8.2, 380843261, 555900000),
(14, 7.4, 268492764, 475066843),
(8, 8, 206445654, 417277164),
(12, 6.4, 191452396, 368400000),
(3, 7.9, 245852179, 239163000),
(6, 8, 261441092, 370001000),
(9, 8.5, 223808164, 297503696),
(11, 8.4, 415004880, 648167031),
(1, 8.3, 191796233, 170162503),
(7, 7.2, 244082982, 217900167),
(10, 8.3, 293004164, 438338580),
(4, 8.1, 289916256, 272900000),
(2, 7.2, 162798565, 200600000),
(13, 7.2, 237283207, 301700000);

select * from boxoffice

select title,domestic_sales, international_sales from movies
inner join boxoffice on movies.id=boxoffice.movie_id

select title,domestic_sales, international_sales from movies
inner join boxoffice on movies.id=boxoffice.movie_id
where international_sales > domestic_sales

select title,rating from movies join boxoffice on movies.id=boxoffice.movie_id
order by rating desc



create table buildings (
    building_name VARCHAR(2),
    capacity INT
);

insert into buildings (building_name, capacity) VALUES
('1e', 24),
('1w', 32),
('2e', 16),
('2w', 20);

create table employees (
    role VARCHAR(20),
    name VARCHAR(50),
    building VARCHAR(2),
    years_employed INT
);

insert into employees (role, name, building, years_employed) VALUES
('Engineer', 'Becky A.', '1e', 4),
('Engineer', 'Dan B.', '1e', 2),
('Engineer', 'Sharon F.', '1e', 6),
('Engineer', 'Dan M.', '1e', 4),
('Engineer', 'Malcom S.', '1e', 1),
('Artist', 'Tylar S.', '2w', 2),
('Artist', 'Sherman D.', '2w', 8),
('Artist', 'Jakob J.', '2w', 6),
('Artist', 'Lillia A.', '2w', 7),
('Artist', 'Brandon J.', '2w', 7),
('Manager', 'Scott K.', '1e', 9),
('Manager', 'Shirlee M.', '1e', 3),
('Manager', 'Daria O.', '2w', 6);


select building from employees
select distinct building from employees

select name,role from employees where building is null

select distinct building_name from buildings
left join employees on building_name=building where role is null

select title,rating*10 as percentage
from movies
join boxoffice on movies.id=boxoffice.movie_id

select title,year from movies where year%2=0

