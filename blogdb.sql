--
-- File generated with SQLiteStudio v3.3.3 on Sun Jun 12 16:37:54 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: About
CREATE TABLE About (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	content varchar,
	image varchar,
	status boolean
);

-- Table: Author
CREATE TABLE Author (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	image varchar,
	email varchar,
	info varchar,
	status boolean,
	date date
);
INSERT INTO Author (id, name, image, email, info, status, date) VALUES (4, 'name1', 'image1', 'email1', 'info1', 'status1', 'date1');
INSERT INTO Author (id, name, image, email, info, status, date) VALUES (5, 'name2', 'image2', 'email2', 'info2', 'status2', 'date2');
INSERT INTO Author (id, name, image, email, info, status, date) VALUES (6, 'name3', 'image3', 'email3', 'info3', 'status3', 'date3');

-- Table: Category
CREATE TABLE Category (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar
);
INSERT INTO Category (id, title) VALUES (1, 'cat1');
INSERT INTO Category (id, title) VALUES (2, 'cat2');
INSERT INTO Category (id, title) VALUES (3, 'cat3');
INSERT INTO Category (id, title) VALUES (4, 'cat4');

-- Table: Comment
CREATE TABLE Comment (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	email varchar,
	content varchar,
	status boolean,
	date datetime,
	post_id integer
);
INSERT INTO Comment (id, name, email, content, status, date, post_id) VALUES (1, 'sender1', 'email1', 'content1', 'status1', 'date1', 1);
INSERT INTO Comment (id, name, email, content, status, date, post_id) VALUES (2, 'sender2', 'email2', 'content2', 'status2', 'date2', 1);
INSERT INTO Comment (id, name, email, content, status, date, post_id) VALUES (3, 'sender3', 'email3', 'content3', 'status3', 'date3', 2);
INSERT INTO Comment (id, name, email, content, status, date, post_id) VALUES (4, 'sender4', 'email4', 'content4', 'status4', 'date4', 3);

-- Table: File
CREATE TABLE File (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar ,
	type varchar ,
	image varchar
);

-- Table: Message
CREATE TABLE Message (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	email varchar,
	subject varchar,
	content varchar,
	date datetime
);

-- Table: Navigation
CREATE TABLE Navigation (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	url varchar
);

-- Table: Post
CREATE TABLE Post (
	id integer PRIMARY KEY AUTOINCREMENT,
	author_id integer,
	category_id integer,
	title varchar,
	content text,
	image varchar
);
INSERT INTO Post (id, author_id, category_id, title, content, image) VALUES (1, 6, 2, 'post1', 'content1', 'image1');
INSERT INTO Post (id, author_id, category_id, title, content, image) VALUES (2, 6, 3, 'post2', 'content2', 'image2');
INSERT INTO Post (id, author_id, category_id, title, content, image) VALUES (3, 4, 1, 'post3', 'content3', 'image3');
INSERT INTO Post (id, author_id, category_id, title, content, image) VALUES (4, 5, 3, 'post4', 'content4', 'image4');

-- Table: PostFile
CREATE TABLE PostFile (
	id integer PRIMARY KEY AUTOINCREMENT,
	post_id integer,
	file_id integer
);

-- Table: PostTag
CREATE TABLE PostTag (
	id integer PRIMARY KEY AUTOINCREMENT,
	post_id integer,
	tag_id integer
);
INSERT INTO PostTag (id, post_id, tag_id) VALUES (1, 1, 2);
INSERT INTO PostTag (id, post_id, tag_id) VALUES (2, 1, 3);
INSERT INTO PostTag (id, post_id, tag_id) VALUES (3, 2, 2);
INSERT INTO PostTag (id, post_id, tag_id) VALUES (4, 3, 1);

-- Table: Setting
CREATE TABLE Setting (
	id integer PRIMARY KEY AUTOINCREMENT,
	address varchar,
	number varchar,
	email string,
	logo varchar,
	copyright varchar
);

-- Table: Slider
CREATE TABLE Slider (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	content varchar,
	image varchar,
	date datetime,
	status boolean
);

-- Table: Social
CREATE TABLE Social (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar,
	path varchar,
	url varchar
);

-- Table: SubNavigation
CREATE TABLE SubNavigation (
	id integer PRIMARY KEY AUTOINCREMENT,
	navigation_id integer,
	title varchar,
	url varchar
);

-- Table: Tags
CREATE TABLE Tags (
	id integer PRIMARY KEY AUTOINCREMENT,
	title varchar
);
INSERT INTO Tags (id, title) VALUES (1, 'title1');
INSERT INTO Tags (id, title) VALUES (2, 'title2');
INSERT INTO Tags (id, title) VALUES (3, 'title3');
INSERT INTO Tags (id, title) VALUES (4, 'title4');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
