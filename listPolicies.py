# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
# If you want to use the private key which is not in the key file, key_content can be the backup of key_file.
pem_prefix = '-----BEGIN PRIVATE KEY-----\n'
pem_suffix = '\n-----END PRIVATE KEY-----'
key = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCSOjraYy2iRKiihFDOdbOK4kWukovLJ8LdAs5+ZlI/RA9YEWK+X96jxci7f8M7ow5vN7bf5a787q/D+Sutw0bjW+1TaYW1gkjkYe3Ud5kkWtBFF7e48VEnutlzuEMJSQTGO+kSlZO3jReBuVc4D9FupYM34Ov4FBCuRTeT/oIDzobw18DuFXeVKE+emYRpK/CRkvA8CtNRT7rWl7Z6qMNHvBut0fzPsIl35mrOeOxDds2VF5qT8VOr9yw3MVpiXg0ZHAhKDsrsU0RgWBs4B5SWO/k8qNSJ0mDxnsB2axoK9F9V3Eb8/cDHILAkCCEpto7m7pWEAsRjqYu2nHjQ+fxXAgMBAAECggEABmPMr5S26Ujbykztj7Vn/5vXVK4VtW51iZ02SHgQhFrlMBbZEZ2fMoPm5ilKmZViAO0r13Pc0N5d8uU1X0CnHTH8AxxGL1d+okWUlCdtG0AWqsuYXS4PuvnjcmGXwv+cWaHuPkAoC397Cqb+jzYYaPU1mzWqdMBCYa3STxbHjVf3oQ6jUcYuHbauvsAu+r1AZMqEczWgjmvyi3ED9QUvLFbQKXMMIS7NKSf9HVzmbRfAkPAkL2906E7sF5Lv3K9dgxHotASmzS24SR5KgBqevizQ2ny0UnxdCZgg2I1B02lfLrdFN7Yai7mrg9pLRvqOUca+6pMb5U8nL7AlmncLNQKBgQDGYsy/bawtlwmP4+VvQgQvpIQhMzR5JjZPKFN6s6QLBq7LTdwTcGUY/FOWriSChH7DfoOI5YRmNvQB8yHFdxWgXQj8BlrdvdTFJonFqOAHR4kB9EnzVgG4q/GyR2uId3VIa5PGNWXzoActhcz5RtY/g71Efv+yVYW03LjG1QSXdQKBgQC8saf8pw7SEdV3mNSsvJS5TyCbEDhUl4t00srKWjPThCQUJZHcifwiUHlQK0suFA2J3rxBCWH58rX8M0C49mB31vzxqY/E6VGYpGHzykLBXbJSoLaWyFYC35eIUeGamrv8ZyqMV61Kr/twRqzRv7N0Oz58ALQ+2OdK2YgptoiXGwKBgQCSFYDV2am27IhjB5sUgVVZy9hsJiuWpnfJdFV8fjnm0KX4GT5cpiAb9PqMc3F5Fp3N0SSEsxX6uq6VnPaaVOV87+VEyF0y+a1q+8Tp40AMvDV8Ven6oLOlzB+vev4JQIYBrQ3lH78SVh3S/LsCOJJdtOGzRZ1+MZHCq+H4sDWwXQKBgCe38ZdSBuGbFWb2SZYOn/Odv0xEjsbnm1g84qjTceNNBlcjTV+xv9vtOovwgQOy/uKNeuzpr7DwMPRkSXRlkArJuzaXLYcSYbWSrHenlIOlWFriL2zvwIMcU4ZDTgzAE1/ey2r9LaHyBygsCEaiZoDJ065Aa7Bq8cykm2/EV14PAoGBAIsyW+NAs/RWj4QTwrCMQBU8Rq00q6TtLt4UyM1aEhU9s5bcYZmFfwMp+QmtY9LYwsEGotYahUfZqavIAfqP55UsuGUbcBbdzG6wAvqWlBWbvnswIF/A0My9osv5AY6/3dBJCiYH0+MPZLndHx/ySN9ZIhyhEP1KNWmzx2adrH1A"    # The content of your private key
key_content = '{}{}{}'.format(pem_prefix, key, pem_suffix)

config = {
    "user": "ocid1.user.oc1..aaaaaaaadbwsim46sa2uh7me2va7ijjrdodnfspjgbkkpggx4pbbsprb4a7a",
    "key_content": key_content,
    "fingerprint": "5c:67:70:f4:e0:b7:ff:ca:f3:f1:f1:bb:4b:50:a0:41",
    "tenancy": "ocid1.tenancy.oc1..aaaaaaaa5rmo36hios35euhptgipx35aqnynv3fya3ybkncwijtjliylqjga",
    "region": "ca-toronto-1"
}

# config = {
#     "user": "ocid1.user.oc1..aaaaaaaadbwsim46sa2uh7me2va7ijjrdodnfspjgbkkpggx4pbbsprb4a7a",
#     "key_file": "Oracle OCI\support@d3soar.com_2024-01-09T19_14_25.995Z.pem",
#     "fingerprint": "5c:67:70:f4:e0:b7:ff:ca:f3:f1:f1:bb:4b:50:a0:41",
#     "tenancy": "ocid1.tenancy.oc1..aaaaaaaa5rmo36hios35euhptgipx35aqnynv3fya3ybkncwijtjliylqjga",
#     "region": "ca-toronto-1"
# }


# Initialize service client with default config file
identity_client = oci.identity.IdentityClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_policies_response = identity_client.list_policies(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaa5rmo36hios35euhptgipx35aqnynv3fya3ybkncwijtjliylqjga",
    # page="EXAMPLE-page-Value",
    # limit=833,
    # name="EXAMPLE-name-Value",
    # sort_by="TIMECREATED",
    # sort_order="ASC",
    # lifecycle_state="DELETED"
    )

# Get the data from response
print(list_policies_response.data)