import os
import ariadne_nda


app = ariadne_nda.create_app(
    config_level=os.environ.get("NDA_CONFIG_LEVEL", 'default'),
)
