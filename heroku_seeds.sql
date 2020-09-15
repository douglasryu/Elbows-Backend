-- DELETE FROM follows;
-- DELETE FROM likes;
-- DELETE FROM comments;
-- DELETE FROM posts;
-- DELETE FROM users;

INSERT INTO users (name, username, email, profile_pic_url, bio, hashed_password, created_at, updated_at)
VALUES
    ('Demo User', 'Guest', 'demouser@demouser.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg', 'Welcome to Elbows, safe and social.', 'pbkdf2:sha256:150000$ZN7RAtcN$a42ebdcc5d703f7d65f578b6bc48b865823cdeb97bc78df6603ab0491f62fbd4', NOW(), NOW()),
    ('Douglas Ryu', 'douglasryu', 'douglasryu@hotmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg', 'Welcome to Elbows, safe and social. I am the creator of Elbows.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Anne Hathaway', 'annehathaway', 'ahathaway@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/annehathaway.jpeg', 'Whatever you are made of, be the best of that.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Jennifer Love Hewitt', 'jenniferlhewitt', 'lovejenn@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/jenniferlovehewitt.jpg', 'The ultimate dream in life is to be able to do what you love and learn something from it.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Jennifer Aniston', 'jenniferaniston', 'jennifera@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/jenniferaniston.jpg', 'The greater your capacity to love, the greater your capacity to feel the pain.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Tom Cruise', 'tomcruise', 'tomc@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/tomcruise.jpg', 'I love what I do. I take great pride in what I do. And I can''t do something halfway, three-quarters, nine-tenths. If I''m going to do something, I go all the way..', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Brad Pitt', 'bradpitt', 'bpitt@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/bradpitt.jpg', 'I''m one of those people you hate because of genetics. It''s the truth.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Julia Roberts', 'juliaroberts', 'juliar@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/juliaroberts.jpg', 'If you love someone, you say it, right then, out loud. Otherwise, the moment just passes you by.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Will Smith', 'willsmith', 'wsmith@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/willsmith.jpeg', 'Money and success don''t change people; they merely amplify what is already there.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Leonardo DiCaprio', 'DiCaprio', 'leonardod@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/leonardodicaprio.jpeg', 'If you can do what you do best and be happy, you''re further along in life than most people.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Johnny Depp', 'johnnydepp', 'jdepp@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/johnnydepp.jpg', 'Not all treasure is silver and gold, mate.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('Harrison Ford', 'harrisonford', 'hford@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/harrisonford.jpg', 'To me, success is choice and opportunity.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW()),
    ('George Clooney', 'georgeclooney', 'gclooney@gmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/georgeclooney.jpg', 'The only failure is not to try.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW());


INSERT INTO posts (user_id, location, post_image, post_body, created_at, updated_at)
VALUES
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/1.jpg', 'Busy New York', NOW(), NOW()),
    (8, 'New Jersey', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/2.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/3.jpg', 'New York Street', NOW(), NOW()),
    (6, 'Nevada', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/4.jpg', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/5.jpg', 'Architecture', NOW(), NOW()),
    (5, 'Korea', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/6.jpg', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (6, 'Wisconsin', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/7.jpg', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', NOW(), NOW()),
    (2, 'Pittsburgh', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/8.jpg', 'How awesome is this?', NOW(), NOW()),
    (7, 'Georgia', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/9.jpg', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/10.jpg', 'Hello', NOW(), NOW()),
    (5, 'Los Angeles', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/11.jpg', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (12, 'Seattle', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/12.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/13.jpg', 'Times Square', NOW(), NOW()),
    (2, 'Pittsburgh', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/14.jpg', 'PNC Park', NOW(), NOW()),
    (3, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/15.jpg', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/16.jpg', 'Construction', NOW(), NOW()),
    (4, 'New Jersey', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/17.jpg', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (12, 'Sahara Desert', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/18.jpg', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', NOW(), NOW()),
    (12, 'Turkey', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/19.jpg', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (10, 'Los Angeles', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/20.jpg', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (9, 'Alabama', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/21.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (11, 'Cape Cod', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/22.jpg', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW());

INSERT INTO follows (user_id, follow_user_id, created_at, updated_at)
VALUES
    (1, 2, NOW(), NOW()),
    (1, 7, NOW(), NOW()),
    (1, 13, NOW(), NOW()),
    (1, 5, NOW(), NOW()),
    (1, 3, NOW(), NOW()),
    (1, 6, NOW(), NOW()),
    (13, 1, NOW(), NOW()),
    (6, 1, NOW(), NOW()),
    (3, 1, NOW(), NOW()),
    (5, 1, NOW(), NOW()),
    (10, 1, NOW(), NOW()),
    (7, 1, NOW(), NOW()),
    (2, 1, NOW(), NOW());

INSERT INTO COMMENTS (user_id, user_name, post_id, comment_body, created_at, updated_at)
VALUES
    (2, 'douglasryu', 1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (3, 'annehathaway', 1, 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (9, 'willsmith', 2, 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', NOW(), NOW()),
    (6, 'tomcruise', 4, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (9, 'willsmith', 5, 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', NOW(), NOW()),
    (10, 'DiCaprio', 9, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (8, 'juliaroberts', 11, 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (10, 'DicCaprio', 13, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (8, 'juliaroberts', 14, 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (11, 'johnnydepp', 15, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (6, 'tomcruise', 17, 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', NOW(), NOW()),(1, 'Guest', 9, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (13, 'georgeclooney', 18, 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', NOW(), NOW()),
    (12, 'harrisonford', 18, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW()),
    (12, 'harrisonford', 19, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', NOW(), NOW()),
    (7, 'bradpitt', 22, 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', NOW(), NOW()),
    (7, 'bradpitt', 22, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', NOW(), NOW());

INSERT INTO LIKES (user_id, post_id, comment_id, created_at, updated_at)
VALUES
    (1, 2, null, NOW(), NOW()),
    (1, 4, null, NOW(), NOW()),
    (1, 6, null, NOW(), NOW()),
    (1, 10, null, NOW(), NOW()),
    (1, 11, null, NOW(), NOW()),
    (1, 18, null, NOW(), NOW()),
    (1, 19, null, NOW(), NOW()),
    (1, 20, null, NOW(), NOW()),
    (2, 5, null, NOW(), NOW()),
    (2, 7, null, NOW(), NOW()),
    (2, 10, null, NOW(), NOW()),
    (2, 19, null, NOW(), NOW()),
    (3, 10, null, NOW(), NOW()),
    (3, 19, null, NOW(), NOW()),
    (4, 19, null, NOW(), NOW()),
    (4, 22, null, NOW(), NOW()),
    (5, 15, null, NOW(), NOW()),
    (5, 22, null, NOW(), NOW()),
    (6, 15, null, NOW(), NOW()),
    (6, 14, null, NOW(), NOW()),
    (7, 13, null, NOW(), NOW()),
    (7, 12, null, NOW(), NOW()),
    (8, 11, null, NOW(), NOW()),
    (8, 10, null, NOW(), NOW()),
    (9, 8, null, NOW(), NOW()),
    (9, 9, null, NOW(), NOW()),
    (10, 7, null, NOW(), NOW()),
    (10, 5, null, NOW(), NOW()),
    (11, 19, null, NOW(), NOW()),
    (11, 22, null, NOW(), NOW()),
    (12, 19, null, NOW(), NOW()),
    (12, 22, null, NOW(), NOW()),
    (13, 19, null, NOW(), NOW()),
    (13, 22, null, NOW(), NOW());
