create table categories(
cid int(5),
category_name varchar(20)
);
desc categories;

alter table categories add primary key(cid);

desc categories;

alter table inv_user
add primary key(user_id);

create table product(
pid INT(5) primary key,
cid int(5) references categories(cid),
bid int(5) references brands(bid),
sid int(5),
pname varchar(20),
p_stock int(5),
price int(5),
added_date date);

desc product;
create table stores(
sid int(5),
sname int(20),
address varchar(20),
mobno int(10)
);

alter table stores modify COLUMN sname varchar(20);
alter table stores modify COLUMN mobno bigint;
desc stores;

alter table stores add primary key(sid);

 alter table product add foreign key(sid)references stores(sid);

 desc product; 

create table provides(
bid int(5)references brands(bid),
sid int(5)references stores(sid),
discount int(5)); 

desc provides;