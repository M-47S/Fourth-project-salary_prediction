SELECT c.continent, AVG(s.salary)::int AS mean, percentile_cont(0.5) WITHIN GROUP (ORDER BY salary) AS median
FROM (SELECT salary, location FROM salaries
	  ORDER BY RANDOM()
	  LIMIT 10000) AS s
	JOIN continents AS c ON s.location = c.country
GROUP BY c.continent
ORDER BY mean DESC, median DESC;