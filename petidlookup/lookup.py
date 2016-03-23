# Copyright 2016 Ben Jackson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import requests
import csv
import json


def search( petid ):
  url = 'http://www.chipitcheckit.co.uk/lookupChip/{0}'.format( petid )
  response = requests.get( url )
  data = response.json()

  if 'Result' not in data or data[ 'Result' ] != "Ok" or 'Data' not in data:
    raise RuntimeError( 'Unrecognised response or error: ' 
                        + json.dumps( data, indent=2 ) )

  dbs = []
  for database in data[ 'Data' ]:
    if database[ 'InDatabase' ]:
      dbs.append( database[ 'DatabaseName' ] )

  return dbs


def run( args ):
  with open( args.file, 'rb' ) as f:
    reader = csv.reader( f )
    with open( args.outfile, 'wb', 1 ) as o:
      writer = csv.writer( o )
      print( 'name,petid,location' )
      writer.writerow( [ 'name', 'petid', 'location' ] )
      for row in reader:
        name = row[ 0 ]
        petid = row[ 1 ]
        location = search( petid )
        if not location:
          location = 'Not found'
        else:
          location = ' and '.join( location )

        print ( '{0},{1},{2}'.format( name, petid, location ) )
        writer.writerow( [ name, petid, location ] )
