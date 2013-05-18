"""
This is a data file for IsyEvent.py
 
"""


__all__ = [] # EVENT_CTRL, LOG_USERID

EVENT_CTRL  = {
        "_0" : "Heartbeat", 
        "_1" : "Trigger", 
        "_2" : "Protocol Specific", 
        "_3" : "Nodes Updated",
        "_4" : "System Config Updated", 
        "_5" : "System Status", 
        "_6" : "Internet Access", 
        "_7" : "System Progress", 
        "_8" : "Security System", 
        "_9" : "System Alert", 
        "_10" : "Electricity",
        "_11" : "Climate", 
        "_12" : "AMI/SEP", 
        "_13" : "Ext Energy Mon", 
        "_14" : "UPB Linker", 
        "_15" : "UPB Dev State", 
        "_16" : "UPB Dev Status", 
        "_17" : "Gas", 
        "_18" : "ZigBee", 
        "_19" : "Elk", 
        "_20" : "Device Link", 
        "DON" : "Device On", 
        "DFON" : "Device Fast On", 
        "DOF" : "Device Off", 
        "DFOF" : "Device Fast Off", 
        "ST" : "Status", 
        "OL" : "On Level",
        "RR" : "Ramp Rate", 
        "BMAN" : "Start Manual Change",
        "SMAN" : "Stop Manual Change",
        "CLISP" : "Setpoint",
        "CLISPH" : "Heat Setpoint",
        "CLISPC" : "Cool Setpoint",
        "CLIFS" : "Fan State",
        "CLIMD" : "Thermostat Mode",
        "CLIHUM" : "Humidity",
        "CLIHCS" : "Heat/Cool State",
        "BRT" : "Brighten",
        "DIM" : "Dim",
        "X10" : "Direct X10 Commands",
        "BEEP" : "Beep",
}


LOG_USERID = [ "SYSTEM_USER", "SYSTEM_DRIVER_USER", "WEB_USER",
	    "SCHEDULER_USER", "D2D_USER", " ELK_USER",
	    "SEP_DEVICE_UMETER_USER", "SEP_DEVICE_UPRICE_USER",
	    "SEP_DEVICE_UMSG_USER", "SEP_DEVICE_UDR_USER",
	    "GAS_METER_USER" ]


LOG_TYPES = {
    "1": "SYSTEM_STARTUP",
    "2": "SYSTEM_SHUTDOWN",
    "3": "WARNING",
    "4": "INFO",
    "5": "LOG",
    "6": "UD_SEP_SUBSYS_STARTUP",
    "-1": "REQUEST_FAILED_ERROR",
    "-2": "DEVICE_COMMUNICATION_ERROR",
    "-3": "DEVICE_RETURNED_INVALID_NODE",
    "-4": "DEVICE_RETURNED_INVALID_ADDRESS",
    "-5": "ERROR_LOGGER_STARTUP",
    "-10": "MAIN_HAML_DRIVER_NOT_FOUND",
    "-20": "MAIN_LOCAL_DEVICE_BLANK",
    "-100": "SYSTEM_NO_NETWORK_CONNECTION",
    "-101": "SYSTEM_WEBSERVER_SELECT_FAILED",
    "-500": "HAML_DRIVER_LISTENER_NOT_REGISTERED",
    "-1000": "HAML_PARSER_UNDEFINED_ELEMENT",
    "-1001": "HAML_PARSER_ONDATA",
    "-5001": "UPNP_DRIVER_NO_DEVICES_CONFIGURED",
    "-5002": "UPNP_DRIVER_SERIAL_READER_FAILED",
    "-5003": "UPNP_DRIVER_MAX_DEVICES",
    "-5004": "UPNP_SERVICE_TYPE_SEARCH_NS",
    "-5005": "UPNP_SUBSCRIPTION_NOT_FOUND_FOR_RENEWAL",
    "-5006": "UPNP_SUBSCRIPTION_NOT_FOUND_FOR_CANCELATION",
    "-5007": "UPNP_INVALID_SUBSCRIPTION_URL",
    "-5008": "UPNP_INVALID_SUBSCRIPTION_CALLBACK",
    "-5009": "UPNP_MAX_SUBSCRIBERS",
    "-5010": "UPNP_SUBSCRIBER_TCP_CONNECT_FAILURE",
    "-5011": "PROCESS_DEVICE_STATE_CHANGE_SID_NOT_FOUND",
    "-5012": "UPNP_SUBSCRIBER_NOREPLY_TO_EVENT_1",
    "-5013": "UPNP_SUBSCRIBER_NOREPLY_TO_EVENT_2",
    "-5014": "UPNP_SUBSCRIBER_NOREPLY_TO_EVENT_3",
    "-5015": "UPNP_CONTROL_MALFORMED_SOAP_REQUEST_1",
    "-5016": "UPNP_CONTROL_MALFORMED_SOAP_REQUEST_2",
    "-6000": "OS_DUPLICATE_TASK_PRIORITY",
    "-6001": "OS_OPEN_SERIAL_FAILED",
    "-7020": "D2D_PARSER_ERROR",
    "-7029": "NOTIFICATIONS_MAIL_TO_ADDRESS_REQUIRED",
    "-7030": "NOTIFICATIONS_SEND_MAIL_FAILED",
    "-7050": "D2D_EXPECTED_D2D_TAG",
    "-7051": "D2D_UNEXPECTED_TAG_IN_SENSE",
    "-7052": "D2D_UNEXPECTED_TAG_IN_CONDITION",
    "-7501": "DIAG_PARSER_ERROR",
    "-7601": "LINK_PARSER_ERROR",
    "-10100": "PNP_SECURITY_NOT_VERIFIED",
    "-10001": "SSL_DECODING_LENGTHS_FAILED",
    "-10002": "SSL_DECODING_PMOD_FAILED",
    "-10003": "SSL_DECODING_PEXP_FAILED",
    "-10004": "SSL_DECODING_PRI_EXP_FAILED",
    "-10005": "SSL_DECODING_PRI_P_FAILED",
    "-10006": "SSL_DECODING_PRI_Q_FAILED",
    "-10007": "SSL_DECODING_PRI_X1_FAILED",
    "-10008": "SSL_DECODING_PRI_X2_FAILED",
    "-10009": "SSL_DECODING_COEFF_FAILED",
    "-10010": "SSL_DECODING_CERT_FAILED",
    "-10011": "SSL_REQUEST_NOT_AUTHENTICATED",
    "-10026": "SECURE_SESSION_DOES_NOT_EXIST",
    "-10027": "SECURE_SESSIONS_EXHAUSTED",
    "-10101": "AUTHENTICATION_UNSUPPORTED_UID_LEN",
    "-10102": "AUTHENTICATION_UNSUPPORTED_PWD_LEN",
    "-10103": "AUTHENTICATION_USER_ID_DOES_NOT_EXIST",
    "-10104": "AUTHENTICATION_USER_ID_PWD_NOT_PRESENT",
    "-10105": "AUTHENTICATION_WRONG_PASSWORD",
    "-10106": "AUTHENTICATION_FAILED",
    "-10107": "HTTP_AUTH_DECODING_FAILED",
    "-11000": "SECURITY_INITIALIZATION_FAILED",
    "-12000": "TIMED_OUT_WAITING_FOR_CRITICAL_SECION",
    "-12001": "ERROR_LEAVING_CRITICAL_SECTION_NOT_OWNED",
    "-13000": "CONTENT_LEN_NOT_EQUAL_TO_HEADER_CONTENT_LEN",
    "-14001 ": "XML_MALFORMED_TAG",
    "-14002": "XML_MALFORMED_END_TAG",
    "-14003 ": "XML_NO_START_TAG",
    "-14004 ": "XML_NO_TAG_NAME",
    "-14005 ": "XML_START_END_NAME_MISMATCH",
    "-20000": "MALFORMED_UPNP_HEADERS",
    "-50000": "MAIL_SERVER_CONNECT_ERROR",
    "-50001": "SMTP_SERVER_FAILURE",
    "-50010": "MAIL_SERVER_DNS_ERROR",
    "-50011": "MAIL_MAX_FROM_LEN",
    "-50012": "MAIL_MAX_SUBJECT_LEN",
    "-50013": "MAIL_MAX_TO_LEN",
    "-60000": "NTP_CONFIG_SERVER_NO_HOST_PARAM",
    "-60001": "NTP_CONFIG_SERVER_ADDRESS_RESOLUTION_FAILED",
    "-60002": "NTP_CONFIG_SERVER_NO_INTERVAL_PARAM",
    "-60006": "NTP_SERVER_NOT_RESPONDING",
    "-60007": "NTP_SERVER_CONNECT_ERROR",
    "-70000": "OUT_OF_MEMORY",
    "-80000": "IGD_FAILED_PARSING_DESCRIPTION_URL",
    "-80001": "IGD_FAILED_RETRIEVING_DESCRIPTION_FILE",
    "-80002": "IGD_FAILED_RETRIEVING_URL_BASE",
    "-80003": "IGD_FAILED_PARSING_URL_BASE",
    "-80004": "IGD_FAILED_RETRIEVING_WAN_CONNECTION_DEVICE",
    "-80005": "IGD_FAILED_RETRIEVING_CONTROL_URL",
    "-80006": "IGD_FAILED_PARSING_CONTROL_URL",
    "-80007": "IGD_FAILED_RETRIEVING_EXTERNAL_IP",
    "-80008": "IGD_NO_RESPONSE_FROM_GATEWAY",
    "-80009": "IGD_FAILED_STRIPPING_HTTP_HEADERS",
    "-80010": "IGD_FAILED_DELETING_PORT_FORWARD_MAP",
    "-80011": "IGD_FAILED_ADDING_PORT_FORWARD_MAP",
    "-80012": "IGD_FAILED_GETTING_SPECIFIC_ENTRY",
    "-90001": "CRC_INVALID_ORDER",
    "-90002": "CRC_INVALID_POLYNOM",
    "-90003": "CRC_INVALID_CRC_INIT",
    "-90004": "CRC_INVALID_CRC_XOR",
    "-100000": "LOGGER_DIRECTORY_CREATION_FAILED",
    "-100001": "LOGGER_SD_IS_NOT_INSTALLED",
    "-100002": "LOGGER_LOG_FILE_OPEN_FAILED",
    "-110000": "FILE_TO_STRING_OPEN_FAILED",
    "-110001": "FILE_TO_STRING_MEM_ALLOC_FAILED",
    "-110002": "SD_DRIVE_FORMAT_FAILED_1",
    "-110003": "SD_DRIVE_FORMAT_FAILED_2",
    "-110004": "SD_DRIVE_MOUNT_FAILED_1",
    "-110005": "SD_DRIVE_MOUNT_FAILED_2",
    "-110006": "SEND_FILE_OPEN_FAILED",
    "-110007": "SEND_FILE_READ_FAILED",
    "-110008": "RECEIVE_FILE_WRITE_FAILED",
    "-110009": "RECEIVE_FILE_OPEN_FAILED",
    "-110010": "SD_DRIVE_DIRECTORY_CREATION_FAILED",
    "-110011": "SD_DRIVE_CONFIG_FILE_OPEN_WRITE_FAILED",
    "-110012": "SD_DRIVE_CONFIG_FILE_OPEN_READ_FAILED",
    "-110013": "SD_DRIVE_CONFIG_WRITE_FAILED",
    "-110014": "SD_DRIVE_CONFIG_READ_FAILED",
    "-110015": "STRING_TO_FILE_OPEN_FAILED",
    "-110016": "STRING_TO_FILE_WRITE_FAILED",
    "-110017": "FILE_TO_STRING_READ_FAILED",
    "-110018": "REMOVE_FILE_FAILED",
    "-110019": "REMOVE_DIR_FAILED",
    "-110020": "FLUSH_FILE_FAILED",
    "-110021": "CLOSE_FILE_FAILED",
    "-110022": "OPEN_FILE_FAILED",
    "-110023": "FLUSH_FILE_SYSTEM_FAILED",
    "-110024": "FILESYSTEM_INIT_FAILED",
    "-110025": "FILESYSTEM_CRIT_FAILED",
    "-120000": "FIRMWARE_UPDATE_OPEN_FILE_FAILED",
    "-120001": "FIRMWARE_UPDATE_HEADER_READ_FAILED",
    "-120002": "FIRMWARE_UPDATE_CHECKSUM_FAILED",
    "-120003": "FIRMWARE_UPDATE_MALLOC_FAILED",
    "-120004": "FIRMWARE_UPDATE_DATA_READ_FAILED",
    "-130000": "ELK_CONFIG_PARSER_ERROR",
    "-140000": "HTTP_CLIENT_DNS_ERROR",
    "-140001": "HTTP_CLIENT_BASE64_ENCRYPTION_FAILED",
    "-140002": "HTTP_CLIENT_CONNECTION_TIMED_OUT",
    "-140003": "HTTP_CLIENT_WRITE_HEADER_FAILED",
    "-140004": "HTTP_CLIENT_WRITE_BODY_FAILED",
    "-140005": "HTTP_CLIENT_READ_RESPONSE_FAILED",
    "-140006": "HTTP_CLIENT_HEADER_NO_STATUS",
    "-140007": "HTTP_CLIENT_RESOURCE_MOVED",
    "-140008": "HTTP_CLIENT_REQUEST_FAILED",
    "-140009": "HTTP_CLIENT_NO_NETWORK",
    "-150000": "TCP_CLIENT_WRITE_FAILED",
    "-150100": "UDP_CLIENT_DNS_ERROR",
    "-160000": "PROTOCOL_READER_READ_ERROR",
    "-160001": "PROTOCOL_READER_BUFFER_OVERFLOW",
    "-160002": "PROTOCOL_READER_REOPEN_ERROR",
    "-170000": "WEB_MODULE_NO_FREE_SPACE",
    "-170001": "SYSTEM_ACCESS_LOG",
    "-180000": "SEP_NETWORK_SCAN_ERROR",
    "-180001": "SEP_NETWORK_KEY_EST_ERROR",
    "-180002": "SEP_NETWORK_DISCOVERY_ERROR",
    "-180003": "SEP_NETWORK_SYNCH_ERROR",
    "-180004": "SEP_MODULE_RESET_ERROR",
    "-180005": "SEP_MODULE_INVALID_CALL_ERROR",
    "-180006": "SEP_MODULE_UNKNOWN_ERROR",
    "-190001": "UDERR_ISY_API_NO_SPACE",
    "-190002": "UDERR_ISY_API_INVALID_8_3_FILENAME",
    "-190003": "UDERR_ISY_API_INVALID_PGM_FILENAME",
    "-190004": "UDERR_ISY_API_INCORRECT_PGM_KEY",
    "-190005": "UDERR_ISY_API_INVALID_PGM_URL_SEARCH_STRING",
    "-200000": "DEVICE_DRIVER_ERROR_MSG",
    "-210001": "CALL_HOME_PORTAL_NO_FD",
}



#
# Do nothing
# (syntax check)
#
if __name__ == "__main__":
    import __main__
    print(__main__.__file__)

    print("syntax ok")
    exit(0)
