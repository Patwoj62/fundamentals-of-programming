# ===== Zadanie 8 =====

import converters  # import własnego modułu

print('### Test converters')  # nagłówek

print(f'Three meters is {converters.m_to_cm(3)}cm')  # test m_to_cm
print(f'250cm is {converters.cm_to_m(250)}m')  # test cm_to_m

print(f'10cm is {converters.cm_to_inches(10)} inches')  # test cm_to_inches

print(f'5ft 10in is {converters.feet_inches_to_cm(5,10)} cm')  # test feet_inches_to_cm