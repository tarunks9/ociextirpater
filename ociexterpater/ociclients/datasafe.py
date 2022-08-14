import logging
import importlib

import oci
from ociexterpater.OCIClient import OCIClient

class datasafe( OCIClient ):
    service_name = "Data Safe"
    clientClass = oci.data_safe.DataSafeClient

    objects = [
        {
            "function_list"    : "list_discovery_jobs",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree" : "True",
                                    "access_level"              : "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_discovery_job",
            "name_singular"    : "Data Safe Discovery Job",
            "name_plural"      : "Data Safe Discovery Jobs",
        },
        {
            "function_list"    : "list_user_assessments",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree" : "True",
                                    "access_level"              : "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_user_assessment",
            "name_singular"    : "Data Safe User Assessment",
            "name_plural"      : "Data Safe User Assessment",
        },
        {
            "function_list"    : "list_data_safe_private_endpoints",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_data_safe_private_endpoint",
            "name_singular"    : "Data Safe Private Endpoint",
            "name_plural"      : "Data Safe Private Endpoints"
        },
        # dicovery_job_results hangs off a discovery job
        # {
        #     "function_list"    : "list_discovery_job_results",
        #     "kwargs_list"      : {
        #                             "compartment_id_in_subtree": "True",
        #                             "access_level": "ACCESSIBLE"
        #                          },
        #     "function_delete"  : "delete_discovery_job_results",
        #     "name_singular"    : "Data Safe Discovery Jobs Result",
        #     "name_plural"      : "Data Safe Discovery Jobs Results"
        # },
        {
            "function_list"    : "list_discovery_jobs",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_discovery_job",
            "name_singular"    : "Data Safe Discovery Job",
            "name_plural"      : "Data Safe Discovery Jobs"
        },
        {
            "function_list"    : "list_library_masking_formats",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_library_masking_format",
            "name_singular"    : "Data Safe library masking format",
            "name_plural"      : "Data Safe library masking formats"
        },

        # this takes masking_policy_id
        # {
        #     "function_list"    : "XXX",
        #     "kwargs_list"      : {
        #                             "compartment_id_in_subtree": "True",
        #                             "access_level": "ACCESSIBLE"
        #                          },
        #     "function_delete"  : "delete_masking_column",
        #     "name_singular"    : "Data Safe masking column",
        #     "name_plural"      : "Data Safe masking columnmasking columns"
        # },

        {
            "function_list"    : "list_masking_policies",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_masking_policy",
            "name_singular"    : "Data Safe masking policy",
            "name_plural"      : "Data Safe masking policies"
        },

        {
            "function_list"    : "list_on_prem_connectors",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_on_prem_connector",
            "name_singular"    : "Data Safe on-premises connector",
            "name_plural"      : "Data Safe on-premises connectors"
        },
        {
            "function_list"    : "list_report_definitions",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE",
                                    # "is_seeded": False
                                 },
            "function_delete"  : "delete_report_definition",
            "name_singular"    : "Data Safe report definition",
            "name_plural"      : "Data Safe report definitions"
        },
        {
            "function_list"    : "list_security_assessments",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_security_assessment",
            "name_singular"    : "Data Safe saved security assessment or schedule",
            "name_plural"      : "Data Safe saved security assessments or schedules"
        },

        # delete_sensitive_column takes sensitive_data_model_id

        {
            "function_list"    : "list_sensitive_data_models",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_sensitive_data_model",
            "name_singular"    : "Data Safe sensitive data model",
            "name_plural"      : "Data Safe sensitive data model"
        },

        {
            "function_list"    : "list_sensitive_types",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_sensitive_type",
            "name_singular"    : "Data Safe sensitive type",
            "name_plural"      : "Data Safe sensitive type"
        },

        #
        {
            "function_list"    : "list_target_alert_policy_associations",
            "kwargs_list"      : {
                                    "compartment_id_in_subtree": "True",
                                    "access_level": "ACCESSIBLE"
                                 },
            "function_delete"  : "delete_target_alert_policy_association",
            "name_singular"    : "Data Safe target-alert policy association",
            "name_plural"      : "Data Safe target-alert policy associations"
        },

    ]

    def findAndDeleteAllInCompartment(self, compartment):
        for object in self.objects:
            logging.debug("Singular name: {}".format(object["name_singular"]))

            for o in self.objects:
                for region in self.clients:
                    # self.clients is a dict from region name to the actual client for that region.
                    logging.info( "Finding all {} in compartment {} in region {}".format( o["name_plural"], compartment, region))
                    kwargs = o["kwargs_list"]
                    os = oci.pagination.list_call_get_all_results(  getattr( (self.clients[region]), o["function_list"] ),
                                                                    compartment,
                                                                    **kwargs).data
                    # compartment_id_in_subtree = True, access_level = "ACCESSIBLE").data
                    logging.info( "Found {} {}".format( len( os ), o["name_plural"] ) )

                    f = getattr((self.clients[region]), o["function_delete"])

                    # we need to filter out any that are in state DELETED
                    for o2 in os:
                        logging.info( "{} with OCID {} / name '{}' is in state {}".format( o["name_singular"], o2.id, o2.display_name, o2.lifecycle_state ) )
                        if o2.lifecycle_state == "DELETED":
                            logging.debug( "skipping")
                        else:
                            logging.info("Deleting {}".format(o2.id))
                            try:
                                f( o2.id )

                            except Exception as e:
                                logging.error( "Failed to delete {} because {}".format(e))
                                logging.debug(e)
