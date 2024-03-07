"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('cymulate-endpoint-security')

API_VERSION = '/v1'


def make_api_call(method="GET", endpoint="", config=None, params=None, data=None, json_data=None):
    try:
        headers = {
            "Content-Type": "application/json",
            "x-token": config.get("key")
        }
        server_url = config.get('url').strip('/')
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://" + server_url
        server_url = server_url + API_VERSION + endpoint
        response = requests.request(method=method, url=server_url,
                                    headers=headers, data=data, json=json_data, params=params,
                                    verify=config.get('verify_ssl'))
        if response.ok:
            return response.json()
        else:
            if response.text != "":
                err_resp = response.json()
                failure_msg = err_resp['errors']
                error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason,
                                                                     failure_msg if failure_msg else '')
            else:
                error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
            logger.error(error_msg)
            raise ConnectorError(error_msg)
    except requests.exceptions.SSLError:
        logger.error('An SSL error occurred')
        raise ConnectorError('An SSL error occurred')
    except requests.exceptions.ConnectionError:
        logger.error('A connection error occurred')
        raise ConnectorError('A connection error occurred')
    except requests.exceptions.Timeout:
        logger.error('The request timed out')
        raise ConnectorError('The request timed out')
    except requests.exceptions.RequestException:
        logger.error('There was an error while handling the request')
        raise ConnectorError('There was an error while handling the request')
    except Exception as err:
        raise ConnectorError(str(err))


def convert_date_time(str_date):
    return datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")


def build_payload(params):
    data = {}
    for k, v in params.items():
        if v:
            if k in ['fromDate', 'toDate']:
                data[k] = convert_date_time(v)
            elif k == 'selectedPlatforms':
                data[k] = [x.strip() for x in str(v).split(",")]
            else:
                data[k] = v
    return data


def get_latest_report_results(config, params):
    params = build_payload(params)
    endpoint = "/edr/attacks"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_latest_technical_report_results(config, params):
    params = build_payload(params)
    endpoint = "/edr/attacks/technical"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_latest_siem_detection_results(config, params):
    params = build_payload(params)
    endpoint = "/edr/attacks/technical/siem"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_detection_results_by_id(config, params):
    endpoint = f"/edr/history/technical/detection/{params.get('id')}"
    return make_api_call(endpoint=endpoint, config=config)


def get_attack_navigator_results(config, params):
    params = build_payload(params)
    endpoint = "/edr/attacks/attacknavigator"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_attack_navigator_results_by_assessment_id(config, params):
    endpoint = f"/edr/attacks/attacknavigator/{params.get('id')}"
    return make_api_call(endpoint=endpoint, config=config)


def get_assessment_history(config, params):
    params = build_payload(params)
    endpoint = "/edr/history/get-ids/"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_technical_report_results_by_assessment_id(config, params):
    params = build_payload(params)
    endpoint = f"/edr/history/technical/{params.pop('id','')}"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_executive_report_results_by_assessment_id(config, params):
    endpoint = f"/edr/history/executive/{params.pop('id','')}"
    return make_api_call(endpoint=endpoint, config=config)


def create_assessment(config, params):
    params = build_payload(params)
    endpoint = "/edr/start"
    return make_api_call(method='POST', endpoint=endpoint, config=config, json_data=params)


def stop_assessment(config, params):
    params = build_payload(params)
    endpoint = "/edr/stop"
    return make_api_call(method='POST', endpoint=endpoint, config=config, json_data=params)


def get_template_list(config, params):
    endpoint = "/edr/templates/"
    return make_api_call(endpoint=endpoint, config=config)


def get_template_by_id(config, params):
    endpoint = f"/edr/templates/{params.get('id')}"
    return make_api_call(endpoint=endpoint, config=config)


def get_assessment_status(config, params):
    params = build_payload(params)
    endpoint = "/edr/status"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def _check_health(config):
    try:
        get_template_list(config, params={})
        return True
    except Exception as e:
        logger.error("Invalid Credentials: %s" % str(e))
        raise ConnectorError("Invalid Credentials")


operations = {
    'get_latest_report_results': get_latest_report_results,
    'get_latest_technical_report_results': get_latest_technical_report_results,
    'get_latest_siem_detection_results': get_latest_siem_detection_results,
    'get_detection_results_by_id': get_detection_results_by_id,
    'get_attack_navigator_results': get_attack_navigator_results,
    'get_attack_navigator_results_by_assessment_id': get_attack_navigator_results_by_assessment_id,
    'get_assessment_history': get_assessment_history,
    'get_technical_report_results_by_assessment_id': get_technical_report_results_by_assessment_id,
    'get_executive_report_results_by_assessment_id': get_executive_report_results_by_assessment_id,
    'get_template_list': get_template_list,
    'get_template_by_id': get_template_by_id,
    'get_assessment_status': get_assessment_status,
    'create_assessment': create_assessment,
    'stop_assessment': stop_assessment
}
