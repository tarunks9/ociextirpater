import logging

import oci
from ociexterpater.OCIClient import OCIClient

class bastion( OCIClient ):
    service_name = "Bastion service"
    clientClass = oci.bastion.BastionClient

    objects = [
        {
            "function_list"    : "list_bastions",
            "kwargs_list"      : {
                                 },
            "function_delete"  : "delete_bastion",
            "name_singular"    : "Bastion",
            "name_plural"      : "Bastions",
            "children"         : [
                                    {
                                        "function_list": "list_sessions",
                                        "kwargs_list": {
                                        },
                                        "function_delete": "delete_session",
                                        "name_singular": "Bastion Sessions",
                                        "name_plural": "",
                                    }
                                 ]
        }
    ]
