-- DELETE FROM follows;
-- DELETE FROM likes;
-- DELETE FROM comments;
-- DELETE FROM posts;
-- DELETE FROM users;

INSERT INTO users (name, username, email, profile_pic_url, bio, hashed_password, created_at, updated_at)
VALUES
    ('Demo User', 'Guest', 'demouser@demouser.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg', 'Welcome to Elbows, safe and social.', 'pbkdf2:sha256:150000$LKqxHRfm$73e1bf621c7891edb619763031a5fa74538662f21e4572c316bdfdc42b89eb07', NOW(), NOW()),
    ('Douglas Ryu', 'douglasryu', 'douglasryu@hotmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg', 'Welcome to Elbows, safe and social.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW());

INSERT INTO posts (user_id, location, post_image, post_body, created_at, updated_at)
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/275.jpg', 'Busy New York', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/9.jpg', 'Construction', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/622.jpg', 'New York Street', NOW(), NOW()),
    (2, 'Pittsburgh', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/159.jpg', 'How awesome is this?', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/889.jpg', 'Times Square', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/620.jpg', 'Architecture', NOW(), NOW()),
    (2, 'Pittsburgh', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/97.jpg', 'PNC Park', NOW(), NOW()),
    (1, 'New York', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/754.jpg', 'Hello', NOW(), NOW());

INSERT INTO follows (user_id, follow_user_id)
VALUES
    (1, 2)
    (2, 1)

-- INSERT INTO COMMENTS (user_id, user_name, post_id, comment_body, created_at, updated_at)
-- VALUES
--     (1, 'Guest', 9, 'Hi there!', NOW(), NOW())