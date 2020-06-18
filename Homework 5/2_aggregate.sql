-- Подсчитайте средний возраст пользователей в таблице users
USE hw5;
SELECT AVG(YEAR(NOW()) - YEAR(birthday_at)) FROM users;


-- Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
SELECT DAYNAME(CONCAT(YEAR(NOW()), SUBSTRING(birthday_at, 5, 6))) AS DaysOfWeek, COUNT(*) AS Days_count 
	FROM users
	GROUP BY DaysOfWeek;

-- Подсчитайте произведение чисел в столбце таблицы
-- (работает только для положительных значений)
SELECT exp(SUM(log(id))) as multiply FROM users;