import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from api.model.event import Event


class Command(BaseCommand):
    help = 'Sync data from a CSV file to the Event model'

    def handle(self, *args, **options):
        csv_file = 'api/dataset/AviationData.csv'

        with open(csv_file, 'r', encoding='latin-1') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                # Convert the date fields to Python datetime objects
                event_date = datetime.strptime(row['Event.Date'], '%Y-%m-%d')
                publication_date = datetime.strptime(row['Publication.Date'], '%d/%m/%Y')\
                    if row['Publication.Date'] else None

                # Create a new Event object and save it to the database
                Event.objects.create(
                    event_id=row['Event.Id'],
                    investigation_type=row['Investigation.Type'] if row['Investigation.Type'] else None,
                    accident_number=row['Accident.Number'],
                    event_date=event_date,
                    location=row['Location'] if row['Location'] else None,
                    country=row['Country'] if row['Country'] else None,
                    latitude=row['Latitude'] if row['Latitude'] else None,
                    longitude=row['Longitude'] if row['Longitude'] else None,
                    airport_code=row['Airport.Code'] if row['Airport.Code'] else None,
                    airport_name=row['Airport.Name'] if row['Airport.Name'] else None,
                    injury_severity=row['Injury.Severity'],
                    aircraft_damage=row['Aircraft.Damage'] if row['Aircraft.Damage'] else None,
                    aircraft_category=row['Aircraft.Category'] if row['Aircraft.Category'] else None,
                    registration_number=row['Registration.Number'] if row['Registration.Number'] else None,
                    make=row['Make'] if row['Make'] else None,
                    model=row['Model'] if row['Model'] else None,
                    amateur_built=row['Amateur.Built'] if row['Amateur.Built'] else None,
                    number_of_engines=row['Number.of.Engines'] if row['Number.of.Engines'] else None,
                    engine_type=row['Engine.Type'] if row['Engine.Type'] else None,
                    far_description=row['FAR.Description'] if row['FAR.Description'] else None,
                    schedule=row['Schedule'] if row['Schedule'] else None,
                    purpose_of_flight=row['Purpose.of.Flight'] if row['Purpose.of.Flight'] else None,
                    air_carrier=row['Air.Carrier'] if row['Air.Carrier'] else None,
                    total_fatal_injuries=row['Total.Fatal.Injuries'] if row['Total.Fatal.Injuries'] else None,
                    total_serious_injuries=row['Total.Serious.Injuries'] if row['Total.Serious.Injuries'] else None,
                    total_minor_injuries=row['Total.Minor.Injuries'] if row['Total.Minor.Injuries'] else None,
                    total_uninjured=row['Total.Uninjured'] if row['Total.Uninjured'] else None,
                    weather_condition=row['Weather.Condition'] if row['Weather.Condition'] else None,
                    broad_phase_of_flight=row['Broad.Phase.of.Flight'] if row['Broad.Phase.of.Flight'] else None,
                    report_status=row['Report.Status'] if row['Report.Status'] else None,
                    publication_date=publication_date,)

                self.stdout.write(
                     self.style.SUCCESS(f'Successfully added event {row["Event.Id"]} to the database'))
