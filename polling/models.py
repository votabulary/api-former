from django.db import models

class County(models.Model):
    name = models.CharField(max_length=200, blank=False)

class Election(models.Model):
    VOTE_ANYWHERE = 'VA'
    VOTE_IN_PRECINCT = 'VP'
    VOTING_RULES = (
        (VOTE_ANYWHERE, "Vote Anywhere"),
        (VOTE_IN_PRECINCT, "Vote In Precinct"),
    )

    county = models.ForeignKey('County')
    election_date = models.DateField()
    voting_rule = models.CharField(max_length=2,
                                   choices=VOTING_RULES,
                                   default=VOTE_IN_PRECINCT)

class Precinct(models.Model):
    name = models.CharField(max_length=200, blank=False)

class PollingPlace(models.Model):
    address = models.ForeignKey('Address')

STATES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NA', 'National'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming'),
)

class Address(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address_line1 = models.CharField(max_length=200, blank=False)
    address_line2 = models.CharField(max_length=200, blank=True)
    address_line3 = models.CharField(max_length=200, blank=True)
    address_line4 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=2,
                             choices=STATES,
                             default='TX',
                             blank=False)
    zip_code = models.CharField(max_length=9, blank=False)
    country = models.CharField(max_length=2, default='US')