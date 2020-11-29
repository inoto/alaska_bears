# Checklist for alaska CRUD
Example data: {"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}.

## POST
* Send POST to /bear with example data - then check POST response status_code is OK
* Send POST to /bear multiple times with different available types - then check all available types are present using GET /bear/<created_bear_ids>
* Send POST to /bear with example data but unavailable type e.g. GREEN - then check POST response status_code is NOT OK

## GET
* Create some number of bears with example data and send GET to /bear - check POST response status_code is OK, check number of bears in response json >= number of created bears
* Create a bear with example data and send GET to /bear/<created_bear_id> - then check POST response status_code is OK, check reponse json has created bear id
* Create a bear with example data and send GET to /bear/<created_bear_id>+1 - then check POST response status_code is NOT OK
* Send GET to /info - check response json is not empty and contains such words: CRUD, POST, GET, PUT, DELETE, bear, id, bear_type, bear_name, bear_age, Example, Available types

## PUT
* Create a bear with example data and send PUT to /bear/<created_bear_id> with new data which is different from example data - then check all values are different in GET /bear/<created_bear_id> response json
* Create a bear with example data and send PUT to /bear/<created_bear_id> with unavailable bear type e.g. GREEN - then check PUT response status_code is NOT OK

## DELETE
* Create some number of bears with example data and send DELETE to /bear - check POST response status_code is OK, check number of bears in response json is 0
* Create a bear with example data and send DELETE to /bear/<created_bear_id> - then check DELETE response status_code is OK, check GET /bear/<created_bear_id> reponse status_code is NOT OK
* Create a bear with example data and send DELETE to /bear/<created_bear_id>+1 - then check DELETE response status_code is NOT OK

# Additional information
This is a project to test RESP API using pytest framework.  
Report file with latest run is included.
