from mamba import description, it

with description('Fixture#with_tags', 'integration'):
    with fit('first example', 'unit'):
        pass

with fdescription('Fixture#with_tags', 'integration'):
    with it('first example', 'unit'):
        pass
