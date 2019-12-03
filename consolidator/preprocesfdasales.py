def preprocess_file(self, file_path, report_type, **kwargs):
        file_path_out = '%s.csv' % file_path.split('.')[0]
           get csv from xls file
        FileServices.xls_to_csv_transform_file(
            file_path_in=file_path,
            file_path_out=file_path_out,
            headers=True,
        )
        FileServices.remove_file(file_path=file_path)

        return super(FDAScraper, self).preprocess_file(file_path_out, report_type, **kwargs)


    def post_validation_process_file(self, file_path, report_type, **kwargs):
        df = pd.read_csv(file_path, encoding='utf-8')
        headers = df.columns.values.tolist()[:11]
        dates_dict = collections.OrderedDict()
        df.rename(columns={'MES ACTUAL': 'MES -0'}, inplace=True)
        date_column_value = df.iloc[:, -1][0]
        newest_date = datetime.strptime(date_column_value, '%Y/%m/%d').replace(day=1)
        for i in range(0, 4):
            dates_dict['MES -{}'.format(i)] = newest_date.replace(month=newest_date.month - i).strftime('%d-%m-%Y')     noqa

        df.rename(
            columns=dates_dict,
            inplace=True,
        )
        df2 = pd.melt(
            frame=df,
            id_vars=headers,
            value_vars=list(dates_dict.values()),
            var_name='FECHA',
            value_name='UNIDADES',
        )

        df2.to_csv(file_path, index=False, encoding='utf-8')

        return file_path