import xml.etree.ElementTree as ET
import csv

file_path = 'C:\\Users\\GAR\\Downloads\\FX_MAS_NEWT_OTHR.xml'
tree = ET.parse(file_path)
root = tree.getroot()

ns = {
    'ns1': 'urn:iso:std:iso:20022:tech:xsd:head.003.001.01',
    'ns2': 'urn:iso:std:iso:20022:tech:xsd:auth.030.001.03'
}

csv_output = 'C:\\Users\\GAR\\Downloads\\CSV_Output.csv'

headers = [
    'RptgCtrPty_LEI', 'TradgCpcty', 'CtrPtySd', 'TradrLctn', 'BookgLctn', 
    'OthrCtrPty_LEI', 'SubmitgAgt_LEI', 'ClrMmb_LEI', 'RptgTmStmp', 'CtrctTp', 
    'AsstClss', 'UnqPdctIdr', 'ISIN', 'SttlmCcy', 'SttlmCcyScndLeg', 'UnqTxIdr', 
    'MrgnPrtflCd', 'PltfmIdr', 'Amt_SGD', 'Amt_AUD', 'DlvryTp', 'ExctnTmStmp', 
    'FctvDt', 'XprtnDt', 'SttlmDt', 'DerivEvt_Tp', 'DerivEvt_TmStmp', 'TradConf_Tp', 
    'TradConf_TmStmp', 'CCP_LEI', 'ClrDtTm', 'XchgRate', 'BaseCcy', 'QtdCcy', 
    'PmtAmt_HKD', 'PmtTp', 'PmtPyer_LEI', 'PmtRcvr_LEI', 'Packg_CmplxTradId', 'TechRcrdId'
]

with open(csv_output, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    for rpt in root.findall('.//ns2:Rpt', ns):
        row = {
            'RptgCtrPty_LEI': rpt.findtext('.//ns2:RptgCtrPty/ns2:Id/ns2:Lgl/ns2:Id/ns2:LEI', '', ns),
            'TradgCpcty': rpt.findtext('.//ns2:RptgCtrPty/ns2:TradgCpcty', '', ns),
            'CtrPtySd': rpt.findtext('.//ns2:DrctnOrSd/ns2:CtrPtySd', '', ns),
            'TradrLctn': rpt.findtext('.//ns2:RptgCtrPty/ns2:TradrLctn', '', ns),
            'BookgLctn': rpt.findtext('.//ns2:RptgCtrPty/ns2:BookgLctn', '', ns),
            'OthrCtrPty_LEI': rpt.findtext('.//ns2:OthrCtrPty/ns2:IdTp/ns2:Lgl/ns2:Id/ns2:LEI', '', ns),
            'SubmitgAgt_LEI': rpt.findtext('.//ns2:SubmitgAgt/ns2:LEI', '', ns),
            'ClrMmb_LEI': rpt.findtext('.//ns2:ClrMmb/ns2:Lgl/ns2:Id/ns2:LEI', '', ns),
            'RptgTmStmp': rpt.findtext('.//ns2:RptgTmStmp', '', ns),
            'CtrctTp': rpt.findtext('.//ns2:CtrctData/ns2:CtrctTp', '', ns),
            'AsstClss': rpt.findtext('.//ns2:CtrctData/ns2:AsstClss', '', ns),
            'UnqPdctIdr': rpt.findtext('.//ns2:PdctId/ns2:UnqPdctIdr/ns2:Id', '', ns),
            'ISIN': rpt.findtext('.//ns2:UndrlygInstrm/ns2:Bskt/ns2:Cnsttnts/ns2:InstrmId/ns2:ISIN', '', ns),
            'SttlmCcy': rpt.findtext('.//ns2:CtrctData/ns2:SttlmCcy/ns2:Ccy', '', ns),
            'SttlmCcyScndLeg': rpt.findtext('.//ns2:CtrctData/ns2:SttlmCcyScndLeg/ns2:Ccy', '', ns),
            'UnqTxIdr': rpt.findtext('.//ns2:TxId/ns2:UnqTxIdr', '', ns),
            'MrgnPrtflCd': rpt.findtext('.//ns2:MrgnPrtflCd/ns2:InitlMrgnPrtflCd/ns2:Prtfl/ns2:Cd', '', ns),
            'PltfmIdr': rpt.findtext('.//ns2:PltfmIdr', '', ns),
            'Amt_SGD': rpt.findtext('.//ns2:NtnlAmt/ns2:FrstLeg/ns2:Amt/ns2:Amt[@Ccy="SGD"]', '', ns),
            'Amt_AUD': rpt.findtext('.//ns2:NtnlAmt/ns2:ScndLeg/ns2:Amt/ns2:Amt[@Ccy="AUD"]', '', ns),
            'DlvryTp': rpt.findtext('.//ns2:DlvryTp', '', ns),
            'ExctnTmStmp': rpt.findtext('.//ns2:ExctnTmStmp', '', ns),
            'FctvDt': rpt.findtext('.//ns2:FctvDt', '', ns),
            'XprtnDt': rpt.findtext('.//ns2:XprtnDt', '', ns),
            'SttlmDt': rpt.findtext('.//ns2:SttlmDt', '', ns),
            'DerivEvt_Tp': rpt.findtext('.//ns2:DerivEvt/ns2:Tp', '', ns),
            'DerivEvt_TmStmp': rpt.findtext('.//ns2:DerivEvt/ns2:TmStmp/ns2:DtTm', '', ns),
            'TradConf_Tp': rpt.findtext('.//ns2:TradConf/ns2:Confd/ns2:Tp', '', ns),
            'TradConf_TmStmp': rpt.findtext('.//ns2:TradConf/ns2:Confd/ns2:TmStmp', '', ns),
            'CCP_LEI': rpt.findtext('.//ns2:CCP/ns2:LEI', '', ns),
            'ClrDtTm': rpt.findtext('.//ns2:ClrDtTm', '', ns),
            'XchgRate': rpt.findtext('.//ns2:XchgRate', '', ns),
            'BaseCcy': rpt.findtext('.//ns2:CcyPair/ns2:BaseCcy', '', ns),
            'QtdCcy': rpt.findtext('.//ns2:CcyPair/ns2:QtdCcy', '', ns),
            'PmtAmt_HKD': rpt.findtext('.//ns2:PmtAmt/ns2:Amt[@Ccy="HKD"]', '', ns),
            'PmtTp': rpt.findtext('.//ns2:PmtTp/ns2:Tp', '', ns),
            'PmtPyer_LEI': rpt.findtext('.//ns2:PmtPyer/ns2:Lgl/ns2:LEI', '', ns),
            'PmtRcvr_LEI': rpt.findtext('.//ns2:PmtRcvr/ns2:Lgl/ns2:LEI', '', ns),
            'Packg_CmplxTradId': rpt.findtext('.//ns2:Packg/ns2:CmplxTradId', '', ns),
            'TechRcrdId': rpt.findtext('.//ns2:TechAttrbts/ns2:TechRcrdId', '', ns)
        }
        writer.writerow(row)

