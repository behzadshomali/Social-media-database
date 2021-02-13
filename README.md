# Social media database

### Tables
This is a database developed in `SQLite` simulating a social media like LinkedIn! This database has 17 tables such that 5 of them are main tables and others are either `many-to-many relationships` or `multi-values` attributes. 
The 5 main  tables are:
<details>
<summary>Event</summary>
  
* EventID
* Title
* Duration
* Organizer
* EventDate
* Description
* No. participants
</details>    

<details> 
  <summary>Job</summary>
  
  * JobID
  * Company name
  * Qualifications
  * Benefits
  * Job description
  * Seniority level
  * No. applicants
  * Employment type
</details> 

<details> 
  <summary>Person</summary>
  
  * PersonID
  * Gender
  * Name (first name + last name)
  * BornDate
  * RegisterDate
  * Nationality
  * Education
  * Skills
  * Favorites
  * Age
  * Signed-in devices
  * Current position
</details> 

<details>
  <summary>Poll</summary>
  
  * PollID
  * Question
  * Options
</details>

<details> 
  <summary>Post</summary>
  
  * PostId
  * PostDate
  * Content
  * Hashtags
  * No. likes
  * No. views
</details> 

</br>and also other tables are as follows:

<details>
  <summary>Person_favorite</summary>
  
  * PersonID (FK)
  * Favorite
</details> 

<details>
  <summary>Person_Signed_in_devices</summary>
  
  * PersonID (FK)
  * DeviceMacAddress
</details> 

<details>
  <summary>Person_Skill</summary>
  
  * PersonID (FK)
  * Skill
</details> 

<details>
  <summary>Poll_Option</summary>
  
  * PollID (FK)
  * OptionID
  * Option
</details> 

<details>
  <summary>Post_hashtags</summary>
  
  * PostID (FK)
  * Hashtag
</details> 

<details>
  <summary>To_apply</summary>
  
  * PersonID (FK)
  * JobID (FK)
  * ApplyID
  * ApplyDate
</details> 

<details>
  <summary>To_comment</summary>
  
  * PersonID (FK)
  * PostID (FK)
  * CommentID
  * Content
  * CommentDate
</details> 

<details>
  <summary>To_like</summary>
  
  * PersonID (FK)
  * PostID (FK)
  * LikeDate
  * ReactionID
</details> 

<details>
  <summary>To_follow</summary>
  
  * FollowerID (FK)
  * FollowedID (FK)
  * FollowershipID
  * StartDate
  * EndDate
</details> 

<details>
  <summary>To_participate_event</summary>
  
  * EventID (FK)
  * PersonID (FK)
  * ParticipationID
</details> 

<details>
  <summary>To_participate_poll</summary>
  
  * PollID (FK)
  * PersonID (FK)
  * ParticipateDate
  * SelectedOption
</details> 

<details>
  <summary>To_share</summary>
  
  * PostID (FK)
  * PersonID (FK)
  * IP
</details> 

### Extra information
I implemented this program as my final project for `Database` course in semester 5 in a short time (this is why it may be a little messy... LOL!!!). To be able to communicate with the database, I developed a `Python` program that is made of two files: 
1. `ui.py` : that input the command from the user and also add some visualization to terminal
2. `socialApp.py` : contains and implements 10 selected queries and also some `CRUD` stuff


### How to run?
First of all to have tables( + fake data) you should create a file named `SocialApp.db`. After creating the file and putting it next to the `ui.py` and `socialApp.py`, it's time to initial the database. To do this, in your terminal first type:
```
sqlite3 SocialApp.db
```
and then paste the contents of the `dumped.sql` file into the terminal and then press enter. Finally to run the program just type:
```
python.ui
```
and then you will face a chart that is there to guide you!
 
Note that the commands start with `S` indicate systematic (or aggregation commands) while commands start with `P` are mostly related to a **single** person or post.

<img src=./ER.png>
