select MAX(years_employed) as max_time from employees

select role, AVG(years_employed) as avg_emp from employees group by role

select building,sum(years_employed) as total from employees group by building

select role, count(*) as num_employees from employees group by role

select role,count(*) from employees group by role

select director,count(*) from movies group by director

select director,sum(international_sales+domestic_sales) as  total from movies
inner join boxoffice on movies.id=boxoffice.movie_id group by director

select max(id) from movies

INSERT INTO movies (id, title, director)
VALUES (11, 'Toy Story 4', 'John Lasseter');


INSERT INTO boxoffice VALUES (11, 8.7, 340000000, 270000000);
