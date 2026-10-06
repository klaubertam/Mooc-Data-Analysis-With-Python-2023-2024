import re

def file_listing():
    result = []

    with open("src/listing.txt") as file:
        for line in file:
            pattern = r"\s+(\d+)\s+([A-Z][a-z]{2})\s+(\d+)\s+(\d{1,2}):(\d{2})\s+(.*)"

            match = re.search(pattern, line)

            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                filename = match.group(6)

                result.append((size, month, day, hour, minute, filename))

    return result