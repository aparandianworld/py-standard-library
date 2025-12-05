import configparser

try:
    parser = configparser.ConfigParser()
    parser.read("config.cfg")

    print(parser.sections())
    print(parser.has_section("metadata"))
    #    print(parser.items("server:dr"))

    host = parser.get("server:main", "host")
    port = parser.getint("server:main", "port")
    print(f"Host: {host} Type: {type(host)}, Port: {port} Type: {type(port)}")

except TypeError as e:
    print(e)
except Exception as e:
    print(e)
