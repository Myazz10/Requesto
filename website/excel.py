import xlsxwriter


def create_excel_metadata(data):
    username = data['USERNAME']

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(f'{username}_metadata.xlsx')
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 50)
    worksheet.set_column('B:B', 150)

    # Iterate over the data and write it out row by row.
    for variable, value in data.items():
        try:
            worksheet.write_string(row, col, variable)
        except:
            pass

        try:
            worksheet.write(row, col + 1, value)
        except:
            worksheet.write(row, col + 1, None)

        row += 1

    workbook.close()


def create_excel_city_data(response, username):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(f'{username}_city_data.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 50)
    worksheet.set_column('B:B', 150)

    worksheet.write('A1', 'Country Name')
    try:
        worksheet.write_string('B1', str(response.country.name))
    except:
        worksheet.write('B1', None)

    worksheet.write('A2', 'Country ISC Code')
    try:
        worksheet.write_string('B2', str(response.country.iso_code))
    except:
        worksheet.write('B2', None)

    worksheet.write('A3', 'State/Province/Parish')
    try:
        worksheet.write_string('B3', str(response.subdivisions.most_specific.name))
    except:
        worksheet.write('B3', None)

    worksheet.write('A4', 'State/Province/Parish Code')
    try:
        worksheet.write_string('B4', str(response.subdivisions.most_specific.iso_code))
    except:
        worksheet.write('B4', None)

    worksheet.write('A5', 'City Name')
    try:
        worksheet.write_string('B5', str(response.city.name))
    except:
        worksheet.write('B5', None)

    worksheet.write('A6', 'Postal Code')
    try:
        worksheet.write_string('B6', str(response.postal.code))
    except:
        worksheet.write('B6', None)

    worksheet.write('A7', 'Location: Latitude')
    try:
        worksheet.write_string('B7', str(response.location.latitude))
    except:
        worksheet.write('B7', None)

    worksheet.write('A8', 'Location: Longitude')
    try:
        worksheet.write_string('B8', str(response.location.longitude))
    except:
        worksheet.write('B8', None)

    worksheet.write('A9', 'IPv4Network')
    try:
        worksheet.write_string('B9', str(response.traits.network))
    except:
        worksheet.write('B9', None)

    workbook.close()


def create_excel_anonymous_ip_data():
    pass


def create_excel_asn_data():
    pass


def create_excel_connection_type_data():
    pass


def create_excel_domain_data():
    pass


def create_excel_enterprise_data():
    pass


def create_excel_isp_data():
    pass
