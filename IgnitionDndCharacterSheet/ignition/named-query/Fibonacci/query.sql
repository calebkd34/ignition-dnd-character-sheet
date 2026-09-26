WITH RECURSIVE fibonacci(a, b, c) as (
	SELECT 0, 1, 0 UNION ALL
	SELECT b, a + b, c + 1 FROM fibonacci WHERE c < :n
)
SELECT max(b) FROM fibonacci;