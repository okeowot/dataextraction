import argparse
import urllib.request
import functions


def main(url):
    # Download data
    incident_data = functions.fetchincidents(url)
    incidents = functions.extractincidents(incident_data)
    incidents_db = functions.createdb()
    # Extract data
#    incidents = project0.extractincidents(incident_data)
	
    # Create new database
 #   db = project0.createdb()
    functions.populatedb(incidents_db, incidents)
    # Print incident counts
    functions.status()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
