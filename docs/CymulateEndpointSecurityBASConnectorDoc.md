## About the connector
The Cymulate Exposure Management and Security Validation Platform provides the technology for exposure
discovery, validation, and prioritization with business insights and intelligence. This simplifies security leaders’ risk
and resilience to emergent threats and a rapidly changing attack surface. With a complete view of the security
posture and business risks, the Cymulate platform gives security leaders the data they need to define the scope for cyber initiatives, successfully mobilize mitigations, and continuously assess security operations performance.
<p>This document provides information about the Cymulate Endpoint Security - BAS Connector, which facilitates automated interactions, with a Cymulate Endpoint Security - BAS server using FortiSOAR&trade; playbooks. Add the Cymulate Endpoint Security - BAS Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cymulate Endpoint Security - BAS.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cymulate-endpoint-security</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cymulate Endpoint Security - BAS server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cymulate Endpoint Security - BAS server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cymulate Endpoint Security - BAS</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Cymulate server URL to connect and perform the automated operations.
</td>
</tr><tr><td>Secret Key</td><td>Specify the Secret Key of the API Application already created in the Cymulate Server.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Assessment</td><td>Creates an Endpoint Security assessment based on the input parameters values provided.</td><td>create_assessment <br/>Investigation</td></tr>
<tr><td>Get Latest Report Results</td><td>Retrieves the latest endpoint security report results from the cymulate server.</td><td>get_latest_report_results <br/>Investigation</td></tr>
<tr><td>Get Latest Technical Report Results</td><td>Retrieves the latest endpoint security technical report results from the cymulate server.</td><td>get_latest_technical_report_results <br/>Investigation</td></tr>
<tr><td>Get Latest SIEM Detection Results</td><td>Retrieves the latest SIEM detection results from endpoint security assessments from cymulate server.</td><td>get_latest_siem_detection_results <br/>Investigation</td></tr>
<tr><td>Get Detection Results By ID</td><td>Retrieves the detection result data for a specific ID from cymulate server.</td><td>get_detection_results_by_id <br/>Investigation</td></tr>
<tr><td>Get Attack Navigator Results</td><td>Retrieves the latest (overview) Endpoint Security ATTACK navigator report results by environment ID from cymulate server.</td><td>get_attack_navigator_results <br/>Investigation</td></tr>
<tr><td>Get Attack Navigator Results By Assessment ID</td><td>Retrieves the Endpoint Security ATTACK navigator report results for a specific assessment from cymulate server.</td><td>get_attack_navigator_results_by_assessment_id <br/>Investigation</td></tr>
<tr><td>Get Assessment History</td><td>Retrieves the Endpoint Security assessment history within the date range provided. If a date range is not provided, the response will retrieve the history from the last 30 days from cymulate server.</td><td>get_assessment_history <br/>Investigation</td></tr>
<tr><td>Get Technical Report Results By Assessment ID</td><td>Retrieves the endpoint security technical report results for a specific assessment from the cymulate server.</td><td>get_technical_report_results_by_assessment_id <br/>Investigation</td></tr>
<tr><td>Get Executive Report Results By Assessment ID</td><td>Retrieves the Endpoint Security executive report results for a specific assessment from the cymulate server.</td><td>get_executive_report_results_by_assessment_id <br/>Investigation</td></tr>
<tr><td>Get Template List</td><td>Retrieve a list of available Endpoint Security templates from cymulate server.</td><td>get_template_list <br/>Investigation</td></tr>
<tr><td>Get Template By ID</td><td>Retrieve a specific Endpoint Security template by its ID from cymulate server.</td><td>get_template_by_id <br/>Investigation</td></tr>
<tr><td>Get Assessment Status</td><td>Retrieve an Endpoint Security assessment status by the assessment ID from cymulate server.</td><td>get_assessment_status <br/>Investigation</td></tr>
<tr><td>Stop Assessment</td><td>Stop an Endpoint Security assessment that is running in cymulate.</td><td>stop_assessment <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Assessment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Agent Name</td><td>Specify the agent name (Computer Name).
</td></tr><tr><td>Agent Profile Name</td><td>Specify the profile name.
</td></tr><tr><td>Template ID</td><td>Specify the template ID.
</td></tr><tr><td>Worm IP Range to Exclude</td><td>Specify the worm IP range to exclude.
</td></tr><tr><td>Schedule Loop</td><td>Specify the frequency for triggering the assessment eg: one-time.
</td></tr><tr><td>Integrations to Select</td><td>Specify the crown jewels (Important resources on which to create assessment).
</td></tr><tr><td>Schedule</td><td>(Optional) Specify the time at which assessment should be triggered.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Latest Report Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>(Optional) Specify the environment ID. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Latest Technical Report Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Offset</td><td>(Optional) Specify the number of records to skip.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the limit of how many items to get - Default = 100.
</td></tr><tr><td>Environment ID</td><td>(Optional) Specify the environment ID. If an ID is not provided, the request will return latest technical report results for the Default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Latest SIEM Detection Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>(Optional) Specify the environment ID. If an ID is not provided, the request will return latest technical report results for the Default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Detection Results By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>Specify the endpoint security payload ID whose details to retrieve from cymulate server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Attack Navigator Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>(Optional) Specify the environment ID. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Attack Navigator Results By Assessment ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>Specify the assessment ID whose details to retrieve from cymulate server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Assessment History
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>From Date</td><td>(Optional) Specify the date from where to fetch assessments.
</td></tr><tr><td>To Date</td><td>(Optional) Specify the date until which assessments should be fetched.
</td></tr><tr><td>Environment ID</td><td>(Optional) Specify the environment ID. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Technical Report Results By Assessment ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>Specify the assessment ID whose details to retrieve from cymulate server.
</td></tr><tr><td>Offset</td><td>(Optional) Specify the number of records to skip.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the limit of how many items to get - Default = all.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Executive Report Results By Assessment ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>Specify the assessment ID whose details to retrieve from cymulate server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Template List
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Template By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>Specify the template ID whose details to retrieve from cymulate server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Assessment Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>(Optional) Specify the assessment ID whose details to retrieve from cymulate server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Stop Assessment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>(Optional) Specify the environment ID. If an ID is not provided, the most recently launched assessment will be stopped.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - cymulate-endpoint-security - 1.0.0` playbook collection comes bundled with the Cymulate Endpoint Security - BAS connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cymulate Endpoint Security - BAS connector.

- Create Assessment
- Get Assessment History
- Get Assessment Status
- Get Attack Navigator Results
- Get Attack Navigator Results By Assessment ID
- Get Detection Results By ID
- Get Executive Report Results By Assessment ID
- Get Latest Report Results
- Get Latest SIEM Detection Results
- Get Latest Technical Report Results
- Get Technical Report Results By Assessment ID
- Get Template By ID
- Get Template List
- Stop Assessment

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
