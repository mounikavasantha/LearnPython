delete from movies where year<2005

delete from movies where director='Andrew Stanton'


create table if not exists database (name text,version float, download_count integer)

alter table movies add column aspect_ratio float default 2.9

drop table if exists database
