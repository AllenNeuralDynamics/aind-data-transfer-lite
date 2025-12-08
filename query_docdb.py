from aind_data_access_api.document_db import MetadataDbClient


docdb_client = MetadataDbClient(
  host="api.allenneuraldynamics-test.org",
  version="v2"
)

location = "s3://aind-open-data-dev-u5u0i5/12345_2022-02-21_16-30-01"

response = docdb_client.retrieve_docdb_records(
  filter_query={"location": location},
  projection={"other_identifiers": 1}
)
print(response)

response = docdb_client.register_asset(
    s3_location=location
)
print(response)