# Log-Analysis

## Introduction
It is an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Steps to use
* download the python file.
* then run this file.

## Contents
* this file uses the database news and fetches data from the tables.
* It contains 3 functions that will fetch data from the database.

## Views created to entertain 3 functionalities
* create view popular_articles as select title,count(title) as views from log,articles where path=concat('/article/',articles.slug) group     by title order by views desc;
* create view first_view as select authors.id, articles.title from authors, articles where articles.author = authors.id;
* create view second_view as select first_view.id, first_view.title, popular_articles.views from first_view, popular_articles where           first_view.title = popular_articles.title;
* create view third_view as select authors.name, (select sum(views) from second_view where second_view.id = authors.id) as views from         authors;
* create view fourth_view as select time::timestamp::date, count(status) as total from log group by time::timestamp::date order by           time::timestamp::date;
* create view fifth_view as select time::timestamp::date, count(status) as fault from log where status = '404 NOT FOUND' group by             time::timestamp::date;
* create view sixth_view as select fourth_view.time, (fault::float * 100)/( total::float) as errors from fourth_view, fifth_view where       fourth_view.time = fifth_view.time;
