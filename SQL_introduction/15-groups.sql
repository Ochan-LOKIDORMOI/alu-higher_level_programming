-- The script that list the numbers of records with the same score

SELECT score, COUNT(score) AS 'number'
FrOM second_table
GROUP BY score
ORDER BY score DESC;
