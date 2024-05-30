insert into brands values(1,'Apple');
insert into brands values(2,'Samsung');
insert into brands values(3,'Nike');
insert into brands values(4,'Fortune');

select * from brands;

insert into inv_user values('tae@gmail.com','Kim Taehyung','1111','2023-12-30 12:40:00','Admin');
insert into inv_user values('jk@gmail.com','Jeon Jungkook','2222','2023-12-31 10:20:00','Manager');
insert into inv_user values('jimin@gmail.com','Park Jimin','3333','2023-12-29 10:20:00','Manager');

select * from inv_user;

insert into categories values(1,'Electronics');
insert into categories values(2,'Clothing');
insert into categories values(3,'Grocery');

select * from categories;

insert into stores values(1,'jung hoseok','khammam',9876543210);
insert into stores values(2,'Min Yoongi','Hyderabad',9456738904);
insert into stores values(3,'Kim Seok Jin','Banglore',9546385847);

select * from stores;

desc product;
insert into product values(1,1,1,1,'Samsung Galaxy',4,45000,'31-12-23');
insert into product values(2,1,1,1,'Airpods',3,19000,'27-12-23');
insert into product values(3,1,1,1,'Smart Watch',3,19000,'28-12-23');
insert into product values(4,2,3,2,'Air max',6,7000,'26-12-23');
insert into product values(5,3,4,3,'Refined Oil',6,750,'24-12-23');
select * from product;

insert into provides values(1,1,12);
insert into provides values(2,2,7);
insert into provides values(3,3,15);
insert into provides values(1,2,7);
insert into provides values(4,2,19);
insert into provides values(4,3,20);
select * from provides;

insert into customer_cart values(1,'Ram',9123456891);
insert into customer_cart values(2,'Kim Namjoon',7777777777);
insert into customer_cart values(3,'Xukai',9932156783);
select * from customer_cart;

insert into select_product values(1,2,2);
insert into select_product values(1,3,1);
insert into select_product values(2,3,3);
insert into select_product values(3,2,1);

select * from select_product;

insert into transactions values(1,57000,2000,5000,350,350,'card',1);
insert into transactions values(2,57000,57000,0,570,570,'cash',2);
insert into transactions values(3,19000,17000,2000,190,190,'card',3);
insert into transactions values(4,19000,17000,2000,190,190,'cash',4);
select * from transactions;

declare
due1 int(7);
cart_id1 int(7);
function get_cart(c_id int)return int is
begin
return (c_id);
end;
begin
cart_id1:=get_cart(&c_id);
select due into due1 from transactions where cart_id=cart_id1;
dbms_output.put_line(due1);
end;
-- Retrieve the names of all products along with their categories and brands:
SELECT p.pname AS Product_Name, c.category_name AS Category, b.bname AS Brand
FROM Product p
JOIN Categories c ON p.cid = c.cid
JOIN Brands b ON p.bid = b.bid;

-- Retrieve the names of all products along with their prices and the total amount paid in the corresponding transactions
SELECT p.pname AS Product_Name, p.price AS Price, t.total_amount AS Total_Amount_Paid
FROM Product p
JOIN Select_product sp ON p.pid = sp.pid
JOIN Transactions t ON sp.cust_id = t.cart_id;

-- Retrieve the names of all customers along with the total amount paid and due amount in their transactions:

SELECT c.user_name AS Customer_Name, t.total_amount AS Total_Amount_Paid, t.due AS Due_Amount
FROM Customer_cart c
JOIN Transactions t ON c.cust_id = t.cart_id;

-- Retrieve the names of all customers who purchased a specific product:

SELECT c.user_name AS Customer_Name
FROM Customer_cart c
JOIN Transactions t ON c.cust_id = t.cart_id
JOIN Select_product sp ON t.cart_id = sp.cust_id
JOIN Product p ON sp.pid = p.pid
WHERE p.pname = 'Airpods';

-- Retrieve the names of all products along with the stores where they are stocked:
SELECT p.pname AS Product_Name, s.sname AS Store_Name
FROM Product p
JOIN Stores s ON p.sid = s.sid;

