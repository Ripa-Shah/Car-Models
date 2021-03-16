
DROP TABLE IF EXISTS #test;
CREATE TABLE #test (City VARCHAR(255), Country VARCHAR(255));

INSERT #test (City, Country)
VALUES
('New York', 'USA'),
('London', 'Brexit'),
('Salt Lake City', 'USA'),
('Paris', 'France'),
('Chicago', 'USA'),
('Avignon', 'France'),
('Ancorage', 'USA'),
('Nice', 'France'),
('Montreal', 'Canada'),
('Quebec', 'Canada');

SELECT DISTINCT Country,
	STUFF((
		SELECT ', ' + T.City
		FROM #test AS T
		WHERE T.Country = c.Country
		ORDER BY T.City
		FOR XML PATH(''), TYPE
	).value('.', 'VARCHAR(MAX)'), 1, 2, ' ')
FROM #test AS c;

SELECT
    Country,
    STRING_AGG(City, ', ') AS CityList
FROM #test
GROUP BY Country;
