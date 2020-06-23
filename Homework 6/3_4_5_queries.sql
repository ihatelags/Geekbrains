USE vk;

-- 3. Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).
SELECT name,
       age
FROM
  (SELECT user_id,

     (SELECT CONCAT(first_name, ' ', last_name)
      FROM users
      WHERE users.id = likes.user_id) name,

     (SELECT TIMESTAMPDIFF(YEAR, birthday, NOW())
      FROM profiles
      WHERE profiles.user_id = likes.user_id) age
   FROM likes
   WHERE target_type_id = 2) AS query_likes
GROUP BY name
ORDER BY age
LIMIT 10;


-- 4. Определить кто больше поставил лайков (всего) - мужчины или женщины?
SELECT
  (SELECT gender
   FROM profiles
   WHERE profiles.user_id = likes.user_id) gender,
       COUNT(user_id) like_count
FROM likes
GROUP BY gender
ORDER BY like_count DESC 
-- ответ - мужчины (111 лайков)


-- 5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети (критерии активности необходимо определить самостоятельно).
-- Активность будет замеряться количеством лайков и постов.
SELECT name,
       SUM(activity_count) AS activity
FROM (
        (SELECT
           (SELECT CONCAT(first_name, ' ', last_name)
            FROM users AS u
            WHERE u.id = l.user_id) name,
                COUNT(*) activity_count
         FROM likes AS l
         GROUP BY name)
      UNION
        (SELECT
           (SELECT CONCAT(first_name, ' ', last_name)
            FROM users AS u
            WHERE u.id = p.user_id) name,
                COUNT(*) activity_count
         FROM posts AS p
         GROUP BY name)) AS activities
GROUP BY name
ORDER BY activity
LIMIT 10;