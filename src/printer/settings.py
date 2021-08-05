import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

if '-p' in sys.argv:
    os.environ['STAGE'] = "PC_MODE"
    print('In PC deployment mode')
else:
    os.environ['STAGE'] = "RASPI_MODE"
    print('In Raspberry Pi deployment mode')