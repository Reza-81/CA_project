def sign_extended_16_32(a : str) -> str:
    return 16*a[0]+a

def sign_extended_8_32(a : str) -> str:
    return 24*a[0]+a

def unsign_extended_16_32(a : str) -> str:
    return 16*'0'+a

def unsign_extended_8_32(a : str) -> str:
    return 24*'0'+a