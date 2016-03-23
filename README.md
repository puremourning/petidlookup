# Look up microchip numbers in database

Greyhound Rescue Wales (and possibly other rescue charities) have large numbers
of animals which are microchipped and the UK law now requires the *keepers* of
such animals to register (and keep up to date) the microchip information.

Doing this manually for hundreds or thousands of dogs is absurd. This tool helps
by looking up the available public information by reverse-engineering the query
from chipitcheckit.co.uk.

# Usage

When supplied with a CSV file with the following columns (without headers):

- pet name
- microchip number

Looks up in chip it check it database to find the database in which the
microchip number is found and saves the result to the output file with the 
following comma-separated fields (again, no header):

- pet name
- microchip number
- database

The database field is one of:

- A list of database names joined with " and "
- "Not found"

# Installation

- `virtualenv runtime/`
- `source runtime/bin/activate`
- `pip install requests`

# Run

- `source runtime/bin/activate`
- `python -m petidlookup --file <source file>.csv --outfile <dest file>.csv`

It prints the output to standard output and the output file.
