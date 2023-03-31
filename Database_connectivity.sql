create database Onego;
show databases;
Use Onego;
create table Customer_Details (Name varchar(30), 
Mobile_No varchar(30), Age varchar(30),
Gender varchar(30), Nationality varchar(30), 
Ref_Code varchar(30), Source varchar(30),
Destination varchar(30), Insurance varchar(30));
desc Customer_Details;
ALTER TABLE details
RENAME COLUMN Referral_Code to Ref_Code;
desc details;
ALTER TABLE details
RENAME COLUMN Referral_Code to Ref_Code;
desc Customer_Details;