module.exports = `
    select VET605213, PVY020213, candidate  from primary_results natural join county_facts where candidate = 'Donald Trump' or candidate = 'Hillary Clinton';
`