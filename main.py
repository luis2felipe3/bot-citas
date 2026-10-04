import os
import sys

from bcncita import CustomerProfile, DocType, Office, OperationType, Province, try_cita

if __name__ == "__main__":
    customer = CustomerProfile(
        anticaptcha_api_key="... your key here ...",
        auto_captcha=False,
        auto_office=True,
        chrome_driver_path="/usr/bin/chromedriver",
        save_artifacts=True,
        province=Province.BARCELONA,
        operation_code=OperationType.TOMA_HUELLAS,
        doc_type=DocType.NIE,
        doc_value="Z4679820S",
        country="COLOMBIA",
        name="LUIS FELIPE BARRETO RAMIREZ",
        phone="613820715",
        email="luisfelipeb2305@hotmail.com",
        offices=[Office.BARCELONA, Office.MATARO],
    )

    if "--autofill" not in sys.argv:
        try_cita(context=customer, cycles=10)
    else:
        from mako.template import Template

        tpl = Template(
            filename=os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "bcncita/template/autofill.mako"
            )
        )
        print(tpl.render(ctx=customer))
