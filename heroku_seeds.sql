DELETE FROM follows;
DELETE FROM likes;
DELETE FROM comments;
DELETE FROM posts;
DELETE FROM users;

INSERT INTO users (name, username, email, bio, hashed_password, created_at, updated_at)
VALUES
    ('Demo User', 'Guest', 'demouser@demouser.com', 'Hi, welcome to Elbows. Social network, the safe way.', 'pbkdf2:sha256:150000$8Hni6iRk$355984f782e51532dadccc50c0a90c933b2be5ebae316dbdd389cd09c0e68237');

