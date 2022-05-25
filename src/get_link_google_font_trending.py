from src.models.text import TextModel
import xlsxwriter

import requests

headers = {
    'User-agent':
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}


class GetLinkGoogleFontTrending:

    @staticmethod
    def build_sheet_google_font(wb):
        sheet_1 = wb.add_worksheet('google font')
        cell_format = wb.add_format()
        cell_format.set_num_format('Times New Roman')

        sheet_1.set_row(0, 40)
        map_field_column = {
            'font_name': 0,
            'font_link': 1,
        }
        format_header = wb.add_format(
            {'bold': True, 'center_across': True, 'valign': 'vcenter', 'border': True})
        sheet_1.write(0, 0, 'Font family', format_header)
        sheet_1.write(0, 1, 'Link font', format_header)

        return sheet_1, map_field_column

    def get_link_google_font(self):
        path = '/home/truongcl/exam_flask/google_font_trending.txt'
        data = TextModel().read_file(path)
        items = data.get('items', {})
        count = 0
        base_URL = 'https://fonts.googleapis.com/css2'
        lst_family_args = list()
        lst_link = list()
        for item in items:
            if 'vietnamese' not in item.get('subsets'):
                continue
            family = item.get('family', '')
            family_args = '?family=' + family.replace(' ', '+')
            lst_family_args.append(base_URL + family_args)
            lst_variants_need = []
            is_italic = 0
            variants = item.get('variants', [])
            lst_italic = ['300italic', 'italic', '500italic', '700italic']
            font_display = '&display=swap'

            for x in lst_italic:
                if x in variants:
                    is_italic = 1

            if is_italic:
                if '300' in variants:
                    lst_variants_need.append('0,300')

                if 'regular' in variants:
                    lst_variants_need.append('0,400')

                if '500' in variants:
                    lst_variants_need.append('0,500')

                if '700' in variants:
                    lst_variants_need.append('0,700')

                if '300italic' in variants:
                    lst_variants_need.append('1,300')

                if 'italic' in variants:
                    lst_variants_need.append('1,400')

                if '500italic' in variants:
                    lst_variants_need.append('1,500')

                if '700italic' in variants:
                    lst_variants_need.append('1,700')
            else:
                if '300' in variants:
                    lst_variants_need.append('300')

                if 'regular' in variants:
                    lst_variants_need.append('400')

                if '500' in variants:
                    lst_variants_need.append('500')

                if '700' in variants:
                    lst_variants_need.append('700')

            if is_italic:
                weight_args = ':ital,wght@' + ";".join(lst_variants_need)
            else:
                weight_args = ':wght@' + ";".join(lst_variants_need)

            lst_link.append({
                'font_name': family,
                'font_link': base_URL + family_args + weight_args + font_display
            })

        # file_name = ''
        file_path = '/home/truongcl/exam_flask/google_font_trending.xlsx'
        wb = xlsxwriter.Workbook(file_path, {'constant_memory': True})
        format_row = wb.add_format({'border': True, 'align': 'center'})
        format_header = wb.add_format({'bold': True, 'center_across': True, 'valign': 'vcenter', 'border': True})

        row = 1
        sheet_1, map_field_column = self.build_sheet_google_font(wb)

        for data in lst_link:
            sheet_1.set_row(row, 20)
            for key, value in data.items():
                column = map_field_column.get(key)
                sheet_1.set_column(column, column, 40)
                sheet_1.write(row, column, value)
            row += 1
        wb.close()

        print(len(lst_link))
        # for URL in lst_link:
        #     content = requests.get(URL, headers=headers)
        #     if content.status_code == 200:
        #         count = count + 1
        #         print(count)
        #     else:
        #         print(URL)

        print('truongcl')


if __name__ == '__main__':
    GetLinkGoogleFontTrending().get_link_google_font()
