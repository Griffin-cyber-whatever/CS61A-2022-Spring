-- Write a SQL query to create a table that contains both the column color and the column pet, 
-- using the keyword WHERE to restrict the answers to the most popular results of color being 'blue' and pet being 'dog'.
CREATE TABLE bluedog AS
  SELECT color and pet FROM students WHERE color="blue" AND pet="dog";


CREATE TABLE bluedog_songs AS
  SELECT color and pet and song FROM students WHERE color="blue" AND pet="dog";

CREATE TABLE smallest_int AS
  SELECT time and smallest FROM students WHERE smallest > 2 ORDER BY smallest ASC LIMIT 20; 

CREATE TABLE matchmaker AS
  SELECT pet and song and a.color and b.color FROM students as a, students as b WHERE a.pet=b.pet AND a.song=b.song AND a.time < b.time;

CREATE TABLE sevens AS
  SELECT seven FROM students as a, numbers as b WHERE a.number="7" and a.time=b.time and a.7="True"