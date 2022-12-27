asciiCodes = {
    "NULL": "",
    "START_OF_HEADING": "i",
    "START_OF_TEXT": "ii",
    "END_OF_TEXT": "iii",
    "END_OF_TRANSMISSION": "iis",
    "ENQUIRY": "iisi",
    "ACKNOWLEDGEMENT": "iisii",
    "BELL": "iisiii",
    "BACK_SPACE": "iiisd",
    "HORIZONTAL_TAB": "iiis",
    "LINE_FEED": "iiisi",
    "VERTICAL_TAB": "iiisii",
    "FORM_FEED": "iiisiii",
    "CARRIAGE_RETURN": "iiisiiii",
    "SHIFT_OUT": "iiiisdd",
    "SHIFT_IN": "iiiisd",
    "DATA_LINK_ESCAPE": "iiiis",
    "DEVICE_CONTROL_1": "iiiisi",
    "DEVICE_CONTROL_2": "iiiisii",
    "DEVICE_CONTROL_3": "iiiisiii",
    "DEVICE_CONTROL_4": "iiiisiiii",
    "NEGATIVE_ACKNOWLEDGE": "iiiisiiii",
    "SYNCHRONOUS_IDLE": "iiiiisddd",
    "END_OF_TRANSMIT_BLOCK": "iiiiisdd",
    "CANCEL": "iiiiisd",
    "END_OF_MEDIUM": "iiiiis",
    "SUBSTITUTE": "iiiiisi",
    "ESCAPE": "iiiiisii",
    "FILE_SEPARATOR": "iiiiisiii",
    "GROUP_SEPARATOR": "iiiiisiiii",
    "RECORD_SEPARATOR": "iiiiisiiiii",
    "UNIT_SEPARATOR": "iiiiiisddddd",
    "SPACE": "iiiiiisdddd",
    "EXCLAMATION_MARK": "iiiiiisddd",
    "DOUBLE_QUOTES": "iiiiiisdd",
    "NUMBER": "iiiiiisd",
    "DOLLAR": "iiiiiis",
    "PERCENT": "iiiiiisi",
    "AMPERSAND": "iiiiiisii",
    "SINGLE_QUOTE": "iiiiiisiii",
    "OPEN_BRACKET": "iiiiiisiiii",
    "CLOSE_BRACKET": "iiiiiisiiiii",
    "ASTERISK": "iiiiiisiiiiii",
    "PLUS": "iiiiiiisdddddd",
    "COMMA": ""
}


def getCodes():
    return asciiCodes


def getCode(c):
    return "placeholder"
