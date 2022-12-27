import time

import colour

rgb_wavelengeths = []
for r in range(256):
    st = time.time()
    for g in range(256):
        print(r*256 + g, "/", 65536)
        for b in range(256):
            dom_wl = colour.dominant_wavelength(colour.XYZ_to_xy(colour.sRGB_to_XYZ((r, g, b))), (0.3138, 0.3310))[0]
    print(time.time()-st)