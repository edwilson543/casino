from data_loading_and_processing import get_wheel_defn_dict
from column_names import euro_wheel_defn_column_names

euro_wheel_defn = get_wheel_defn_dict(filename = 'euro_wheel_defn',
                                      number_column = euro_wheel_defn_column_names['NUMBER'],
                                      colour_column = euro_wheel_defn_column_names['COLOUR'])
