module.exports = `
    select POP645213, LFE305213, candidate  from primary_results natural join county_facts where candidate = 'Donald Trump' or candidate = 'Hillary Clinton';
`