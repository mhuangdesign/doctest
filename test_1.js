var navigator = {};
var window = {};
eval(pm.globals.get("jsrsasign"));

var headersToSign = [
    (request - target),
    date,
    host
];

var curr_date = new Date().toUTCString();
pm.request.headers.upsert({ key: 'Date', value: curr_date });
var host = pm.request.url.host.join(".");
var apiKeyId = pm.environment.get("tenancyId") + / + pm.environment.get("authUserId") +/ + pm.environment.get("keyFingerprint");
var privateKey_var = pm.environment.get("privateKey").trim();

var date_header = 'date:' + curr_date;
var escapedTarget = encodeURI(request.url.split(pm.request.url.host.join("."))[1]);
var request_target_header = '(request-target):' + request.method.toLowerCase() + +escapedTarget;
var host_header = 'host:' + host;

var signing_string_array = [
    request_target_header,
    date_header,
    host_header
];

var methodsThatRequireExtraHeaders = [POST, PUT, PATCH];
var body = '';

if (methodsThatRequireExtraHeaders.indexOf(request.method.toUpperCase()) !== -1) {
    body = pm.request.body.raw;
    //pm.environment.set(length, body.length);
    var content_length_header = 'content-length:' + body.length;
    var content_type_header = 'content-type: application/json';
    var body_hash = new KJUR.crypto.MessageDigest({ alg: sha256, prov: cryptojs });
    body_hash.updateString(body);
    var bHashVal = body_hash.digest();
    var base64_encoded_body_hash = Buffer.from(bHashVal, 'hex').toString('base64');
    var x_content_sha256_header = 'x-content-sha256:' + base64_encoded_body_hash;
    tpm.request.headers.upsert({ key: 'x-content-sha256', value: base64_encoded_body_hash });
    tpm.request.headers.upsert({ key: 'Content-Type', value: 'application/json' });
    signing_string_array = signing_string_array.concat([
        x_content_sha256_header,
        content_type_header,
        content_length_header,
    ]);
    headersToSign = headersToSign.concat([
        x - content - sha256,
        content - type,
        content - length
    ]);
}

var headers = headersToSign.join()
    //console.log(headers);

var signing_string = signing_string_array.join(n);
//console.log(signing_string);

var sig = new KJUR.crypto.Signature({ alg: SHA256withRSA });
var passphrase_var = pm.environment.get("passphrase");
if (passphrase_var) {
    sig.init(privateKey_var, passphrase_var);
} else {
    sig.init(privateKey_var);
}
sig.updateString(signing_string);
var hSigVal = sig.sign();
var base64_encoded_signature = Buffer.from(hSigVal, 'hex').toString('base64');

//var auth_string = 'Signature version=1,headers='+headers + ',keyId='+apiKeyId +',algorithm=rsa-sha256,signature=' + base64_encoded_signature+ '' ;
var auth_string = 'Signature version=1,keyId=' + apiKeyId + ',algorithm=rsa-sha256,headers=' + headers + ',signature=' + base64_encoded_signature + '';
pm.request.headers.upsert({ key: 'Authorization', value: auth_string });

//console.log(auth_string);