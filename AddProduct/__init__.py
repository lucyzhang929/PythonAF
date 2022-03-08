# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import azure.functions as func


def main(req: func.HttpRequest, row: func.Out[func.SqlRow]) -> func.HttpResponse:
    # data = "{\"ProductId\":6,\"Name\":\"Test1\",\"Cost\":100}"
    # row.set(data)
    row.set(func.SqlRow({"ProductId": "6", "Name": "test", "Cost": "100"}))
    return 'OK'