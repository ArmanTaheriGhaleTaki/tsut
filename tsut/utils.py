def id_normalizer(identifier: str) -> str:
    if identifier.startswith('@'):
        return identifier
    else:
        return '@' + identifier
