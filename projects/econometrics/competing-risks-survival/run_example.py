import csv
import json
from pathlib import Path

from survival import aalen_johansen, kaplan_meier_net_approval


def main():
    path = Path(__file__).with_name("example_data.csv")
    with path.open(newline="", encoding="utf-8") as handle:
        records = [
            {"time": float(row["days_from_complete_application"]), "event": row["event"]}
            for row in csv.DictReader(handle)
        ]
    result = {
        "synthetic_data_only": True,
        "observation_count": len(records),
        "aalen_johansen": aalen_johansen(records),
        "one_minus_kaplan_meier_net_approval": kaplan_meier_net_approval(records),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
