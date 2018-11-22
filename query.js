module.exports = `
    SELECT
        unemployment_view.avg as "avg_unemployment_2016",
        votes.votes_dem_2016,
        votes.votes_gop_2016,
        votes.clinton,
        votes.trump,
        county_facts.*
    FROM votes
    LEFT JOIN unemployment_view ON votes.fips = unemployment_view.fips
    LEFT JOIN county_facts ON votes.fips = county_facts.fips
    ORDER BY fips ASC;
`
