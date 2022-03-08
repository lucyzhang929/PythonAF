# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import azure.functions as func


def main(req: func.HttpRequest, rows: func.SqlRowList) -> func.HttpResponse:
    return func.HttpResponse(rows.to_json(), mimetype='application/json')