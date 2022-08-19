import demis_token
import demis_api
import json
from demis_example_json_commit_sars import d

token = demis_token.token_generation()

submit_res = demis_api.api(data =json.dumps(d), access_token=token['access_token'])
submit_res
