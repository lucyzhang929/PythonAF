# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import azure.functions as func


def main(req: func.HttpRequest, rows: func.Out[str]) -> func.HttpResponse:
    row_1 = "{\"ProductId\":" + str(6) + ",\"Name\":" + "\"" + "Bottle" + "\"" + ",\"Cost\":" + str(10) + "}"
    row_2 = "{\"ProductId\":" + str(7) + ",\"Name\":" + "\"" + "Bottle" + "\"" + ",\"Cost\":" + str(10) + "}"
    rows.set("[" + row_1 + "," + row_2 + "]")
    return row_2