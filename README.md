# DEMIS_Lab_API
Open-Source DEMIS FHIR API

# Prerequisites
The API is tested and configured for communication with the DEMIS Docker Testing Environment, but it can be easily reconfigured to run in the productive Environment
https://github.com/gematik/DEMIS-Test_Environment

# Current status
-The fundamental functions of Authetication token request and submission of example reports ist implemented in python an works well.
-Generation of diseas specific reports in json format is currently in development
-A cruxial point is the integration into LIS-Systems. One possible Solution is based on LIS-based queries to obtain data and construction of json-containers using python or R (whichever is more suitable for the lab) 
