PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "To_apply" (
"ApplyID"INTEGER PRIMARY KEY ON CONFLICT IGNORE AUTOINCREMENT,
"PersonID"INTEGER NOT NULL,
"ApplyDate"DATETIME NOT NULL,
"JobID"INTEGER NOT NULL,
CONSTRAINT "FK_Apply_Job" FOREIGN KEY("JobID") REFERENCES "Job"("JobID") ON DELETE CASCADE,
CONSTRAINT "FK_Apply_Person" FOREIGN KEY("ApplyID") REFERENCES "Person"("PersonID") ON DELETE CASCADE,
CONSTRAINT "UK_Apply" UNIQUE("PersonID","JobID")
);
INSERT INTO To_apply VALUES(2,3,'2020-04-04 00:00:00',1);
INSERT INTO To_apply VALUES(3,5,'2020-09-09 00:00:00',2);
CREATE TABLE Post_Hashtags
(
  Hashtag CHAR(30) NOT NULL,
  PostID INTEGER NOT NULL,
  PRIMARY KEY (Hashtag, PostID),
  FOREIGN KEY (PostID) REFERENCES Post(PostID) ON DELETE CASCADE
);
INSERT INTO Post_Hashtags VALUES('Computer',1);
INSERT INTO Post_Hashtags VALUES('machinelearning',3);
INSERT INTO Post_Hashtags VALUES('datascience',3);
INSERT INTO Post_Hashtags VALUES('washington_university',1);
INSERT INTO Post_Hashtags VALUES('coursera',1);
INSERT INTO Post_Hashtags VALUES('datascience',1);
INSERT INTO Post_Hashtags VALUES('machinelearning',1);
INSERT INTO Post_Hashtags VALUES('python',1);
INSERT INTO Post_Hashtags VALUES('sorting',2);
INSERT INTO Post_Hashtags VALUES('algorithms',2);
INSERT INTO Post_Hashtags VALUES('timecomplexity',2);
INSERT INTO Post_Hashtags VALUES('visualization',2);
INSERT INTO Post_Hashtags VALUES('datastructure',2);
INSERT INTO Post_Hashtags VALUES('University',1);
INSERT INTO Post_Hashtags VALUES('University',2);
INSERT INTO Post_Hashtags VALUES('University',3);
INSERT INTO Post_Hashtags VALUES('coursera',2);
INSERT INTO Post_Hashtags VALUES('deeplearning',4);
INSERT INTO Post_Hashtags VALUES('newyear',3);
INSERT INTO Post_Hashtags VALUES('newyear',4);
INSERT INTO Post_Hashtags VALUES('newyear',6);
INSERT INTO Post_Hashtags VALUES('datascience',5);
INSERT INTO Post_Hashtags VALUES('University',5);
INSERT INTO Post_Hashtags VALUES('datascience',4);
INSERT INTO Post_Hashtags VALUES('University',4);
CREATE TABLE Person_Skill
(
  Skill CHAR(50) NOT NULL,
  PersonID INTEGER NOT NULL,
  PRIMARY KEY (Skill, PersonID) ON CONFLICT IGNORE,
  CONSTRAINT FK_Person_skill FOREIGN KEY (PersonID) REFERENCES Person(PersonID) ON DELETE CASCADE
);
INSERT INTO Person_Skill VALUES('Python',4);
INSERT INTO Person_Skill VALUES('Java',4);
INSERT INTO Person_Skill VALUES('SQL',4);
INSERT INTO Person_Skill VALUES('Machine learning',4);
INSERT INTO Person_Skill VALUES('Management',3);
INSERT INTO Person_Skill VALUES('Leadership',3);
INSERT INTO Person_Skill VALUES('Public speech',3);
INSERT INTO Person_Skill VALUES('Solo perform',1);
INSERT INTO Person_Skill VALUES('Coaching',2);
INSERT INTO Person_Skill VALUES('SQL',3);
INSERT INTO Person_Skill VALUES('Horse Riding',2);
INSERT INTO Person_Skill VALUES('Python',1);
INSERT INTO Person_Skill VALUES('Python',2);
INSERT INTO Person_Skill VALUES('Python',3);
INSERT INTO Person_Skill VALUES('SQL',2);
CREATE TABLE Person_Favorite
(
  Favorite CHAR(50) NOT NULL,
  PersonID INTEGER NOT NULL,
  PRIMARY KEY (Favorite, PersonID),
  CONSTRAINT FK_Person_Favorite FOREIGN KEY (PersonID) REFERENCES Person(PersonID) ON DELETE CASCADE
);
INSERT INTO Person_Favorite VALUES('Painting',1);
INSERT INTO Person_Favorite VALUES('Horse riding',1);
INSERT INTO Person_Favorite VALUES('Music',2);
INSERT INTO Person_Favorite VALUES('Watching movies',3);
INSERT INTO Person_Favorite VALUES('Deep learning',4);
INSERT INTO Person_Favorite VALUES('Sci-fi movies',4);
CREATE TABLE IF NOT EXISTS "To_share" (
"IP"CHAR(24) NOT NULL,
"PersonID"INTEGER NOT NULL,
"PostID"INTEGER NOT NULL,
CONSTRAINT "FK_Share_Post" FOREIGN KEY("PostID") REFERENCES "Post"("PostID") ON DELETE CASCADE,
CONSTRAINT "FK_Share_Person" FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE,
PRIMARY KEY("PersonID","PostID")
);
INSERT INTO To_share VALUES('31.14.84.5',4,1);
INSERT INTO To_share VALUES('31.14.84.2',3,3);
INSERT INTO To_share VALUES('31.14.84.2',3,2);
INSERT INTO To_share VALUES('31.14.84.2',1,4);
INSERT INTO To_share VALUES('31.14.84.5',4,5);
INSERT INTO To_share VALUES('31.14.84.2',3,6);
CREATE TABLE IF NOT EXISTS "Poll_Option" (
"Option"char(100) NOT NULL,
"PollID"INTEGER NOT NULL,
"OptionID"INTEGER NOT NULL,
PRIMARY KEY("PollID","OptionID") ON CONFLICT IGNORE,
CONSTRAINT "FK_Poll_Option" FOREIGN KEY("PollID") REFERENCES "Poll"("PollID") ON DELETE CASCADE,
CONSTRAINT "UK_Person" UNIQUE("Option","PollID", "OptionID")
);
INSERT INTO Poll_Option VALUES('Great!',1,1);
INSERT INTO Poll_Option VALUES('Not bad!',1,2);
INSERT INTO Poll_Option VALUES('Awful!',1,3);
CREATE TABLE IF NOT EXISTS "To_participate_poll" (
"PersonID"INTEGER NOT NULL,
"ParticipateDate"DATETIME NOT NULL,
"PollID"INTEGER NOT NULL,
"SelectedOption"INTEGER NOT NULL,
PRIMARY KEY("PollID","PersonID"),
CONSTRAINT "FK_Participate_Poll" FOREIGN KEY("PollID") REFERENCES "Poll"("PollID") ON DELETE CASCADE,
CONSTRAINT "FK_Participate_Person" FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE
);
INSERT INTO To_participate_poll VALUES(1,19,1,1);
INSERT INTO To_participate_poll VALUES(4,20,1,1);
CREATE TABLE IF NOT EXISTS "To_participate_event" (
"ParticipationID"INTEGER PRIMARY KEY AUTOINCREMENT,
"PersonID"INTEGER NOT NULL,
"EventID"INTEGER NOT NULL,
CONSTRAINT "FK_Participate_Person" FOREIGN KEY("PersonID") REFERENCES "PersonID"("PersonID") ON DELETE CASCADE,
CONSTRAINT "FK_Participate_Event" FOREIGN KEY("EventID") REFERENCES "EventID"("EventID") ON DELETE CASCADE
);
INSERT INTO To_participate_event VALUES(1,2,1);
INSERT INTO To_participate_event VALUES(3,2,1);
INSERT INTO To_participate_event VALUES(4,3,1);
INSERT INTO To_participate_event VALUES(5,4,1);
CREATE TABLE IF NOT EXISTS "To_like" (
"PersonID"INTEGER NOT NULL,
"PostID"INTEGER NOT NULL,
"LikeDate"DATETIME NOT NULL,
"ReactionID" INTEGER NOT NULL,
CONSTRAINT "PK_To_Like" PRIMARY KEY(PersonID, PostID) ON CONFLICT IGNORE,
CONSTRAINT "FK_Like_Post" FOREIGN KEY("PostID") REFERENCES "Post"("PostID") ON DELETE CASCADE,
CONSTRAINT "FK_Like_Person" FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE
);
INSERT INTO To_like VALUES(1,1,'2019-04-04 00:19:56',1);
INSERT INTO To_like VALUES(1,3,'2020-03-05 23:55:43',2);
INSERT INTO To_like VALUES(4,4,'2021-01-01 23:56:19',2);
INSERT INTO To_like VALUES(3,1,'2018-12-23 18:18:09',3);
CREATE TABLE IF NOT EXISTS "Person" (
"PersonID"INTEGER NOT NULL,
"Gender"CHAR(1) NOT NULL,
"First_name"CHAR(20) NOT NULL,
"Last_name"CHAR(20) NOT NULL,
"Education"VARCHAR,
"Current_position"VARCHAR,
"Nationality"CHAR(20) NOT NULL,
"BornDate"DATETIME NOT NULL,
"RegisterDate"DATETIME NOT NULL,
PRIMARY KEY("PersonID") ON CONFLICT IGNORE,
CONSTRAINT "UK_Person" UNIQUE("First_name","Last_name", "BornDate")
);
INSERT INTO Person VALUES(1,'M','Alex','Rybak',NULL,'Musician','Spanish','1998-01-05 00:00:00','2005-05-05 00:00:00');
INSERT INTO Person VALUES(2,'M','George','Michael',NULL,'Athlete','Brazillian','1998-11-25 00:00:00','2007-01-01 00:00:00');
INSERT INTO Person VALUES(3,'F','Sarah','Handerson','PHD candidate at University of Amesterdam','CEO at Databricks','American','1990-07-15 00:00:00','2006-01-13 00:00:00');
INSERT INTO Person VALUES(4,'F','Mary','Johnsson','Computer Engineering Student','Software Engineer','American','1994-04-04 00:00:00','2004-04-04 00:00:00');
INSERT INTO Person VALUES(5,'M','Jack','Street',NULL,'Student','Canadian','1994-04-14 00:00:00','2015-12-12 00:00:00');
INSERT INTO Person VALUES(6,'F','Tina','Seelig','Stanford University School of Medicine','Entrepreneur','American','1958-12-01 00:00:00','2019-11-02 00:00:00');
INSERT INTO Person VALUES(7,'M','Behazd','Shomali','Computer Engineering','Undergraduate Student','Iranian','2000-08-20 00:00:00','2021-01-07 00:00:00');
CREATE TABLE IF NOT EXISTS "Job" (
"JobID"INTEGER NOT NULL,
"Job_description"VARCHAR NOT NULL,
"Seniority_Level"CHAR(20) NOT NULL,
"Company_name"CHAR(100) NOT NULL,
"Employment_type"CHAR(20) NOT NULL,
"Benefits"VARCAHR,
"Qualifications"VARCAHR,
PRIMARY KEY("JobID") ON CONFLICT IGNORE
);
INSERT INTO Job VALUES(2,replace('Create dashboards to gain greater insight into our models and data streams\nQuality Assurance of our Machine Learning models.\nAssess model performance, data compliance, etc\nImprove the Machine Learning models thanks to the findings of the above','\n',char(10)),'Internship','3D Hubs','Internship','Opportunity to have impact in a high paced culture and accelerate our growth # Dynamic, international team of 140+ people from (30+ nationalities) growing to 200+ in the next 12-18 months # Awesome office location in the harbour of Amsterdam (Houthavens) # 700 euros per month # Free healthy lunches and team bonding over Friday events # Generous stock option plan # Learn more about us on our Office Instagram and Careers page','You are currently a 3rd/4th year student and enrolled student for a Bachelors or Master’s degree in Computer Science / Data Science / Machine Learning or a related field (No research students) # You are available for 5 months minimum, 32-40 hours per week # You are eligible to work in the Netherlands or enrolled in University of the Netherlands # Good knowledge of Python # Basic knowledge of Machine Learning # Experience with Python Scientific stack (Numpy, Matplotlib, Scikit-learn, etc.) # Some knowledge of SQLEnjoy working with passionate engineers # Thrive in a dynamic, creative, and innovation focused environmentHave solid English skills, both spoken and written');
INSERT INTO Job VALUES(3,'We aim to deliver our clients with unprecedented, extensive, and up-to-date data around valuable tech-companies. As part of the Data Team, the Data Science Intern’s main objective is to contribute to executing upon this data-strategy. At Dealroom.co we value intelligent, articulate and motivated individuals who want to learn a great team and rapidly growing business, but who also thrive working independently with clearly defined responsibilities.','Internship','Dealroom.co','Internship',replace('An internship compensation fee # Freedom and responsibility to execute on your own ideas # Positive, empathetic and outward-focused colleagues and customers that are the forefront of innovation and technology # A great office, in the heart of a vibrant neighbourhood # Training on the job to improve your SaaS knowledge plus an extensive training budget # A daily office lunch and many more perks upcoming # Travel reimbursement #\nThe minimum length for the internship is 4 months and a maximum length of 6 months','\n',char(10)),'Currently enrolled in the last year of an undergraduate or graduate level studies with a declared major in Data Science, Mathematics, Statistics, Econometrics, Business, Economics, or similar field of study # You are enrolled in a Dutch college/university # Python skills are mandatory # You’re proficient in Excel # You are meticulous and creative # Good analytical skills, good with numbers # You enjoy solving problems # NLP knowledge (bonus) # You have a passion for technology, startups and venture capital markets.');
INSERT INTO Job VALUES(4,'At Arm you will shape the future of technology and collaborate in the development of next generation GPUs, CPUs, Machine Learning accelerators, and System components to power billions of devices worldwide.','Internship','Arm','Full-time','As an intern you will directly influence the development of hardware # IP that is used extensively in a wide variety of devices, from mobile phones and tablets to sensors to servers','Use of UNIX and shell programming # Strong knowledge in C programming language # Ability to express ideas and communicate effectively # Fluency in English');
INSERT INTO Job VALUES(5,replace('As a Software Development Engineer intern, you will be responsible for data-driven improvements to our models. Regardless of the team you join, your work will directly impact our customers.\nEnsure data quality throughout all stages of acquisition and processing, including such areas as data sourcing/collection, ground truth generation, normalization, transformation, cross-lingual alignment/mapping, etc.\nClean, analyze and select data to achieve goals.\nBuild and release models that elevate the customer experience and track impact over time.','\n',char(10)),'Internship','Amazon','Full-time',NULL,'Excellent written and verbal communication skills in English # You must have the right to work in Austria # Bachelor’s or Master''s Degree in Computer Science or related field # Knowledge of fundamentals in computer vision and machine learning # Experience with hardware/software integration and real-time systems # Strong coding skills in at least C++ and Python #Excellent problem solving ability');
CREATE TABLE IF NOT EXISTS "Poll" (
"Question"VARCHAR NOT NULL,
"PollID"INTEGER NOT NULL,
"PostID"INTEGER NOT NULL,
PRIMARY KEY("PollID") ON CONFLICT IGNORE
);
INSERT INTO Poll VALUES('How doyou guys think about this?',1,1);
CREATE TABLE IF NOT EXISTS "Post" (
"Content"VARCHAR NOT NULL,
"Views"INTEGER DEFAULT 0,
"PostID"INTEGER NOT NULL,
"Date"DATETIME NOT NULL,
"PersonID"INTEGER NOT NULL,
FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE,
PRIMARY KEY("PostID")
);
INSERT INTO Post VALUES(replace('Recently, I completed a course offered by University of Washington on Coursera. Throughout this course, the basics of the following topics were covered:\nRegression\nClassification\nClustering and Similarity\nRecommending Systems\nDeep Learning\nNow am I a data scientist? hahaha... of course NOT! This is just the beginning of this long way and I''m notably optimistic about this onward path.','\n',char(10)),45,1,'2002-01-05 17:19:20',4);
INSERT INTO Post VALUES(replace('While I was studying for Data Structure exam (as I wasn''t really in the mood!) I toughly found a way to visualize different sorting algorithms without knowing "React Native". What I actually did is using "Graphics.h" header file to be able to have some simple shapes and limited number of colors while programming in C++.\nFirst the user chooses the data size. Then a random data-set (the values range from 0 to 400) will be generated based on the input size. After generating random data, it''s time to show them! To do this each value is mapped to a line whose length is that datum value.\nIn this video I''m showing the difference between "Bubble Sort" and "Selection Sort" which we already know that the time complexity of both of them is O(n^2). But as it is obvious Selection sort is so fast while Bubble sort which its data size is exactly double is actually taking much more time!!!!','\n',char(10)),142,2,'2003-12-15 17:19:20',3);
INSERT INTO Post VALUES('Team MLI wishes you a very happy new year!',999,3,'2021-01-01 18:26:45',2);
INSERT INTO Post VALUES(replace('2020 was a test for the software that runs the simulation. Bugs were found. Humans survived. New version deployed.\n\nLet''s make 2021 an amazing bounce-back year. Love you all!','\n',char(10)),1335,4,'2021-01-01 20:07:03',1);
INSERT INTO Post VALUES(replace('Today is the first day of the new year in the Gregorian Calendar! I wish all of you a pleasant, productive, and most importantly creative new year!\n\nWhat about you making a difference for others in 2021?\n\nIf you trust some sources despite all those bad news, mankind is making progress. World poverty went down significantly in recent history. World hunger is going down, too. We see fewer and fewer wars. Life expectancy is rising a lot. There are more and more rights for everyone. And we are on the way to reintegrate our existence with nature.\n\nAll of this has been a group effort. If you read this, I am sure that you contributed to that. Keep up the great work! Help others and make a difference for them!\n\nHappy 2021!','\n',char(10)),21,5,'2021-01-01 21:12:04',4);
INSERT INTO Post VALUES('Happy New Year, everyone. Thank you for being a part of my network. I have learned so much from many of you and have been so inspired by the conversations. I have also made genuine friends. Thank you.',231,6,'2021-01-01 20:41:23',3);
INSERT INTO Post VALUES('The Dream Chaser is an American reusable lifting-body spaceplane being developed by Sierra Nevada Corporation (SNC) Space Systems. Originally intended as a crewed vehicle, the Dream Chaser Space System, to be produced after the cargo variant, Dream Chaser Cargo System, is operational.',0,7,'2021-01-07 01:48:34',5);
INSERT INTO Post VALUES(replace('Machine learning skills are in high demand, and people are using this transformative technology to make global impacts in so many fields.\nStart exploring the incredible world of machinelearning today!','\n',char(10)),0,8,'2021-01-04 21:45:59',6);
INSERT INTO Post VALUES('27 years ago in 1993, Yann LeCun showing the world''s first convolutional neural network for digit recognition. Today we call it as a MNIST handwritten digit classification.',421,9,'2021-01-01 12:54:12',5);
INSERT INTO Post VALUES(replace('A wearable technology that helps workers in performing their everyday activities and allows them to replicate the dynamic movements of the shoulders while wrapping the body like a second skin.\n\n\nThe MATE exoskeleton suit has been designed to improve the quality of life at work by providing consistent, advanced shoulder and arm assistance during repetitive operations and daily tasks.','\n',char(10)),124,10,'2021-01-05 21:43:56',5);
CREATE TABLE IF NOT EXISTS "To_comment" (
"CommentID"INTEGER PRIMARY KEY AUTOINCREMENT,
"Content"VARCHAR NOT NULL,
"PersonID"INTEGER NOT NULL,
"PostID"INTEGER NOT NULL,
"CommentDate"DATETIME NOT NULL,
CONSTRAINT "FK_Comment_Post" FOREIGN KEY("PostID") REFERENCES "Post"("PostID") ON DELETE CASCADE,
CONSTRAINT "FK_Comment_Person" FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE,
CONSTRAINT "UK_Comment_Person_Post" UNIQUE("PersonID","PostID")
);
INSERT INTO To_comment VALUES(1,replace('I think data science is one of the IT fields that needs unlimited education and nonstop self development... every mission ...every employer ...ever goal that we set for  ourselves need us to learn new tool and educate ourselves more and more....\n\nKeep up the good work!','\n',char(10)),1,1,'2020-01-05 17:19:20');
INSERT INTO To_comment VALUES(2,'Keep it up. You have the creativity and determination to do whatever you can dream.',2,1,'2020-09-05 17:19:29');
INSERT INTO To_comment VALUES(3,'Great job! ',5,1,'2020-11-05 07:19:20');
CREATE TABLE IF NOT EXISTS "Event" (
"EventID"INTEGER NOT NULL,
"Title"CHAR(100) NOT NULL,
"Organaizer"CHAR(50) NOT NULL,
"Description"VARCHAR NOT NULL,
"Duration"INTEGER NOT NULL,
"Date"DATETIME NOT NULL,
PRIMARY KEY("EventID") ON CONFLICT IGNORE,
UNIQUE("Organaizer","Title")
);
INSERT INTO Event VALUES(1,'Introduction to Tensorflow','OpenAI','TensorFlow is a free and open-source software library for machine learning. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks. In this event we will discuss about some basics of Tensorflow library.',120,'2021-01-01 18:30:00');
INSERT INTO Event VALUES(2,'Gentle Yoga for Terrible Times','Rose','Human beings are not meant to be in constant fight or flight mode. Chronic stress takes a devastating toll on our mental and physical well-being. If you are exhausted, stressed out, burnt out, or just looking to relax and nourish your mind, body, and spirit, please join me for an hour of gentle yoga.',120,'2021-01-07 16:30:00');
INSERT INTO Event VALUES(3,'Introduction to MongoDB','MongoDB co.',replace('In this event we will cover:\nRDBMS / NOSQL\nData sharding\nCAP Theorem\nACID\nand so on.','\n',char(10)),240,'2021-05-01 12:30:00');
CREATE TABLE IF NOT EXISTS "To_follow" (
	"FollowrshipID"	INTEGER,
	"FollowerID"	INTEGER NOT NULL,
	"FollowedID"	INTEGER NOT NULL,
	"StartDate"	DATETIME NOT NULL,
	"EndDate"	DATETIME NOT NULL DEFAULT '0000-00-00 00:00:00',
	PRIMARY KEY("FollowrshipID") ON CONFLICT IGNORE,
	CONSTRAINT "UK_Follow" UNIQUE("FollowerID","FollowedID"),
	CONSTRAINT "FK_Followed" FOREIGN KEY("FollowedID") REFERENCES "Person"("PersonID") ON DELETE CASCADE,
	CONSTRAINT "FK_Follower" FOREIGN KEY("FollowerID") REFERENCES "Person"("PersonID") ON DELETE CASCADE
);
INSERT INTO To_follow VALUES(1,1,2,'2007-01-01 00:00:00','0000-00-00 00:00:00');
INSERT INTO To_follow VALUES(2,2,1,'2007-01-01 00:00:00','0000-00-00 00:00:00');
INSERT INTO To_follow VALUES(3,2,3,'2017-01-05 00:00:00','0000-00-00 00:00:00');
INSERT INTO To_follow VALUES(4,3,2,'2017-01-08 00:00:00','0000-00-00 00:00:00');
INSERT INTO To_follow VALUES(5,4,2,'2017-02-02 00:00:00','0000-00-00 00:00:00');
INSERT INTO To_follow VALUES(6,2,4,'2017-02-06 00:00:00','2018-02-06 00:00:00');
INSERT INTO To_follow VALUES(7,4,1,'2007-12-03 00:00:00','2021-01-01 20:13:29');
INSERT INTO To_follow VALUES(8,4,3,'2005-05-12 00:00:00','0000-00-00 00:00:00');
INSERT INTO To_follow VALUES(9,1,4,'2007-07-08 00:00:00','0000-00-00 00:00:00');
CREATE TABLE IF NOT EXISTS "Person_Signed_in_devices" (
	"DeviceMacAddress"	TEXT NOT NULL,
	"PersonID"	INTEGER NOT NULL,
	PRIMARY KEY("DeviceMacAddress","PersonID"),
	CONSTRAINT "FK_Person_Device" FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE
);
INSERT INTO Person_Signed_in_devices VALUES('00:0a:95:9d:68:00',4);
INSERT INTO Person_Signed_in_devices VALUES('00:0a:95:9d:68:09',5);
INSERT INTO Person_Signed_in_devices VALUES('00:0a:95:9d:68:16',1);
INSERT INTO Person_Signed_in_devices VALUES('00:0a:95:9d:68:17',1);
INSERT INTO Person_Signed_in_devices VALUES('00:0a:95:9d:68:24',2);
INSERT INTO Person_Signed_in_devices VALUES('00:0a:95:9d:68:35',3);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('To_apply',3);
INSERT INTO sqlite_sequence VALUES('To_participate_event',5);
INSERT INTO sqlite_sequence VALUES('To_comment',3);
COMMIT;
