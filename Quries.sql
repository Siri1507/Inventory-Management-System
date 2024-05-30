use inv_manage;
create table brands(
    bid int(5),
    bname varchar(20)
);
desc brands;
alter table brands add primary key(bid);

create table inv_user(
user_id varchar(20),
user_name varchar(20),
user_password varchar(20),
last_login timestamp,
user_type varchar(10)
);

desc inv_user;

create table categories(
cid int(5),
category_name varchar(20)
);

desc categories;

> create table customer_cart(
cust_id int(5) primary key,
user_name varchar(20),
mobno int(10)
);

alter table customer_cart modify COLUMN mobno bigint;
desc customer_cart;

create table select_product(
cust_id int(5) references customer_cart(cust_id),
pid int(5)references product(pid),
quantity int(4)
);

desc select_product;

create table transactions(
id int(5) primary key,
total_amount int(5),
paid int(5),
due int(5),
gst int(3),
discount int(5),
payment_method varchar(10),
cart_id int(5) references customer_cart(cust_id)
);

desc transactions;

create table invoice(
item_no int(5),
product_name varchar(20),
quantity int(5),
net_price int(5),
transaction_id int(5)references transactions(id)
);

desc invoice;
