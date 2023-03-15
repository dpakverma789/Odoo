
def syntax(*args):
    data_type = {
        'c': 'Char',
        'i': 'Integer',
        'f': 'Float',
        'd': 'date',
        'dt': 'Datetime',
        'bi': 'Binary',
        's': 'Selection',
        'b': 'Boolean',
        'mo': 'Many2one',
        'om': 'One2many',
        'mm': 'Many2many'}
    var, py_container, xml_container = args
    var_name, var_type = var.split(".")
    line_string = ' '.join(var_name.split("_")).title()
    partial_string = f"{var_name} = fields.{data_type[var_type]}"
    line_format = {
        'mo': f"{partial_string}(comodel_name='', string='{line_string}')",
        'om': f"{partial_string}(comodel_name='',inverse_name='', string='{line_string}')",
        's': f"{partial_string}([('option_1','Option_1')], string='{line_string}')",
        'mm': f"{partial_string}(comodel_name='', 'TableName1_TableName2_rel',"
              f" 'table1_column_id', 'table2_column_id', string='{line_string}')"
    }
    py_line = line_format.setdefault(var_type, f"{partial_string}(string='{line_string}')")
    xml_line = f'<field name="{var_name}"/>'
    py_container.append(py_line)
    xml_container.append(xml_line)
    return py_container, xml_container


def odoo_fields_generator(variable_tuple=None):
    py_container = []
    xml_container = []
    if variable_tuple:
        for var in variable_tuple:
            py_container, xml_container = syntax(var, py_container, xml_container)
        print('\n\n#==== Odoo Python Syntax ====')
        [print(line) for line in py_container]
        print('\n\n#==== Odoo xml Syntax ====')
        [print(line) for line in xml_container]
        del py_container, xml_container
    else:
        print('\n\n==== No Variable List is Given ====')
    return


variable_list = (
    'name.c',
    'age.i',
    'salary.f',
    'dob.d',
    'doj.dt',
    'image.bi',
    'gender.s',
    'employee_id.b',
    'project_manager.mo',
    'assets.om',
    'hobbies.mm')

odoo_fields_generator(variable_list)
