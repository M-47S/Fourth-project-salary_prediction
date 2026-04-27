SELECT  c.continent, j.cluster,  AVG(salary)::int
FROM (SELECT salary, location, job_title FROM salaries
	  ORDER BY RANDOM()
	  LIMIT 10000) AS s
	  JOIN continents AS c ON s.location = c.country
	  JOIN job_clusters AS j ON s.job_title = j.job_title
GROUP BY c.continent, j.cluster
ORDER BY c.continent, AVG(salary) DESC