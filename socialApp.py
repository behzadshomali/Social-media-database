import sqlite3
import time

TITLECOLOR = '\033[1m\033[95m'
MESSAGECOLOR = '\033[1m\033[92m'
WARNINGCOLOR = '\033[1m\033[31m'
RESETCOLOR = '\033[0m'
MAXCHAR = 200


def get_input(message, defaultVal='', multipleLines=False, canBeNull=True):
    try:
        inputVal = input(MESSAGECOLOR + message + RESETCOLOR)
        while multipleLines:
            inputVal  += '\n' + input()
    except KeyboardInterrupt:
        pass
    finally:
        while inputVal == '' and not canBeNull:
            inputVal = input(WARNINGCOLOR + 'Invalid! Try again: ' + RESETCOLOR)

        if inputVal == '':
            return defaultVal
        return inputVal


class SocialApp:
    def __init__(self):
        self.conn = sqlite3.connect('./SocialApp.db')
        self.conn.execute('PRAGMA foreign_keys = 1')
        self.conn.execute('PRAGMA automatic_index = 1')
        print(MESSAGECOLOR + 'Connection has been established successfully!' + RESETCOLOR)

########### READ Queries ###########

    def get_posts(self):
        person_id = get_input('Pleases enter your PersonID: ', canBeNull=False)

        cursor = self.conn.execute('''
            SELECT PostID, Content, Date
            FROM Post
            WHERE PersonID = {}
        '''.format(person_id))

        titles = ['PostID', 'Content', 'Post date']
        warning_message = "The intended person hasn't posted anything yet!"
        self.show_result(titles, cursor, warning_message)


    def get_recent_like_comment(self):
        person_id = get_input('Pleases enter your PersonID: ', canBeNull=False)
        since = get_input('Since (e.g. 1 year): ', defaultVal='1 year')

        cursor = self.conn.execute('''
            SELECT
                p.PostID,
                'Like' AS Action,
                Content,
                strftime('%Y-%m-%d', p.Date) AS ActionDate
            FROM Post p INNER JOIN To_like tl ON p.PostID = tl.PostID
            WHERE
                tl.PersonID = {0}
                AND tl.LikeDate BETWEEN datetime('now', '-{1}') AND datetime('now', 'localtime')
            UNION
            SELECT
                p.PostID,
                'Comment' AS Action,
                p.Content,
                strftime('%Y-%m-%d', tc.CommentDate) AS ActionDate
            FROM Post p INNER JOIN To_comment tc ON p.PostID = tc.PostID
            WHERE
                tc.PersonID = {0}
                AND tc.CommentDate BETWEEN datetime('now', '-{1}') AND datetime('now', 'localtime')
        '''.format(person_id, since))

        titles = ['PostID', 'Action', 'Content', 'PostDate']
        warning_message = "The intended person haven't had any activity since {}(s) ago!".format(since)
        self.show_result(titles, cursor, warning_message, limitedText=True)


    def get_skilful_connections(self):
        person_id = get_input('Pleases enter your PersonID: ', canBeNull=False)
        skill = get_input('Pleases enter the intended skill: ', canBeNull=False)

        cursor = self.conn.execute('''
            SELECT
                friend.First_name || ' ' || friend.Last_name AS FullName,
                Skill
            FROM
                Person myself INNER JOIN To_follow tf ON myself.PersonID = tf.FollowerID
                INNER JOIN Person friend ON friend.PersonID = tf.FollowedID
                INNER JOIN Person_Skill ps ON friend.PersonID = ps.PersonID
            WHERE
                myself.PersonID = {0}
                AND Skill = '{1}'
        '''.format(person_id, skill))

        titles = ['Full name', 'Skill']
        warning_message = "None of your connections is skilful at {}!".format(skill)
        self.show_result(titles, cursor, warning_message)


    def get_posts_with_hashtag(self):
        hashtag = get_input('Pleases enter the intended hashtag: ', canBeNull=False)

        cursor = self.conn.execute('''
            SELECT
                p.PostID,
                creator.First_name || ' ' || creator.Last_name AS Creator,
                Hashtag,
                Content,
                Date
            FROM
                Post p INNER JOIN Post_Hashtags ph ON p.PostID = ph.PostID
                INNER JOIN Person creator ON p.PersonID = creator.PersonID
            WHERE Hashtag = '{}'
        '''.format(hashtag))

        titles = ['PostID', 'Creator', 'Hashtag', 'Content', 'Date']
        warning_message = "Hashtag '{}' hasn't been used yet!".format(hashtag)
        self.show_result(titles, cursor, warning_message, limitedText=True)


    def get_post_views_likes(self):
        person_id = get_input('Pleases enter your PersonID: ', canBeNull=False)

        cursor = self.conn.execute('''
            SELECT
                p.PostID,
                Date,
                Content,
                Views,
                COUNT(*) AS Likes
            FROM
                Post p INNER JOIN Person creator ON p.PersonID = creator.PersonID
                LEFT JOIN To_like tl ON p.PostID = tl.PostID
            WHERE creator.PersonID = 4
            GROUP BY p.PostID
            ORDER BY Views DESC, Likes DESC
        ''')

        titles = ['PostID', 'Date', 'Content', 'Views', 'Like']
        warning_message = "User '{}' hasn't posted anything yet!".format(person_id)
        self.show_result(titles, cursor, warning_message, limitedText=True)


    def get_connection_top_k_used_hashtags(self):
        person_id = get_input('Pleases enter your PersonID: ', canBeNull=False)
        k = get_input('Please choose the number of most used hashtags by your friends? ', defaultVal=3)

        cursor = self.conn.execute('''
            SELECT
                Hashtag,
                COUNT(*) AS Count
            FROM
                Person myself INNER JOIN To_follow tf ON myself.PersonID = tf.FollowerID
                INNER JOIN Person friend ON tf.FollowedID = friend.PersonID
                INNER JOIN Post po ON po.PersonID = friend.PersonID
                INNER JOIN Post_Hashtags ph ON po.PostID = ph.PostID
            WHERE myself.PersonID = {0}
            GROUP BY Hashtag
            ORDER BY Count DESC
            LIMIT {1}
        '''.format(person_id, k))


        titles = ['Hashtag', 'Count']
        warning_message = "Your connections haven't used any hashtag yet!"
        self.show_result(titles, cursor, warning_message)


    def get_same_nationality_people(self):
        person_id = get_input('Pleases enter your PersonID: ', canBeNull=False)

        cursor = self.conn.execute('''
            SELECT
                other.First_name || ' ' || other.Last_name AS FullName,
                CASE
                    WHEN other.Gender = "M" THEN "Male"
                    ELSE "Female"
                END AS Gender,
                strftime('%Y', 'now') - strftime('%Y', other.BornDate) AS Age,
                other.Education,
                other.Current_position,
                other.Nationality
            FROM Person myself JOIN Person other ON myself.Nationality = other.Nationality
            WHERE
                myself.PersonID = {}
                AND myself.PersonID != other.PersonID
                AND myself.Nationality = other.Nationality
        '''.format(person_id))

        nation_cursor = self.conn.execute('''
                SELECT Nationality
                FROM Person
                WHERE PersonID = {}
        '''.format(person_id))

        nationality = nation_cursor.fetchone()[0]
        titles = ['Full name', 'Gender', 'Age', 'Education', 'Position', 'Nationality']
        warning_message = "Your the only person who is '{}' in our database!".format(nationality)
        self.show_result(titles, cursor, warning_message)


    def get_trend_hashtags(self):
        k = get_input('Please choose the number of trend hashtags:  ', defaultVal=3)
        since = get_input('Since (e.g. 1 year): ', defaultVal='3 month')

        cursor = self.conn.execute('''
            SELECT
                Hashtag,
                COUNT(*) AS Count
            FROM Post p INNER JOIN Post_Hashtags ph ON p.PostID = ph.PostID
            WHERE p.Date BETWEEN datetime('now', '-{0}') AND datetime('now', 'localtime')
            GROUP BY Hashtag
            ORDER BY Count DESC
            LIMIT {1}
        '''.format(since, k))

        titles = ['Hashtag', 'Count']
        warning_message = "No hashtag is used since {} ago!".format(since)
        self.show_result(titles, cursor, warning_message)


    def get_trend_posts_in_hashtag(self):
        hashtag = get_input('Pleases enter the intended hashtag: ', canBeNull=False)

        cursor = self.conn.execute('''
            SELECT
                p.PostID,
                Hashtag,
                Views,
                Content
            FROM Post p INNER JOIN Post_Hashtags ph ON p.PostID = ph.PostID
            WHERE
                Hashtag = '{}'
                AND Views >= 100
            ORDER BY Views DESC
        '''.format(hashtag))

        titles = ['PostID', 'Hashtag', 'Views', 'Content']
        warning_message = "Hashtag '{}' hasn't been used yet!".format(hashtag)
        self.show_result(titles, cursor, warning_message, limitedText=True)


    def groupby_ip_gender(self):

        cursor = self.conn.execute('''
            SELECT
                IP,
                CASE
                    WHEN Gender = "M" THEN "Male"
                    ELSE "Female"
                END AS Gender,
                AVG(strftime('%Y', 'now') - strftime('%Y', BornDate)) AS Age_avg,
                COUNT(*) Count
            FROM To_share ts INNER JOIN Person p ON ts.PersonID = p.PersonID
            GROUP BY
                IP,
                Gender
            ORDER BY Count DESC
        ''')

        titles = ['IP', 'Gender', 'Age average', 'Count']
        warning_message = "No data is provided for 'To_share' table!"
        self.show_result(titles, cursor, warning_message)


    def get_all_jobs(self):
        cursor = self.conn.execute('''
            SELECT
                Company_name,
                Job_description,
                Seniority_Level,
                Employment_type,
                Qualifications
                Benefits
            From Job
        ''')

        titles = ['Company_name', 'Job_description', 'Seniority_Level', 'Employment_type', 'Qualifications', 'Benefits']
        warning_message = "No job record is available in our database!"
        self.show_result(titles, cursor, warning_message, splitter=' # ')


########### WRITE Queries ###########

    def insert_post(self):
        personID = get_input('Please enter the id of the content creator: ', canBeNull=False)
        date = get_input('Please enter the date (YYYY-MM-DD hh:mm:ss): ', canBeNull=False)
        views = get_input('Please enter the views # of this post: ', defaultVal=0)
        content = get_input('Please enter the content: ', canBeNull=False, multipleLines=True)

        try:
            self.conn.execute('''
                INSERT INTO Post (PersonID, Date, Views, Content)
                VALUES (?, ?, ?, ?)
            ''', (personID, date, views, content))
            self.conn.commit()
            print(MESSAGECOLOR + "The post is inserted successfully into the database!" + RESETCOLOR)
        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)


    def insert_event(self):
        title = get_input('Please enter the title of the event: ', canBeNull=False)
        organizer = get_input('Please enter organizer of the event: ', canBeNull=False)
        description = get_input('Please enter the description of the event: ', canBeNull=False, multipleLines=True)
        duration = get_input('Please enter the duration of the event (in minutes): ', canBeNull=False)
        date = get_input('Please enter the date: ', canBeNull=False)

        try:
            self.conn.execute('''
                INSERT INTO Event (Title, Organaizer, description, Duration, Date)
                VALUES ('{}', '{}', '{}', '{}', '{}')
            '''.format(title, organizer, description, duration, date))
            self.conn.commit()
            print(MESSAGECOLOR + "The event is inserted successfully into the database!" + RESETCOLOR)
        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)


    def insert_person(self):
        gender = get_input('Please input the gender (M/F): ', canBeNull=False)
        firstName, lastName = get_input('Please input the full name (space seperated): ', canBeNull=False).split(' ')
        education = get_input('Please input the education: ', defaultVal='')
        position = get_input('Please input the current position: ', defaultVal='')
        nationality = get_input('Please input the nationality: ', canBeNull=False)
        bornDate = get_input('Please input the born date (YYYY-MM-DD): ', canBeNull=False)
        registerDate = get_input('Please input the register date (YYYY-MM-DD): ', canBeNull=False)

        bornDate += ' 00:00:00'
        registerDate += ' 00:00:00'

        try:
            self.conn.execute('''
                INSERT INTO Person (Gender, First_name, Last_name, Education, Current_position, Nationality, BornDate, RegisterDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (gender, firstName, lastName, education, position, nationality, bornDate, registerDate))
            self.conn.execute(r"UPDATE Person SET Education = NULL WHERE Education = '';")
            self.conn.execute(r"UPDATE Person SET Current_position = NULL WHERE Current_position = '';")
            self.conn.commit()
            print(MESSAGECOLOR + "The person is inserted successfully into the database!" + RESETCOLOR)
        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)

########### UPDATE Queries ###########

    def update_post(self):
        postID = get_input('Please enter the the postID: ', canBeNull=False)
        cursor = self.conn.execute('''
            SELECT
                PersonID,
                Date,
                Views,
                Content
            FROM Post
            WHERE PostID = '{}'
        '''.format(postID))

        fetched = cursor.fetchone()
        if fetched == None:
            print(WARNINGCOLOR + 'There is no post related to input postID!' + RESETCOLOR)
            return

        personID, date, views, content = fetched
        print(MESSAGECOLOR + "Press enter if you want leave the column unchanged!" + RESETCOLOR)
        personID = get_input('Please input the personID: ', defaultVal=personID)
        date = get_input('Please input the date: ', defaultVal=date)
        views = get_input('Please input the views #: ', defaultVal=views)
        content = get_input('Please input the content: ', defaultVal=content, multipleLines=True)

        try:
            cursor = self.conn.execute('''
                UPDATE Post
                SET
                    PersonID = ?,
                    Date = ?,
                    Views = ?,
                    Content = ?
                WHERE PostID = ?
            ''', (personID, date, views, content, postID))

            self.conn.commit()
            print(MESSAGECOLOR + 'The post with id {}, has been updated successfully!'.format(postID) + RESETCOLOR)
            cursor = self.conn.execute('''
                SELECT
                    PostID,
                    PersonID,
                    Date,
                    Views,
                    Content
                FROM Post
                WHERE PostID = '{}'
            '''.format(postID))

            titles = ['PostID', 'PersonId', 'Date', 'Views', 'Content']
            print(MESSAGECOLOR + 'The updated rows are as follows: ' + RESETCOLOR)
            self.show_result(titles, cursor)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)





    def update_event(self):
        eventID = get_input('Please enter the the eventID: ', canBeNull=False)
        cursor = self.conn.execute('''
            SELECT
                Title,
                Organaizer,
                Description,
                Duration,
                Date
            FROM Event
            WHERE EventID = '{}'
        '''.format(eventID))

        fetched = cursor.fetchone()
        if fetched == None:
            print(WARNINGCOLOR + 'There is no event related to input eventID!' + RESETCOLOR)
            return

        title, organizer, description, duration, date = fetched
        print(MESSAGECOLOR + "Press enter if you want leave the column unchanged!" + RESETCOLOR)
        title = get_input('Please input the title: ', defaultVal=title)
        organizer = get_input('Please input the organizer: ', defaultVal=organizer)
        description = get_input('Please input the description: ', defaultVal=description, multipleLines=True)
        duration = get_input('Please input the duration: ', defaultVal=duration)
        date = get_input('Please input the date: ', defaultVal=date)

        try:
            cursor = self.conn.execute('''
                UPDATE Event
                SET
                    Title = ?,
                    Organaizer = ?,
                    Description = ?,
                    Duration = ?,
                    Date = ?
                WHERE EventID = ?
            ''', (title, organizer, description, duration, date, eventID))

            self.conn.commit()
            print(MESSAGECOLOR + 'The event with id {}, has been updated successfully!'.format(eventID) + RESETCOLOR)
            cursor = self.conn.execute('''
                SELECT
                    EventID,
                    Title,
                    Organaizer,
                    Description,
                    Duration,
                    Date
                FROM Event
                WHERE EventID = '{}'
            '''.format(eventID))

            titles = ['EventID', 'Title', 'Organizer', 'Description', 'Duration', 'Date']
            print(MESSAGECOLOR + 'The updated rows are as follows: ' + RESETCOLOR)
            self.show_result(titles, cursor)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)



    def update_person(self):
        personID = get_input('Please enter the the personID: ', canBeNull=False)
        cursor = self.conn.execute('''
            SELECT
                Gender,
                First_name,
                Last_name,
                Education,
                Current_position,
                Nationality,
                BornDate,
                RegisterDate
            FROM Person
            WHERE PersonID = '{}'
        '''.format(personID))

        fetched = cursor.fetchone()
        if fetched == None:
            print(WARNINGCOLOR + 'There is no person related to input personID!' + RESETCOLOR)
            return

        gender, firstName, lastName, education, position, nationality, bornDate, registerDate = fetched
        print(MESSAGECOLOR + "Press enter if you want leave the column unchanged!" + RESETCOLOR)
        gender = get_input('Please input the gender: ', defaultVal=gender)
        firstName = get_input('Please input the first name: ', defaultVal=firstName)
        lastName = get_input('Please input the last name: ', defaultVal=lastName)
        education = get_input('Please input the education: ', defaultVal=education)
        position = get_input('Please input the current position: ', defaultVal=position)
        nationality = get_input('Please input the nationality: ', defaultVal=nationality)
        bornDate = get_input('Please input the birth date: ', defaultVal=bornDate)
        registerDate = get_input('Please input the register date: ', defaultVal=registerDate)

        try:
            cursor = self.conn.execute('''
                UPDATE Person
                SET
                    Gender = ?,
                    First_name = ?,
                    Last_name = ?,
                    Education = ?,
                    Current_position = ?,
                    Nationality = ?,
                    BornDate = ?,
                    RegisterDate = ?
                WHERE PersonID = ?
            ''', (gender, firstName, lastName, education, position, nationality, bornDate, registerDate, personID))

            self.conn.commit()
            print(MESSAGECOLOR + 'The post with id {}, has been updated successfully!'.format(personID) + RESETCOLOR)
            cursor = self.conn.execute('''
                SELECT
                    PersonID,
                    Gender,
                    First_name,
                    Last_name,
                    Education,
                    Current_position,
                    Nationality,
                    BornDate,
                    RegisterDate
                FROM Person
                WHERE PersonID = '{}'
            '''.format(personID))

            titles = ['PersonID', 'Gender', 'FirstName', 'LastName', 'Education', 'Position', 'Nationality', 'BornDate', 'RegisterDate']
            print(MESSAGECOLOR + 'The updated rows are as follows: ' + RESETCOLOR)
            self.show_result(titles, cursor)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)


########### DELETE Queries ###########

    def delete_post(self):
        postID = get_input('Please enter the the postID: ', canBeNull=False)

        try:
            self.conn.execute('''
                DELETE FROM Post WHERE PostID = {};
            '''.format(postID))
            self.conn.commit()

            print(MESSAGECOLOR + 'The post with {} id has been deleted successfully!'.format(postID) + RESETCOLOR)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)


    def delete_event(self):
        eventID = get_input('Please enter the the eventID: ', canBeNull=False)

        try:
            self.conn.execute('''
                DELETE FROM Event WHERE EventID = {};
            '''.format(eventID))
            self.conn.commit()

            print(MESSAGECOLOR + 'The event with {} id has been deleted successfully!'.format(eventID) + RESETCOLOR)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)


    def delete_person(self):
        personID = get_input('Please enter the the personID: ', canBeNull=False)

        try:
            self.conn.execute('''
                DELETE FROM Person WHERE PersonID = {};
            '''.format(personID))
            self.conn.commit()

            print(MESSAGECOLOR + 'The person with {} id has been deleted successfully!'.format(personID) + RESETCOLOR)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)


########### CREATE Queries ###########

    def create_poll(self):
        try:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Poll
                (
                    Question VARCHAR NOT NULL,
                    PollID INTEGER NOT NULL,
                    PostID INTEGER NOT NULL,
                    PRIMARY KEY("PollID") ON CONFLICT IGNORE
                );
            ''')
            self.conn.commit()
            print(MESSAGECOLOR + '"Poll table" has been created successfully!' + RESETCOLOR)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)

        self.show_tables()


    def create_influencer(self):
        try:
            cursor = self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Influencer
                (
                    PersonID INTEGER NOT NULL,
                    InfluencerID INTEGER NOT NULL,
                    IsAlive INTEGER NOT NULL,
                    Accomplishments VARCHAR NOT NULL,
                    PRIMARY KEY("InfluencerID") ON CONFLICT IGNORE,
                    FOREIGN KEY("PersonID") REFERENCES "Person"("PersonID") ON DELETE CASCADE
                );
            ''')
            self.conn.commit()
            print(MESSAGECOLOR + '"Influencer table" has been created successfully!' + RESETCOLOR)

        except sqlite3.Error as error:
            print(WARNINGCOLOR + str(error) + RESETCOLOR)

        self.show_tables()


########### Structural functions ###########

    def show_result(self, titles, cursor, warning_message=WARNINGCOLOR+'There is nothing to show!'+RESETCOLOR, limitedText=False, splitter=None):
        rowCount = 0
        for row in cursor:
            rowCount += 1
            for i, col in enumerate(row):
                time.sleep(.1)
                etc = ''
                if limitedText and len(str(col)) > MAXCHAR:
                    etc = '...'
                if splitter == None:
                    print(TITLECOLOR + titles[i] + ': ' + RESETCOLOR + str(col).replace('\n', ' ')[:MAXCHAR] + etc)
                else:
                    print(TITLECOLOR + titles[i] + ': ' + RESETCOLOR + '\n\t* '.join(str(col).split(splitter)))
            print()

        if rowCount == 0:
            print(WARNINGCOLOR + warning_message + RESETCOLOR)


    def show_tables(self):
        print(MESSAGECOLOR + 'Here is the list of tables in our database: ' + RESETCOLOR)
        cursor = self.conn.execute(r"SELECT name FROM sqlite_master WHERE type = 'table';")
        for i, tableName in enumerate(cursor):
            if i != 0 and i % 3 == 0:
                time.sleep(.1)
                print()
            print('{:30s}'.format(tableName[0]), end='')
        print()


    def exit(self):
        self.conn.close()
        print(MESSAGECOLOR + 'Database closed successfully!' + RESETCOLOR)


