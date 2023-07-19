-- Lists all privileges of the MySQL Users `user_0d_1`
-- and `user_0d_2` in `localhost`.
SELECT * 
FROM mysql.user 
WHERE User IN ('user_0d_1', 'user_0d_2');
