SELECT date, name, wind, temp
FROM TEST.PUBLIC.WEATHER
WHERE name in ('BUFFALO NIAGARA INTERNATIONAL', 'ROCHESTER');

SELECT date, name, wind, temp
FROM TEST.PUBLIC.WEATHER
WHERE name in (
    'BUFFALO NIAGARA INTERNATIONAL',
    'ROCHESTER',
    'SYRACUSE HANCOCK INTERNATIONAL',
    'ALBANY INTERNATIONAL AIRPORT',
    'CENTRAL PARK');

select count(1) / (
        select count(1)
        from test.PUBLIC.WEATHER
        where name = 'BUFFALO NIAGARA INTERNATIONAL') percentage_of_results,
    floor(temp / 17) * 17 bin
from test.PUBLIC.WEATHER
where name = 'BUFFALO NIAGARA INTERNATIONAL'
group by bin
order by bin;
