def get_password(username, context):
    user_key = username.upper().replace("-", "_")
    password = context.config.userdata[f"{user_key}_PWD"]
    return password
