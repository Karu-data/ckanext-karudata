import ckan.plugins.toolkit as tk
import ckanext.karudata.logic.schema as schema


@tk.side_effect_free
def karudata_get_sum(context, data_dict):
    tk.check_access(
        "karudata_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.karudata_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'karudata_get_sum': karudata_get_sum,
    }
