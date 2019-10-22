BASE_URL = 'http://www3.laanonima.com.ar'
props = {
    'basic_auth': {
        'username': 'anonima',
        'password': 'patagonia',
    },
    'mstrweb_lnk_url': f'{BASE_URL}/cgi-bin/mstr.lnk',
    'mstrweb_url': f'{BASE_URL}/MicroStrategy/servlet/mstrWeb',
    'export_url': 'http://www3.laanonima.com.ar/MicroStrategy/export/{timestamp}',
    'export_1_document_id_sales': '5D2C687943A5EB1ACA5E59BBCF5B2812',
    'export_1_document_id_stock': '22C818B549859853973A9F81C7DDADC1',
    'export_2_report_id_sales': 'DB85A60A49D593803BA717991B7D3FEE',
    'export_2_report_id_stock': 'C8FE86524F114FE542C275958DD5F35B',
    'last_update': {
        'evt': '3069',
        'src': 'mstrWeb.3069',
        'executionMode': '4',
        'documentID': '',
        'messageID': '',
        'mstrWeb': '',
        'historyList': '*-1.*-1.0.0.0',
        'inbox': '<bean bt="ib"><ib hms="1" isa="0" isf="7" if="2"/></bean>',
        'iTb': '*-1.*-1.0.0.',
    },
    'last_update_download': {
        'evt': '3103',
        'src': 'mstrWeb',
        'executionMode': '4',
        'messageID': '',
        'mstrWeb': '',
        'rwFastExport': '*-1.*-1.0.0.0',
        'rwframe': '*-1.*-1.0.0',
        'rwb': '',
    },
    'client_auth_params': {
        'evt': '',
        'src': '',
        'documentViewMode': '',
        'documentID': '',
        'server': '',
        'project': '',
        'hiddenSections': '',
        'uid': '',
        'pwd': '',
        'valuePromptAnswers': '',
    },
    # SALES F7ED5A494EB6EBD94A929FBBEAE69296
    # STOCK 391B5EF94C03499CE22C2A96646961B8
    'export_1_data': {
        'evt': '2048001',
        'documentID': '',
        'visualizationMode': '0',
        'hiddensections': 'path',
        'promptAnswerMode': '2',
        'src': 'mstrWeb.2048001',
        'valuePromptAnswers': '{username}^{date}',
    },
    # STOCK C8FE86524F114FE542C275958DD5F35B
    # SALES DB85A60A49D593803BA717991B7D3FEE
    'export_2_data': {
        'evt': '3067',
        'src': 'mstrWeb.3067',
        'fastExport': 'true',
        'reportViewMode': '1',
        'reportID': '',
        'valuePromptAnswers': '{username}^{start_date}^{end_date}',
        'promptAnswerMode': '2',
        'hiddenSections': 'header,path',
    },
    'events_stock': (
        '-4098001*.mstrWeb***.fastExport***.rsfb***.rb***.rb***_ep***.pb***_FBDE0DDD4F544C573D9CBD'
        'A849D08C18@0@10***.4098001*.answerOptions***_1*.2*.answerFormat***_1*.1*.answer***_1*.C9D'
        '1B16111D595681000089D8D9BF44B~12~Sucursal55B36D1911D594E21000079D8D9BF44B~12~Articulo*.pr'
        'omptAnswerName***_1*.*.isDefaultPromptAnswer***_1*.0*.promptAnswerID***_1*.*.answerByID**'
        '*_1*.*.promptAnswerIsAutoClose***_1*.0*.promptAnswerAction***_1*.null.4098001*.mstrWeb***'
        '.fastExport***.rsfb***.rb***.rb***_ep***.pb***_CFE629C243DD3CE3C832749129524BB0@0@10***.4'
        '098001*.answerOptions***_4*.2*.answerFormat***_4*.1*.answer***_4*.643DC5CE11D5AA9B1000249'
        'D8D9BF44B:D24818***_01~1048576~D24818***_01:PERFUMERIA*.promptAnswerName***_4*.*.isDefaul'
        'tPromptAnswer***_4*.0*.promptAnswerID***_4*.*.answerByID***_4*.*.promptAnswerIsAutoClose*'
        '**_4*.0*.promptAnswerAction***_4*.null.8001*.mstrWeb***.fastExport***.rsfb***.rb***.rb***'
        '_ep***.8001*.useSetAnswers*.true_'
    ),
    'events_sales': (
        '-4098001*.mstrWeb***.fastExport***.rsfb***.rb***.rb***_ep***.pb***_9D4D997F4901275EFCE82F'
        '9D53ED0DFE@0@10***.4098001*.answerOptions***_1*.2*.answerFormat***_1*.1*.answer***_1*.C9D'
        '1B16111D595681000089D8D9BF44B~12~Sucursal55B36D1911D594E21000079D8D9BF44B~12~Articulo*.pr'
        'omptAnswerName***_1*.*.isDefaultPromptAnswer***_1*.0*.promptAnswerID***_1*.*.answerByID**'
        '*_1*.*.promptAnswerIsAutoClose***_1*.0*.promptAnswerAction***_1*.null.4098001*.mstrWeb***'
        '.fastExport***.rsfb***.rb***.rb***_ep***.pb***_88EFCCED4895FEF61E0F609CBD6CFD27@0@10***.4'
        '098001*.answerOptions***_2*.2*.answerFormat***_2*.1*.answer***_2*.C9D1B4FF11D595681000089'
        'D8D9BF44B~12~Dia*.promptAnswerName***_2*.*.isDefaultPromptAnswer***_2*.0*.promptAnswerID*'
        '**_2*.*.answerByID***_2*.*.promptAnswerIsAutoClose***_2*.0*.promptAnswerAction***_2*.null'
        '.4098001*.mstrWeb***.fastExport***.rsfb***.rb***.rb***_ep***.pb***_CFE629C243DD3CE3C83274'
        '9129524BB0@0@10***.4098001*.answerOptions***_5*.2*.answerFormat***_5*.1*.answer***_5*.*.p'
        'romptAnswerName***_5*.*.isDefaultPromptAnswer***_5*.0*.promptAnswerID***_5*.*.answerByID*'
        '**_5*.*.promptAnswerIsAutoClose***_5*.0*.promptAnswerAction***_5*.null.8001*.mstrWeb***.f'
        'astExport***.rsfb***.rb***.rb***_ep***.8001*.useSetAnswers*.true_'
    ),
    'export_3_data': {
        'promptLoaded': 'true',
        'innerWidth': '621',
        'innerHeight': '475',
        'events': '',
        'evt': '1024001',
        'src': 'mstrWeb.fastExport.1024001',
        '1024001': '1',
        'evtorder': '1024001',
        'hiddenSections': 'header,path',
        'mstrWeb': '-*-IHy6O6XC6Ew8CxL0Oap8y0hrCa8=.Prisma.*-12hAAxtAWRvK4qgQ_',
        'fastExport': '*-1.*-1.0.0.0',
        'rsfb': '*-1.*-1.0.0',
        'r': '',
        'directExport': '*-1.*-1.0.0.1.1',
    },
    'export_4_data': {
        'hiddenSections': 'header,path',
        'evt': '3068',
        'src': 'mstrWeb.3068',
        'mstrWeb': '-*-gxRPiBitj2dBrL1dlSvGwws7ekM=.Prisma.*-RtvkabkmjIoIrwSm_',
        'fastExport': '*-1.*-1.0.0.0',
        'rsfb': '*-1.*-1.0.0',
        'r': '',
        'directExport': '*-1.*-1.0.0.1.1',
    },
    'export_5_data': [
        ('3131', 'Exportar'),
        ('exportSection', '1'),
        ('exportFormatGrids', 'csvIServer'),
        ('exportPlaintextDelimiter', '3'),  # 1 comma, 2 tabs, 3 semi colon
        ('exportReportTitle', '0'),
        ('exportFilterDetails', '0'),
        ('exportOverlapGridTitles', '1'),
        ('hiddenSections', 'header,path'),
        ('hiddenSections', 'header,path'),
        ('hiddenSections', 'header,path'),
        ('evt', '25002'),
        ('evt', '3131'),
        ('evt', '25003'),
        ('src', 'mstrWeb.exportOptionsFromReport.options.25002'),
        ('src', 'mstrWeb.3131'),
        ('src', 'mstrWeb.exportOptionsFromReport.options.25003'),
        ('target', 'excelHeaderFooter'),
        ('prevGroupName', 'export'),
        ('keepPreferences', '0'),
        ('exportMetricValuesAsText', '0'),
        ('exportHeadersAsText', '0'),
        ('excelEmbedImages', '0'),
        ('eventToForwardTo', '3012'),
        ('actionType', '3'),
        ('level', 'user_project'),
        ('mstrWeb', '-*-SwupKvGu3KhhmEcFotgAfFJmloY=.Prisma.*-cFDwmN5MTcY3Wh94_'),  # item no 25
        ('exportOptionsFromReport', '*-1.*-1.0.0.0'),
        ('options', '*-1.*-1.0.0.user.export...1..0.*0.*0.*0.*0.*0.*0.0.0.0.'),
        ('directExport', '*-1.*-1.0.0.1.1'),
        ('r', ''),  # item no 29
    ],
    'download_data': [
        ('hiddenSections', 'header,path'),
        ('evt', '3012'),
        ('src', 'mstrWeb.3012'),
        ('exportOverlapGridTitles', '1'),
        ('exportHeadersAsText', '0'),
        ('exportMetricValuesAsText', '0'),
        ('exportPlaintextDelimiter', '3'),  # 1 comma, 2 tabs, 3 semi colon
        ('exportFilterDetails', '0'),
        ('exportSection', '1'),
        ('exportFormatGrids', 'csvIServer'),
        ('mstrWeb', ''),  # item no 10
        ('SaveReportProperties', '*-1.*-1.0.0.0'),
        ('r', ''),  # item no 12
    ],
    'stock_download_timeout': 5000,
    'request_page_timeout': 300,
}
