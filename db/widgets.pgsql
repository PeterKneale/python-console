drop table widgets;

create table widgets (
   id int primary key,
   name varchar(10)
);

insert into widgets (id,name) values(1,'Apple');

select * from widgets;