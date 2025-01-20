CREATE DATABASE movie_db;



INSERT INTO movies (title, director, year, length_minutes) VALUES
('Toy Story', 'John Lasseter', 1995, 81),
('A Bug''s Life', 'John Lasseter', 1998, 95),
('Toy Story 2', 'John Lasseter', 1999, 93),
('Monsters, Inc.', 'Pete Docter', 2001, 92),
('Finding Nemo', 'Andrew Stanton', 2003, 107),
('The Incredibles', 'Brad Bird', 2004, 116),
('Cars', 'John Lasseter', 2006, 117),
('Ratatouille', 'Brad Bird', 2007, 115),
('WALL-E', 'Andrew Stanton', 2008, 104),
('Up', 'Pete Docter', 2009, 101);




select title from movies
select director from movies
select title,director from movies
select title,year from movies
select * from movies;

select distinct title from movies

select id,title from movies where id =6
select title,year from movies where year between 2000 and 2010
select title,year from movies where year < 2000 or year> 2010
select title,year from movies where year <=2003

