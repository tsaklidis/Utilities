import json
import logging
import re
import requests


def handle_non_200(answer):
    try:
        rsp = json.loads(answer.content)
        detail = rsp.get('detail', answer.text)
    except json.decoder.JSONDecodeError:
        try:
            detail = re.search(r"(?<=<title).*?(?=</title)",
                               answer.text).group(0)
        except AttributeError:
            detail = answer.text
        return detail


def send_request(method, url, extra_headers=None, params=None, body=None,
                 cookies=None, return_json=False, convert_to_json=True,
                 debug=False):

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    s = requests.Session()
    final_headers = {}

    if extra_headers:
        final_headers.update(extra_headers)

    if convert_to_json and body:
        # Load body in json format
        try:
            body = json.dumps(body)
        except (ValueError, TypeError):
            raise Exception('send_request() body is not json formatted')

    if method == 'GET':
        ans = s.get(url, params=params, headers=final_headers, cookies=cookies)
    elif method == 'POST':
        ans = s.post(url, data=body, cookies=cookies)
    elif method == 'DELETE':
        ans = requests.delete(url, data=body, headers=final_headers)
    elif method == 'PATCH':
        ans = requests.patch(url, data=body, headers=final_headers)
    elif method == 'PUT':
        ans = requests.put(url, data=body, headers=final_headers)
    else:
        raise Exception('Bad request type')

    if ans.status_code in [200, 201, 204]:
        return json.loads(ans.content) if return_json else ans
    handle_non_200(ans)
