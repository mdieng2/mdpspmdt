#!/usr/bin/env python
# -*- coding:Utf-8 -*-

"""
Management of all the package components.

This module defined the components dictionary list within these informations:
    - Component's number
    - Component's trigram or short name
    - Component's full name
    - Component's type (System, Manager, Application, Certificats SSL)

It also defines an default unknown component for those present in the package but not match with the general repertory.

Funtions test a received component and tells whether it is known or not. If yes, they return additional informations
about the said component (within the version).

"""

__author__ = "Moussa DIENG"
__copyright__ = "Copyright 2018, Ingenico FR"
__credits__ = ["Moussa DIENG (Ingenico Partner)"]
__license__ = "Ingenico Internal Licence"
__version__ = "1.0.2"
__maintainer__ = "Moussa DIENG"
__email__ = "moussa.dieng@ingenico.com"
__status__ = "Development"

ndiff_catalog_name = "Comparison"
"""Components reference dictionary list"""
system_pack = ["3777", "999000000003"]
manager_pack = "844778"
t3_sdk_pack = ["99920470", "99921470"]
application_components = [
    ('829341', 'ACE', 'ACCORD EMV', 'APP'),
    ('829339', 'ACP', 'ACCORD PISTE', 'APP'),
    ('ADB8FRA', 'ADB8FRA', 'FICHIER MESSAGE PARAMS FRA', 'PAR'),
    ('829322', 'ADM', 'ADM', 'APP'),
    ('829320', 'ADS', 'ADS APPLI', 'APP'),
    ('929320', 'ADS', 'ADS APPLI T2+', 'APP'),
    ('829321', 'DLL', 'ADS DLL', 'APP'),
    ('929321', 'DLL', 'ADS DLL T2+', 'APP'),
    ('829328', 'ELL', 'ADS ENCRYPT DLL', 'APP'),
    ('829415', 'AES', 'ADS CRYPT', 'APP'),
    ('829348', 'APH', 'ALPHYRA', 'APP'),
    ('829389', 'AMEMPA', 'AMEX EMV MPA', 'APP'),
    ('829358', 'AMX', 'AMEX Piste', 'APP'),
    ('829334', 'AME', 'AMEX EMV', 'APP'),
    ('829402', 'AMS', 'AMEX EXPRESSPAY', 'APP'),
    ('829512', 'Acry', 'APPLE CRYPT', 'DLL'),
    ('829513', 'AInj', 'APPLE INJECT', 'DLL'),
    ('829342', 'VAD', 'BANCAIRE VAD', 'APP'),
    ('829411', 'BAS', 'BASE ASSOCIATION', 'DLL'),
    ('829393', 'BTP', 'BT PAIRING', 'APP'),
    ('829395', 'C3D', 'C3DRIVER DLL', 'APP'),
    ('829350', 'CED', 'CARTE ED', 'APP'),
    ('829345', 'CAF', 'CASINO', 'APP'),
    ('829377', 'CTD', 'CB ENSEIGNE-CTD', 'APP'),
    ('829337', 'CTM', 'CETELEM', 'APP'),
    ('829336', 'CHQ', 'CHEQUE', 'APP'),
    ('829417', 'CMC', 'CMCIC SCHEME', 'APP'),
    ('829338', 'COF', 'COFINOGA', 'APP'),
    ('829346', 'CFE', 'COFINOGA EMV', 'APP'),
    ('829368', 'CAT', 'COMARCH', 'APP'),
    ('829398', 'CNS', 'CONECS', 'APP'),
    ('829399', 'CNX', 'CONECS CLESS', 'APP'),
    ('823040', 'courB10', '-', 'XXX'),
    ('823044', 'courB14', '-', 'XXX'),
    ('823048', 'courB18', '-', 'XXX'),
    ('823042', 'courBO10', '-', 'XXX'),
    ('823046', 'courBO14', '-', 'XXX'),
    ('823050', 'courBO18', '-', 'XXX'),
    ('823041', 'courO10', '-', 'XXX'),
    ('823045', 'courO14', '-', 'XXX'),
    ('823049', 'courO18', '-', 'XXX'),
    ('823038', 'courR08', '-', 'XXX'),
    ('823039', 'courR10', '-', 'XXX'),
    ('823043', 'courR14', '-', 'XXX'),
    ('823047', 'courR18', '-', 'XXX'),
    ('829367', 'PSA', 'CREDIPAR', 'APP'),
    ('829372', 'PSF', 'PSA FIDELITE', 'APP'),
    ('829405', 'CPA', 'SEPA', 'APP'),
    ('851220', 'CPAFAST', 'SEPA SEPA-FAST', 'APP'),
    ('85122A', 'IHMDLL', 'SEPA IHM DLL', 'APP'),
    ('851230', 'IHMDLL', 'SEPA IHM DLL', 'APP'),
    ('85122E', 'CPAENG', 'SEPA EMV ENGINE', 'APP'),
    ('851234', 'CPAENG', 'SEPA EMV ENGINE', 'APP'),
    ('851227', 'UTILs_DLL', 'SEPA UTIL DLL', 'APP'),
    ('829344', 'CUP', 'CUP', 'APP'),
    ('829382', 'CUN', 'CUP NATIXIS', 'APP'),
    ('829409', 'CUI', 'CUP ICBC', 'APP'),
    ('829347', 'FCC', 'DCC FCC', 'APP'),
    ('829408', 'PCC', 'DCC PCC', 'APP'),
    ('829413', 'DFF', 'DEF FLASH', 'APP'),
    ('829412', 'DLF', 'DEL FILE', 'APP'),
    ('829331', 'DCF', 'DINERS', 'APP'),
    ('829394', 'DSY', 'DISNEY FID', 'APP'),
    ('840002', 'DLLFR', 'DLL France', 'APP'),
    ('853040', 'EID', 'EID', 'APP'),
    ('829363', 'ELF', 'ELF TOTAL', 'APP'),
    ('3065', 'EMVDC', 'EMV DC', 'APP'),
    ('3421', 'EMVENG', 'EMV ENG', 'APP'),
    ('844567', 'EMVCS', 'EMVCo checksum', 'APP'),
    ('829330', 'EMV', 'CB EMV MPE', 'APP'),
    ('829357', 'SSC', 'CB EMV MPE CLESS', 'APP'),
    ('829383', 'CCB', 'CB EMV BIS-CCB', 'APP'),
    ('829374', 'CEV', 'EVEREST', 'APP'),
    ('829359', 'FXO', 'DCC FEXCO', 'APP'),
    ('829332', 'FNF', 'FINAREF', 'APP'),
    ('829371', 'FTX', 'FINTRAX', 'APP'),
    ('829400', 'FIV', 'FIVORY', 'APP'),
    ('829387', 'FNP', 'FLASH AND PAY', 'APP'),
    ('829349', 'FNC', 'FNAC', 'APP'),
    ('829352', 'FFI', 'FRANFINANCE', 'APP'),
    ('829375', 'GLF', 'GALERIES LAFAYETTE', 'APP'),
    ('844053', 'GWD', 'GATEWAY DLL', 'APP'),
    ('829360', 'GAV', 'GAV', 'APP'),
    ('829355', 'GEN', 'GENERIQUE', 'APP'),
    ('829365', 'GAX', 'GENERIQUE AX', 'APP'),
    ('829343', 'DTV', 'GIFTCARD-DTV', 'APP'),
    ('840021', 'GPRS3G', 'ING GPRS 3G', 'SYS'),
    ('853042', 'H24', 'H24', 'APP'),
    ('851221', 'HAP', '-', 'APP'),
    ('823014', 'helvB10', '-', 'XXX'),
    ('823018', 'helvB14', '-', 'XXX'),
    ('823022', 'helvB18', '-', 'XXX'),
    ('823016', 'helvBO10', '-', 'XXX'),
    ('823020', 'helvBO14', '-', 'XXX'),
    ('823024', 'helvBO18', '-', 'XXX'),
    ('823015', 'helvO10', '-', 'XXX'),
    ('823019', 'helvO14', '-', 'XXX'),
    ('823023', 'helvO18', '-', 'XXX'),
    ('823012', 'helvR08', '-', 'XXX'),
    ('823013', 'helvR10', '-', 'XXX'),
    ('823017', 'helvR14', '-', 'XXX'),
    ('823021', 'helvR18', '-', 'XXX'),
    ('829416', 'IAB', 'Procedure de detaxe en France', 'APP'),
    ('823000', 'ibr-t2', '-', 'XXX'),
    ('823010', 'IE1', '-', 'XXX'),
    ('823011', 'IE2', '-', 'XXX'),
    ('823004', 'inc_NFCp', '-', 'XXX'),
    ('829379', 'IPS', 'IPS', 'APP'),
    ('829340', 'JCE', 'JCB EMV', 'APP'),
    ('853043', 'LOY', 'LOYALTY', 'APP'),
    ('853044', 'MVO', 'SODEXO MEAL VOUCHER', 'APP'),
    ('829370', 'MPASSC', 'EMV MPA CLESS', 'APP'),
    ('829351', 'MPA', 'EMV MPA', 'APP'),
    ('829385', 'MPACCB', 'EMV MPA BIS-CCB', 'APP'),
    ('829361', 'MPAA1', 'CB EMV MPA Autoroute 1', 'APP'),
    ('829362', 'MPAA2', 'CB EMV MPA Autoroute 2', 'APP'),
    ('829390', 'MPAA3', 'CB EMV MPA Autoroute 3', 'APP'),
    ('829397', 'MPAA4', 'CB EMV MPA Autoroute 4', 'APP'),
    ('829388', 'MPAP', 'MPAP', 'APP'),
    ('829325', 'ADSmsg', 'MESSAGES ADS', 'APP'),
    ('829326', 'APPmsg', 'MESSAGES APPLI', 'APP'),
    ('822882', 'MGRmsg', 'MESSAGES MANAGER', 'APP'),
    ('829366', 'MTSV2', 'MULTISSIME', 'APP'),
    ('829356', 'NAV', 'NAVIGO', 'APP'),
    ('829369', 'NSE', 'NS EMV', 'APP'),
    ('829392', 'NXS', 'MULTI SCHEMES', 'APP'),
    ('829386', 'OLA', 'OLA', 'APP'),
    ('844081', 'PEEE', '-', 'APP'),
    ('829407', 'PAS', 'PASS EMV', 'APP'),
    ('844051', 'PPA', 'PINPAD AGENT', 'APP'),
    ('829353', 'PLBS', 'EMV PLBS', 'APP'),
    ('829414', 'PME', 'PME CARREFOUR', 'APP'),
    ('829396', 'PSC', 'PMU', 'APP'),
    ('829376', 'CDM', 'PNF CM', 'APP'),
    ('829373', 'PMS', 'PROMOSTIM', 'APP'),
    ('829333', 'PSD', 'PROSODIE', 'APP'),
    ('844103', 'pl100EMV', '-', 'APP'),
    ('853046', 'QTC', 'QTC', 'APP'),
    ('829364', 'CTF', 'REFLEXE', 'APP'),
    ('829410', 'RPI', 'RPI', 'APP'),
    ('851226', 'SCAP', 'SEPA SCAP', 'APP'),
    ('829406', 'SDM', 'SDM', 'APP'),
    ('823001', 'sec-ad', '-', 'APP'),
    ('40013', 'SNCF_ADS', 'SNCF ADS', 'APP'),
    ('40034', 'SNCF_ADS_BLS', 'SNCF ADS-BLS', 'APP'),
    ('40011', 'SNCF_BIL', 'SNCF BILLETIQUE', 'APP'),
    ('829354', 'SC4', 'SOFINCO', 'APP'),
    ('829418', 'CSU', 'CARTE SYSTEME U', 'APP'),
    ('823027', 'timB10', 'timB10', 'XXX'),
    ('823031', 'timB14', '-', 'XXX'),
    ('823035', 'timB18', '-', 'XXX'),
    ('823029', 'timBI10', '-', 'XXX'),
    ('823033', 'timBI14', '-', 'XXX'),
    ('823037', 'timBI18', '-', 'XXX'),
    ('823028', 'timI10', '-', 'XXX'),
    ('823032', 'timI14', '-', 'XXX'),
    ('823036', 'timI18', '-', 'XXX'),
    ('823025', 'timR08', '-', 'XXX'),
    ('823026', 'timR10', '-', 'XXX'),
    ('823030', 'timR14', '-', 'XXX'),
    ('823034', 'timR18', '-', 'XXX'),
    ('851225', 'TMAP', 'SEPA TMAP', 'APP'),
    ('844370', 'TMS', 'TMS CALL', 'APP'),
    ('829403', 'VAS', 'PME CARREFOUR', 'APP'),
    ('999999', 'VIDE', '-', 'APP'),
    ('829381', 'VBK', 'VISITORS BOOK', 'APP'),
    ('829405', 'CPA', 'SEPA FAST', 'APP'),
    ('829406', 'SDM', 'SODELEM', 'APP'),
    ('829407', 'PAS', 'PASS LIB', 'APP'),
    ('829323', '', 'LibALogDll', 'DLL'),
    ('829419', 'ADS', 'ADS AMOUNT TETRA', 'APP'),
    ('853040', 'EID', 'EID BELGIUM', 'APP'),
    ('853041', '', 'DETOKENIZAT (iLABS)', 'APP'),
    ('853045', 'AGC', 'DETOKENIZAT (iLABS)', 'APP'),
    ('829378', 'EMV-INT', 'EMV-INT (Va disparaitre)', 'APP'),
    ('829384', 'SCB', 'SSC BIS (Va disparaitre)', 'APP'),
    ('829380', '', 'ITPOSFUEL', 'APP'),
    ('829335', '', 'PRIVATIF', 'APP'),
    ('829391', '', 'SYNC CARD', 'APP'),
    ('829401', '', 'BUNDLE-P2PE', 'APP'),
    ('829404', '', 'CROSS CHANNEL', 'APP'),
    #('830063', '-', 'BOOSTER III Boot Flash', 'SYS'),
    #('830064', '-', 'Booster III system', 'SYS'),
    #('3014', '-', 'Boot Ram', 'SYS'),
    #('820125', '-', 'Driver BC06 Portable', 'SYS'),
    #('820049', '-', 'Driver C30', 'SYS'),
    #('820012', '-', 'Driver GPRS 930', 'SYS'),
    #('820052', '-', 'Driver PRINTER EXTERNE', 'SYS'),
    #('820021', '-', 'Driver UMS', 'SYS'),
    #('820032', '-', 'Driver USB CDC', 'SYS'),
    #('3021', '-', 'Driver VFS', 'SYS'),
    #('820103', '-', 'LEDS', 'SYS'),
    #('3777', '-', 'Pack Systeme', 'SYS'),
    #('820036', '-', 'Systeme R+', 'SYS'),
    #('820134', '-', '-', 'SYS'),
    #('844920', '-', '-', 'SYS'),
    #('', '-', '-', 'MAN'),
]
system_components = [
    ('3014', 'Boot Ram', 'SYS'),
    ('3018', 'Driver synch GPM271 Thunder I & II', 'SYS'),
    ('3019', 'Driver synch S10 Thunder I & II', 'SYS'),
    ('3020', 'Driver synch S9 Thunder I & II', 'SYS'),
    ('3021', 'Driver VFS', 'SYS'),
    ('3777', 'PACK SYSTEM', 'SYS'),
    ('4015', 'Driver Modem 930', 'SYS'),
    ('813014', 'Boot Ram no self refresh', 'SYS'),
    ('813308', 'LDBG Remote Debugger', 'SYS'),
    ('820012', 'Driver GPRS 930', 'SYS'),
    ('820021', 'Driver UMS', 'SYS'),
    ('820022', 'Driver HID', 'SYS'),
    ('820031', 'Driver synch GPM896 Thunder I & II', 'SYS'),
    ('820032', 'Driver USB CDC', 'SYS'),
    ('820034', 'Driver synch GFM Thunder I & II', 'SYS'),
    ('820035', 'Driver synch SLE4436 Thunder I & II', 'SYS'),
    ('820036', 'System R+', 'SYS'),
    ('820049', 'Driver CLESS', 'SYS'),
    ('820052', 'Driver external printer', 'SYS'),
    ('820057 8', 'System P30 Mockup', 'SYS'),
    ('820057', 'System P30', 'SYS'),
    ('820091 8', 'Driver PP30S Mockup', 'SYS'),
    ('820091', 'Driver PP30S', 'SYS'),
    ('820093', 'Driver synch SLE4404 Thunder I & II', 'SYS'),
    ('820094', 'Driver synch AT88SC1003 Thunder I & II', 'SYS'),
    ('820103', 'generic driver leds', 'SYS'),
    ('820125(04)', 'Driver BT BC06 handheld Thunder II', 'SYS'),
    ('820126(04)', 'Driver BT BC06 base Thunder II', 'SYS'),
    ('820130', 'Driver Printer SPM', 'SYS'),
    ('820134', 'Driver iST', 'SYS'),
    ('820135', 'LLT Image Config', 'SYS'),
    ('820136', 'iWL220-250-MCV2 base list', 'SYS'),
    ('820137', 'iWL280-350 base archive', 'SYS'),
    ('820141', 'Driver BT BC06 handheld Thunder III', 'SYS'),
    ('820144', 'Driver synch AT88SC102 Thunder I & II', 'SYS'),
    ('820145', 'Driver synch AT88SC102 Thunder III', 'SYS'),
    ('820148', 'Driver synch AT88SC1608 Thunder I & II', 'SYS'),
    ('820149', 'Driver synch AT88SC1608 Thunder III', 'SYS'),
    ('820150', 'Driver external printer Thunder III', 'SYS'),
    ('820151', 'Touch screen firmware iSC480', 'SYS'),
    ('820153', 'BoosterIII display Fpga iSC480', 'SYS'),
    ('820162', 'Driver WIFI TI', 'SYS'),
    ('820163', 'System R+ NET2', 'SYS'),
    ('820164', 'System Thunder Thunder III NET2', 'SYS'),
    ('820165', 'iWL280-350 NET2 base archive', 'SYS'),
    ('820166', 'iWL220-250 base list NET2', 'SYS'),
    ('820185', 'Driver Audio', 'SYS'),
    ('820304', 'Driver CAM Thunder II', 'SYS'),
    ('820312', 'Driver color', 'SYS'),
    ('820368', 'Driver SSC_DAA', 'SYS'),
    ('820369', 'Driver Modem V34', 'SYS'),
    ('820370 8', 'System IPP2XX Mockup Thunder II', 'SYS'),
    ('820370', 'System IPP2XX Thunder II', 'SYS'),
    ('820372', 'Driver iSMP', 'SYS'),
    ('820378', 'Booster III system X07 (iUC160B)', 'SYS'),
    ('820500', 'Boot Ram Thunder III', 'SYS'),
    ('820501', 'System Thunder Thunder III', 'SYS'),
    ('820508', 'BoosterIII display Fpga iSC350', 'SYS'),
    ('820510', 'Driver VFS Thunder III', 'SYS'),
    ('820511', 'Driver CLESS Thunder III', 'SYS'),
    ('820512', 'LDBG Remote Debugger Thunder III', 'SYS'),
    ('820513 8', 'Booster III system ISC Mockup', 'SYS'),
    ('820513', 'Booster III system ISC', 'SYS'),
    ('820515', 'Booster III Boot Flash ISC', 'SYS'),
    ('820519', 'BoosterIII display Fpga iSC250', 'SYS'),
    ('820520', 'Driver synch GPM896 Thunder III', 'SYS'),
    ('820521', 'Driver synch GFM Thunder III', 'SYS'),
    ('820522', 'Driver synch SLE4436 Thunder III', 'SYS'),
    ('820523', 'Driver synch SLE4404 Thunder III', 'SYS'),
    ('820524', 'Driver synch AT88SC1003 Thunder III', 'SYS'),
    ('820525', 'Driver synch GPM271 Thunder III', 'SYS'),
    ('820526', 'Driver synch S10 Thunder III', 'SYS'),
    ('820527', 'Driver synch S9 Thunder III', 'SYS'),
    ('820529', 'Driver GPRS Thunder III', 'SYS'),
    ('820537', 'DLL WIFI Thunder III', 'SYS'),
    ('820538', 'DLL WIFI TI', 'SYS'),
    ('820540', 'Driver ECR SPI', 'SYS'),
    ('820541', 'Driver Barcode Reader', 'SYS'),
    ('820542 8', 'System IPP2XX Mockup Thunder III', 'SYS'),
    ('820542', 'System IPP2XX Thunder III', 'SYS'),
    ('820543', 'Driver WIFI TI Thunder III', 'SYS'),
    ('820552 8', 'Booster III system IDE Mockup', 'SYS'),
    ('820552', 'Booster III system IDE', 'SYS'),
    ('820553 8', 'Booster III system IWX Mockup', 'SYS'),
    ('820553', 'Booster III system IWX', 'SYS'),
    ('830063', 'BOOSTER III Boot Flash', 'SYS'),
    ('830064 8', 'Booster III system X07 Mockup', 'SYS'),
    ('830064', 'Booster III system X07', 'SYS'),
    ('844231', 'TS Configuration file iWL280', 'SYS'),
    ('844237', 'DLL TCP iSMP', 'SYS'),
    ('844377', 'TS Configuration file iWL350', 'SYS'),
    ('844575', 'TS Configuration file iWL280 MXT224E', 'SYS'),
    ('844580', 'DLL BCR', 'SYS'),
    ('844605', 'DLL GPS', 'SYS'),
    ('844863', 'TS Configuration file iDE280', 'SYS'),
    ('844920', 'SELF TEST Application', 'SYS'),
# CalData
    ('3628',   'LINK LAYER with IP', 'SYS'),
    ('3655',   'CLESS DLL', 'SYS'),

    ('813349', 'Kernel CLESS Mastercard PayPass', 'SYS'),
    ('813350', 'Kernel CLESS Visa payWave', 'SYS'),
    ('813352', 'Kernel CLESS Discover', 'SYS'),
    ('844013', 'Kernel CLESS Visa Wave 2', 'SYS'),
    ('813350', 'Kernel CLESS Visa payWave', 'SYS'),
    ('813349', 'Kernel CLESS Mastercard PayPass', 'SYS'),
    ('844231', 'Mastercard Paypass Kernel CLESS', 'SYS'),
    ('844241', 'Mastercard PayPass Kernel CLESS', 'SYS'),
    ('844050', 'Kernel CLESS Interac Kernel', 'SYS'),
    ('813351', 'Kernel CLESS AMEX ExpressPay', 'SYS'),
    ('844297', 'CLESS Amex Express Pay', 'SYS'),
    ('844241', 'Mastercard PayPass Kernel CLESS', 'SYS'),

    ('813354', 'CLESS ENTRY POINT', 'SYS'),
    ('820125', 'Driver BT BC06 handheld', 'SYS'),
    ('820126', 'Driver BT BC06 base', 'SYS'),

    ('844216', 'FONT ISO 1', 'SYS'),
    ('844217', 'FONT ISO 2', 'SYS'),
    ('844218', 'FONT ISO 3', 'SYS'),
    ('844219', 'FONT ISO 5', 'SYS'),
    ('844213', 'FONT ISO 6', 'SYS'),
    ('844220', 'FONT ISO 7', 'SYS'),
    ('844221', 'FONT ISO 15', 'SYS'),

    # From 11.12.2
    ('800001', 'EXTENS', 'SYS'),
    ('800002', 'EMUL', 'SYS'),
    ('800002', 'M2OS', 'SYS'),
    ('800003', 'LIBGR', 'SYS'),
    ('800004', 'PARAM', 'SYS'),
    ('800005', 'ENTRY', 'SYS'),
    ('800008', 'DLLPSC', 'SYS'),
    ('800009', 'PROTOCOLE', 'SYS'),
    ('800010', 'CRYPTO', 'SYS'),
    ('800012', 'EMVSQ', 'SYS'),
    ('800013', 'IAM', 'SYS'),
    ('800015', 'PINPAD', 'SYS'),
    ('800019', 'UMS', 'SYS'),
    ('800051', 'COLOR', 'SYS'),
    ('822444', 'TPass', 'SYS'),
    ('844200', 'SCREEN', 'SYS'),
    ('844371', 'SCREEN', 'SYS'),
    ('844372', 'ZIPM2OS_BW', 'SYS'),
    ('844562', 'libWrapper', 'SYS'),
    ('844593', 'CB2A', 'SYS'),
    ('844622', 'TMTOOLS', 'SYS'),
    ('844699', 'LibEmul', 'SYS'),
    ('846007', 'ZIPM2OS', 'SYS'),
    ('846010', 'SPMCIWR', 'SYS'),
    ('999000000003', 'T3_PACK_SYSTEM', 'SYS'),
    ('999000010807', 'LIBLINKLAYER', 'SYS'),
    ('999000010807', 'SVCLINKLAYER', 'SYS'),
    ('999000010807', 'SVCLINKLAYER', 'SYS'),
    ('999003280201', 'OSLAYER', 'SYS'),
    ('999004405405', 'TOOL_LIBRARY', 'SYS'),
    ('999004405505', 'GRAPHIC_LIBRARY', 'SYS'),
    ('999004405605', 'GRAPHIC_SERVER', 'SYS'),
    ('999004405705', 'GRAPHIC_CLIENT', 'SYS'),
    ('999004405805', 'GOAL_FONT', 'SYS'),
    ('999004429902', 'DLLSQLITE', 'SYS'),
    ('999004430005', 'GOAL_IMGWGU', 'SYS'),
    ('999004430105', 'GOAL_IMGPNG', 'SYS'),
    ('999004430205', 'GOAL_LIBZIP', 'SYS'),
    ('999004430305', 'GOAL_LIBPNG', 'SYS'),
    ('999004430405', 'GOAL_IMGJPG', 'SYS'),
    ('999004430505', 'GOAL_LIBJPG', 'SYS'),
    ('999004430605', 'GOAL_IMGGIF', 'SYS'),
    ('999004430705', 'GOAL_LIBGIF', 'SYS'),
    ('999004430805', 'GOAL_IMGBMP', 'SYS'),
    ('999004430905', 'GOAL_IMGIPF', 'SYS'),
    ('999004431205', 'GRAP_SERV_APP', 'SYS'),
    ('999004432005', 'GOAL_PLGMMEDIA', 'SYS'),
    ('999004432105', 'GOAL_PLGSIGN', 'SYS'),
    ('999004432205', 'GOAL_PLGCAMERA', 'SYS'),
    ('999004432805', 'GOAL_LIBAZTEC', 'SYS'),
    ('999004432905', 'GOAL_BCAZTEC', 'SYS'),
    ('999004433101', 'DEFAULT_KEYMAP', 'SYS'),
    ('999004433205', 'GOAL_BCQR', 'SYS'),
    ('999004433305', 'GOAL_BCCODE128', 'SYS'),
    ('999004433405', 'GOAL_BCCODE25', 'SYS'),
    ('999004433505', 'GOAL_BCCODE39', 'SYS'),
    ('999004433605', 'GOAL_BCEAN8', 'SYS'),
    ('999004433705', 'GOAL_BCEAN13', 'SYS'),
    ('999004433905', 'GOAL_PRINTER', 'SYS'),
    ('999004434005', 'GOAL_ARIAL', 'SYS'),
    ('999004434105', 'GOAL_LIBQR', 'SYS'),
    ('999004434305', 'LIBGRAPHICS', 'SYS'),
    ('999004434405', 'GOAL_ARIAL_BOLD', 'SYS'),
    ('999004434505', 'GOAL_ARIAL_ITAL', 'SYS'),
    ('999004434605', 'GOAL_ARIAL_BOIT', 'SYS'),
    ('999004439004', 'SpiBLight', 'SYS'),
    ('999004439004', 'SpiBLight', 'SYS'),
    ('999004439104', 'Backlight', 'SYS'),
    ('999004439204', 'SpiBuzzer', 'SYS'),
    ('999004439204', 'SpiBuzzer', 'SYS'),
    ('999004439304', 'Buzzer', 'SYS'),
    ('999004439502', 'DAL_DLL', 'SYS'),
    ('999004448405', 'Protobuf', 'SYS'),
    ('999004448505', 'OsLib', 'SYS'),
    ('999004448604', 'Service', 'SYS'),
    ('999004448704', 'SrvDirecto', 'SYS'),
    ('999004448704', 'SrvDirecto', 'SYS'),
    ('999004448804', 'SrvDirSkel', 'SYS'),
    ('999004448904', 'SrvDirProx', 'SYS'),
    ('999004453905', 'STON_SK128_64', 'SYS'),
    ('999004454005', 'STON_SK320_240', 'SYS'),
    ('999004454305', 'STON_SK240_320', 'SYS'),
    ('999004454405', 'STON_SK320_480', 'SYS'),
    ('999004454505', 'STON_SK800_480', 'SYS'),
    ('999004454605', 'STON_SK480_320', 'SYS'),
    ('999004461404', 'ConfBLight', 'SYS'),
    ('999004461504', 'ConfBuzzer', 'SYS'),
    ('999004462407', 'BTVIEW', 'SYS'),
    ('999004462407', 'BTVIEW', 'SYS'),
    ('999004462503', 'LIBPCL', 'SYS'),
    ('999004462503', 'SVCPCL', 'SYS'),
    ('999004462503', 'SVCPCL', 'SYS'),
    ('999004462603', 'LIBSPMCI', 'SYS'),
    ('999004462603', 'SVCSPMCI', 'SYS'),
    ('999004462603', 'SVCSPMCI', 'SYS'),
    ('999004462703', 'PCLVIEW', 'SYS'),
    ('999004462703', 'PCLVIEW', 'SYS'),
    ('999004462907', 'GPRSVIEW', 'SYS'),
    ('999004462907', 'GPRSVIEW', 'SYS'),
    ('999004463307', 'SVCPACKIP', 'SYS'),
    ('999004463307', 'LIBPACKIP', 'SYS'),
    ('999004463506', 'LIBETHERNET', 'SYS'),
    ('999004463507', 'SVCETHERNET', 'SYS'),
    ('999004463507', 'SVCETHERNET', 'SYS'),
    ('999004463607', 'ETHVIEW', 'SYS'),
    ('999004463707', 'SOFTMGTCLI', 'SYS'),
    ('999004463906', 'LIBTLVTREEXML', 'SYS'),
    ('999004464007', 'LIBGPRS', 'SYS'),
    ('999004464007', 'SVCGPRS', 'SYS'),
    ('999004464007', 'SVCGPRS', 'SYS'),
    ('999004464107', 'MODEMVIEW', 'SYS'),
    ('999004469706', 'DEVICE_LEDS', 'SYS'),
    ('999004469807', 'LIBSOFTMGT', 'SYS'),
    ('999004469807', 'SOFTMGTSRV', 'SYS'),
    ('999004469807', 'SOFTMGTSRV', 'SYS'),
    ('999004470004', 'Desktop', 'SYS'),
    ('999004470004', 'Desktop', 'SYS'),
    ('999004470004', 'Desktop', 'SYS'),
    ('999004470104', 'Header', 'SYS'),
    ('999004470104', 'Header_BW', 'SYS'),
    ('999004470104', 'Header_Color', 'SYS'),
    ('999004470204', 'Settings', 'SYS'),
    ('999004470204', 'Settings', 'SYS'),
    ('999004470204', 'Settings', 'SYS'),
    ('999004470304', 'Explorer', 'SYS'),
    ('999004470404', 'ScreenSaver', 'SYS'),
    ('999004470504', 'ConfPlatf', 'SYS'),
    ('999004470504', 'ConfSettings', 'SYS'),
    ('999004470604', 'VirtualKb', 'SYS'),
    ('999004470704', 'Inactivity', 'SYS'),
    ('999004470704', 'Inactivity', 'SYS'),
    ('999004470704', 'Inactivity', 'SYS'),
    ('999004470804', 'InactivityCfg', 'SYS'),
    ('999004470904', 'SpiNotifyUs', 'SYS'),
    ('999004470904', 'SpiNotifyUs', 'SYS'),
    ('999004471004', 'Battery', 'SYS'),
    ('999004471104', 'SpiPINpad', 'SYS'),
    ('999004471104', 'SpiPINpad', 'SYS'),
    ('999004471204', 'GPS', 'SYS'),
    ('999004471304', 'ConfGPS', 'SYS'),
    ('999004471404', 'Monitoring', 'SYS'),
    ('999004471504', 'SpiMonitor', 'SYS'),
    ('999004471504', 'SpiMonitor', 'SYS'),
    ('999004471604', 'ExpView_BW', 'SYS'),
    ('999004471604', 'ExpView_Color', 'SYS'),
    ('999004471704', 'Capture', 'SYS'),
    ('999004471704', 'Capture', 'SYS'),
    ('999004471704', 'CapturePlf', 'SYS'),
    ('999004471804', 'Capture', 'SYS'),
    ('999004471904', 'ConfCapture', 'SYS'),
    ('999004472004', 'PINPADTEXT', 'SYS'),
    ('999004472204', 'LibAccelero', 'SYS'),
    ('999004472304', 'SpiAccelero', 'SYS'),
    ('999004472304', 'SpiAccelero', 'SYS'),
    ('999004474104', 'SpiExplorer', 'SYS'),
    ('999004474104', 'SpiExplorer', 'SYS'),
    ('999004474204', 'SpiHeader', 'SYS'),
    ('999004474304', 'SpiVirtKb', 'SYS'),
    ('999004474304', 'SpiVirtKb', 'SYS'),
    ('999004474404', 'SpiGPS', 'SYS'),
    ('999004474404', 'SpiGPS', 'SYS'),
    ('999004474504', 'SpiBattery', 'SYS'),
    ('999004474504', 'SpiBattery', 'SYS'),
    ('999004474604', 'SrvNative', 'SYS'),
    ('999004475105', 'TrEngine', 'SYS'),
    ('999004475105', 'TrEngine', 'SYS'),
    ('999004475105', 'TrEngine', 'SYS'),
    ('999004482803', 'LIBWHITELIS', 'SYS'),
    ('999004483201', 'SrvPinpad', 'SYS'),
    ('999004488603', 'DGPRST3', 'SYS'),
    ('999004488703', 'DBTT3', 'SYS'),
    ('999004710605', 'DeviceChip', 'SYS'),
    ('999004710705', 'DeviceCless', 'SYS'),
    ('999004710805', 'DeviceSwipe', 'SYS'),
    ('999004712907', 'LIBMODEM', 'SYS'),
    ('999004712907', 'SVCMODEM', 'SYS'),
    ('999004712907', 'SVCMODEM', 'SYS'),
    ('999004713207', 'LIBBTOOTH', 'SYS'),
    ('999004713207', 'SVCBTOOTH', 'SYS'),
    ('999004713207', 'SVCBTOOTH', 'SYS'),
    ('999004713307', 'WIFIVIEW', 'SYS'),
    ('999004713407', 'LIBWIFI', 'SYS'),
    ('999004713407', 'SVCWIFI', 'SYS'),
    ('999004713407', 'SVCWIFI', 'SYS'),
    ('999004713907', 'LIBIAP', 'SYS'),
    ('999004713907', 'SVCIAP', 'SYS'),
    ('999004713907', 'SVCIAP', 'SYS'),
    ('999004715903', 'NANOX_TTF', 'SYS'),
    ('999004716403', 'NETMAN', 'SYS'),
    ('999004718803', 'LIBBTDLL', 'SYS'),
    ('999004721803', 'LIBBLTOOTH', 'SYS'),
    ('999004722801', 'CRDMGT_LNCH', 'SYS'),
    ('999004722906', 'DEVICE_LEDS', 'SYS'),
    ('999004722906', 'DEVICE_LEDS', 'SYS'),
    ('999005288115', 'Bridge', 'SYS'),
    ('999102020003', 'TLINUX', 'SYS'),
    ('999102020103', 'KERNEL_MOD', 'SYS'),
    ('999102020303', 'CONFIG_PROD', 'SYS'),
    ('999102020403', 'SRV_MANAGER', 'SYS'),
    ('999102020503', 'CONFIG_STARTUP', 'SYS'),
    ('999102020603', 'APP_MGT', 'SYS'),
    ('999102020703', 'T3UTILS', 'SYS'),
    ('999102021003', 'NANOX', 'SYS'),
    ('999102021203', 'SLM_CLIENT', 'SYS'),
    ('999102021303', 'SLM_ADMIN', 'SYS'),
    ('999104467303', 'LINGOT_BASE', 'SYS'),
    ('999104467403', 'LINGOT_SEC', 'SYS'),
    ('999104467503', 'LINGOT_NET', 'SYS'),
    ('999104467603', 'LINGOT_MM', 'SYS'),
    ('999104467803', 'SEC_BOOT', 'SYS'),
    ('999104467903', 'SW_ACTIVATE', 'SYS'),
    ('999104480203', 'APP_SYS', 'SYS'),
    ('999104480303', 'SRV_SCH', 'SYS'),
    ('999104480903', 'SRV_RES_ALLOC', 'SYS'),
    ('999104481003', 'SLM_CORE', 'SYS'),
    ('999104482003', 'TZ', 'SYS'),
    ('999104484003', 'SRV_KBD', 'SYS'),
    ('999104708005', 'T2_PP_SYST', 'SYS'),
    ('999104710100', 'T2_PP_BFL', 'SYS'),
    ('999104714001', 'LLTSIM', 'SYS'),
    ('999104714110', 'T2_PP_PACK', 'SYS'),
    ('999104715303', 'MOTOROLA_BC', 'SYS'),
    ('999104717103', 'KERNEL_MOD_QATCHER', 'SYS'),
    ('999104722200', 'T2_BASE_PACK', 'SYS'),
    ('999114467603', 'LINGOT_MB', 'SYS'),
    ('999114481003', 'SLM_CORE_LIGHT', 'SYS'),
    ('999200000106', 'LLTCLIENT', 'SYS'),
    ('999200002705', 'Security_Dll', 'SYS'),
    ('999204437006', 'TMSCALL', 'SYS'),
    ('999204437006', 'TMSCALL', 'SYS'),
    ('999204461805', 'TransactionPx', 'SYS'),
    ('999204461805', 'TransactionPx', 'SYS'),
    ('999204461906', 'TMSCALLVIEW', 'SYS'),
    ('999204462006', 'LIBTMSCALLPX', 'SYS'),
    ('999204462803', 'LIBPRINTER', 'SYS'),
    ('999204462803', 'SRVPRINTER', 'SYS'),
    ('999204462803', 'SRVPRINTER', 'SYS'),
    ('999204463106', 'LIBSVCTMSC', 'SYS'),
    ('999204463106', 'SVCTMSC', 'SYS'),
    ('999204463106', 'SVCTMSC', 'SYS'),
    ('999204463206', 'APPTMSC', 'SYS'),
    ('999204468500', 'LIBCLAPDU', 'SYS'),
    ('999204468602', 'LIBCLLOA', 'SYS'),
    ('999204468704', 'LIBCLASE', 'SYS'),
    ('999204468802', 'LIBCLTE', 'SYS'),
    ('999204469502', 'LIBSWTE', 'SYS'),
    ('999204469602', 'LIBMETE', 'SYS'),
    ('999204475105', 'TransactionSrv', 'SYS'),
    ('999204481002', 'LIBCTTE', 'SYS'),
    ('999204481202', 'LIBGCDR', 'SYS'),
    ('999204705311', 'SDKDESK5000', 'SYS'),
    ('999204705411', 'SDKMOVE5000', 'SYS'),
    ('999204705511', 'SDKLANE5000', 'SYS'),
    ('999204705611', 'SDKDESK3200', 'SYS'),
    ('999204705711', 'SDKDESK3500', 'SYS'),
    ('999204705811', 'SDKMOVE3500', 'SYS'),
    ('999204705911', 'SDKMOVE2500', 'SYS'),
    ('999204706011', 'SDKLANE7000', 'SYS'),
    ('999204706111', 'SDKLINK2500', 'SYS'),
    ('999204706211', 'SDKLANE8000', 'SYS'),
    ('999204706311', 'SDKMOVE5000LITE', 'SYS'),
    ('999204710205', 'DEVICE_CHIP', 'SYS'),
    ('999204710205', 'DEVICE_CHIP', 'SYS'),
    ('999204710305', 'DEVICE_CLES', 'SYS'),
    ('999204710305', 'DEVICE_CLES', 'SYS'),
    ('999204712202', 'SchemeClient', 'SYS'),
    ('999204712601', 'SecurityPrx', 'SYS'),
    ('999204712601', 'SecuritySvc', 'SYS'),
    ('999204712601', 'SecuritySvc', 'SYS'),
    ('999204716102', 'LIBCLEEPx', 'SYS'),
    ('999204716202', 'LIBCLEESrv', 'SYS'),
    ('999204716403', 'LIBNETMAN', 'SYS'),
    ('999204716902', 'TUICustoTp', 'SYS'),
    ('999204717002', 'TUIEngine', 'SYS'),
    ('999204718906', 'LIBTMSEMU', 'SYS'),
    ('999204722002', 'TUserInterfSvc', 'SYS'),
    ('999204722002', 'TUserInterfSvc', 'SYS'),
    ('999204722705', 'LIBDEV_SWIP', 'SYS'),
    ('999204722705', 'LIBDEV_SWIP', 'SYS'),
    ('999204726606', 'TPass', 'SYS'),
    ('999204726606', 'TPassT3', 'SYS'),
    ('999204726701', 'SecurityTp', 'SYS'),
    ('999204790004', 'PltfLang', 'SYS'),
    ('999204790104', 'PltfParam', 'SYS'),
    ('999204800011', 'OPT_BCR', 'SYS'),
    ('999204800111', 'OPT_BT', 'SYS'),
    ('999204800211', 'OPT_WF', 'SYS'),
    ('999204800311', 'OPT_GPS', 'SYS'),
    ('999204800411', 'OPT_PP', 'SYS'),
    ('999204800511', 'OPT_GBC', 'SYS'),
    ('999204800611', 'OPT_FR', 'SYS'),
    ('999204800711', 'OPT_SQLI', 'SYS'),
    ('999204800811', 'OPT_PCL', 'SYS'),
    ('999204800911', 'OPT_QATCH', 'SYS'),
    ('999204801011', 'OPT_PRINT', 'SYS'),
    ('999214705311', 'SDKDESK5000', 'SYS'),
    ('999214705411', 'SDKMOVE5000', 'SYS'),
    ('999214705511', 'SDKLANE5000', 'SYS'),
    ('999214705611', 'SDKDESK3200', 'SYS'),
    ('999214705711', 'SDKDESK3500', 'SYS'),
    ('999214705811', 'SDKMOVE3500', 'SYS'),
    ('999214705911', 'SDKMOVE2500', 'SYS'),
    ('999214706011', 'SDKLANE7000', 'SYS'),
    ('999214706111', 'SDKLINK2500', 'SYS'),
    ('999214706211', 'SDKLANE8000', 'SYS'),
    ('999214706311', 'SDKMOVE5000LITE', 'SYS'),
    ('999214790004', 'PltfLang', 'SYS'),
    ('999214800011', 'OPT_BCR', 'SYS'),
    ('999214800111', 'OPT_BT', 'SYS'),
    ('999214800211', 'OPT_WF', 'SYS'),
    ('999214800411', 'OPT_PP', 'SYS'),
    ('999224800011', 'OPT_BCR', 'SYS'),
    ('999224800111', 'OPT_BT', 'SYS'),
    ('999224800211', 'OPT_WF', 'SYS'),
    ('999224800411', 'OPT_PP', 'SYS'),
    ('999234800011', 'OPT_BCR', 'SYS'),
    ('999234800111', 'OPT_BT', 'SYS'),
    ('999234800211', 'OPT_WF', 'SYS'),
    ('999244800011', 'OPT_BCR', 'SYS'),
    ('999244800111', 'OPT_BT', 'SYS'),
    ('999244800211', 'OPT_WF', 'SYS'),
    ('999254800111', 'OPT_BT', 'SYS'),
    ('999254800211', 'OPT_WF', 'SYS'),
    ('999264800211', 'OPT_WF', 'SYS'),
    ('999274800111', 'OPT_BT', 'SYS'),
    ('999274800211', 'OPT_WF', 'SYS'),
    ('999304708102', 'TUserInterfPx', 'SYS'),
    ('999504497903', 'SRV_TEST_OEMSER', 'SYS'),

    # ('', 'TERMINALS_DLLSQLITE', 'SYS'),
    # ('', 'TERMINALS_EMULATION_FOR_FRANCE_ONLY', 'SYS'),
    # ('', 'TERMINALS_GOAL_BARCODES', 'SYS'),
    # ('', 'TERMINALS_PCL_SPMCI', 'SYS'),
    # ('', 'TERMINALS_QATCHER', 'SYS'),
    # ('', 'd', 'SYS'),

    ('DESK', 'CAMERA BC_Reader', 'SYS'),
    ('DESK', 'PINPAD', 'SYS'),
    ('DESK', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('DESK', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('DESK', 'CAMERA BC_Reader', 'SYS'),
    ('DESK', 'PINPAD', 'SYS'),
    ('DESK', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('DESK', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('DESK', 'CAMERA BC_Reader', 'SYS'),
    ('DESK', 'COMMUNICATION_BT', 'SYS'),
    ('DESK', 'COMMUNICATION_WIFI', 'SYS'),
    ('DESK', 'PINPAD', 'SYS'),
    ('DESK', 'TRANSAC_T3_FULL_CONF - Loader', 'SYS'),
    ('DESK', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('DESK', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    # ('', 'F', 'SYS'),
    ('FontsL', 'FontsLe', 'SYS'),
    ('LANE', 'CAMERA BC_Reader', 'SYS'),
    ('LANE', 'COMMUNICATION_BT', 'SYS'),
    ('LANE', 'COMMUNICATION_WIFI', 'SYS'),
    ('LANE', 'LANE1000', 'SYS'),
    ('LANE', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('LANE', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('LANE', 'COMMUNICATION_BT', 'SYS'),
    ('LANE', 'COMMUNICATION_WIFI', 'SYS'),
    ('LANE', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('LANE', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('LANE', 'COMMUNICATION_BT', 'SYS'),
    ('LANE', 'COMMUNICATION_WIFI', 'SYS'),
    ('LANE', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('LANE', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('LINK', 'COMMUNICATION_BT', 'SYS'),
    ('LINK', 'COMMUNICATION_WIFI', 'SYS'),
    ('LINK', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('LINK', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('MOVE', 'COMMUNICATION_WIFI', 'SYS'),
    ('MOVE', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('MOVE', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('MOVE', 'COMMUNICATION_BT', 'SYS'),
    ('MOVE', 'COMMUNICATION_WIFI', 'SYS'),
    ('MOVE', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('MOVE', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('MOVE5000', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('MOVE5000', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
    ('MOVE', 'CAMERA BC_Reader', 'SYS'),
    ('MOVE', 'COMMUNICATION_BT', 'SYS'),
    ('MOVE', 'COMMUNICATION_WIFI', 'SYS'),
    ('MOVE', 'GPS', 'SYS'),
    ('MOVE', 'TRANSAC_T3_FULL_CONF', 'SYS'),
    ('MOVE', 'TRANSAC_TPLUS_FULL_CONF', 'SYS'),
]
manager_components = [
    ('4778',   'COMP_INGESTATE', 'MAN'),
    ('813687', 'CGUI', 'MAN'),
    ('813909', 'CGUI_SIGNATURE', 'MAN'),
    ('813910', 'CGUI_VIDEO', 'MAN'),
    ('820160', 'OSLAYER', 'MAN'),
    ('820161', 'OSLAYER', 'MAN'),
    ('820371', 'NX_DRIVER', 'MAN'),
    ('820517', 'NX_DRIVER', 'MAN'),
    ('820532', 'DAL', 'MAN'),
    ('844016', 'CGUI_MONOSPACE', 'MAN'),
    ('844017', 'CGUI_SANSSERIF', 'MAN'),
    ('844018', 'CGUI_SERIF', 'MAN'),
    ('844054', 'TOOL_LIBRARY', 'MAN'),
    ('844055', 'GRAPHIC_LIBRARY', 'MAN'),
    ('844056', 'GRAPHIC_SERVER', 'MAN'),
    ('844057', 'GRAPHIC_CLIENT', 'MAN'),
    ('844058', 'GOAL_FONT', 'MAN'),
    ('844059', 'GOAL_SK128_64', 'MAN'),
    ('844060', 'GOAL_SK320_240', 'MAN'),
    ('844061', 'GOAL_SK480_272', 'MAN'),
    ('844062', 'GOAL_SK640_480', 'MAN'),
    ('844063', 'GOAL_SK240_320', 'MAN'),
    ('844064', 'GOAL_SK320_480', 'MAN'),
    ('844065', 'GOAL_SK800_480', 'MAN'),
    ('844082', 'Ppload', 'MAN'),
    ('844085', 'COLOR HEADER FOR ICT2XX-IPP3XX', 'MAN'),
    ('844086', 'COLOR HEADER FOR ISC3XX', 'MAN'),
    ('844087', 'COLOR HEADER FOR ISC2XX', 'MAN'),
    ('844089', 'COLOR HEADER FOR IWL280', 'MAN'),
    ('844097', 'COLOR HEADER FOR IWL250', 'MAN'),
    ('844098', 'COLOR HEADER FOR IWL350', 'MAN'),
    ('844221', 'FONT ISO15 STANDARD', 'MAN'),
    ('844229', 'SDK', 'MAN'),
    ('844300', 'GOAL_IMGWGU', 'MAN'),
    ('844301', 'GOAL_IMGPNG', 'MAN'),
    ('844302', 'GOAL_LIBZIP', 'MAN'),
    ('844303', 'GOAL_LIBPNG', 'MAN'),
    ('844304', 'GOAL_IMGJPG', 'MAN'),
    ('844305', 'GOAL_LIBJPG', 'MAN'),
    ('844306', 'GOAL_IMGGIF', 'MAN'),
    ('844307', 'GOAL_LIBGIF', 'MAN'),
    ('844308', 'GOAL_IMGBMP', 'MAN'),
    ('844309', 'GOAL_IMGIPF', 'MAN'),
    ('844310', 'GOAL_SK480_320', 'MAN'),
    ('844320', 'GOAL_PLGMMEDIA', 'MAN'),
    ('844321', 'GOAL_PLGSIGN', 'MAN'),
    ('844322', 'GOAL_PLGCAMERA', 'MAN'),
    ('844328', 'GOAL_LIBAZTEC', 'MAN'),
    ('844329', 'GOAL_BCAZTEC', 'MAN'),
    ('844331', 'KEYMAP', 'MAN'),
    ('844332', 'GOAL_BCQR', 'MAN'),
    ('844333', 'GOAL_BCCODE128', 'MAN'),
    ('844334', 'GOAL_BCCODE25', 'MAN'),
    ('844335', 'GOAL_BCCODE39', 'MAN'),
    ('844336', 'GOAL_BCEAN8', 'MAN'),
    ('844337', 'GOAL_BCEAN13', 'MAN'),
    ('844338', 'GOAL_BCPDF417', 'MAN'),
    ('844339', 'GOAL_PRINTER', 'MAN'),
    ('844341', 'GOAL_LIBQR', 'MAN'),
    ('844351', 'GL_DLL_FOR_EFT930CCICT250IPP350ML30CCIWL250', 'MAN'),
    ('844357', 'GM RESOURCE FOR COLOR ICT2XX-IWL2XX-IPP3XX', 'MAN'),
    ('844358', 'GM RESOURCE FOR ISC3XX', 'MAN'),
    ('844359', 'GM RESOURCE FOR ISC2XX', 'MAN'),
    ('844361', 'GM RESOURCE FOR IWL350', 'MAN'),
    ('844362', 'COLOR HEADER FOR IPP480', 'MAN'),
    ('844363', 'GM RESOURCE FOR IPP480', 'MAN'),
    ('844366', 'FTPC', 'MAN'),
    ('844371', 'GL_DLL_FOR_EFT930ICT220IPP320ML30IWL220', 'MAN'),
    ('844372', 'GM RESOURCE FOR BW ICT2XX-IWL2XX-IPP3XX', 'MAN'),
    ('844373', 'BW HEADER FOR ICT2XX-IPP3XX', 'MAN'),
    ('844376', 'HOMESCREEN', 'MAN'),
    ('844405', 'GM RESOURCE FOR ISC4XX', 'MAN'),
    ('844436', 'GM RESOURCE FOR IWL280', 'MAN'),
    ('844437', 'GM RESOURCE FOR COLOR IWL2XX3T', 'MAN'),
    ('844438', 'GM RESOURCE FOR BW IWL2XX3T', 'MAN'),
    ('844439', 'GM RESOURCE FOR ICE280', 'MAN'),
    ('844440', 'GM RESOURCE FOR PINPAD', 'MAN'),
    ('844441', 'GM RESOURCE FOR COLOR IMP6XX', 'MAN'),
    ('844592', 'M2OS', 'MAN'),
    ('844593', 'CB2A', 'MAN'),
    ('844594', 'Extension', 'MAN'),
    ('844596', 'Graphic_Librairy', 'MAN'),
    ('844597', 'M2OS_Parameters', 'MAN'),
    ('844598', 'Entry', 'MAN'),
    ('844599', 'CamDate_Librairy', 'MAN'),
    ('844601', 'PSC_Protocol', 'MAN'),
    ('844602', 'NULL_Protocol', 'MAN'),
    ('844603', 'Protocol', 'MAN'),
    ('844604', 'Protocol', 'MAN'),
    ('844606', 'Cryptographic_librairy', 'MAN'),
    ('844607', 'Partage', 'MAN'),
    ('844608', 'EMV_Selection', 'MAN'),
    ('844609', 'IAM', 'MAN'),
    ('844610', 'Pinpad', 'MAN'),
    ('844616', 'ums', 'MAN'),
    ('844621', 'gprs', 'MAN'),
    ('844622', 'tmtools', 'MAN'),
    ('844642', 'Hardware_cnf', 'MAN'),
    ('844692', 'COLOR', 'MAN'),
    ('844778', 'PACK', 'MAN'),
# CalData
    ('4656',   'Security_Exp_T2', 'MAN'),
    ('4685',   'Security_Fr_T2', 'MAN'),
    ('844078', 'DLL_E2EE', 'MAN'),
    ('3656',   'Security', 'MAN'),
    ('3778',   'INGESTATE_COMPATIBILITY', 'MAN'),
    ('4778',   'INGESTATE_COMPATIBILITY_T2', 'MAN'),
    ('4611',   'PPR30_T2', 'MAN'),
    ('813687', 'CGUI', 'MAN'),
    ('813909', 'CGUI_SIGNATURE', 'MAN'),
    ('813910', 'CGUI_VIDEO', 'MAN'),
]
security_components = [
    ('8460120101', '', 'CKF France T2', 'KGN'),
    ('AXISCA', '', 'Certificat Axis', 'CRT'),
    ('AFOCAROOT', '', 'Certificat Com Caisse', 'CRT'),
    ('SERVER_POS', '', 'Certificat Com Caisse', 'CRT'),
    ('9990020621010100_00007', '', 'CKF France T3', 'CRT'),
    ('9990020621010400_00007', '', 'CKF France T3 Autonome', 'CRT'),
    ('9990020621010500_00007', '', 'CKF France T3 Autonome', 'CRT'),
]
unknown_component = ('??????', '???', '???')
dict_file_types = {
    "AGN" : "Application",
    "LGN" : "Library",
    "PGN" : "Parameter",
    "DGN" : "Driver",
    "BIN" : "Unsigned",
    "TXT" : "Descriptor",

    "CRT" : "Pub. Certif.",
    "PEM" : "Priv. Certif.",
    "KGN" : "Key",

    "P3A" : "Application",
    "P3L" : "Library",
    "P3P" : "Parameter",
    "P3S" : "OS File",
    "P3O" : "OS File",
    "P3K" : "OS File",
    "P3T" : "Key",
}
sdk_versions = [
    #('Sys', 'Man', 'SDK'),
    ('38.04', '84.02', '9.18.1'),
    ('38.06', '84.07', '9.18.2'),
    ('39.00', '84.12', 'Beta 9.19.0'),
    ('40.08', '84.18', 'Beta 9.19.1'),
    ('40.12', '84.18', '9.20.0'),
    ('40.34', '84.18', '9.20.0'),
    ('40.14', '84.18', '9.20.1'),
    ('40.36', '84.19', '9.20.1'),
    ('40.42', '84.21', '9.20.2'),
    ('40.44', '84.22', '9.20.3'),
    ('42.00', '84.34', 'Beta 9.21.0'),
    ('42.06', '84.36', '9.22.0'),
    ('42.08', '84.38', '9.22.1'),
    ('42.08', '84.39', '9.22.2'),
    ('43.06', '84.51', 'Beta 9.23.1'),
    ('44.00', '84.54', '9.24.0'),
    ('44.00', '84.55', '9.24.1'),
    ('44.22', '84.56', '9.24.2'),
    ('44.22', '84.57', '9.24.3'),
    ('46.02', '84.74', 'Beta 9.25.0'),
    ('46.06', '84.78', '9.26.0'),
    ('46.12', '84.80', '9.26.1'),
    ('46.14', '84.81', '9.26.2'),
    ('47.03', '85.03', 'Beta 9.27.0'),
    ('47.03', '85.04', '9.28.0'),
    ('48.01', '85.06', '9.28.1'),
    ('49.01', '85.31', 'Beta 9.29.0'),
    ('50.02', '85.35', '9.30.0'),
    ('50.05', '85.35', '9.30.1'),
    ('50.12', '85.51', '9.30.2'),
    ('50.20', '85.75', '9.30.2 Patch I'),
    ('51.07', '86.02', 'Beta 9.31.0'),
    ('52.00', '86.05', '9.32.0'),
    ('52.11', '86.08', '9.32.1'),
    ('52.15', '86.11', '9.32.2'),
    ('52.20', '86.15', '9.32.2 Patch D'),
    ('53.04', '87.02', '9.32.3'),
]
ads_params = [
    ('TAG_SIGNATURE_CAPTURE', '1-Active, 0-Desactive'),
    ('TAG_SIGNATURE_PARAM', 'XYZ dont X-Format (0-BMP, 1-PNG...), Y-Zippe, Z-Metadata'),
    ("TAG_ACTIV_OFFLINE_SAVE", "Duplicate Transaction"),
    ("TAG_ACTIV_ANNUL_AUTO", "Annulation automatique"),
    ("TAG_NUM_TERM", "System -> Numero terminal"),
    ("TAG_PROFILE_CAPTURE_POS", " "),
    ("TAG_POS_TYPE", "CAISSE -> Protocole   0 : neant, 1 : protocole_6, "
                                "2 : protocole_9,  3 : protocole_STC5,   4 : Integre"),
    ("TAG_POS_VOIE", "CAISSE -> speed 0 : 1200bds , 1 :  9600bds, 2 :  19200bds,  3 :  38400bds, 4 :   115200"),
    ("TAG_POS_SPEED", " "),
    ("TAG_POS_TCPIP_SSL", " "),
    ("TAG_POS_COMAXIS", "CAISSE -> communication AXIS via caisse, 0 = non, 1 = oui"),
    ("TAG_POS_TCPIP_PORT", "Port en cas de configuration voie. Doit "
                           "correspondre au port du paramètre C3Config TCP_COM."),
    ("TAG_POS_ACQCANCEL", "CAISSE -> repondre"),
    ("TAG_PROT9_CHECK_CARD", "lancement d\’une transaction meme si la carte est presente avant paiement"),
    ("TAG_AXIS_TYPE", "CHOIX MEDIA AXIS -> 0= TCP/IP (ETHERNET, GPRS ou WIFI selon TPE)"),
    ("TAG_PROFILE_CAPTURE_AXIS_1", "ADRESSE D\'APPEL AXIS PRIMAIRE"),
    ("TAG_AXIS_REMOTE_HOST_ADD_1", ""),
    ("TAG_AXIS_REMOTE_HOST_PORT_1", ""),
    ("TAG_AXIS_REMOTE_HOST_SSL_1", ""),
    ("TAG_AXIS_REMOTE_HOST_SSL_PROFILE_1", ""),
    ("TAG_PROFILE_CAPTURE_AXIS_2", "ADRESSE D\'APPEL AXIS SECONDAIRE"),
    ("TAG_AXIS_REMOTE_HOST_ADD_2", ""),
    ("TAG_AXIS_REMOTE_HOST_PORT_2", ""),
    ("TAG_AXIS_REMOTE_HOST_SSL_2", ""),
    ("TAG_AXIS_REMOTE_HOST_SSL_PROFILE_2", ""),
    ("TAG_DL_MODE", "TELECHARGEMENT MODE : 1=TMS, 2=CAL, 3=CAL+TMS (TAL)"),
    ("TAG_TMS_CHANNEL", "TMS CHANNEL :  5=TMS_IP_DEFAULT, 1=TMS_IP_ETH, 2 = TMS_IP_GPRS, 3=TMS_IP_ECR; 4=Reserved"),
    ("TAG_TMS_IP_ADD", ""),
    ("TAG_TMS_IP_PORT", ""),
    ("TAG_TMS_SSL", ""),
    ("TAG_TMS_SSL_PROFILE", ""),
    ("TAG_OS_TMS_LOGON", ""),
    ("TAG_NB_NOUVEL_ESSAI", ""),
    ("TAG_ASSISTANCE_DEFICIENT_VISUEL", ""),
    ("TAG_NBTRY_BEFORE_FALLBACK", ""),
    ("TAG_PROFILE_CAPTURE_IP", ""),
    ("TAG_AXIS_IP_DHCP", "")
]
c3config_params = [
    ("SSL_MODE", "-0 : Sans SSL C3-Axis (xx)\n -1 : avec SSL"),
    ("AXIS_COM", "Serveur AXIS Primaire (nom du serveur ou adresse @ ou IP)"),
    ("AXIS_COM2", "Serveur AXIS Secondaire (nom du serveur ou adresse @ ou IP)"),
    ("AXIS_COM3", "Serveur AXIS Tertiaire (nom du serveur ou adresse @ ou IP)"),
    ("AXIS_ALT", "Serveur AXIS alternatif (nom du serveur ou adresse @ ou IP)"),
    ("VBK.SSL_MODE", "Activation, Désactivation Mode SSL AXIS VBK"),
    ("VBK.AXIS_COM", "Serveur AXIS VBK (nom du serveur ou adresse @ ou IP)"),
    ("IPS.SSL_MODE", "Activation, Désactivation Mode SSL AXIS IPS"),
    ("IPS.AXIS_COM", "Serveur AXIS IPS (nom du serveur ou adresse @ ou IP)"),
    ("OLA.SSL_MODE", "Activation, Désactivation Mode SSL AXIS OLA"),
    ("OLA.AXIS_COM", "Serveur AXIS OLA (nom du serveur ou adresse @ ou IP)"),
    ("CTD.SSL_MODE", "Activation, Désactivation Mode SSL AXIS CTD"),
    ("CTD.AXIS_COM", "Serveur AXIS CTD (nom du serveur ou adresse @ ou IP)"),
    ("AXIS_RECONNECT", "Connexion systematique Axis Primaire"),
    ("TIME_OUT_IP", "Timeout lors de la connexion"),
    ("TIME_OUT_IP_INIT", "Timeout lors de la connexion pour les initialisations"),
    ("TIME_OUT_CNX", "Timeout de déconnexion si pas de réponse Axis (en secondes)"),
    ("C3NET_MONOSESSION", " - 0 : C3 multi-session \n - 1 : C3 mono-session "),
    ("C3NET_POSDISPLAY_TIMEOUT", "Timeout d’attente de l’acquittement d\'affichage au niveau C3NET"
                                 "\n(en millisecondes, 1700 par défaut)"),
    ("L10_COM", "port de communication \n le port série (x) est adresse de la manière suivante "
                "selon les environnements :\n"
                "L10_COM=COMx 115200/8/1/0      : Windows\n"
                "L10_COM=x-1 38400/8/1/0        : DOS\n"
                "L10_COM=COMx: 115200/8/1/0     : Win CE\n"
                "L10_COM=/dev/ttySx 115200/8/1/0 : Linux\n"),
    ("TPE_SSL_MODE", "0 : Sans SSL C3Drvier-TPE (xx)\n"
                     "1 : avec SSL"),
    ("TCP_COM", "IP et Port COM"),
    ("TPE_TIMEOUT_CONNECT", "Timeout lors de la connexion du TPE connecte en IP (en secondes)"),
    ("CARTES", "Liste des applications activees"),
    ("QTPV", "Numero de terminal (8 chiffres)"),
    ("QCASH", "Numero de caissiere (8 chiffres)"),
    ("LPR_COM", "nom du fichier de sortie contenant le ticket client (XXX) et commercant (XXX.com)"),
    ("TICKET_COMM", "Activation / desactivation ticket commercant\n"
                    "0 : pas de generation du ticket commercant\n"
                    "1 : generation du ticket commercant  (xx)"),
    ("PRINTER_MODE", "Aiguillage des tickets\n"
                     "0 : pas d\'impression des tickets (xx)\n"
                     "2 : impression des tickets sur le TPE equipe d\'une imprimante"),
    ("DISPLAY_MODE", "Aiguillage Affichage et saisie\n"
                     "0 : Affichage et saisie sur le clavier de la caisse (xx)\n"
                     "1 : Affichage et saisie sur le clavier du TPE"),
    ("BUZZER_MODE", "Activation du buzzer\n"
                    "0 : Desactive\n"
                    "1 : Alarme uniquement (xx)\n"
                    "2 : Alarme + clavier"),
    ("AXIS_OFF", "fonctionnement degrade\n"
                 "- 0 : No Offline Mode\n"
                 "- 2 : Switch Protected - Validation First Transaction - No Cnx Retry\n"
                 "- 3 : Switch Protected - Validation All Transactions - No Cnx Retry\n"
                 "- 5 : Switch Not Protected - Validation First Transaction - No Cnx Retry\n"
                 "- 7 : Switch Not Protected - Validation All Transactions - No Cnx Retry\n"
                 "- 9 : Switch Protected - Validation First Transaction - Connection Retry\n"
                 "- B : Switch Protected - Validation All Transactions - Connection Retry\n"
                 "- D : Switch Not Protected - Validation First Transaction - Connection Retry\n"
                 "- F : Switch Not Protected - Validation All Transactions - Connection Retry"),
    ("AXIS_OFF_COUNTER", "Compteur tentative de bascule online à chaque transaction (AXIS_OFF = 9, B, D ou F)\n"
                         "Effectue une tentative toutes les n transactions\n"
                         "Valeur comprise entre 0 et 99 (0 ou 1 => Tentative a chaque transaction)"),
    ("TRNS_OFFLINE_COUNTER", "Nombre maximum de transactions offline à remonter sur Axis, hors V13.\n"
                             "Numerique de 0-999. Si non present ce parametre n'est pas envoye au terminal."),
    ("AUTOMATE", "0 : fonctionnement de c3 en mode normal (interactif)  (xx)\n"
                 "1 : fonctionnement de c3 en mode automate\n"
                 "4 : fonctionnement de c3 en mode automate avec refus de transaction en cas de demande de signature"),
    ("TRACE", "Trace Fichier dYYMMDD.log\n"
              "0 : pas de traces  (xx)\n"
              "1 : Erreurs fatales\n"
              "2 : Simples Erreurs\n"
              "3 : warnings\n"
              "4 : info\n"
              "5 : debug\n"
              "6 : debug les callbacks\n"
              "7 : debug les callbacks + polling getkey"),
    ("TRACE_PURGE", "-"),
    ("TRACE_OUTPUT_TYPE", "-"),
    ("TRACE_PATH", "-"),
    ("TRACE_MULTI_THREAD", ""),
    ("TRACE_CRYPT", "Generation des traces tronquees avec cryptage des traces\n"
                    "0 : Genere uniquement le fichier de traces tronquees (dAAMMJJ.log)\n"
                    "1 : Genere le fichier de traces tronquees (dAAMMJJ.log) et le fichier "
                    "de traces cryptees (dAAMMJJ_crypt.log) (xx)"),
    ("TIMEOUT_CARTE", "Timeout d\'insertion d\'une carte dans le lecteur (en secondes) par defaut 30 s"),
    ("REPOS_1", "Messages de repos: 1ere ligne"),
    ("REPOS_2", "Messages de repos: 2eme ligne"),
    ("MODE_PAIEMENT", "Mode de paiement = ERT. Supportee à partir de 2.2.2 et 2.1.13\n"
                      "- 10 : paiement de proximite (xx)\n"
                      "- 20 : Vente A Distance (VAD)\n"
                      "- 41 : automate de classe 1 ADM\n"
                      "- 42 : automate de classe 2.1 ADM\n"
                      "- 43 : automate de classe 2.2\n"
                      "- 45 : automate de classe 1 SST\n"
                      "- 46 : automate de classe 2.1 SST\n"
                      "- 48 : SST Parking\n"
                      "- 49 : LAT Classe 1\n"
                      "- 50 : LAT Classe 2.1\n"
                      "- 57 : Location\n"
                      "- 80 : PLBS "),
    ("COMPLEMENT_ERT", "Precision sur le mode de paiement pour automate. Supportee à partir de 2.2.2 et 2.1.13\n"
                       "- 0 : Standard (xx)\n"
                       "- 1 : MPAA (MPA Autoroute : MODE_PAIEMENT=48)\n"
                       "- 2 : MPAP (MPA Parking : MODE_PAIEMENT=48)"),
    ("TICKET_TNA", "Edition des tickets des transactions non abouties\n"
                   "- 0 : Pas de generation du ticket\n"
                   "- 1 : Generation du ticket  (xx)"),
    ("TICKET_TNA_OFF", "Impression du ticket TNA offline\n"
                       "- 0 : non (xx)\n"
                       "- 1 : oui"),
    ("CARTE_TEST", "Acceptation / refus des cartes de test\n"
                   "- 0 : Refuse\n"
                   "- 1 : Accepte (xx)"),
    ("PREFIX_TPV", "Prefixe du terminal pour le changement dynamique des nÝ TPV"),
    ("FFI_TYPE_SAISIE_OPTION", "Definit le type de selection pour les option de l'application FFI.\n"
                               " Format : 1 caractere numerique\n"
                               "- 0 : Saisie actuelle. (xx)\n"
                               "- 1 : Option par menu deroulant.\n"
                               "- 2 : Choix option client par commerçant. "),
    ("OPTION_C3_CTM", "Choix du defilement des options de paiement CETELEM par les fleches ou la touche COR\n"
                      "- 0 ou absent : defilement des options de paiement CTM par la touche COR (xx)\n"
                      "- 1 : defilement des options de paiement CTM par les fleches  "),
    ("C3API_VERSION", "Fonction appelee par l'outil fptpv/c3net.\n"
                      "- 2 : C3DRIVER    c3dll_v2 (c3dll + posconfirmation) (xx)\n"
                      "- 3 : C3DRIVER    c3dll_v3 (c3dll_v2 + generic function) "),
    ("CALLBACK_GET_SALES_CONFIRM", "0 : pas de callback, fonctionnement standard c3config (xx)\n"
                                   "1 : callback actif. "),
    ("TELIUM_TELECH_DIR", "Package utilise pour le chargement local"),
    ("TELIUM_TELECH_FTP", "Serveur telechargement FTP"),
    ("CHGT_CAL_AXIS", "Telechargement local declenche par Axis (ADM)\n"
                      "- 0 : Non\n"
                      "- 1 : Oui"),
    ("TMS_LOCK", "TMS call restriction shall be configurable as one or several time slots (ADM)"
                 " Should respect the following format : xxxx-yyyy where xxxx is the start time (hhmm)  and"
                 " yyyy the end time (hhmm)"),
    ("PLBS_MODE_GMM", "PLBS cloture de dossier à 115%\n"
                      "0 : la transaction est abandonnee. (xx)\n"
                      "1 : re-saisie le montant de cloture s'il depasse le montant d\'ouverture PLBS_MODE_GMM=1"),
    ("PLBS_NO_DIRECT_DEBIT", "Activation/Desactiver du paiement par la commande 'C' dans PLBS.\n"
                             "- 0 : Paiement par la commande 'C' active (xx).\n"
                             "- 1 : Paiement par la commande 'C' desactive"),
    ("PSD_DEACTIVATE_CTRL_LUHN", "Desactivation du contrôle de la cle de Luhn de l'application PSD (Prososie).\n"
                                 " Format : 1 caractere numerique\n"
                                 " - 0 : Controle de la cle de luhn. (xx)\n"
                                 " - 1 : Desactivation du contrôle de la cle de luhn. "),
    ("TRANSLATE_DTV_TO_IPS", "Traduction des commandes DTV en IPS.\n"
                             " Format : 1 caractere numerique\n"
                             " - 0 : Pas de traduction des commandes. (xx)\n"
                             " - 1 : Les commandes DTV sont traduites en IPS."),
    ("CHEQUE", "Type de configuration lecteur chèque\n"
               "- 00 0 : pas de lecteur cheque : le cheque est lu par l'encaissement\n"
               "- 10 1 : Crouzet ELC2000, Dassault 501 ou C2002 Connecte sur L3000 avec Impression\n"
               "- 20 1 : Dassault 502, Ingenico EDICHEC ou C2002 Connecte sur L3000 avec Impression\n"
               "- 22 1 : Ingenico EDICHEC ou C2002 Connecte sur L3000 avec Impression du montant en gras\n"
               "- 30 0 : CKD C1000 Connecte sur L3000 sans Impression\n"
               "- 60 0 : ELC930 Connecte en direct sur port USB\n"
               "- 70 0 : i2200 / C4000 Connecte en direct sur port COM ou USB (emulation port COM)\n"
               "- 80 0 : lecteur Elite 2x0 connecte en direct sur le port COM\n"
               "- 90 0 nameDLL nameReader : lecteur 'nameReader' fourni "
               "par integrateur connecte en direct sur le port COM/USB\n"
               "      dont les fonctions de base (readCheque/eject/...) dont le module nameDLL."),
    ("L10_CHQ", "Lecteur connecte en direct sur port com/usb"),
    ("TICKET_CHQ", "Impression du libelle imprime sur le cheque dans le ticket"),
    ("VERSION_CHEQUE", "Version cheque\n"
                       "- 0 : standard (xx)\n"
                       "- 1 : Profil A."),
    ("CHQ_FORMAT", "Format d\'impression du cheque\n"
                   "- 1 : Profil B\n"
                   "- 2 : Profil C - validation du message FNCI/garantisseur toujours demandee\n"
                   "- 3 : Profil D - Format cheque SFD\n"
                   "- 4 : Profil E - copie du format 2 avec possibilite de parametrer "
                   "la validation du message FNCI/Garantisseur\n"
                   "- 6 : Profil F - Format equivalent C3i avec la valeur 0\n"
                   "- autre : normal (xx)"),
    ("CHQ_VAL_FNCI_GAR", "Demande de validation du msg FNCI/Garantisseur\n"
                         "- 0 : pas de validation - msg affiche pendant 1 seconde (xx)\n"
                         "- 1 : validation demandee"
                         "- si CHQ_FORMAT=2, validation toujours demandee quelque soit la valeur ci-dessous"),
    ("MIGRATION_MERCURE_FID_ACE", "Gestion de la phase de migration PAN/ALGO/UID\n"
                                  "- 0 : Fonctionnement standard, remonte du PAN à la caisse dans le champ cPAN (xx).\n"
                                  "- 1 : Remonte du PAN/ALGO/UID à la caisse dans le champ cPAN.\n"
                                  "- 2 : Remonte du UID à la caisse dans le champ cPAN."),
    ("MIGRATION_MERCURE_FID_ACP", "Gestion de la phase de migration PAN/ALGO/UID\n"
                                  "- 0 : Fonctionnement standard, remonte du PAN à la caisse dans le champ cPAN (xx).\n"
                                  "- 1 : Remonte du PAN/ALGO/UID à la caisse dans le champ cPAN.\n"
                                  "- 2 : Remonte du UID à la caisse dans le champ cPAN."),
    ("FIV_TICKET_CLIENT", "Gestion de l'impression d\'un ticket client pour l'application FIVORY\n"
                          "- 0 : Pas d\'impression de ticket client (xx).\n"
                          "- 1 : Generation d\'un ticket client"),
    ("SUPPORT_MAPPING_FIVORY", "Mapping des commandes typ‚es FIVORY.\n"
                               "- 0 : Pas de traduction des commandes. (xx)\n"
                               "- 1 : Les commandes C, D, U types Fivory sont mappes "
                               "en ordre Z + valeur du cOperation.\n"
                               "- 2 : Toutes les commandes sont mapp‚es en dur en Z+P "
                               "=> pas de modification application Fivory"),
    ("CAISSE_ON_US", "Activation/desactivation du critère ON US par la caisse\n"
                     "- 0 ou absent : selection du TPV par AXIS (appel du message de referencement AXIS)(xx)\n"
                     "- 1 : selection par le numero de TPV envoye par la caisse\n"
                     "- 2 : Init et selection par le numero de TPV envoye par la caisse  "),
    ("PRINT_CONTACTLESS_INDICATOR_PLACEHOLDER", "0 : Don’t print a placeholder for the EMV "
                                                "contactless indicator.  (xx)\n"
                                                "1 : Add “@@logo_CTLS@@” in the receipt as a placeholder"
                                                " for the EMV contactless indicator.\n"
                                                "It is the ECR responsibility to replace this placeholder "
                                                "(if present) by the corresponding logo."),
    ("ICL_MODE", "Intelligent Callback Logic Mode\n"
                 "- 0 : Mode standard (xx)\n"
                 "- 1 : Mode avance (Gestion evoluee des Wait key)\n"
                 "- 2 : Mode avance + possibilite d\'avertir la caisse sur un point acceptant l'abandon "),
    ("READ_NUM_MAG", "Profil 'A': Prise en compte ou non du numero de magasin envoye par le systeme d\'encaissement\n"
                     "- 0 : Numero de magasin ignore (xx)\n"
                     "- 1 : Numero de magasin est pris en compte"),
    ("NUM_MAG", "Numero de magasin/commerçant à ajouter en tant que prefixe au numero du TPV # de 1 à 7 chiffres "),
    ("SECURITY_MSG", "Reponse à la fonction GetSecurity\n"
                     "- 0 : Fonction reponse caisse est getKey (xx)\n"
                     "- 1 : Fonction reponse caisse GetSecurity"),
    ("CASHIER_DISPLAY_NB_COLUMN", "nombre de colonnes de l’afficheur de la caisse\n"
                                  "- 24 : valeur par defaut (xx)\n"
                                  "- n :  valeur comprise entre 16 et 24"),
    ("RECEIPT_WIDTH", "largeur du ticket de caisse\n"
                      "- 24 : valeur par defaut (xx)\n"
                      "- n :  valeur comprise entre 24 et 80"),
    ("WAIT_REMOVE_CARD", "Attente du retrait de la carte à puce avant de rendre la main à l'encaissement\n"
                         "- 0 : retourne à l'encaissement même si la carte est encore dans le pinpad\n"
                         "- 1 : reste dans C3 tant que la carte n'est pas retiree du pinpad"),
    ("LNOIRE_C3", "Liste noire  lncba, lnace, lnasc, lnemv"),
    ("LNOIRE_C3_MODE", "-"),
    ("GENERIC_CALLBACK", "-"),
    ("MSG_INF_SUP_INF", "concatenation <> aux messages de confirmation\n"
                        "- 0 : Pas de concatenation (xx)\n"
                        "- 1 : concatenation <> aux messages"),
    ("CHECK_INSERT", "Parametrage du lancement de la transaction avec carte deja inseree\n"
                     "- 0  => lancement d’une transaction meme si la carte est presente avant paiement\n"
                     "- 1  => rejet d’une transaction si la carte est presente avant paiement "
                     "avec erreur (0311/2010) (xx)"),
    ("GSQT", "Parametrage de la fonction GetSecurity du C3 en QT\n"
             "- VALID    : pas de mot de passe\n"
             "- DEFAULT  : mot de passe = 4097\n"
             "- xxxxx    : valeur numerique utilisee pour le calcul du mot de passe "),
    ("SET_DATE_TIME", "Mise à l'heure\n"
                      "- 0= Pas de mise a l'heure"
                      "- 1= Mise à l'heure du terminal par le système d\'encaissement lors de l'init(xx)\n"
                      "- 2= Mise à l'heure du système d\'encaissement par le terminal lors de l'init (WinNT/WinCE)"),
    ("P9_DISPLAY_DELAY", "Prise en compte ou non des temporisations dans les demandes\n"
                         "- d\'affichage du TPE selon le parametre fourni dans la fonction 03\n"
                         "- 0 : Temporisation non prise en compte\n "
                         "- 1 : Temporisation prise en compte (xx)"),
    ("P9_IDLE_AFTER_F05", "Retour a l'ecran de repos apres une saisie/affichage sur le terminal (fonction 05)\n"
                          "- 0 : Pas de retour a l'ecran de repos pour enchainer plusieurs saisies (xx)\n"
                          "- 1 : Retour a l'ecran de repos"),
    ("P9_PROTOCOL_TYPE", "Configuration du type de protocole 9\n"
                         "- 0 : simplifie sans sequences ENQ-ACK-EOT (xx)\n"
                         "- 1 : standard avec sequences ENQ-ACK-EOT"),
    ("TIMEOUT_P9_INTER_FRAME", "Timeout d\'attente exprime en millisencodes intertrame en protocole 9."
                               " 2000 millisencodes par defaut."),
    ("CODE_LANGUE", "Code langue. Si absent le terminal utilise sa langue par defaut, "
                    "le C3driver utilise le français."),
    ("CODE_LCID", "cs : Tcheque    : CODE_LCID=5\n"
                  "en : English    : CODE_LCID=9\n"
                  "es : Spanish    : CODE_LCID=10\n"
                  "fr : Français   : CODE_LCID=12  (xx)\n"
                  "it : Italian    : CODE_LCID=16\n"
                  "nl : Nederlands : CODE_LCID=19\n"
                  "pt : Portuguese : CODE_LCID=22\n"
                  "sv : Swedish    : CODE_LCID=29\n"
                  "de : German     : CODE_LCID=7"),
    ("FORMAT_DATE", "Format Date. Si absent format defini dans le terminal\n"
                    "# 0 : Format Francais JJ/MM/AAAA\n"
                    "# 1 : Format Francais AAAA/MM/JJ"),
    ("CALLBACK_INDICATION_CONFIRM", "Callback de confirmation d\'enregistrement de transaction.\n"
                                    "# 0 : pas de callback, callback desactivee.\n"
                                    "# 1 : callback active, fonctionnement par defaut (xx)"),
    ("CALLBACK_PRINT_SUPPORT", "Suport Callback d\'impression de ticket en C3NET\n"
                               "# 0 : pas de callback, Compatibilte ascendante (xx)\n"
                               "# 1 : callback active."),
    ("EXTENDED_C3API_SUPPORT", "Suport Nouvelle interface C3API MsgIn/MsgOut\n"
                               "# 0 : pas de support, Compatibilte ascendante (xx)\n"
                               "# 1 : support actif, necessite modification des Systèmes d\'encaissement"),
    ("ADM_INFO_FIRMWARE", "Informations etat firmwre remontees  à AXIS par l'ADM lors de l'init\n"
                          "# 0 : Informations standards, Compatibilte ascendante\n"
                          "# 1 : Informations etendues (xx)"),
    ("SAIS_NCB_MENS_CAIS", "Pour recuperer les nombre d\'echeance à partir du système d\'encaissement\n"
                           "# 0 : non (xx)\n"
                           "# 1 : oui"),
    ("C3NET_NOGETKEYINIT", "En C3driver_net à partir de 2.1.2 la valeur par defaut est 0 et non pas 1\n"
                           "# contrairement au C3i et versions anterieures du C3driver_net.\n"
                           "# 0 : Consulte le resultat de getkey() pendant l'init\n"
                           "# 1 : Ne consulte pas le resultat de getkey() pendant l'init "),
    ("PRINT_ID_TRS", "Impression Identifiant de transaction sur le ticket \n"
                     "# 0 : le cUserData n'est pas interpretee  (xx)\n"
                     "# 1 : le cUserData contient l'identifiant de transaction à imprimer sur le ticket  "),
    ("SECURE_OP_BY_MERCHANT_CARD", "Securiser les operations d\'annulation et du credit, ... par la carte commerçant\n"
                                   "# à partir de 2.2.2 et 2.1.13\n"
                                   "# 0 : Fonctionnement standard (xx)\n"
                                   "# 1 : les operations d\'annulation et du credit, ... "
                                   "sont securisees par la carte commerçant "),
    ("TYPE_LINK_IP", "Ce paramètre defini le type de liaison IP à utiliser pour le dialogue AXIS.\n"
                     "# Il est transmis à l'initialisation. Supporte à partir de 2.2.5.\n"
                     "# Remarque : Afin de ne pas modifier la config courante du terminal, un '?'\n"
                     "# est transmis si ce paramètre est absent\n"
                     "# 0 : IP natif terminal\n"
                     "# 1 : IP du point encaissement "),
    ("REPEAT_F06", "Repetition de la fonction 06 en debut de transaction\n"
                   "# 0 : La fonction 06 n’est pas répétée en cas d’erreur.\n"
                   "# 1 : La fonction 06 est répétée en cas d’erreur (xx)."),
    ("C3_APPAIRAGE_ON", "Activer ou désactiver l'appairage entre le C3Driver et le terminal.\n"
                        "# 0 ou absent: pas d\'appairage (aucune vérification) (xx)\n"
                        "# 1 : Appairage activé (vérification du fichier C3SECURE)\n"
                        "# 2 : Appairage activé en mode multi-thread (vérification du fichier c3CtxGen.tttttttt)"),
    ("C3_APPAIRAGE_MSG_1", "Message d\'alerte (sur 2 lignes) à afficher sur la caisse en cas de changement de terminal"),
    ("C3_APPAIRAGE_MSG_2", "Message d\'alerte (sur 2 lignes) à afficher sur la caisse en cas de changement de terminal"),
    ("DELAI_KEEPALIVE", "Activation mécanisme keepalive, uniquement si le paramètre est présent."
                        "Le délai entre 2 envois de message est de X secondes."),
    ("TYPE_LECT", "Reconfigurer les types de lecture acceptés\n"
                  "# 0 : Lecture puce + piste + sans contact (xx)\n"
                  "# 1 : Lecture puce uniquement\n"
                  "# 2 : Lecture puce + piste uniquement\n"
                  "# 3 : Lecture puce + sans contact uniquement "),
    ("C3I_COMPATIBILITY", "Gestion de certaines compatibilté avec le C3i Générique\n"
                          "# 0 : Compatibilité Standard (xx)\n"
                          "# 1:  Compatibilté pour borne ACRELEC"),
    ("AUTO_PARTIELLE", "Gestion autorisation partielle\n"
                       "# 0 ou absent: Auto partielle désactivée (xx)\n"
                       "# 1 : Auto partielle activée"),
    ("RECEIPT_ENDLINE", "Caractères ajoutés au ticket pour chaque fin de ligne (config Windows C3Net uniquement)\n"
                        "# CR_LF : Chaque fin de ligne contient CR LF\n"
                        "# Non present ou autre valeur, chaque fin de ligne contient LF (xx)."),
    ("PRINT_PAYMENT_ID", "Impression PaymentID sur le ticket commerçant\n"
                         "# 0 : Pas d\'impression du PaymentID sur le ticket commerçant (xx)"
                         "# 1 : Impression du PaymentID sur le ticket commerçant  "),
    ("PCL_STARTBEFORE", "Démarrage du service PCL\n"
                        "# 0 : Ne pas démarrer le service PCL (xx)\n"
                        "# 1:  Démarrer le service à chaque commande C3API"),
    ("PCL_STOPAFTER", "Arrêt du service PCL. Pris en compte uniquement si PCL_STARTBEFORE=1\n"
                      "# 0 : Ne pas arrêter le service PCL (xx)\n"
                      "# 1:  Arrêter le service à chaque commande C3API"),
    ("PCL_COM", "Type du media PCL (RS232, USB, BLUETOOTH) + adresse physique du terminal. "
                "Pris en compte uniquement si PCL_STARTBEFORE=1"),
    ("TMS_AGENT_SLEEP_TIME", "Le timeout de reconnexion au TMSA entre les deux appels exprimés "
                             "en secondes(valeurs possibles de 10 à 400). valeur par défaut 100s\n"
                             "# C3Driver must pool the terminal for a long time (400 sec) "
                             "waiting for the reboot to finish\n"
                             "#	Starting from 10 seconds, « Waiting for Terminal to respond » "
                             "is displayed to the cashier\n"
                             "# At the end of the long time, an error message is displayed"),
    ("TMS_AGENT_REBOOT_TIME", "temps d\'attente, en secondes, avant le reboot du terminal. "
                              "Lorsque cette valeur est à -1, le paramètre est désactivé.\n"
                              "# Dans ce cas le sleep_time est utilisé comme temporisation après chaque reboot. "),
    ("TMS_AGENT_TRACE_LEVEL", "Niveau de trace de TMS Agent, valeur entre 0 et 6. Valeur par défaut est 6. "
                              "# NONE = 0, FATAL = 1, CRITICAL = 2, ERROR = 3, WARNING = 4, "
                              "NOTICE = 5, INFO = 6, DEBUG = 7, TRACE = 8,"),
    ("SCREENSAVER", "Gestion affichage Idle screen sur le terminal\n"
                    "#0 : Activer l\'affichage de l\'idle screen (xx)\n"
                    "#1 : Désactiver l\'affichage de l\'idle screen"),
    ("IDLE_BACKLIGHT", "Gestion backlight  sur l’écran du terminal en mode repos\n"
                       "#0 : Désactiver le backlight\n"
                       "#1 : Activer le backlight (xx) "),
    ("AUTOTEST", "Activation / désactivation du mode autotest\n"
                 "# 0 : Seule la V04 est interprétée comme commande AUTOTEST (Fonctionnement Standard) (xx)\n"
                 "# 1 : Toutes commandes émanant de la caisse est est interprétée comme commande AUTOTEST"),
]
catalog_list = [
    ".M30", ".M31", ".M32", ".M33", ".M34", ".M35", ".M36", ".M37", ".M38", ".M39",
    ".M40", ".M41", ".M42", ".M43", ".M44", ".M45", ".M46", ".M47", ".M48", ".M49",
    ".M50", ".M51", ".M52", ".M53", ".M54", ".M55", ".M56", ".M57", ".M58", ".M59",
    ".M60", ".M61", ".M62", ".M63", ".M64", ".M65", ".M66", ".M67", ".M68", ".M69",
    ".M70", ".M71", ".M72", ".M73", ".M74", ".M75", ".M76", ".M77", ".M78", ".M79",
]
dict_terminal_NameFromMxx = {
    "M30": "EFT30",
    "M31": "EFT930",
    "M32": "TWIN30",
    "M34": "CAD30 UCM",
    "M36": "ML30",
    "M37": "SMART2",
    "M38": "CAD30 UCR",
    "M39": "EFT930_BL2",

    "M40": "iCT2XX",
    "M41": "iPA280",
    "M42": "iMP3XX",
    "M43": "iSC350",
    "M44": "iWL2XX",
    "M45": "iSC250",
    "M46": "iPP3XX",
    "M47": "iST1XX",
    "M48": "iWL280",
    "M49": "iUP2XX",

    "M50": "iUC1XX",
    "M51": "iWL350",
    "M52": "iPP4XX",
    "M53": "iSC480",
    "M54": "iWB2XX",
    "M55": "iUC180B",

    "M63": "iPP3XX v4",
    "M64": "iWB2XX",
    "M65": "iUC180B",
    "M67": "IUP 250",

    "M70": "DESK 5000",
    "M71": "MOVE 5000",
    "M72": "LANE 5000",

    "M78": "LINK 2500",
}
# dico fichier de conf .PAS
dict_param_file = {
    "UCMI000b.PAS" : "iUP250 No Device",
    "UCMJ001b.PAS" : "iUC180 No Device",
    "UCMIZ61e.PAS" : "iUP250+iUR250+SAMS+NOEP",
    "UCMIZ61e.PAS" : "CAD30 UPT-C + CAD30 UCRM123 + SAMS + CAD30 UPP + NO EP",
    "ADS.PAR"      : "ADS Parameter file",
    "MANAGER.PAR"  : "Manager parameter file",
    "C3CONFIGT"    : "c3Config embedded file",
}


"""
Fuction to check whether a filename matches a component.
@:param comp_num: the cimponent or filename to check into dictionary
@:return a dict corresponding of:
    - le matching component
    - the unknown component if no matching component found
"""
def app_component_present(comp_num):
    for component in application_components:
        if comp_num.startswith(component[0]):
            return component
    return unknown_component


def sys_component_present(comp_num):
    for component in system_components:
        if comp_num.startswith(component[0]):
            # if len(component[0]) == 0:
            #     print comp_num
            return component
    return unknown_component


def man_component_present(comp_num):
    for component in manager_components:
        if comp_num.startswith(component[0]):
            return component
    return unknown_component


def get_sdk_version(sys_version, man_version):
    for (sys_pack, man_pack, sdk_pack) in sdk_versions:
        if sys_pack == sys_version and man_pack == man_version:
            return sdk_pack
    return "XX.YY.TT"


def get_t3_sdk_version(file_name):
    return file_name[10:16]


def check_system_pack(cpn_name):
    return cpn_name in system_pack


def check_manager_pack(cpn_name):
    return cpn_name == manager_pack
