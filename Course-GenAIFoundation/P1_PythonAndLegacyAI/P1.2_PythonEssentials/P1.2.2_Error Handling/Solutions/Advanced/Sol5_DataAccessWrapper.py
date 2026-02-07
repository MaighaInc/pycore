"""
Solution: Advanced Assignment 5 - Data Access Wrapper
"""

# Test data
configs = [
    {"database": {"host": "localhost", "port": 5432}},
    {"database": {"host": "remote.com"}},
    {"cache": {"ttl": 300}},
    None
]

paths = [
    ["database", "host"],
    ["database", "port"],
    ["database", "host"],
    ["database", "host"]
]

default_value = "default"

def get_config(config_dict, path, default):
    try:
        if config_dict is None:
            raise TypeError("Config is None")
        
        current = config_dict
        for key in path:
            current = current[key]
        return current, None
    except KeyError:
        return default, "KeyError"
    except TypeError:
        return default, "TypeError"
    except IndexError:
        return default, "IndexError"

# Process configs
for i, (config, path) in enumerate(zip(configs, paths)):
    value, error = get_config(config, path, default_value)
    path_str = ".".join(path)
    
    if error:
        print(f"Config {i}, path {path_str} -> {value} ({error})")
    else:
        print(f"Config {i}, path {path_str} -> {value}")
