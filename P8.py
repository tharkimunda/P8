# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))