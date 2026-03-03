import json
import pprint


def save_to_json(logs, filename=None):
    if filename:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2)
    return json.dumps(logs, indent=2)


def pars_logs(logs):
    parsed_logs = []

    for line in logs:
        parts = line.split("|")

        date = parts[0]
        level = parts[1]
        message = parts[2]

        fields = message.split(" ")
        data = {}

        for f in fields:
            kv = f.split("=")
            try:
                kv[1] = int(kv[1])
            except:
                pass

            data[kv[0]] = kv[1]

        data["date"] = date
        data["level"] = level

        parsed_logs.append(data)
    return parsed_logs


def filter_logs(logs, **kwargs):
    filtered = []
    for log in logs:
        flag = True
        for key, value in kwargs.items():
            if key not in log or log[key] != value:
                flag = False
                break
        if flag:
            filtered.append(log)
    return filtered


def count_logs(logs):
    info = 0
    error = 0
    warning = 0

    for log in logs:
        if log["level"] == "INFO":
            info += 1
        if log["level"] == "ERROR":
            error += 1
        if log["level"] == "WARNING":
            warning += 1

    print(f"INFO: {info}, ERROR: {error}, WARNING: {warning}")
    return {"INFO": info, "ERROR": error, "WARNING": warning}


if __name__ == "__main__":
    logs = [
        "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
        "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
        "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
        "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
        "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
    ]

    parsed_logs = pars_logs(logs)


    """
    ТЕСТЫ
    
    print("=== ВСЕ ЛОГИ ===")
    pprint.pprint(parsed_logs)
    print()

    print("=== ПОДСЧЕТ ПО УРОВНЯМ ===")
    count_logs(parsed_logs)
    print()

    print("=== ФИЛЬТР: level=ERROR ===")
    error_logs = filter_logs(parsed_logs, level="ERROR", user="tom")
    pprint.pprint(error_logs)
    print()

    print("=== ФИЛЬТР: status=fail ===")
    fail_logs = filter_logs(parsed_logs, status="fail")
    pprint.pprint(fail_logs)
    print()

    json_str = save_to_json(parsed_logs)
    print(json_str)

    print("=== ФИЛЬТР: user=anna, action=payment ===")
    anna_payment = filter_logs(parsed_logs, user="anna", action="payment")
    pprint.pprint(anna_payment)
    print()


    """











