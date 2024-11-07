Properties Sayfası Test Senaryoları
=====================

 * "qa@testinium.io" ve "Q6XpZ?6GsMbA" bilgileriyle geçerli giriş yapılır ve dashboard sayfasına ulaşılır.

Seçilen senaryoda edite tıklanması ve properties sayfasının açılması
----------------
Tags: SecilenSenaryodaEditeTiklanmasiVePropertiesSayfasininAcilmasi

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür

Properties sayfasında seçilen projenin Copy URL butonunun çalışması
-----------------
Tags: PropertiesSayfasindaSecilenProjeninCopyURLButonununCalismasi

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Copy URL butonuna tıklanır
// Butona tıklandığında "Copied" ifadesinin ekrana geldiği görülür

Properties sayfasında seçilen senaryonun Source File bölümünün kontrolü
----------------
Tags: PropertiesSayfasindaSecilenSenaryonunSourceFileBolumununKontrolü

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Spec ve cpt dosyalarının select source file başlığının altında sıralandığı görülür

Seçilen senaryonun Source File seçtikten sonra test methodunun seçilmesi kontrolü
-----------------
Tags: SecilenSenaryonunSourceFileSectiktenSonraTestMethodununSecilmesiKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Consept ve Spec dosyalarının sıralandığı görülür


Seçilen senaryo için File Content kısmında Save butonunun active olmama kontrolü
-----------------
Tags: SecilenSenaryoIcinFileContentKismindaSaveButonununActiveOlmamaKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* File Content tarafında herhangi değişiklik yapmadan save butonuna tıklanır
* Save butonunun active olmadığı görülür

Seçilen senaryo için File Content kısmında Save butonunun active olması kontrolü
-----------------
Tags: SecilenSenaryoIcinFileContentKismindaSaveButonununActiveOlmasiKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* File Content tarafında değişiklik yapıldıktan sonra save butonuna tıklanır
* Save butonunun active olduğu görülür

Seçilen senaryo için Set System Parameters kısmında Name kutucuğuna değer girilip ekleme kontrolü
-----------------
Tags: SecilenSenaryoIcinSetSystemParametersKismindaNameKutucugunaDegerGirilipEklemeKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Set System Parameters Name kısmına rastgele kelime yazılır
* Add butonuna tıklanır ve sadece name ile eklenemediği görülür

Seçilen senaryo için Set System Parameters kısmında hem Name kutucuğuna hemde Value  kutucuğuna değer girilip ekleme kontrolü
-----------------
Tags : SecilenSenaryoIcinNameVeValueKutucugunaDegerGirilipEklemeKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Set System Parameters Name ve value kısmına rastgele kelime yazılır
* Add butonuna tıklanır ve sadece name value ile eklenemediği görülür

Properties sayfasında Apply butonunun çalışma kontrolü
-----------------
Tags : PropertiesSayfasindaApplyButonununCalısmaKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Apply butonuna tıklanır ve kontrolu yapılır
* Properties sayfasının ekrana geldiği görülür


Properties sayfasında Save butonunun çalışma kontrolü
-----------------
Tags : PropertiesSayfasindaSaveButonununCalısmaKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Senaryo ismi rastgele bir isim ile değiştirilir
* Edit Save butonuna tıklanır
* "Scenario successfully updated." yazısının ekrana geldiği görülür
* Scenario editten senaryo sayfasına dönülür ve sayfa elementlerinin ekrana geldiği görülür
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Senaryo ismi kontrol edilir

Properties sayfasında Cancel butonunun çalışma kontrolü
-----------------
Tags : PropertiesSayfasindaCancelButonununCalısmaKontrolu

* Scenarios tabına tıklanır.
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Senaryo ismi rastgele bir isim ile değiştirilir
* Cancel butonuna tıklanır
* Scenario editten senaryo sayfasına dönülür ve sayfa elementlerinin ekrana geldiği görülür
* "Amazon" adlı proje seçilir
* Scenarios sayfasında seçilen projede edite tıklanır
* Properties sayfasının ekrana geldiği görülür
* Senaryo isminin aynı olmadığı görülür


















Dashboard sayfasından project sayfasına geçiş11
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis11

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş11
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis11

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş11
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis11

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş11
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis11

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş11
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis11

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş11
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis11

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş11
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis11

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü11
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu11

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü11
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu11

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü11
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu11

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü11
------------------------------
Tags: DashboardDarkModeButonuKontrolu11

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü11
------------------------------
Tags: DashboardLatestTestRunsKontrolu11

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü11
------------------------------
Tags: DashboardCompanyDegisimiKontrolu11
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company11
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany11

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş11
------------------------------
Tags: DashboarddanUserProfileGecis11

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş11
------------------------------
Tags: DashboarddanAccountInformationaGecis11

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü11
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu11

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü11
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu11

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür

















Dashboard sayfasından project sayfasına geçiş12
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis12

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş12
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis12

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş12
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis12

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş12
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis12

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş12
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis12

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş12
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis12

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş12
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis12

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü12
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu12

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü12
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu12

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü12
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu12

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü12
------------------------------
Tags: DashboardDarkModeButonuKontrolu12

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü12
------------------------------
Tags: DashboardLatestTestRunsKontrolu12

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü12
------------------------------
Tags: DashboardCompanyDegisimiKontrolu12
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company12
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany12

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş12
------------------------------
Tags: DashboarddanUserProfileGecis12

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş12
------------------------------
Tags: DashboarddanAccountInformationaGecis12

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü12
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu12

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü12
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu12

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür

















Dashboard sayfasından project sayfasına geçiş13
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis13

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş13
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis13

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş13
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis13

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş13
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis13

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş13
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis13

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş13
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis13

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş13
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis13

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü13
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu13

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü13
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu13

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü13
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu13

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü13
------------------------------
Tags: DashboardDarkModeButonuKontrolu13

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü13
------------------------------
Tags: DashboardLatestTestRunsKontrolu13

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü13
------------------------------
Tags: DashboardCompanyDegisimiKontrolu13
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company13
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany13

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş13
------------------------------
Tags: DashboarddanUserProfileGecis13

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş13
------------------------------
Tags: DashboarddanAccountInformationaGecis13

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü13
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu13

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü13
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu13

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür


















Dashboard sayfasından project sayfasına geçiş14
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis14

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş14
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis14

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş14
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis14

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş14
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis14

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş14
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis14

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş14
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis14

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş14
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis14

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü14
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu14

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü14
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu14

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü14
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu14

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü14
------------------------------
Tags: DashboardDarkModeButonuKontrolu14

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü14
------------------------------
Tags: DashboardLatestTestRunsKontrolu14

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü14
------------------------------
Tags: DashboardCompanyDegisimiKontrolu14
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company14
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany14

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş14
------------------------------
Tags: DashboarddanUserProfileGecis14

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş14
------------------------------
Tags: DashboarddanAccountInformationaGecis14

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü14
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu14

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü14
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu14

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür



















Dashboard sayfasından project sayfasına geçiş15
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis15

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş15
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis15

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş15
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis15

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş15
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis15

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş15
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis15

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş15
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis15

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş15
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis15

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü15
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu15

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü15
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu15

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü15
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu15

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü15
------------------------------
Tags: DashboardDarkModeButonuKontrolu15

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü15
------------------------------
Tags: DashboardLatestTestRunsKontrolu15

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü15
------------------------------
Tags: DashboardCompanyDegisimiKontrolu15
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company15
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany15

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş15
------------------------------
Tags: DashboarddanUserProfileGecis15

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş15
------------------------------
Tags: DashboarddanAccountInformationaGecis15

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü15
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu15

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü15
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu15

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür



















Dashboard sayfasından project sayfasına geçiş16
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis16

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş16
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis16

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş16
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis16

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş16
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis16

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş16
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis16

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş16
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis16

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş16
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis16

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü16
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu16

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü16
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu16

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü16
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu16

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü16
------------------------------
Tags: DashboardDarkModeButonuKontrolu16

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü16
------------------------------
Tags: DashboardLatestTestRunsKontrolu16

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü16
------------------------------
Tags: DashboardCompanyDegisimiKontrolu16
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company16
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany16

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş16
------------------------------
Tags: DashboarddanUserProfileGecis16

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş16
------------------------------
Tags: DashboarddanAccountInformationaGecis16

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü16
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu16

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü16
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu16

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür
















Dashboard sayfasından project sayfasına geçiş17
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis17

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş17
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis17

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş17
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis17

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş17
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis17

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş17
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis17

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş17
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis17

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş17
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis17

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü17
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu17

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü17
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu17

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü17
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu17

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü17
------------------------------
Tags: DashboardDarkModeButonuKontrolu17

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü17
------------------------------
Tags: DashboardLatestTestRunsKontrolu17

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü17
------------------------------
Tags: DashboardCompanyDegisimiKontrolu17
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company17
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany17

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş17
------------------------------
Tags: DashboarddanUserProfileGecis17

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş17
------------------------------
Tags: DashboarddanAccountInformationaGecis17

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü17
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu17

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü17
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu17

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür















Dashboard sayfasından project sayfasına geçiş18
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis18

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş18
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis18

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş18
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis18

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş18
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis18

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş18
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis18

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş18
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis18

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş18
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis18

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü18
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu18

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü18
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu18

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü18
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu18

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü18
------------------------------
Tags: DashboardDarkModeButonuKontrolu18

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü18
------------------------------
Tags: DashboardLatestTestRunsKontrolu18

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü18
------------------------------
Tags: DashboardCompanyDegisimiKontrolu18
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company18
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany18

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş18
------------------------------
Tags: DashboarddanUserProfileGecis18

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş18
------------------------------
Tags: DashboarddanAccountInformationaGecis18

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü18
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu18

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü18
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu18

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür














Dashboard sayfasından project sayfasına geçiş19
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis19

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından scenarios sayfasına geçiş19
--------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis19

* Scenarios tabına tıklanır
* Dashboarddan scenarios sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından plans sayfasına geçiş19
--------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis19

* Plans tabına tıklanır
* Dashboarddan plans sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Test Executions(auto) sayfasına geçiş19
--------------------------------
Tags: DashboardSayfasindanTestExecutionAutoSayfasinaGecis19

* Reports tabına tıkla
* Test Executions Auto tabına tıkla
* Dashboard sayfasından Test Executions(Auto) sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Scheduled Reports sayfasına geçiş19
--------------------------
Tags: DashboardSayfasindanScheduledReportsSayfasinaGecis19

* Reports tabına tıkla
* Scheduled Reports tabına tıkla
* Dashboard sayfasından Scheduled Reports sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Smart Prioritization Report sayfasına geçiş19
------------------------------
Tags: DashboardSayfasindanSmartPrioritizationReportSayfasinaGecis19

* Reports tabına tıkla
* Smart priorization reports tabına tıkla
* Dashboard sayfasından Smart Prioritization sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard sayfasından Automated Tests sayfasına geçiş19
------------------------------
Tags: DashboardSayfasindanAutomatedTestsSayfasinaGecis19

* Reports tabına tıkla
* Automated Tests tabına tıkla
* Dashboard sayfasından Automated Tests sayfasına başarılı şekilde yönlendiği görülmelidir

Dashboard Hamburger menü açılıp kapanma kontrolü19
------------------------------
Tags: DashboardHamburgerMenüAcilipKapanmaKontrolu19

* Dashboard sayfasında hamburger menü butonuna tıklanır
* Sol menünün daraldığı görülür
* Hamburger menü butonuna tıklanır
* Sol menünün genişlediği görülür

Dashboard sayfasında Active Scenarios Buton Kontrolü19
------------------------------
Tags: DashboardSayfasindaActiveScenariosButonKontrolu19

* Dashboard sayfasında active tests paneli butonuna tıklanır
* Active tests sayfasına başarılı şekilde yönlendiği görülür

Dashboard sayfasında Active Plans Buton Kontrolü19
------------------------------
Tags: DashboardActivePlansShowDetailsButonKontrolu19

* Dashboard sayfasında active plans paneli butonuna tıklanır
* Active plans sayfasına başarılı şekilde yönlendiği görülür

Dashboard dark mode butonu kontrolü19
------------------------------
Tags: DashboardDarkModeButonuKontrolu19

* Dashboard sayfasında güneş şeklindeki dark mode butonuna tıklanır
* Web sitesinin dark mode a geçtiği ve butonun ay şekline dönüştüğü görülür

Dashboard - Latest Test Runs kontrolü19
------------------------------
Tags: DashboardLatestTestRunsKontrolu19

* Koşulan son 10 planın rundate, runtime, test result ve details'i Latest Test Runs panelinde görünür

Dashboard Company değişimi kontrolü19
------------------------------
Tags: DashboardCompanyDegisimiKontrolu19
* CompanyDropdowndan developer company seçilir
* Company seçimi kısmında seçilen companye ait dataların ekrana geldiği görülür

Dashboard Company Seçimi - return to your own company19
------------------------------
Tags: DashboardCompanySecimiReturnToYourOwnCompany19

* Return to own company butonuna tıklanır
* Kendi ana company'e geçiş yapıldığı ve ana company nin dashboard sayfasına ulaşıldığı görülür

Dashboarddan User Profile geçiş19
------------------------------
Tags: DashboarddanUserProfileGecis19

* Hesap ismine tıklanır
* Profile tabına tıklanır
* User profile sayfasına yönlendiği görülür

Dashboarddan Account Information a geçiş19
------------------------------
Tags: DashboarddanAccountInformationaGecis19

* Hesap ismine tıklanır
* Account Information tabına tıklanır
* Account Information sayfasına yönlendiği görülür

Dashboardda logout işleminin yapılması kontolü19
------------------------------
Tags: DashboarddaLogoutIslemininYapilmasiKontolu19

* Hesap ismine tıklanır
* Log out tabına tıklanır
* Hesaptan çıkış yapıldığı ve login sayfasına yönlendiği görülür

Dashboard Latest Test Runs - Details butonu kontrolü19
------------------------------
Tags: DashboardLatestTestRunsDetailsButonuKontrolu19

* Daha önce koşulmuş herhangi bir planın details butonuna tıklanır
* Rapor detayları sayfasına yönlendiği görülür




**Dashboard sayfasından Smart Prioritization sayfasına geçiş408**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis408

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş408**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis408

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş409**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis409

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş410**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis410

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş411**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis411

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş412**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis412

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş413**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis413

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş414**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis414

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş415**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis415

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş416**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis416

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş417**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis417

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş418**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis418

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Project sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanProjectSayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scenarios sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanScenariosSayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Plans sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanPlansSayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Test Executions(Auto) sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanTest Executions(Auto)SayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Scheduled Reports sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanScheduled ReportsSayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Smart Prioritization sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanSmart PrioritizationSayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir


**Dashboard sayfasından Automated Tests sayfasına geçiş419**
-------------------------------
Tags: DashboardSayfasindanAutomated TestsSayfasinaGecis419

* Projects tabına tıklanır
* Dashboarddan project sayfasına başarılı şekilde yönlendiği görülmelidir

