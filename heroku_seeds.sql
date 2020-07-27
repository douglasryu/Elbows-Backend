-- DELETE FROM follows;
-- DELETE FROM likes;
-- DELETE FROM comments;
-- DELETE FROM posts;
-- DELETE FROM users;

INSERT INTO users (name, username, email, profile_pic_url, bio, hashed_password, created_at, updated_at)
VALUES
    ('Demo User', 'Guest', 'demouser@demouser.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg', 'Welcome to Elbows, safe and social.', 'pbkdf2:sha256:150000$LKqxHRfm$73e1bf621c7891edb619763031a5fa74538662f21e4572c316bdfdc42b89eb07', NOW(), NOW()),
    ('Douglas Ryu', 'douglasryu', 'douglasryu@hotmail.com', 'https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg', 'Welcome to Elbows, safe and social.', 'pbkdf2:sha256:150000$RCtcoxz2$856023dcbdf4a13f61109d8419148a65ac7dbbcc8235083b29d4db2c20c7ee39', NOW(), NOW());

INSERT INTO posts (user_id, location, post_image, post_body, created_at, update_at)
    (1, 'New York', )

INSERT INTO follows (user_id, follow_user_id)
VALUES
    (1, 2)
    (2, 1)

