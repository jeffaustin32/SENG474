module.exports = `
    SELECT * 
    FROM public.primary_results as pr
    LEFT JOIN public.county_facts as cf ON (cf.area_name  ILIKE '%' || pr.county || '%' AND cf.state_abbreviation = pr.state_abbreviation)
`