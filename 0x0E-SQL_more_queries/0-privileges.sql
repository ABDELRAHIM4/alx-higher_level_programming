-- Check if user already exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE User = 'user_0d_1') INTO @user_exists;

-- If user doesn't exist, create it
IF NOT @user_exists THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
