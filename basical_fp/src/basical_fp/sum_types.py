from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            result = [
                [x if isinstance(x, str) else str(x) for x in row] for row in data
            ]
            return ("Pending...", result)
        case CSVExportStatus.PROCESSING:
            temp = ""
            for xs in data:
                temp.join(",".join(xs) + "\\n")

            return ("Processing...", temp)
        case CSVExportStatus.SUCCESS:
            return ["Success!", data]
        case CSVExportStatus.FAILURE:
            return ["Unknown error, retrying...", data]
        case _:
            raise Exception("unknown export status")
