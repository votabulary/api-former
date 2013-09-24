from polling.models import County, Precinct, PollingPlace, Address, Election, ElectionPrecinctPollingPlace
import datetime


def run():
    county_dict = {}
    precinct_dict = {}
    polling_place_dict = {}
    with open('import_files/counties.csv', 'r') as f:
        first = True
        for line in f:
            if not first:
                data = line.strip()
                (name, code, state) = data.split(',')
                county = County(name=name, code=code, state=state)
                county.save()
                county_dict[county.code] = county
            first = False
        print "Counties Saved!"

    with open('import_files/precincts.csv') as f:
        first = True
        for line in f:
            if not first:
                data = line.strip()
                (name, county_code, enabled) = data.split(',')
                e = True if enabled == 'TRUE' else False
                precinct = Precinct(name=name, county=county_dict[county_code], enabled=e)
                precinct.save()
                precinct_dict[name] = precinct
            first = False
        print "Precincts Saved!"

    with open('import_files/polling_locations.csv') as f:
        first = True
        for line in f:
            if not first:
                data = line.strip()
                print data
                (name, address_name, address1, address2, address3, address4, city, state, zip_code, country) = data.split(',')
                address = Address(
                    name=address_name,
                    address_line1=address1,
                    address_line2=address2,
                    address_line3=address3,
                    address_line4=address4,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    country=country
                )
                address.save()
                polling_place = PollingPlace(
                    name=name,
                    address=address
                )
                polling_place.save()
                polling_place_dict[name] = polling_place
            first = False
        print "Polling Places Saved!"

    with open('import_files/election_precinct_polling_locations.csv') as f:
        first = True
        for line in f:
            if not first:
                data = line.strip()
                (county_code, early_voting_start_date, early_voting_end_date, voting_date, voting_rule, precinct, polling_location_name) = data.split(',')
                ev_start = datetime.datetime.strptime(early_voting_start_date, "%m/%d/%Y")
                ev_end = datetime.datetime.strptime(early_voting_end_date, "%m/%d/%Y")
                v_date = datetime.datetime.strptime(voting_date, "%m/%d/%Y")
                election = Election(
                    county=county_dict[county_code],
                    early_voting_start_date=ev_start,
                    early_voting_end_date=ev_end,
                    voting_date=v_date,
                    voting_rule=voting_rule,
                )
                election.save()
                election_precinct_polling_place = ElectionPrecinctPollingPlace(
                    election=election,
                    precinct=precinct_dict[precinct],
                    polling_place=polling_place_dict[polling_location_name]
                )
                election_precinct_polling_place.save()
            first = False
        print "Precincts Saved!"