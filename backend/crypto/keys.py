from typing import TypedDict
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.asymmetric.rsa import (
    RSAPublicKey,
    RSAPrivateKey,
    generate_private_key,
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PublicFormat,
    PrivateFormat,
    load_pem_private_key,
    load_pem_public_key,
)


class KeyGenRSA(TypedDict):
    private_key: bytes
    public_key: bytes


def key_gen_RSA() -> KeyGenRSA:
    private_key = generate_private_key(65537, 2048)
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
    )
    public_bytes = public_key.public_bytes(
        Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
    )
    return {"private_key": private_bytes, "public_key": public_bytes}


def encrypt_with_public_key(key: bytes, message: bytes) -> bytes:
    public_key = load_pem_public_key(key)
    if isinstance(public_key, RSAPublicKey):
        return encrypt_message_with_rsa(public_key, message)
    raise Exception("Type of key is invalid")


def decrypt_with_private_key(key: bytes, message: bytes) -> bytes:
    private_key = load_pem_private_key(key, None)
    if isinstance(private_key, RSAPrivateKey):
        return decrypt_message_with_rsa(private_key, message)
    raise Exception("Type of key is invalid")


def encrypt_message_with_rsa(key: RSAPublicKey, message: bytes) -> bytes:
    return key.encrypt(message, OAEP(MGF1(SHA256()), SHA256(), None))


def decrypt_message_with_rsa(key: RSAPrivateKey, message: bytes) -> bytes:
    return key.decrypt(message, OAEP(MGF1(SHA256()), SHA256(), None))
