module.exports = `
    select RHI825214, RHI225214, candidate from county_facts natural join primary_results where candidate = 'Donald Trump' or candidate = 'Hillary Clinton';
`