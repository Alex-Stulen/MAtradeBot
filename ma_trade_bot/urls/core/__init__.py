def build_absolute_url(host: str, relative_url: str):
    """
    Builds and returns an absolute path based on a host and a relative path.
    Examples:
        host = https://example.com
        relative_url = ./images/some-url/
        returns: https://example.com/images/some-url/

        OR

        host = https://example.com
        relative_url = ../files/some-file-path/
        returns: https://example.com//files/some-file-path/

        OR

        host = https://example.com
        relative_url = /////photos/some-photo-url/
        returns: https://example.com/photos/some-photo-url/

    """
    # replace last / for host while host endswith /
    while host.endswith('/'):
        host = host[:-1]

    slash = '/'
    dot_slash = './'
    dot2_slash = '../'

    # replace ./ and ../ while url part startswith ./ or ../
    while relative_url.startswith(dot_slash) or relative_url.startswith(dot2_slash):
        if relative_url.startswith(dot_slash):
            relative_url = relative_url.replace(dot_slash, '', 1)
        elif relative_url.startswith(dot2_slash):
            relative_url = relative_url.replace(dot2_slash, '', 1)

    # replace / while url part startswith / and next symbol also /
    while relative_url.startswith(slash) and len(relative_url) > 1 and relative_url[1] == slash:
        relative_url = relative_url.replace(slash, '', 1)

    # add a / to the beginning if the relative url does not start with a slash
    if not relative_url.startswith(slash) and not relative_url.startswith(dot_slash) \
            and not relative_url.startswith(dot2_slash):
        relative_url = slash + relative_url

    return host + relative_url
