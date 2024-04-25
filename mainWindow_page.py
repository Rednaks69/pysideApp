


import os
from datetime import datetime, date,time
from PySide6 import QtCore
from PySide6.QtGui import QScreen, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from ui_mainAppWindow import Ui_MainWindow
from dbPopulate import db
from PySide6.QtCore import Qt

# personel
class MainWindow_page(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SocialKeeper")
        self.init()
        # print(self.log)
        MyScn = QScreen
        self.setGeometry(0, 0, MyScn.availableGeometry(QApplication.primaryScreen()).width(), MyScn.availableGeometry(QApplication.primaryScreen()).height()) 


#| ALL buttons
        #? main_menu events
        self.menu_btn.clicked.connect(self.menuToggle_1)
        self.menu_btn_2.clicked.connect(self.menuToggle_2)
        self.home_btn.clicked.connect(self.toggleHomePage)

        self.new_btn.clicked.connect(self.toggleNewPage)
        self.data_btn.clicked.connect(self.toggleDataPage)
        self.autre_btn.clicked.connect(self.toggleAutrePage)
        
        #? main_menu events slim
        self.home_btn_2.clicked.connect(self.toggleHomePage)
        self.new_btn_2.clicked.connect(self.toggleNewPage)
        self.data_btn_2.clicked.connect(self.toggleDataPage)
        self.autre_btn_2.clicked.connect(self.toggleAutrePage)

        #? subMenu event
        self.nvDossier_EXT_btn.clicked.connect(self.nvDossier_ProdEXT_page)
        self.nvDossier_IVW_btn.clicked.connect(self.nvDossier_ProdINW_page)
        self.nvDossier_IVD_btn.clicked.connect(self.nvDossier_ProdIVD_page)
        self.nvDossier_Digital_btn.clicked.connect(self.nvDossier_digital_page)
        self.nvDossier_Autre_btn.clicked.connect(self.nvDossier_autre_page)

        self.nvEquipement_btn.clicked.connect(self.nvEquipement_page)
        self.nvPersonne_btn.clicked.connect(self.nvPersonne_page)
        self.nvFournisseur_btn.clicked.connect(self.nvFournisseur_page)
        self.nvClient_btn.clicked.connect(self.nvClient_page)

        self.mission_btn.clicked.connect(self.nvMission_page)
        self.bC_btn.clicked.connect(self.nvBC_page)
        self.devis_btn.clicked.connect(self.nvDevis_page)



        self.pushButton_2.clicked.connect(self.close_subMenu)
        self.pushButton_31.clicked.connect(self.close_subMenu)
        self.pushButton_3.clicked.connect(self.close_subMenu)

        #* Fournisseur
        # next_fournisseur_persoData 
        self.pushButton_156.clicked.connect(self.next_fournisseur_persoData)
        # 
        self.pushButton_158.clicked.connect(self.next_fournisseur_bancData)
        # submitFournisseur 
        self.pushButton_180.clicked.connect(self.submitFournisseur)
        
        #* Cleints
        # next_Client_persoData 
        self.pushButton_168.clicked.connect(self.next_Client_persoData)
        # next_Client_bancData
        self.pushButton_166.clicked.connect(self.next_Client_bancData)
        # submitClient 
        self.pushButton_184.clicked.connect(self.submitClient)
        
        #* Personel
        # next_personne_persoData 
        self.pushButton_149.clicked.connect(self.next_personne_persoData)
        # next_personne_detailsPost
        self.pushButton_151.clicked.connect(self.next_personne_detailsPost)
        # dateValidation
        self.pushButton_144.clicked.connect(self.next_personne_dateValidation)
        # submitpersonne 
        self.pushButton_161.clicked.connect(self.submitpersonne)

        #* Equipement 
        self.pushButton_159.clicked.connect(self.calculate_equipement_emprient_cout_total)
        # next_equipement_persoData 
        self.pushButton_152.clicked.connect(self.next_equipement_Data)
        # next_equipement_bancData
        self.pushButton_154.clicked.connect(self.next_equipement_status)
        # submitequipement 
        self.pushButton_199.clicked.connect(self.submitequipement)
        # * Bandes de Commandes 
        # bc date
        self.pushButton_258.clicked.connect(self.next_BC_Date)
        self.pushButton_279.clicked.connect(self.create_bandeDeCommande)
        self.pushButton_275.clicked.connect(self.validate_Bcommande)
        self.pushButton_274.clicked.connect(self.annuller_Bcommande)
        #* COMMANDE
        self.pushButton_272.clicked.connect(self.add_commande)
        self.pushButton_271.clicked.connect(self.remove_commande)
        self.pushButton_263.clicked.connect(self.refresh_commande)
        self.pushButton_262.clicked.connect(self.next_commande_data)
        
        #* DEVIS_container
        self.pushButton_266.clicked.connect(self.next_devis_container_date)
        self.pushButton_282.clicked.connect(self.create_devis_container)
        self.pushButton_286.clicked.connect(self.validate_DEVIS_container)
        self.pushButton_285.clicked.connect(self.annuller_DEVIS_container)
        #* DEVIS
        self.pushButton_283.clicked.connect(self.add_DEVIS)
        self.pushButton_284.clicked.connect(self.remove_DEVIS)
        self.pushButton_267.clicked.connect(self.refresh_DEVIS)
        self.pushButton_268.clicked.connect(self.next_DEVIS_data)


        #* NV_DOSSIER
        # * PROD_EXT
        self.pushButton_41.clicked.connect(self.date_prod_ext_validation)
        self.pushButton_43.clicked.connect(self.nature_prod_ext_validation)
        self.pushButton_35.clicked.connect(self.addPersonel_prod_ext)
        self.pushButton_36.clicked.connect(self.removePersonel_prod_ext)
        self.pushButton_44.clicked.connect(self.personel_prod_ext_validation)
        self.pushButton_56.clicked.connect(self.addEquipement_prod_ext)
        self.pushButton_57.clicked.connect(self.removeEquipement_prod_ext)
        self.pushButton_62.clicked.connect(self.equipement_prod_ext_validation)
        self.pushButton_63.clicked.connect(self.charge_TTC_prod_ext_calculation)
        self.pushButton_59.clicked.connect(self.charge_prod_ext_validation)
        self.pushButton_66.clicked.connect(self.facturation_TTC_prod_ext_calculation)
        self.pushButton_61.clicked.connect(self.facturation_prod_ext_validation)
        self.pushButton_67.clicked.connect(self.marge_prod_ext_calculation)
        self.pushButton_53.clicked.connect(self.nv_dossier_prod_ext_validation)
        self.pushButton_51.clicked.connect(self.nv_dossier_prod_ext_annulation)
        # # * PROD_INW
        self.pushButton_68.clicked.connect(self.date_prod_INW_validation)
        self.pushButton_162.clicked.connect(self.nature_prod_INW_validation)
        self.pushButton_72.clicked.connect(self.addPersonel_prod_INW)
        self.pushButton_73.clicked.connect(self.removePersonel_prod_INW)
        self.pushButton_70.clicked.connect(self.personel_prod_INW_validation)
        self.pushButton_75.clicked.connect(self.addEquipement_prod_INW)
        self.pushButton_76.clicked.connect(self.removeEquipement_prod_INW)
        self.pushButton_163.clicked.connect(self.equipement_prod_INW_validation)
        # self.pushButton_63.clicked.connect(self.charge_TTC_prod_INW_calculation)
        self.pushButton_78.clicked.connect(self.charge_prod_INW_validation)
        # self.pushButton_66.clicked.connect(self.facturation_TTC_prod_INW_calculation)
        self.pushButton_82.clicked.connect(self.facturation_prod_INW_validation)
        # self.pushButton_67.clicked.connect(self.marge_prod_INW_calculation)
        self.pushButton_85.clicked.connect(self.nv_dossier_prod_INW_validation)
        self.pushButton_84.clicked.connect(self.nv_dossier_prod_INW_annulation)

    

# | Fin all Buttons


        
#|initialisation all components
    def init(self):
        self.main_sideBar_container_2.setVisible(False)
        
        self.subMenu_container.setVisible(False)
        self.stackedWidget.setCurrentIndex(0)
        self.home_btn.setChecked(True)
        self.home_btn_2.setChecked(True)
        self.label_10.setText("Admin   ")
        self.widget_3.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget_6.setVisible(False)
        self.widget_7.setVisible(False)
        self.widget_8.setVisible(False)
        self.widget_2.setVisible(False)
        self.widget_4.setVisible(False)
        self.widget_29.setVisible(False)
        self.widget_13.setVisible(False)
        self.widget_60.setVisible(False)
        self.widget_61.setVisible(False)
        self.widget_748.setVisible(False)
        self.widget_730.setVisible(False)
        self.widget_716.setVisible(False)
        self.widget_388.setVisible(False)
        self.widget_398.setVisible(False)
        self.widget_304.setVisible(False)
        self.widget_286.setVisible(False)
        self.widget_272.setVisible(False)
        self.widget_263.setVisible(False)
        self.widget_256.setVisible(False)
        self.widget_250.setVisible(False)
        self.widget_46.setVisible(False)
        self.widget_33.setVisible(False)
        self.widget_63.setVisible(False)
        self.widget_73.setVisible(False)
        self.widget_73.setVisible(False)
        self.widget_30.setVisible(False)
        self.widget_48.setVisible(False)
        self.widget_102.setVisible(False)
        self.widget_108.setVisible(False)
        self.widget_115.setVisible(False)
        self.widget_115.setVisible(False)
        self.widget_124.setVisible(False)
        self.widget_124.setVisible(False)
        self.widget_138.setVisible(False)
        self.widget_156.setVisible(False)
        self.widget_176.setVisible(False)
        self.widget_182.setVisible(False)
        self.widget_189.setVisible(False)
        self.widget_198.setVisible(False)
        self.widget_198.setVisible(False)
        self.widget_212.setVisible(False)
        self.widget_230.setVisible(False)
        self.widget_324.setVisible(False)
        self.widget_330.setVisible(False)
        self.widget_337.setVisible(False)
        self.widget_346.setVisible(False)
        self.widget_360.setVisible(False)
        self.widget_378.setVisible(False)
        self.widget_360.setVisible(False)
        self.widget_835.setVisible(False)
        self.widget_838.setVisible(False)

        self.widget_243.setVisible(False)
        self.widget_246.setVisible(False)
        self.widget_481.setVisible(False)
        self.widget_38.setVisible(False)
        self.widget_43.setVisible(False)
        self.widget_95.setVisible(False)
        self.widget_98.setVisible(False)
        self.widget_169.setVisible(False)
        self.widget_172.setVisible(False)
        self.widget_317.setVisible(False)
        self.widget_320.setVisible(False)
        self.widget_687.setVisible(False)
        self.widget_690.setVisible(False)
        self.widget_454.setVisible(False)
        self.widget_451.setVisible(False)
        self.widget_391.setVisible(False)
        self.widget_393.setVisible(False)

        
#|initialisation labels (msg erreurs)
# ////////////////////////////////////////////////////
        # fournisseur 
        self.widget_warning_9.setVisible(False) # fournisseur donnees (error)
        self.widget_warning_10.setVisible(False) # fournisseur donnees (error)
        self.widget_502.setVisible(False) # fournisseur info banque (error)

        # clients
        self.widget_warning_11.setVisible(False) # clients donnees (error)
        self.widget_warning_12.setVisible(False) # clients donnees (error)
        self.widget_472.setVisible(False) # clients info banque (error)
        # mission
        # self.label_238.setVisible(False)
        # Personel
        self.widget_warning_6.setVisible(False) # perso donnees
        self.widget_post.setVisible(False) # perso details_donnees
        self.widget_warning_7.setVisible(False) # perso details_donnees (error)
        self.widget_warning_8.setVisible(False) # perso details_donnees_date (error)
        # equipement
        self.widget_442.setVisible(False)
        self.widget_warning_4.setVisible(False) # equipement donnees (error)
        self.widget_warning_5.setVisible(False) # equipement status (error)

        # bande de commandes
        self.label_286.setVisible(False)
        self.label_170.setVisible(False)
        self.label_291.setVisible(False)
        self.label_171.setVisible(False)
        self.widget_warning.setVisible(False)
        self.widget_483.setVisible(False)
        self.widget_878.setVisible(False)
        self.label_167.setVisible(False)
        self.label_168.setVisible(False)
        # Devis
        self.widget_warning_3.setVisible(False)
        self.widget_862.setVisible(False)
        self.widget_859.setVisible(False)
        self.widget_490.setVisible(False)
        self.widget_906.setVisible(False)
        self.label_294.setVisible(False)
        self.label_205.setVisible(False)
        self.label_295.setVisible(False)
        self.label_211.setVisible(False)
        self.label_210.setVisible(False)
        self.label_209.setVisible(False)
        # NV_DOSSIER
        # PROD_EXT
        self.widget_warning_14.setVisible(False) #  (error) date
        self.widget_warning_15.setVisible(False) #  (error) nature
        self.widget_warning_13.setVisible(False) #  (error) personelles
        self.widget_warning_18.setVisible(False) #  (error) equipement
        self.widget_warning_16.setVisible(False) #  (error) charge
        self.widget_warning_17.setVisible(False) #  (error) facturation
        # PROD_IVW
        self.widget_warning_19.setVisible(False) #  (error) date
        self.widget_warning_20.setVisible(False) #  (error) nature
        self.widget_warning_21.setVisible(False) #  (error) personelles
        self.widget_warning_22.setVisible(False) #  (error) equipement
        self.widget_warning_23.setVisible(False) #  (error) charge
        self.widget_warning_24.setVisible(False) #  (error) facturation




#//////////////////////////////////////////////////// 
# | initialisation tableaux
        # bande de Commande (commandes table)
        # self.refresh_commande()
        self.tableWidget_commande.setColumnWidth(0,40)
        self.tableWidget_commande.setColumnWidth(1,80)
        self.tableWidget_commande.setColumnWidth(2,80)
        self.tableWidget_commande.setColumnWidth(3,80)
        self.tableWidget_commande.setColumnWidth(4,80)
        self.tableWidget_commande.setColumnWidth(5,220)
        # devis (devis table)
        self.tableWidget_commande_3.setColumnWidth(0,40)
        self.tableWidget_commande_3.setColumnWidth(1,80)
        self.tableWidget_commande_3.setColumnWidth(2,80)
        self.tableWidget_commande_3.setColumnWidth(3,80)
        self.tableWidget_commande_3.setColumnWidth(4,80)
        self.tableWidget_commande_3.setColumnWidth(5,220)

# | warnings functions declarations 

    def valiate_warning(self,widget_name, label_name_1, label_name_2):
        current_directory = os.getcwd()
        new_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'valid-30.png')
        if not os.path.exists(new_msg_icon_path):
            print("Error: Image file does not exist:", new_msg_icon_path)

        new_msg_icon = QPixmap(new_msg_icon_path)
        if new_msg_icon.isNull():
            print("Error: Failed to load image:", new_msg_icon_path)
        
        widget_name.setVisible(True)        
        label_name_1.setVisible(True)
        label_name_1.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
        label_name_2.setText("ok !")
        label_name_2.setVisible(True)
        label_name_2.setStyleSheet("color:green")

    def erreur_warning(self,widget_name, label_name_1, label_name_2):
        current_directory = os.getcwd()
        error_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'warning-30.png')

        if not os.path.exists(error_msg_icon_path):
            print("Error: Image file does not exist:", error_msg_icon_path)

        new_msg_icon = QPixmap(error_msg_icon_path)
        
        if new_msg_icon.isNull():
            print("Error: Failed to load image:", error_msg_icon_path)

        widget_name.setVisible(True)
        label_name_1.setVisible(True)
        label_name_1.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
        label_name_2.setText("error !")
        label_name_2.setVisible(True)
        label_name_2.setStyleSheet("color:red")

# | initialisation des comboBox 
    def addToComboBox(self, name, id):
        pass



        
#| navigation
    # menu
    def menuToggle_1(self):
        self.main_sideBar_container_2.setVisible(True)
        self.main_sideBar_container.setVisible(False)

    def menuToggle_2(self):
        self.main_sideBar_container.setVisible(True)
        self.main_sideBar_container_2.setVisible(False)

    # submenu
    def toggleHomePage(self):
        self.subMenu_container.setVisible(False)
        self.stackedWidget.setCurrentIndex(0)
    def toggleNewPage(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(0)
    def toggleDataPage(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(1)
    def toggleAutrePage(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(2)
    def close_subMenu(self):
        self.subMenu_container.setVisible(False)

    
    # nouveau -> dossier 
    def nvDossier_ProdEXT_page(self):
        self.stackedWidget.setCurrentIndex(1)
    # id
        max_id_query ="""SELECT MAX(id) FROM nv_dossier_prod_ext"""
        myCursor = db.cursor(buffered=True)
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        self.label_13.setText("{}".format(max_id+1))

    # personel
        allStuff_query = "SELECT nom,prenom FROM stuff"

        myCursor.execute(allStuff_query)
        allStuff_table = myCursor.fetchall()
        print(allStuff_table)
        for stuff in allStuff_table:
            nom , prenom = stuff
            stuff_name = f"{nom} {prenom}"
            self.comboBox_personel.addItem(stuff_name)
    
    # equipement
        allEquipement_query = "SELECT nomEquipement FROM equipement"
        myCursor.execute(allEquipement_query)
        allEquipement_table = myCursor.fetchall()
        for equipement in allEquipement_table:
            nomEquipement = ''.join(equipement)
            # equipement_name = f"{nomEquipement}"
            self.comboBox_6.addItem(nomEquipement)
        # self.comboBox_2.addItems(allEquipement_table)
    
    # charge
        # id
        extract_charge_id_query= "SELECT charge_id FROM charge order by created DESC"
        myCursor.execute(extract_charge_id_query)
        charge_id= myCursor.fetchone()[0]
        self.label_15.setText("{}".format(charge_id+1))
        # fournisseur
        allFournisseur_query = "SELECT nom,prenom FROM fournisseur"
        myCursor.execute(allFournisseur_query)
        allfournisseur_table = myCursor.fetchall()
        # print(allfournisseur_table)
        for fournisseur in allfournisseur_table:
            nom , prenom = fournisseur
            fournisseur_name = f"{nom} {prenom}"
            self.comboBox_5.addItem(fournisseur_name)
    
    # facturation 
        # clients
        allClient_query = "SELECT nom,prenom FROM clients"
        myCursor.execute(allClient_query)
        allClient_table = myCursor.fetchall()
        # print(allClient_table)
        for Client in allClient_table:
            nom , prenom = Client
            Client_name = f"{nom} {prenom}"
            self.comboBox_8.addItem(Client_name)


    
    def nvDossier_ProdINW_page(self):
        self.stackedWidget.setCurrentIndex(2)
    # id
        max_id_query ="""SELECT MAX(id) FROM nv_dossier_prod_inw"""
        myCursor = db.cursor(buffered=True)
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        self.label_35.setText("{}".format(max_id+1))

    # personel
        allStuff_query = "SELECT nom,prenom FROM stuff"

        myCursor.execute(allStuff_query)
        allStuff_table = myCursor.fetchall()
        print(allStuff_table)
        for stuff in allStuff_table:
            nom , prenom = stuff
            stuff_name = f"{nom} {prenom}"
            self.comboBox_4.addItem(stuff_name)
    
    # equipement
        allEquipement_query = "SELECT nomEquipement FROM equipement"
        myCursor.execute(allEquipement_query)
        allEquipement_table = myCursor.fetchall()
        for equipement in allEquipement_table:
            nomEquipement = ''.join(equipement)
            # equipement_name = f"{nomEquipement}"
            self.comboBox_7.addItem(nomEquipement)
        # self.comboBox_2.addItems(allEquipement_table)
    
    # charge
        # id
        extract_charge_id_query= "SELECT charge_id FROM charge order by created DESC"
        myCursor.execute(extract_charge_id_query)
        charge_id= myCursor.fetchone()[0]
        # self.label_15.setText("{}".format(charge_id+1))
        # fournisseur
        allFournisseur_query = "SELECT nom,prenom FROM fournisseur"
        myCursor.execute(allFournisseur_query)
        allfournisseur_table = myCursor.fetchall()
        # print(allfournisseur_table)
        for fournisseur in allfournisseur_table:
            nom , prenom = fournisseur
            fournisseur_name = f"{nom} {prenom}"
            self.comboBox_9.addItem(fournisseur_name)
    
    # facturation 
        # clients
        allClient_query = "SELECT nom,prenom FROM clients"
        myCursor.execute(allClient_query)
        allClient_table = myCursor.fetchall()
        # print(allClient_table)
        for Client in allClient_table:
            nom , prenom = Client
            Client_name = f"{nom} {prenom}"
            self.comboBox_10.addItem(Client_name)

    def exit_nvDossier_ProdINW_page(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def nvDossier_ProdIVD_page(self):
        self.stackedWidget.setCurrentIndex(3)
    def exit_nvDossier_ProdIVD_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def nvDossier_digital_page(self):
        self.stackedWidget.setCurrentIndex(4)
    def exit_nvDossier_digital_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def nvDossier_autre_page(self):
        self.stackedWidget.setCurrentIndex(12)
    def exit_nvDossier_autre_page(self):
        self.stackedWidget.setCurrentIndex(0)

    # donnes
        # equipement
    def nvEquipement_page(self):
        self.stackedWidget.setCurrentIndex(6)

        max_id_query ="""SELECT MAX(id) FROM equipement"""
        myCursor = db.cursor()
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        self.label_257.setText("{}".format(max_id+1))
    
        # Personne 
    def nvPersonne_page(self):
        self.stackedWidget.setCurrentIndex(7)
    
        # Fournisseur
    def nvFournisseur_page(self):
        self.stackedWidget.setCurrentIndex(8)

        max_id_query ="""SELECT MAX(id) FROM Fournisseur"""
        myCursor = db.cursor()
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        self.label_271.setText("{}".format(max_id+1))

    def nvClient_page(self):
        self.stackedWidget.setCurrentIndex(9)

        max_id_query ="""SELECT MAX(id) FROM clients"""
        myCursor = db.cursor()
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        self.label_278.setText("{}".format(max_id+1))

    
    # Autre
    def nvMission_page(self):
        self.stackedWidget.setCurrentIndex(5)
    
    def nvBC_page(self):
        self.stackedWidget.setCurrentIndex(10)
    def nvDevis_page(self):
        self.stackedWidget.setCurrentIndex(11)
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#|nv Fournisseur
# next_fournisseur_persoData
    def next_fournisseur_persoData(self):
        last_name=self.lineEdit_74.text()
        first_name=self.lineEdit_87.text()
        adress=self.lineEdit_88.text()
        id_fiscal=self.lineEdit_89.text()
        
        if last_name == '' or first_name == '' or adress == '' or id_fiscal == '':
            # error
            self.erreur_warning(self.widget_warning_9,self.label_225,self.label_309)

        else:
            # valid
            self.valiate_warning(self.widget_warning_9,self.label_225,self.label_309)

# next_fournisseur_bancData
    def next_fournisseur_bancData(self):
        banqueNom=self.lineEdit_90.text()
        NumRib=self.lineEdit_91.text()
        if banqueNom == '' or NumRib == '':
            # error
            self.erreur_warning(self.widget_warning_10,self.label_226,self.label_310)            

        else:
            # valid
            self.valiate_warning(self.widget_warning_10,self.label_226,self.label_310)



# submitFournisseur 
    def submitFournisseur(self):
        last_name=self.lineEdit_74.text()
        first_name=self.lineEdit_87.text()
        adress=self.lineEdit_88.text()
        id_fiscal=self.lineEdit_89.text()
        banqueNom=self.lineEdit_90.text()
        NumRib=self.lineEdit_91.text()
        data =  (last_name,first_name,adress,id_fiscal,banqueNom,NumRib, datetime.now())
        print("data0",data)
        if last_name == '' or first_name == '' or adress == '' or id_fiscal == ''or banqueNom == '' or NumRib == '':
            pass
        else:
            myCursor = db.cursor()
            add_fournisseur_query= """INSERT INTO Fournisseur (
                    nom, 
                    prenom, 
                    address,
                    id_fiscal,
                    nomBanque,
                    NumeroRIB,
                    created) 
                    VALUES (%s, %s, %s,%s, %s, %s, %s)
                    """
            myCursor.execute(add_fournisseur_query,data)
            print(data)
        db.commit()

#|nv Client
    def next_Client_persoData(self):
        last_name=self.lineEdit_76.text()
        first_name=self.lineEdit_99.text()
        adress=self.lineEdit_100.text()
        Cin=self.lineEdit_101.text()
        if last_name == '' or first_name == '' or adress == '' or Cin == '':
            #error
            self.erreur_warning(self.widget_warning_11,self.label_227,self.label_311)  

        else:
            # valid
            self.valiate_warning(self.widget_warning_11,self.label_227,self.label_311)


    def next_Client_bancData(self):
        banqueNom=self.lineEdit_97.text()
        NumRib=self.lineEdit_98.text()
        if banqueNom == '' or NumRib == '':
            #error
            self.erreur_warning(self.widget_warning_12,self.label_228,self.label_312)  

        else:
            #valid
            self.valiate_warning(self.widget_warning_12,self.label_228,self.label_312)

    def submitClient(self):
        last_name=self.lineEdit_76.text()
        first_name=self.lineEdit_99.text()
        adress=self.lineEdit_100.text()
        Cin=self.lineEdit_101.text()
        banqueNom=self.lineEdit_97.text()
        NumRib=self.lineEdit_98.text()
        data = (last_name,first_name,adress,Cin,banqueNom,NumRib, datetime.now())
        if last_name == '' or first_name == '' or adress == '' or Cin == ''or banqueNom == '' or NumRib == '':
            pass
        else:
            myCursor = db.cursor()
            add_Client_query= """INSERT INTO clients (
                  nom, 
                  prenom, 
                  address,
                  CIN,
                  nomBanque,
                  NumeroRIB,
                  created) 
                    VALUES (%s, %s, %s,%s, %s, %s, %s)
                    """
            myCursor.execute(add_Client_query,data)
            print(data)
            db.commit()


#|nv personel
    def next_personne_persoData(self):
        last_name=self.lineEdit_63.text()
        first_name=self.lineEdit_64.text()
        birthD=self.dateEdit_person.date()
        Cin=self.lineEdit_65.text()
        # print(birthD)

        if last_name == '' or first_name == '' or birthD == '' or Cin == '':
            #error
            self.erreur_warning(self.widget_warning_6,self.label_222,self.label_303)  

        else:
            #valid
            self.valiate_warning(self.widget_warning_6,self.label_222,self.label_303)

    def next_personne_detailsPost(self):
        global status_personne
        global tempsAffect
        NomPsotAffect = self.lineEdit_66.text()
       
        if self.checkBox_51.isChecked()==True:
            status_personne="Permanant"
        if self.checkBox_49.isChecked()==True:
            status_personne="Contractuel"
        if self.checkBox_50.isChecked()==True:
            status_personne="Saisonier"   

        if self.checkBox_52.isChecked()==True:
            tempsAffect="Plein-Temps"
        elif self.checkBox_53.isChecked()==True:
            tempsAffect="Temps Partiel"
        
        departement = self.comboBox_personne.currentText()
        
        if NomPsotAffect == '' or status_personne == '' or tempsAffect == '' or departement=='':
            #error
            self.erreur_warning(self.widget_warning_7,self.label_223,self.label_304) 
        else:
            #valid 
            self.valiate_warning(self.widget_warning_7,self.label_223,self.label_304)
        
        

    def next_personne_dateValidation(self):
        global dateDebut
        global dateFin

        if self.checkBox_DateAujourdui.isChecked()==True:
            dateDebut = datetime.now().date()
        if self.checkBox_22.isChecked() == True:
            dateDebut_temps = self.dateEdit_8.date()
            dateDebut = date(dateDebut_temps.year(),dateDebut_temps.month(),dateDebut_temps.day())
        if self.checkBox_23.isChecked() == True:
            dateFin_temps = self.dateEdit_15.date()
            dateFin = date(dateFin_temps.year(),dateFin_temps.month(),dateFin_temps.day())
        else:
            dateFin = None
        
        if dateDebut == "" or dateFin == "":
            self.erreur_warning(self.widget_warning_8,self.label_224,self.label_305) 
        else:
            self.valiate_warning(self.widget_warning_8,self.label_224,self.label_305)    
            
                

    def submitpersonne(self):
        notes= self.plainTextEdit_63.toPlainText()
        print(notes)
        NomPsotAffect = self.lineEdit_66.text()
        last_name=self.lineEdit_63.text()
        first_name=self.lineEdit_64.text()
        birthD=self.dateEdit_person.date()
        py_date = date(birthD.year(),birthD.month(),birthD.day() )
        print("py_date", py_date)
        Cin=self.lineEdit_65.text()
        departement = self.comboBox_personne.currentText()
        if last_name == '' or first_name == '' or py_date == '' or Cin == ''or NomPsotAffect == '' or status_personne == '' or tempsAffect == '' or departement == '':
            print("in empty string",last_name,first_name,birthD,Cin,NomPsotAffect,status_personne,tempsAffect,departement)
        else:
                                # nom varchar(50) NOT NULL,
                                # prenom varchar(50) NOT NULL,
                                # bith_D DATE NOT NULL,
                                # CIN int NOT NULL,
                                # nomPost varchar(50) NOT NULL,
                                # status_personne varchar(50) NOT NULL,
                                # temps_aff varchar(50) NOT NULL, 
                                # created datetime NOT NULL,
                                # departement enum('EXT','INW', 'IVD', 'Digital', 'Autre')

            data=(last_name,first_name,py_date,Cin,NomPsotAffect,status_personne,tempsAffect,datetime.now(),departement, dateDebut, dateFin, notes)
            myCursor = db.cursor()
            add_Client_query= """INSERT INTO stuff (
                  nom, 
                  prenom, 
                  bith_D,
                  CIN,
                  nomPost,
                  status,
                  temps_aff,
                  created,
                  departement, 
                  dateDebut, 
                  dateFin, 
                  notes) 
                    VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            myCursor.execute(add_Client_query,data)
            print("data",data)
            db.commit()

        


#|nv equipement
    def next_equipement_Data(self):
        global etas
        equipement_name=self.lineEdit_67.text()
        equipement_marque=self.lineEdit_68.text()
        equipement_couleur=self.lineEdit_69.text()
        if self.checkBox_24.isChecked()== True:
            etas = "Neuf"
        if self.checkBox_29.isChecked()== True:
            etas = "Occasion"        
        
        equipement_numSeries=self.lineEdit_71.text()

        if equipement_name == "" or equipement_marque== "" or equipement_couleur== "" or etas== "" or equipement_numSeries== "":
            #error
            self.erreur_warning(self.widget_warning_4,self.label_220,self.label_296) 

        else:
            #valid
            self.valiate_warning(self.widget_warning_4,self.label_220,self.label_296)

        if etas == "":
            etas = None
   
    def calculate_equipement_emprient_cout_total(self):
        global equipement_emprient_dateDebut
        global equipement_emprient_dateFin
        global equipement_emprient_cout_total
        
        equipement_emprient_dateDebut_temps = self.dateEdit_2.date()
        equipement_emprient_dateFin_temps = self.dateEdit_10.date()
        equipement_emprient_nombre_de_jours = equipement_emprient_dateDebut_temps.daysTo(equipement_emprient_dateFin_temps)  
        
        equipement_emprient_dateDebut = date(
                                            equipement_emprient_dateDebut_temps.year(),
                                            equipement_emprient_dateDebut_temps.month(),
                                            equipement_emprient_dateDebut_temps.day()
                                            )
        
        
        equipement_emprient_dateFin = date(
                                            equipement_emprient_dateFin_temps.year(),
                                            equipement_emprient_dateFin_temps.month(),
                                            equipement_emprient_dateFin_temps.day()
                                            )

        equipement_emprient_cout_parJour=self.lineEdit_70.text()
        equipement_emprient_cout_total = int(equipement_emprient_cout_parJour) * equipement_emprient_nombre_de_jours

        # print("equipement_emprient_cout_parJour",equipement_emprient_cout_parJour,"typeof_equipement_emprient_cout_parJour",type(self.lineEdit_70.text()))
        # print("nbJours",equipement_emprient_nombre_de_jours,"typeof_equipement_emprient_nombre_de_jours", type(equipement_emprient_nombre_de_jours))
        # print("total",equipement_emprient_cout_total)
        self.label_166.setText('{}'.format(equipement_emprient_cout_total)) 
        # equipement_emprient_dateDebut
        if equipement_emprient_dateDebut == "":
            equipement_emprient_dateDebut = None
        # equipement_emprient_dateFin
        if equipement_emprient_dateFin == "":
            equipement_emprient_dateFin = None

        # equipement_emprient_cout_total
        if equipement_emprient_cout_total == "":
            equipement_emprient_cout_total = None
  
    def next_equipement_status(self):
        global equipement_nature
        if self.checkBox_30.isChecked()== True:
            equipement_nature = "Acheter"
            cout_achat=self.lineEdit_73.text()
            tva=self.lineEdit_86.text()
            if  cout_achat =="" or tva=="":
                #error
                self.erreur_warning(self.widget_warning_5,self.label_221,self.label_298) 

            else:
                #valid
                self.valiate_warning(self.widget_warning_5,self.label_221,self.label_298)



        if self.checkBox_31.isChecked()== True:
            equipement_nature = "Empreinter"
            if  equipement_nature =="" or self.label_166.text()=="":
                #error
                self.erreur_warning(self.widget_warning_5,self.label_221,self.label_298) 

            else:
                #valid
                self.valiate_warning(self.widget_warning_5,self.label_221,self.label_298)

        # equipement_nature
        if equipement_nature == "":
            equipement_nature = None

    def submitequipement(self):
        equipement_name=self.lineEdit_67.text() #notnul
        equipement_marque=self.lineEdit_68.text() # notnul
        equipement_couleur=self.lineEdit_69.text() # notnul
        equipement_numSeries=self.lineEdit_71.text() # notnul

        # cout_achat
        cout_achat=self.lineEdit_73.text()
        if cout_achat == "":
            cout_achat = None
        # tva
        tva=self.lineEdit_86.text()
        if tva == "":
            tva = None
        # equipement_cout_parJour
        equipement_cout_parJour= self.lineEdit_70.text()
        if equipement_cout_parJour == "":
            equipement_cout_parJour = None



        data = (equipement_name,
                equipement_marque,
                equipement_couleur,
                etas,
                equipement_numSeries,
                equipement_nature,
                cout_achat,
                tva,
                equipement_emprient_dateDebut,
                equipement_emprient_dateFin,
                equipement_cout_parJour,
                equipement_emprient_cout_total, 
                datetime.now()
                )
        
        if equipement_name == '' or equipement_marque == '' or equipement_couleur == '' or equipement_numSeries == '':
            pass
        else:
            myCursor = db.cursor()
            add_equipement_query= """INSERT INTO equipement (
                 nomEquipement,
                 marque,
                 couleur,
                 etas,
                 NumSeries,
                 natureEquipement,
                 coutAchat,
                 tva,
                 dateDebitEmprient,
                 dateFinEmprient,
                 coutsParjour,
                 coutTotal,
                 created) 
                 VALUES (%s, %s, %s,%s, %s, %s, %s,%s,%s,%s, %s, %s, %s)
                """
            myCursor.execute(add_equipement_query,data)
            print(data)
            db.commit()


#|nv Bande de Commande
# bande de commande table 
    def next_BC_Date(self):
        global bc_Date_date
        global bc_Date_time
        if self.checkBox_45.isChecked()==True:
            bc_Date_date = datetime.now().date()
       
        if self.checkBox_46.isChecked()==True:
            bc_Date_date_temps = self.dateEdit_10.date()
            bc_Date_date = date(        
                            bc_Date_date_temps.year(),
                            bc_Date_date_temps.month(),
                            bc_Date_date_temps.day()
                            )
        if self.checkBox_47.isChecked()==True:
            bc_Date_time = datetime.now().time()
        if self.checkBox_48.isChecked()==True:
            bc_Date_time_temps = self.timeEdit.time()
            bc_Date_time = time(        
                            bc_Date_time_temps.hour(),
                            bc_Date_time_temps.minute(),
                            bc_Date_time_temps.second()
                            )
        if bc_Date_date=="" or bc_Date_time=="":
            self.label_286.setText("donnees manquantes")
            self.label_286.setVisible(True)
        else:
            self.label_286.setText("ok !")
            self.widget_warning.setVisible(True)
            current_directory = os.getcwd()
            new_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'valid-30.png')
            if not os.path.exists(new_msg_icon_path):
                print("Error: Image file does not exist:", new_msg_icon_path)

            new_msg_icon = QPixmap(new_msg_icon_path)
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", new_msg_icon_path)
            else:
                self.label_170.setVisible(True)
                self.label_170.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_286.setVisible(True)
                self.label_286.setStyleSheet("color:green")
                print("ok")
    
    def create_bandeDeCommande(self):
        global max_id
        bc_data = (bc_Date_date,datetime.now(), bc_Date_time)
        if bc_Date_date == '' or bc_Date_time == '':
            pass
        else:
            myCursor = db.cursor()
            add_bc_data_query="""INSERT INTO bandeDeCommande (
                                    date_bc,                                
                                    created,
                                    time
                                    ) 
                                    VALUES (%s, %s, %s)
                                """
            myCursor.execute(add_bc_data_query,bc_data)
            db.commit()
            max_id_query ="""SELECT MAX(id) FROM bandeDeCommande"""
            self.label_168.setVisible(True)
            myCursor.execute(max_id_query)
            max_id = myCursor.fetchone()[0]
            self.label_167.setVisible(True)
            self.label_167.setText("{}".format(max_id))



# todo commande
    def add_commande(self):
   
        commande_name = self.plainText_commande.toPlainText()
        commande_montant=self.lineEdit_142.text()
        commande_nombre=self.lineEdit_141.text()
        commande_total = int(commande_montant)*int(commande_nombre)
        commande_data = (commande_name,commande_montant,commande_nombre,max_id,commande_total)

        if commande_name == '' or commande_montant == '' or commande_nombre == '' or max_id == '':
            pass
        else:
            myCursor = db.cursor()
            add_commande_table_query = """INSERT INTO commande (
                        nomCommande,
                        Montant,
                        nombre,
                        bandeCommade_id,
                        total
                        ) 
                        VALUES (%s, %s,%s, %s, %s)
                        """
            myCursor.execute(add_commande_table_query,commande_data)
            db.commit()
        # self.refresh_commande()

    def refresh_commande(self):
        myCursor = db.cursor()
        max_id_query ="""SELECT MAX(id) FROM bandeDeCommande"""
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        # print("in refrech")
        commande_allTable_query = f"SELECT * FROM commande where bandeCommade_id = {max_id}"
        # print("after query")
        myCursor.execute(commande_allTable_query)
        data_commande_table = myCursor.fetchall()
        # print("data",data_commande_table)
        self.tableWidget_commande.setRowCount(len(data_commande_table))
        # self.tableWidget_commande.setColumnCount(len(data_commande_table[0]))
        
        for row_num, row_data in enumerate(data_commande_table):
            # print("row_num, row_data",row_num, row_data)
            for col_num, col_data in enumerate(row_data):
                # print("col_num, col_data",col_num, col_data)
                item = QTableWidgetItem(str(col_data))
                if col_num != 4:
                    if col_num == 5: 
                        col_num = col_num -1
                        self.tableWidget_commande.setItem(row_num, col_num, item)
                    else:
                        self.tableWidget_commande.setItem(row_num, col_num, item)
                else:
                    col_num = col_num +1
                    self.tableWidget_commande.setItem(row_num, col_num, item)

    def remove_commande(self):
        currentRow = self.tableWidget_commande.currentRow()
        myCursor = db.cursor()

        commande_remove_query = "DELETE FROM commande WHERE id = %s"  
        primary_key_value = self.tableWidget_commande.item(currentRow, 0)
        
        if primary_key_value is not None:
            primary_key_value = self.tableWidget_commande.item(currentRow, 0).text()
            myCursor.execute(commande_remove_query, (primary_key_value,))
            self.tableWidget_commande.removeRow(currentRow)
        else:
            print("error primary_key_value is null")

    
    def next_commande_data(self):
        if self.tableWidget_commande.item(0, 0) == None:
            self.widget_483.setVisible(True)
            current_directory = os.getcwd()
            error_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'warning-30.png')
            if not os.path.exists(error_msg_icon_path):
                print("Error: Image file does not exist:", error_msg_icon_path)

            new_msg_icon = QPixmap(error_msg_icon_path)
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", error_msg_icon_path)
            else:
                self.label_171.setVisible(True)
                self.label_171.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_291.setText("error !")
                self.label_291.setVisible(True)
                self.label_291.setStyleSheet("color:red")

        else:
            self.widget_483.setVisible(True)
            current_directory = os.getcwd()
            validation_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'valid-30.png')
            if not os.path.exists(validation_msg_icon_path):
                print("Error: Image file does not exist:", validation_msg_icon_path)

            new_msg_icon = QPixmap(validation_msg_icon_path)
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", validation_msg_icon_path)
            else:
                self.label_171.setVisible(True)
                self.label_171.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_291.setText("ok !")
                self.label_291.setVisible(True)
                self.label_291.setStyleSheet("color:green")
                print("ok")
    
    def validate_Bcommande(self):
        pass
    def annuller_Bcommande(self):
        pass    


# DEVIS
# todo devis conatiner
    def next_devis_container_date(self):
        # day and time
        global devis_Date_date
        global devis_Date_time
        if self.checkBox_58.isChecked()==True:
            devis_Date_date = datetime.now().date()
        
        if self.checkBox_59.isChecked()==True:
            devis_Date_date_temps = self.dateEdit_17.date()
            devis_Date_date = date(        
                            devis_Date_date_temps.year(),
                            devis_Date_date_temps.month(),
                            devis_Date_date_temps.day()
                            )
        if self.checkBox_60.isChecked()==True:
            devis_Date_time = datetime.now().time()
        if self.checkBox_61.isChecked()==True:
            devis_Date_time_temps = self.timeEdit_3.time()
            devis_Date_time = time(        
                            devis_Date_time_temps.hour(),
                            devis_Date_time_temps.minute(),
                            devis_Date_time_temps.second()
                            )
        # validation
        if devis_Date_date=="" or devis_Date_time=="":
            current_directory = os.getcwd()
            error_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'warning-30.png')

            if not os.path.exists(error_msg_icon_path):
                print("Error: Image file does not exist:", error_msg_icon_path)
            new_msg_icon = QPixmap(error_msg_icon_path)
            
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", error_msg_icon_path)
            else:
                self.widget_warning_3.setVisible(True)
                self.label_205.setVisible(True)
                self.label_205.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_294.setText("error !")
                self.label_294.setVisible(True)
                self.label_294.setStyleSheet("color:red")

        else:
            current_directory = os.getcwd()
            new_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'valid-30.png')
            
            if not os.path.exists(new_msg_icon_path):
                print("Error: Image file does not exist:", new_msg_icon_path)

            new_msg_icon = QPixmap(new_msg_icon_path)
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", new_msg_icon_path)
            else:
                self.widget_warning_3.setVisible(True)
                self.label_205.setVisible(True)
                self.label_205.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_294.setText("ok !")
                self.label_294.setVisible(True)
                self.label_294.setStyleSheet("color:green")
                print("ok")


    def create_devis_container(self):
        global max_id_devis
        devis_data = (devis_Date_date,datetime.now(), devis_Date_time)
        if devis_Date_date == '' or devis_Date_time == '':
            pass
        else:
            myCursor = db.cursor()
            add_devis_data_query="""INSERT INTO devisContainer (
                                    date_bc,                                
                                    created,
                                    time
                                    ) 
                                    VALUES (%s, %s, %s)
                                """
            myCursor.execute(add_devis_data_query,devis_data)
            db.commit()
            max_id_devis_query ="""SELECT MAX(id) FROM devisContainer"""
            self.label_209.setVisible(True)
            myCursor.execute(max_id_devis_query)
            max_id_devis = myCursor.fetchone()[0]
            self.label_210.setVisible(True)
            self.label_210.setText("{}".format(max_id_devis))


    # todo devis
    def add_DEVIS(self):

        devis_name = self.plainText_devis.toPlainText()
        devis_montant=self.lineEdit_145.text()
        devis_nombre=self.lineEdit_146.text()
        devis_total = int(devis_montant)*int(devis_nombre)
        devis_data = (devis_name,devis_montant,devis_nombre,max_id_devis,devis_total)

        if devis_name == '' or devis_montant == '' or devis_nombre == '' or max_id_devis == '':
            pass
        else:
            myCursor = db.cursor()
            add_devis_table_query = """INSERT INTO devis (
                        nomdevis,
                        Montant,
                        nombre,
                        devisContainer_id,
                        total
                        ) 
                        VALUES (%s, %s,%s, %s, %s)
                        """
            myCursor.execute(add_devis_table_query,devis_data)
            db.commit()

# ? ******************************************************************
    def refresh_DEVIS(self):
        myCursor = db.cursor()
        max_id_query ="""SELECT MAX(id) FROM devisContainer"""
        myCursor.execute(max_id_query)
        max_id = myCursor.fetchone()[0]
        # print("in refrech")
        devis_allTable_query = f"SELECT * FROM devis where devisContainer_id = {max_id}"
        # print("after query")
        myCursor.execute(devis_allTable_query)
        data_devis_table = myCursor.fetchall()
        # print("data",data_devis_table)
        self.tableWidget_commande_3.setRowCount(len(data_devis_table))
        # self.tableWidget_commande.setColumnCount(len(data_devis_table[0]))
        
        for row_num, row_data in enumerate(data_devis_table):
            # print("row_num, row_data",row_num, row_data)
            for col_num, col_data in enumerate(row_data):
                # print("col_num, col_data",col_num, col_data)
                item = QTableWidgetItem(str(col_data))
                if col_num != 4:
                    if col_num == 5: 
                        col_num = col_num -1
                        self.tableWidget_commande_3.setItem(row_num, col_num, item)
                    else:
                        self.tableWidget_commande_3.setItem(row_num, col_num, item)
                else:
                    col_num = col_num +1
                    self.tableWidget_commande_3.setItem(row_num, col_num, item)

#
    def remove_DEVIS(self):
        currentRow = self.tableWidget_commande_3.currentRow()
        myCursor = db.cursor()

        devis_remove_query = "DELETE FROM devis WHERE id = %s"  
        primary_key_value = self.tableWidget_commande_3.item(currentRow, 0)
        
        if primary_key_value is not None:
            primary_key_value = self.tableWidget_commande_3.item(currentRow, 0).text()
            myCursor.execute(devis_remove_query, (primary_key_value,))
            self.tableWidget_commande_3.removeRow(currentRow)
        else:
            print("error primary_key_value is null")

    def next_DEVIS_data(self):
        if self.tableWidget_commande_3.item(0, 0) == None:
            self.widget_490.setVisible(True)
            current_directory = os.getcwd()
            error_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'warning-30.png')
            if not os.path.exists(error_msg_icon_path):
                print("Error: Image file does not exist:", error_msg_icon_path)

            new_msg_icon = QPixmap(error_msg_icon_path)
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", error_msg_icon_path)
            else:
                self.label_211.setVisible(True)
                self.label_211.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_295.setText("error !")
                self.label_295.setVisible(True)
                self.label_295.setStyleSheet("color:red")

        
        else:
            self.widget_490.setVisible(True)
            current_directory = os.getcwd()
            validation_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'valid-30.png')
            if not os.path.exists(validation_msg_icon_path):
                print("Error: Image file does not exist:", validation_msg_icon_path)

            new_msg_icon = QPixmap(validation_msg_icon_path)
            if new_msg_icon.isNull():
                print("Error: Failed to load image:", validation_msg_icon_path)
            else:
                self.label_211.setVisible(True)
                self.label_211.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
                self.label_295.setText("ok !")
                self.label_295.setVisible(True)
                self.label_295.setStyleSheet("color:green")
                print("ok")



    
    def validate_DEVIS_container(self):
        pass
    def annuller_DEVIS_container(self):
        pass

#| Prod_nv_dossier
# ? prod_ext
# validation func

    def date_prod_ext_validation(self):
        global date_prod_ext
        global time_prod_ext

        if self.checkBox_ext.isChecked()==True:
            date_prod_ext = datetime.now().date()
       
        if self.checkBox_2.isChecked()==True:
            date_prod_ext_temps = self.dateEdit_3.date()
            date_prod_ext = date(        
                            date_prod_ext_temps.year(),
                            date_prod_ext_temps.month(),
                            date_prod_ext_temps.day()
                            )
        if self.checkBox_3.isChecked()==True:
            time_prod_ext = datetime.now().time()
        if self.checkBox_4.isChecked()==True:
            time_prod_ext_temps = self.timeEdit_2.time()
            time_prod_ext = time(        
                            time_prod_ext_temps.hour(),
                            time_prod_ext_temps.minute(),
                            time_prod_ext_temps.second()
                            )
        if date_prod_ext == "" or time_prod_ext =="":
            self.erreur_warning(self.widget_warning_14,self.label_219,self.label_314) 
        else:
            self.valiate_warning(self.widget_warning_14,self.label_219,self.label_314)
            

    def nature_prod_ext_validation(self):
        global nature_prod_ext
        nature_prod_ext= self.plainTextEdit_8.toPlainText()
        if nature_prod_ext== '':
            self.erreur_warning(self.widget_warning_15,self.label_229,self.label_315)
        else:
            self.valiate_warning(self.widget_warning_15,self.label_229,self.label_315)


    def addPersonel_prod_ext(self):
        text = str(self.comboBox_personel.currentText())
        list_current_row_index = self.listWidget_2.currentRow()
        self.listWidget_2.insertItem(list_current_row_index, text)
    def removePersonel_prod_ext(self):
        list_current_row_index = self.listWidget_2.currentRow()
        item = self.listWidget_2.takeItem(list_current_row_index)
        del item


    def personel_prod_ext_validation(self):
        global id_personnel_table
        id_personnel_table = []
        myCursor = db.cursor()
        stuff_table=[] 
        if self.listWidget_2.count()==0:
            self.erreur_warning(self.widget_warning_13,self.label_207,self.label_313)
        else:
            self.valiate_warning(self.widget_warning_13,self.label_207,self.label_313)
            for i in range(self.listWidget_2.count()):
                item = self.listWidget_2.item(i)
                fullName_tab_extract = item.text().split(" ")
                stuff_FirstName = fullName_tab_extract[0]
                stuff_Lastname = fullName_tab_extract[1]
                print(fullName_tab_extract)
                id_query = f"SELECT id FROM stuff where nom = '{str(stuff_FirstName)}' and prenom = '{str(stuff_Lastname)}'"
                myCursor.execute(id_query)
                for j in myCursor:
                    stuff_table.append((item.text(),j[0]))
                    id_personnel_table.append(j[0])
        # myCursor.close()
        # print(stuff_table)
        print(id_personnel_table)

    def addEquipement_prod_ext(self):
        text = str(self.comboBox_6.currentText())
        list_current_row_index = self.listWidget_5.currentRow()
        self.listWidget_5.insertItem(list_current_row_index, text)
    
    def removeEquipement_prod_ext(self):
        list_current_row_index = self.listWidget_5.currentRow()
        item = self.listWidget_5.takeItem(list_current_row_index)
        del item

    def equipement_prod_ext_validation(self):
        global id_equipement_table
        id_equipement_table = []
        myCursor = db.cursor()
        equipements_table=[] 
        
        if self.listWidget_5.count()==0:
            self.erreur_warning(self.widget_warning_18,self.label_232,self.label_318)
        
        else:
            self.valiate_warning(self.widget_warning_18,self.label_232,self.label_318)
            for i in range(self.listWidget_5.count()):
                item = self.listWidget_5.item(i)
                equipement_name = item.text()
                id_query = f"SELECT id FROM equipement where nomEquipement = '{str(equipement_name)}'"
                myCursor.execute(id_query)
                for j in myCursor:
                    equipements_table.append((item.text(),j[0]))
                    id_equipement_table.append(j[0])
 
        # print(equipements_table)
        # print(id_equipement_table)
    
    def charge_TTC_prod_ext_calculation(self):
        charge_montant = self.lineEdit_5.text()
        charge_tva = self.lineEdit_6.text()
        charge_tva_montant = (int(charge_montant) * int(charge_tva)) / 100
        self.lineEdit_7.setText(str(charge_tva_montant))
        charge_ttc = int(charge_montant) - int(charge_tva_montant) 
        self.lineEdit_8.setText(str(charge_ttc))
    
    def charge_prod_ext_validation(self):
        global charge_id_prod_ext
        myCursor = db.cursor(buffered=True)
        text = str(self.comboBox_5.currentText())
        fullname_table_fournisseurs = text.split(" ")
        firstName_fournisseur = fullname_table_fournisseurs[0]
        lastName_fournisseur = fullname_table_fournisseurs[1]
        extract_fournisseur_id_query = f" select id from fournisseur where nom = '{lastName_fournisseur}' and prenom = '{firstName_fournisseur}' "
        myCursor.execute(extract_fournisseur_id_query)
        id_fournisseur = myCursor.fetchone()[0]
        print(id_fournisseur)
        
        
        charge_designation = self.lineEdit_4.text()
        charge_montant = self.lineEdit_5.text()
        charge_tva = self.lineEdit_6.text()
        if charge_tva=='' or charge_montant =='':
            self.erreur_warning(self.widget_warning_16,self.label_230,self.label_316)
        charge_tva_montant = (int(charge_montant) * int(charge_tva)) / 100
        charge_ttc = int(charge_montant) - int(charge_tva_montant) 
        
        nv_charge_query = """INSERT INTO charge (
                designiation,
                montant,
                tva,
                tva_montant,
                ttc,
                created,
                charge_id
                 ) 
                 VALUES (%s, %s,%s, %s,%s, %s,%s)
                """
        charge_data=(charge_designation, charge_montant, charge_tva, charge_tva_montant, charge_ttc, datetime.now(), id_fournisseur)
        if charge_tva=='' or charge_montant =='' or charge_tva_montant =='' or charge_ttc == '':
            self.erreur_warning(self.widget_warning_16,self.label_230,self.label_316)
            
        else:
            self.valiate_warning(self.widget_warning_16,self.label_230,self.label_316)
            myCursor.execute(nv_charge_query, charge_data)
            db.commit()
            extract_charge_id_query= "SELECT charge_id FROM charge order by created DESC"
            myCursor.execute(extract_charge_id_query)
            charge_id_prod_ext= myCursor.fetchone()[0]
            print(charge_id_prod_ext)
            # myCursor.close()


    def facturation_TTC_prod_ext_calculation(self):
        facturation_montant = self.lineEdit_15.text()
        facturation_tva = self.lineEdit_16.text()
        facturation_tva_montant = (int(facturation_montant) * int(facturation_tva)) / 100
        self.lineEdit_17.setText(str(facturation_tva_montant))
        facturation_ttc = int(facturation_montant) - int(facturation_tva_montant) 
        self.lineEdit_18.setText(str(facturation_ttc))

    def facturation_prod_ext_validation(self):
        myCursor = db.cursor(buffered=True)
        text = str(self.comboBox_8.currentText())
        fullname_table_clients = text.split(" ")
        firstName_client = fullname_table_clients[0]
        lastName_client = fullname_table_clients[1]
        extract_client_id_query = f" select id from clients where nom = '{firstName_client}' and prenom = '{lastName_client}' "
        myCursor.execute(extract_client_id_query)
        id_client = myCursor.fetchall()[0]
        print(id_client)
        
        
        facturation_designation = self.lineEdit_14.text()
        facturation_montant = self.lineEdit_15.text()
        facturation_tva = self.lineEdit_16.text()
        
        if facturation_tva=='' or facturation_montant =='' :
            self.erreur_warning(self.widget_warning_17,self.label_231,self.label_317)

        facturation_tva_montant = (int(facturation_montant) * int(facturation_tva)) / 100
        facturation_ttc = int(facturation_montant) - int(facturation_tva_montant) 
        
        nv_facturation_query = """INSERT INTO facturation (
                designiation,
                montant,
                tva,
                tva_montant,
                ttc,
                created,
                facturaction_id
                 ) 
                 VALUES (%s, %s,%s, %s,%s, %s,%s)
                """
        facturation_data=(facturation_designation, facturation_montant, facturation_tva, facturation_tva_montant, facturation_ttc, datetime.now(), id_client[0])
        if facturation_tva=='' or facturation_montant =='' or facturation_tva_montant =='' or facturation_ttc == '':
            self.erreur_warning(self.widget_warning_17,self.label_231,self.label_317)
            
        else:
            self.valiate_warning(self.widget_warning_17,self.label_231,self.label_317)
            myCursor.execute(nv_facturation_query, facturation_data)
            db.commit()
            myCursor.close()
    
    def marge_prod_ext_calculation(self):
        global marge
        
        myCursor = db.cursor(buffered=True)
        charge_max_recent_ttc_query = "SELECT ttc FROM charge order by created DESC"
        myCursor.execute(charge_max_recent_ttc_query)
        charge_max_recent_tupel= myCursor.fetchall()[0]
        charge_ttc = charge_max_recent_tupel[0]
        print(charge_ttc)

        facturation_max_id_query ="""SELECT MAX(id) FROM facturation"""
        myCursor.execute(facturation_max_id_query)
        facturation_max_id = myCursor.fetchone()[0]
        facturation_max_id_ttc_query =f"SELECT ttc FROM facturation where id = '{facturation_max_id}'"
        myCursor.execute(facturation_max_id_ttc_query)
        facturation_max_id_ttc = myCursor.fetchone()[0]
        print(facturation_max_id_ttc)

        marge = int(facturation_max_id_ttc) - int(charge_ttc)
        self.lineEdit_3.setText("{}".format(marge))
        myCursor.close()

    def nv_dossier_prod_ext_validation(self):
        myCursor = db.cursor(buffered=True)

        extract_facturation_id_prod_ext_query= "SELECT facturaction_id FROM facturation order by created DESC"
        myCursor.execute(extract_facturation_id_prod_ext_query)
        facturation_id_prod_ext= myCursor.fetchone()[0]

        """
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
        """
        

        nv_dossier_prod_ext_data = (date_prod_ext,nature_prod_ext,charge_id_prod_ext,facturation_id_prod_ext ,marge,datetime.now())

        nv_dossier_prod_ext_validation_query = """INSERT INTO nv_dossier_prod_ext (
                date,
                nature,
                id_charge, 
                id_facturation,
                marge, 
                created
                 ) 
                 VALUES (%s, %s, %s,%s, %s, %s)
                """
        myCursor = db.cursor()
        myCursor.execute(nv_dossier_prod_ext_validation_query,nv_dossier_prod_ext_data)
        db.commit()




# annulation func
    def nv_dossier_prod_ext_annulation(self):
        pass
# ////////////////////////////////////////////////////////////////////////////////
# ? prod_INW
# validation func

    def date_prod_INW_validation(self):
        global date_prod_INW
        global time_prod_INW

        if self.checkBox_5.isChecked()==True:
            date_prod_INW = datetime.now().date()
       
        if self.checkBox_6.isChecked()==True:
            date_prod_INW_temps = self.dateEdit_3.date()
            date_prod_INW = date(        
                            date_prod_INW_temps.year(),
                            date_prod_INW_temps.month(),
                            date_prod_INW_temps.day()
                            )
        if self.checkBox_7.isChecked()==True:
            time_prod_INW = datetime.now().time()
        if self.checkBox_8.isChecked()==True:
            time_prod_INW_temps = self.timeEdit_2.time()
            time_prod_INW = time(        
                            time_prod_INW_temps.hour(),
                            time_prod_INW_temps.minute(),
                            time_prod_INW_temps.second()
                            )
        if date_prod_INW == "" or time_prod_INW =="":
            self.erreur_warning(self.widget_warning_19,self.label_280,self.label_319) 
        else:
            self.valiate_warning(self.widget_warning_19,self.label_280,self.label_319)
            
    def nature_prod_INW_validation(self):
        global nature_prod_INW
        nature_prod_INW= self.plainTextEdit_19.toPlainText()
        if nature_prod_INW== '':
            self.erreur_warning(self.widget_warning_20,self.label_281,self.label_320)
        else:
            self.valiate_warning(self.widget_warning_20,self.label_281,self.label_320)


    def addPersonel_prod_INW(self):
        text = str(self.comboBox_4.currentText())
        list_current_row_index = self.listWidget_3.currentRow()
        self.listWidget_3.insertItem(list_current_row_index, text)
    def removePersonel_prod_INW(self):
        list_current_row_index = self.listWidget_3.currentRow()
        item = self.listWidget_3.takeItem(list_current_row_index)
        del item


    def personel_prod_INW_validation(self):
        global id_personnel_table_prod_INW
        id_personnel_table_prod_INW = []
        myCursor = db.cursor()
        stuff_table=[] 
        if self.listWidget_3.count()==0:
            self.erreur_warning(self.widget_warning_21,self.label_282,self.label_321)
        else:
            self.valiate_warning(self.widget_warning_21,self.label_282,self.label_321)
            for i in range(self.listWidget_3.count()):
                item = self.listWidget_3.item(i)
                fullName_tab_extract = item.text().split(" ")
                stuff_FirstName = fullName_tab_extract[0]
                stuff_Lastname = fullName_tab_extract[1]
                # print(fullName_tab_extract)
                id_query = f"SELECT id FROM stuff where nom = '{str(stuff_FirstName)}' and prenom = '{str(stuff_Lastname)}'"
                myCursor.execute(id_query)
                for j in myCursor:
                    stuff_table.append((item.text(),j[0]))
                    id_personnel_table_prod_INW.append(j[0])

    def addEquipement_prod_INW(self):
        text = str(self.comboBox_7.currentText())
        list_current_row_index = self.listWidget_6.currentRow()
        self.listWidget_6.insertItem(list_current_row_index, text)
    
    def removeEquipement_prod_INW(self):
        list_current_row_index = self.listWidget_6.currentRow()
        item = self.listWidget_6.takeItem(list_current_row_index)
        del item

    def equipement_prod_INW_validation(self):
        global id_equipement_table_prod_INW
        id_equipement_table_prod_INW = []
        myCursor = db.cursor()
        equipements_table=[] 
        
        if self.listWidget_6.count()==0:
            self.erreur_warning(self.widget_warning_22,self.label_283,self.label_322)
        
        else:
            self.valiate_warning(self.widget_warning_22,self.label_283,self.label_322)
            for i in range(self.listWidget_6.count()):
                item = self.listWidget_6.item(i)
                equipement_name = item.text()
                id_query = f"SELECT id FROM equipement where nomEquipement = '{str(equipement_name)}'"
                myCursor.execute(id_query)
                for j in myCursor:
                    equipements_table.append((item.text(),j[0]))
                    id_equipement_table_prod_INW.append(j[0])
                    
    def charge_TTC_prod_INW_calculation(self):
        charge_montant = self.lineEdit_11.text()
        charge_tva = self.lineEdit_12.text()
        charge_tva_montant = (int(charge_montant) * int(charge_tva)) / 100
        self.lineEdit_13.setText(str(charge_tva_montant))
        charge_ttc = int(charge_montant) - int(charge_tva_montant) 
        self.lineEdit_19.setText(str(charge_ttc))


    def charge_prod_INW_validation(self):
        global charge_id_prod_INW
        myCursor = db.cursor(buffered=True)
        text = str(self.comboBox_9.currentText())
        fullname_table_fournisseurs = text.split(" ")
        firstName_fournisseur = fullname_table_fournisseurs[0]
        lastName_fournisseur = fullname_table_fournisseurs[1]
        extract_fournisseur_id_query = f" select id from fournisseur where nom = '{lastName_fournisseur}' and prenom = '{firstName_fournisseur}' "
        myCursor.execute(extract_fournisseur_id_query)
        id_fournisseur = myCursor.fetchone()[0]
        print(id_fournisseur)     
        charge_designation = self.lineEdit_10.text()
        charge_montant = self.lineEdit_11.text()
        charge_tva = self.lineEdit_12.text()
        if charge_tva=='' or charge_montant =='':
            self.erreur_warning(self.widget_warning_23,self.label_287,self.label_323)
        charge_tva_montant = (int(charge_montant) * int(charge_tva)) / 100
        charge_ttc = int(charge_montant) - int(charge_tva_montant)      
        nv_charge_query = """INSERT INTO charge (
                designiation,
                montant,
                tva,
                tva_montant,
                ttc,
                created,
                charge_id
                 ) 
                 VALUES (%s, %s,%s, %s,%s, %s,%s)
                """
        charge_data=(charge_designation, charge_montant, charge_tva, charge_tva_montant, charge_ttc, datetime.now(), id_fournisseur)
        if charge_tva=='' or charge_montant =='' or charge_tva_montant =='' or charge_ttc == '':
            self.erreur_warning(self.widget_warning_23,self.label_287,self.label_323)
            
        else:
            self.valiate_warning(self.widget_warning_23,self.label_287,self.label_323)
            myCursor.execute(nv_charge_query, charge_data)
            db.commit()
            extract_charge_id_query= "SELECT charge_id FROM charge order by created DESC"
            myCursor.execute(extract_charge_id_query)
            charge_id_prod_INW= myCursor.fetchone()[0]
            print(charge_id_prod_INW)

    def facturation_TTC_prod_INW_calculation(self):
        facturation_montant = self.lineEdit_21.text()
        facturation_tva = self.lineEdit_22.text()
        facturation_tva_montant = (int(facturation_montant) * int(facturation_tva)) / 100
        self.lineEdit_23.setText(str(facturation_tva_montant))
        facturation_ttc = int(facturation_montant) - int(facturation_tva_montant) 
        self.lineEdit_24.setText(str(facturation_ttc))

    def facturation_prod_INW_validation(self):
        myCursor = db.cursor(buffered=True)
        text = str(self.comboBox_10.currentText())
        fullname_table_clients = text.split(" ")
        firstName_client = fullname_table_clients[0]
        lastName_client = fullname_table_clients[1]
        extract_client_id_query = f" select id from clients where nom = '{firstName_client}' and prenom = '{lastName_client}' "
        myCursor.execute(extract_client_id_query)
        id_client = myCursor.fetchall()[0]
        print(id_client)
        
        
        facturation_designation = self.lineEdit_20.text()
        facturation_montant = self.lineEdit_21.text()
        facturation_tva = self.lineEdit_22.text()
        
        if facturation_tva=='' or facturation_montant =='' :
            self.erreur_warning(self.widget_warning_24,self.label_288,self.label_324)

        facturation_tva_montant = (int(facturation_montant) * int(facturation_tva)) / 100
        facturation_ttc = int(facturation_montant) - int(facturation_tva_montant) 
        
        nv_facturation_query = """INSERT INTO facturation (
                designiation,
                montant,
                tva,
                tva_montant,
                ttc,
                created,
                facturaction_id
                 ) 
                 VALUES (%s, %s,%s, %s,%s, %s,%s)
                """
        facturation_data=(facturation_designation, facturation_montant, facturation_tva, facturation_tva_montant, facturation_ttc, datetime.now(), id_client[0])
        if facturation_tva=='' or facturation_montant =='' or facturation_tva_montant =='' or facturation_ttc == '':
            self.erreur_warning(self.widget_warning_24,self.label_288,self.label_324)
            
        else:
            self.valiate_warning(self.widget_warning_24,self.label_288,self.label_324)
            myCursor.execute(nv_facturation_query, facturation_data)
            db.commit()
            myCursor.close()


    def marge_prod_INW_calculation(self):
        global marge_prod_INW
        
        myCursor = db.cursor(buffered=True)
        charge_max_recent_ttc_query = "SELECT ttc FROM charge order by created DESC"
        myCursor.execute(charge_max_recent_ttc_query)
        charge_max_recent_tupel= myCursor.fetchall()[0]
        charge_ttc = charge_max_recent_tupel[0]
        print(charge_ttc)

        facturation_max_id_query ="""SELECT MAX(id) FROM facturation"""
        myCursor.execute(facturation_max_id_query)
        facturation_max_id = myCursor.fetchone()[0]
        facturation_max_id_ttc_query =f"SELECT ttc FROM facturation where id = '{facturation_max_id}'"
        myCursor.execute(facturation_max_id_ttc_query)
        facturation_max_id_ttc = myCursor.fetchone()[0]
        print(facturation_max_id_ttc)
        marge_prod_INW = int(facturation_max_id_ttc) - int(charge_ttc)
        self.lineEdit_25.setText("{}".format(marge))
        myCursor.close()

    def nv_dossier_prod_INW_validation(self):
        myCursor = db.cursor(buffered=True)

        extract_facturation_id_prod_ext_query= "SELECT facturaction_id FROM facturation order by created DESC"
        myCursor.execute(extract_facturation_id_prod_ext_query)
        facturation_id_prod_INW= myCursor.fetchone()[0]

        """
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
        """
        

        nv_dossier_prod_INW_data = (date_prod_INW,nature_prod_INW,charge_id_prod_INW,facturation_id_prod_INW ,marge_prod_INW,datetime.now())

        nv_dossier_prod_INW_validation_query = """INSERT INTO nv_dossier_prod_inw (
                date,
                nature,
                id_charge, 
                id_facturation,
                marge, 
                created
                 ) 
                 VALUES (%s, %s, %s,%s, %s, %s)
                """
        myCursor = db.cursor()
        myCursor.execute(nv_dossier_prod_INW_validation_query,nv_dossier_prod_INW_data)
        db.commit()


# annulation func
    def nv_dossier_prod_INW_annulation(self):
        pass

# ///////////////////////////////////////////////////////////////////////////////////////////////
# ? prod_IVD
# validation func

    def date_prod_IVD_validation(self):
        global date_prod_IVD
        global time_prod_IVD

        if self.checkBox_IVD.isChecked()==True:
            date_prod_IVD = datetime.now().date()
       
        if self.checkBox_2.isChecked()==True:
            date_prod_IVD_temps = self.dateEdit_3.date()
            date_prod_IVD = date(        
                            date_prod_IVD_temps.year(),
                            date_prod_IVD_temps.month(),
                            date_prod_IVD_temps.day()
                            )
        if self.checkBox_3.isChecked()==True:
            time_prod_IVD = datetime.now().time()
        if self.checkBox_4.isChecked()==True:
            time_prod_IVD_temps = self.timeEdit_2.time()
            time_prod_IVD = time(        
                            time_prod_IVD_temps.hour(),
                            time_prod_IVD_temps.minute(),
                            time_prod_IVD_temps.second()
                            )
        if date_prod_IVD == "" or time_prod_IVD =="":
            self.erreur_warning(self.widget_warning_14,self.label_219,self.label_314) 
        else:
            self.valiate_warning(self.widget_warning_14,self.label_219,self.label_314)
            
    def nature_prod_IVD_validation(self):
        pass
    def personel_prod_IVD_validation(self):
        pass
    def equipement_prod_IVD_validation(self):
        pass
    def charge_prod_IVD_validation(self):
        pass
    def facturation_prod_IVD_validation(self):
        pass
    def nv_dossier_prod_IVD_validation(self):
        pass

# annulation func
    def nv_dossier_prod_IVD_annulation(self):
        pass


# ? prod_Digital
# validation func

    def date_prod_Digital_validation(self):
        pass
    def nature_prod_Digital_validation(self):
        pass
    def personel_prod_Digital_validation(self):
        pass
    def equipement_prod_Digital_validation(self):
        pass
    def charge_prod_Digital_validation(self):
        pass
    def facturation_prod_Digital_validation(self):
        pass
    def nv_dossier_prod_Digital_validation(self):
        pass

# annulation func
    def nv_dossier_prod_Digital_annulation(self):
        pass

# ? prod_autre
# validation func

    def date_prod_autre_validation(self):
        pass
    def nature_prod_autre_validation(self):
        pass
    def personel_prod_autre_validation(self):
        pass
    def equipement_prod_autre_validation(self):
        pass
    def charge_prod_autre_validation(self):
        pass
    def facturation_prod_autre_validation(self):
        pass
    def nv_dossier_prod_autre_validation(self):
        pass

# annulation func
    def nv_dossier_prod_autre_annulation(self):
        pass