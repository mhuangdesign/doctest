connectorId = "f20c7880-39f3-11ed-a261-0242ac120002"
api_url = "http://192.168.85.143:8080"
api_token = "225460c4-39fa-11ed-a261-0242ac120002"

# UI website
# Server URL: http://192.168.85.143:8080
# Username: d3user@d3lab.com
# Passwd: D3security!

from pycti import OpenCTIApiClient
import logging
from pycti import OpenCTIConnectorHelper
import json

runtime = {'connector':{'serverurl':api_url,'apikey':api_token}}


def getCTIClient():
    serverUrl = runtime["connector"]["serverurl"]
    apikey = runtime["connector"]["apikey"]
    logger = logging.getLogger()
    logger.disabled = True
    opencti_api_client = OpenCTIApiClient(serverUrl, apikey)
    return opencti_api_client

def findConnectorName(id):
    ctiClient = getCTIClient()
    data = ctiClient.connector.list()
    for item in data:
        if item['id'] == id:
            return item['name']
    return None

def getCTIConnectorHelper(connectorId):
    serverUrl = runtime["connector"]["serverurl"]
    apikey = runtime["connector"]["apikey"]
    logger = logging.getLogger()
    logger.disabled = True
    connectorName = findConnectorName(connectorId)
    if not connectorName:
        errObj = {
            "failedAction": "Can not connect to the Connector.",
            "message": "Connector id provide incorrectly."
        }
        raise Exception(errObj)
    config = {
   "opencti":{
        "url":serverUrl,
        "token":apikey
    },
   "connector":{
        "id":connectorId,
        "name":connectorName,
        "type":"INTERNAL_EXPORT_FILE",
        "scope":"application/json",
        # "confidence_level":50,
        "log_level":"info"
        }
    }
    opencti_api_helper = OpenCTIConnectorHelper(config)
    return opencti_api_helper

opencti_Connector_helper = getCTIConnectorHelper(connectorId)
stix2_bundle = {
        "type": "bundle",
        "id": "bundle--8c939929-688f-4a72-badb-3dd1bd6af0fa",
        "objects": [
            {
            "id": "indicator--d81f86b9-975b-4c0b-875e-810c5ad45a4f",
            "labels": [
                "url-watchlist"
            ],
            "name": "Malicious site hosting downloader",
            "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
            "pattern_type": "stix",
            "spec_version": "2.1",
            "type": "indicator"
        }]}
stix2_bundle_full_size = {
        "type": "bundle",
        "id": "bundle--8c939929-688f-4a72-badb-3dd1bd6af0fa",
        "objects": [
            {
            "id": "indicator--d81f86b9-975b-4c0b-875e-810c5ad45a4f",
            "labels": [
                "url-watchlist"
            ],
            "name": "Malicious site hosting downloader",
            "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
            "pattern_type": "stix",
            "spec_version": "2.1",
            "type": "indicator"
        },{
            "id": "identity--7b82b010-b1c0-4dae-981f-7756374a17df",
            "type": "identity",
            "spec_version": "2.1",
            "name": "ANSSI",
            "identity_class": "organization",
            "labels": ["identity"],
            "created": "2020-02-23T23:40:53.575Z",
            "modified": "2020-02-27T08:45:39.351Z",
            "x_opencti_organization_type": "CSIRT",
            "created_by_ref": "identity--7b82b010-b1c0-4dae-981f-7756374a17df"
            },
            {
            "id": "marking-definition--78ca4366-f5b8-4764-83f7-34ce38198e27",
            "type": "marking-definition",
            "spec_version": "2.1",
            "definition_type": "TLP",
            "definition": {
                "TLP": "TLP:TEST"
            },
            "created": "2020-02-25T09:02:29.040Z",
            "modified": "2020-02-25T09:02:29.040Z",
            "created_by_ref": "marking-definition--78ca4366-f5b8-4764-83f7-34ce38198e27"
            },
            {
            "id": "report--a445d22a-db0c-4b5d-9ec8-e9ad0b6dbdd7",
            "type": "report",
            "spec_version": "2.1",
            "name": "A demo report for testing purposes",
            "labels": ["report"],
            "description": "Report for testing purposes (random data).",
            "published": "2020-03-01T14:02:48.111Z",
            "created": "2020-03-01T14:02:55.327Z",
            "modified": "2020-03-01T14:09:48.078Z",
            "report_types": ["threat-report"],
            "x_opencti_report_status": 2,
            "confidence": 3,
            "created_by_ref": "identity--7b82b010-b1c0-4dae-981f-7756374a17df",
            "object_marking_refs": ["marking-definition--78ca4366-f5b8-4764-83f7-34ce38198e27"],
            "object_refs": [
                "indicator--d81f86b9-975b-4c0b-875e-810c5ad45a4f",
                "report--a445d22a-db0c-4b5d-9ec8-e9ad0b6dbdd7"
            ]
            }
        ]
        }
sampleReport = {
            "id": "report--a445d22a-db0c-4b5d-9ec8-e9ad0b6dbdd7",
            "type": "report",
            "spec_version": "2.1",
            "name": "A demo report for testing purposes",
            "labels": ["report"],
            "description": "Report for testing purposes (random data).",
            "published": "2020-03-01T14:02:48.111Z",
            "created": "2020-03-01T14:02:55.327Z",
            "modified": "2020-03-01T14:09:48.078Z",
            "report_types": ["threat-report"],
            "x_opencti_report_status": 2,
            "confidence": 3,
            "created_by_ref": "identity--7b82b010-b1c0-4dae-981f-7756374a17df",
            "object_marking_refs": ["marking-definition--78ca4366-f5b8-4764-83f7-34ce38198e27"],
            "object_refs": [
                "indicator--d81f86b9-975b-4c0b-875e-810c5ad45a4f",
                "report--a445d22a-db0c-4b5d-9ec8-e9ad0b6dbdd7"
            ]
            }
sampleEntity = {
    "created_by_ref": "identity--7b82b010-b1c0-4dae-981f-7756374a17df",
        "object_marking_refs": ["marking-definition--78ca4366-f5b8-4764-83f7-34ce38198e27"],
        }

# Since the first split_stix2_bundle load the correct data, the following get_entity_objects and get_report_objects works ( under onetime credential)
print("For createAndSendStix2Bundle: ",opencti_Connector_helper.send_stix2_bundle(json.dumps(stix2_bundle))) # can be replace with send_stix2_bundle, split_stix2_bundle
print("For getStix2EntityObjects: ",opencti_Connector_helper.stix2_get_entity_objects(sampleEntity))
print("For getStix2ReportObjects: ",opencti_Connector_helper.stix2_get_report_objects(sampleReport))


# Since the first split_stix2_bundle load the correct data, but seprate connector connecting following get_entity_objects and get_report_objects works ( under multitime connector)
# simulate command issue
opencti_Connector_helper = getCTIConnectorHelper(connectorId)
print("For createAndSendStix2Bundle: ",opencti_Connector_helper.split_stix2_bundle(json.dumps(stix2_bundle))) # can be replace with send_stix2_bundle
opencti_Connector_helper = getCTIConnectorHelper(connectorId)
print("For getStix2EntityObjects: ",opencti_Connector_helper.stix2_get_entity_objects(sampleEntity))
opencti_Connector_helper = getCTIConnectorHelper(connectorId)
print("For getStix2ReportObjects: ",opencti_Connector_helper.stix2_get_report_objects(sampleReport))