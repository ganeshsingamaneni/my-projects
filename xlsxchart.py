# chart.py
import xlsxwriter
# data
data = [
     	 {"month": "jan", "dolphins":150, "whales":80},
        {"month": "feb", "dolphins":77, "whales":54}, 
        {"month": "mar", "dolphins":32, "whales":100},
        {"month": "apr", "dolphins":11, "whales":76},
        {"month": "may", "dolphins":6, "whales":93},
        {"month": "jun", "dolphins":1, "whales":72}
       ]

def create_chart(data_in):
    """
    creates excel file with data and charts
    """
    # creation of workbook with name 'chart.xlsx'
    workbook = xlsxwriter.Workbook('chart.xlsx')
    # creation of worksheet for 'data'
    worksheet = workbook.add_worksheet('data')
    # creation of seperate worksheet for 'chart'
    worksheet1 = workbook.add_worksheet('chart')
    bold = workbook.add_format({'bold': 1})

    # Add the worksheet data that the charts will refer to.
    headings = ['months', 'dolphins', 'whales']
    data =  [
              [doc["month"] for doc in data_in],
              [doc["dolphins"] for doc in data_in],
              [doc["whales"] for doc in data_in]
            ]
    # writing rows or columns from starting from specific cell
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    # specify type of chart (bar,column,pie,line,etc..)
    chart1 = workbook.add_chart({'type': 'column'})

    # Configure the first series.
    chart1.add_series({
                        'name'      : '=data!$B$1',
                        'categories': '=data!$A$2:$A$7',
                        'values'    : '=data!$B$2:$B$7',
                     })

    # adding extra series
    chart1.add_series({  'name'      : '=data!$C$1',
                         'values'    : '=data!$C$2:$C$7'
                      })

    # Add a chart title and some axis labels.
    chart1.set_title ({'name': 'Dolphins & Whales'})

    chart1.set_x_axis({'name': 'Months','name_font': \
                        {'size': 14, 'bold': True}})

    chart1.set_y_axis({'name': 'no of animals born','name_font': \
                        {'size': 14, 'bold': True}})

    # Set an Excel chart style.
    chart1.set_style(11)

    # Insert the chart into the worksheet (with an offset).
    worksheet1.insert_chart('B2', chart1, {'x_offset': 25, \
                        'y_offset': 10,'x_scale': 2, 'y_scale': 3})
    workbook.close()

create_chart(data)