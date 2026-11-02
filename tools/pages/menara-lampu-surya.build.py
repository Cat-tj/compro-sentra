"""Builds menara-lampu-surya.json (service page content, 5 languages). Spec numbers come from the GIDA mobile light tower
brochure (PT GIDA International Trading Indonesia); prices are deliberately NOT included (distributor price list is for partners)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(here, "starlink.json")))["langs"]

# model, mast m, LED, lumen/area, PV, battery kWh, genset, runtime h, note
ROWS = [
    ("GD5-S", "5", "2×50 W", "12.000 lm", "300 W", "2,4 (gel)", "–", "±20", "manual"),
    ("GD7-S", "7", "4×150 W", "90.000 lm", "1.785 W", "10,24", "–", "11–15", "manual"),
    ("GD9-S", "9", "4×200 W", "120.000 lm", "1.785 W", "20,48", "–", "12–20", "manual"),
    ("GD9-M", "9", "4×200 W", "120.000 lm", "1.785 W", "10,24", "5 kW", "9–12", "manual"),
    ("GD7-H", "7", "4×150 W", "90.000 lm", "1.785 W", "16,08", "5 kW", "15–24", "elektrik"),
    ("GD9-H", "9", "4×200 W", "120.000 lm", "1.785 W", "16,08", "5 kW", "11–18", "elektrik"),
    ("GDQ9-M", "9", "4×300 W", "180.000 lm", "3.570 W", "32", "5 kW", "15–24", "skid"),
    ("GDP04-M", "4,2", "3×100 W", "30.000 lm", "–", "2,88 (lepas)", "–", "8 (100%)", "elektrik"),
]
HEAD = {
 "": ("Model", "Tiang (m)", "Lampu LED", "Fluks", "Panel surya", "Baterai (kWh)", "Genset", "Operasi (jam)", "Tiang/dudukan"),
 "en": ("Model", "Mast (m)", "LED", "Flux", "Solar", "Battery (kWh)", "Generator", "Runtime (h)", "Mast/base"),
 "zh": ("型号", "灯杆(米)", "LED", "光通量", "光伏", "电池(kWh)", "发电机", "续航(小时)", "升降/底座"),
 "ko": ("모델", "마스트(m)", "LED", "광속", "태양광", "배터리(kWh)", "발전기", "가동(시간)", "마스트/베이스"),
 "ms": ("Model", "Tiang (m)", "LED", "Fluks", "Panel suria", "Bateri (kWh)", "Penjana", "Operasi (jam)", "Tiang/pangkalan"),
}
NOTE = {
 "manual": {"": "manual", "en": "manual", "zh": "手动", "ko": "수동", "ms": "manual"},
 "elektrik": {"": "elektrik", "en": "electric", "zh": "电动", "ko": "전동", "ms": "elektrik"},
 "skid": {"": "manual, skid", "en": "manual, skid", "zh": "手动，底座式", "ko": "수동, 스키드", "ms": "manual, skid"},
}
FOOT = {
 "": "Data dari brosur pabrikan (GIDA). Waktu operasi bergantung pada cuaca, beban, dan konfigurasi. Spesifikasi dapat berubah; penawaran resmi menjadi acuan.",
 "en": "Data from the manufacturer's brochure (GIDA). Runtime depends on weather, load and configuration. Specifications may change; the official quotation is the reference.",
 "zh": "数据来自制造商（GIDA）产品册。续航取决于天气、负载和配置。规格可能变更，以正式报价为准。",
 "ko": "제조사(GIDA) 브로셔 기준 데이터입니다. 가동 시간은 날씨, 부하, 구성에 따라 달라지며 사양은 변경될 수 있습니다. 공식 견적이 기준입니다.",
 "ms": "Data daripada risalah pengilang (GIDA). Masa operasi bergantung pada cuaca, beban dan konfigurasi. Spesifikasi boleh berubah; sebut harga rasmi menjadi rujukan.",
}
def table(lang):
    th = "".join(f'<th style="text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);white-space:nowrap">{h}</th>' for h in HEAD[lang])
    trs = ""
    for r in ROWS:
        cells = list(r[:8]) + [NOTE[r[8]][lang]]
        if lang != "":
            cells = [c.replace(".", ",") if False else c for c in cells]
        td = "".join(f'<td style="padding:10px 12px;border-bottom:1px solid var(--line);white-space:nowrap{";font-weight:700" if i == 0 else ""}">{c}</td>' for i, c in enumerate(cells))
        trs += f"<tr>{td}</tr>"
    return (f'<div class="rv" style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.92rem"><thead><tr>{th}</tr></thead>'
            f'<tbody>{trs}</tbody></table></div><p class="lead" style="margin-top:14px;font-size:.9rem">{FOOT[lang]}</p>')

L = {}
L[""] = dict(
 title="Menara Lampu Surya & Hybrid (Light Tower) untuk Tambang & Proyek | Sentra",
 description="Pengadaan mobile light tower tenaga surya dan hybrid untuk tambang, konstruksi, dan tanggap darurat: tiang 4–9 meter, LED 90.000–180.000 lumen, baterai LiFePO4, genset 5 kW opsional, dan opsi CCTV.",
 name="Menara Lampu Surya & Hybrid",
 h1="Menara lampu surya dan hybrid untuk area kerja yang gelap.",
 lead="Sentra bermitra dengan PT GIDA International Trading Indonesia untuk menyediakan mobile light tower: menara lampu yang bisa dipindah, memakai panel surya, baterai LiFePO4, dan genset cadangan pada versi hybrid. Dipakai di jalan hauling, pit, proyek konstruksi, pelabuhan, dan area darurat.",
 wa_text="Halo Sentra, saya ingin konsultasi menara lampu surya (light tower) untuk lokasi kami.",
 btn_kits="Lihat pilihan model",
 pains_h2="Masalah yang sering ada di lapangan",
 pains=[["Shift malam bekerja dengan penerangan seadanya","Area gelap menaikkan risiko kecelakaan dan memperlambat pekerjaan."],
        ["Menara lampu diesel boros BBM dan berisik","Solar untuk genset, perawatan mesin, dan getaran jadi biaya berulang."],
        ["Lokasi tanpa listrik jaringan","Proyek sementara dan area remote butuh penerangan yang bisa dipindah."],
        ["Penerangan dan keamanan berjalan sendiri-sendiri","Area yang terang tetap perlu kamera untuk pemantauan."]],
 do=[["Konsultasi kebutuhan penerangan","Luas area, tinggi tiang, jumlah lampu, dan jam kerja menentukan model yang cocok."],
     ["Pengadaan light tower","Model surya (S), hybrid (H dan M), skid, dan portabel (P) dari GIDA, sesuai penawaran resmi."],
     ["Pemilihan konfigurasi","Tiang manual atau elektrik, kapasitas baterai, port pengisian luar, dan rotasi lampu."],
     ["Opsi CCTV di menara","Beberapa model menyediakan opsi sistem CCTV, terhubung ke jaringan lokasi Anda."],
     ["Dukungan jaringan dan CCTV","Sentra dapat menyambungkan kamera ke jaringan site, Starlink, dan pemantauan terpusat."],
     ["Pendampingan pemakaian","Penjelasan cara menaikkan tiang, mengisi baterai, dan perawatan dasar mengikuti panduan pabrikan."]],
 kits_h2="Pilihan model", kits_lead="Delapan model dari brosur GIDA. Harga mengikuti penawaran resmi, silakan minta lewat WhatsApp.",
 sectors=[["Tambang","Jalan hauling, pit, disposal, dan stockpile untuk shift malam."],
          ["Proyek dan konstruksi","Penerangan sementara yang pindah mengikuti progres pekerjaan."],
          ["Pemerintahan dan tanggap darurat","Area bencana, acara, dan lokasi tanpa listrik jaringan."]],
 steps=["Tentukan area, tinggi tiang, dan jam kerja","Pilih model: surya, hybrid, atau portabel","Minta penawaran resmi sesuai konfigurasi","Pengiriman dan penjelasan pemakaian","Perawatan baterai, panel, dan mast secara berkala"],
 related=["Layanan: Pengadaan dan Instalasi CCTV","Layanan: Starlink untuk Bisnis","Layanan: IoT dan Hardware"],
 faq=[["Apa bedanya model surya, hybrid, dan skid?","Model S memakai panel surya dan baterai saja. Model H dan M menambah genset 5 kW sebagai cadangan saat cuaca buruk atau beban tinggi. Model Q memakai dudukan skid untuk diangkat, bukan ditarik. Model P kecil dan portabel dengan baterai yang bisa dilepas."],
      ["Berapa jam lampu bisa menyala?","Menurut brosur, antara sekitar 9 sampai 24 jam tergantung model dan konfigurasi, dan satu model portabel bisa 8 sampai 30 jam sesuai tingkat kecerahan. Hasil nyata bergantung pada cuaca, pengisian, dan beban."],
      ["Berapa harga menara lampu?","Harga bergantung model, konfigurasi, dan jumlah unit, dan mengikuti penawaran resmi dari pabrikan. Hubungi Sentra untuk meminta penawaran."],
      ["Bisakah menara dipasangi CCTV?","Beberapa model menyediakan CCTV sebagai opsi. Konfigurasinya didiskusikan sesuai kebutuhan lokasi dan jaringan yang ada."],
      ["Bagaimana dengan garansi dan suku cadang?","Garansi dan layanan purna jual mengikuti ketentuan pabrikan dan dicantumkan di penawaran."]],
 cta_h2="Butuh penerangan untuk lokasi Anda?", cta_p="Ceritakan area, jam kerja, dan sumber listrik yang ada. Diskusi awal gratis.",
 cta_trust=["Diskusi awal gratis","Penawaran resmi dari pabrikan","Model surya, hybrid, dan portabel"],
 card=dict(num="Penerangan lapangan", desc="Light tower surya dan hybrid untuk tambang, proyek, dan area tanpa listrik jaringan.", tags=["Surya", "Hybrid", "LiFePO4", "Opsi CCTV"], meta_after="pengadaan laptop & server, ", meta_add="menara lampu surya, "))
L["en"] = dict(
 title="Solar & Hybrid Light Towers for Mines & Construction | Sentra",
 description="Procurement of solar and hybrid mobile light towers for mines, construction and emergency response: 4 to 9 metre masts, 90,000 to 180,000 lumen LED, LiFePO4 batteries, optional 5 kW generator and CCTV option.",
 name="Solar & Hybrid Light Towers",
 h1="Solar and hybrid light towers for dark work areas.",
 lead="Sentra partners with PT GIDA International Trading Indonesia to supply mobile light towers: movable lighting masts with solar panels, LiFePO4 batteries and, on hybrid versions, a backup generator. Used on haul roads, pits, construction sites, ports and emergency areas.",
 wa_text="Hello Sentra, I would like advice on solar light towers for our site.",
 btn_kits="See model options",
 pains_h2="Problems we see in the field",
 pains=[["Night shifts working with poor lighting","Dark areas raise accident risk and slow work down."],
        ["Diesel light towers burn fuel and are noisy","Generator fuel, engine maintenance and vibration become recurring costs."],
        ["Sites without grid power","Temporary projects and remote areas need lighting that can be moved."],
        ["Lighting and security run separately","A lit area still needs cameras for monitoring."]],
 do=[["Lighting needs consultation","Area size, mast height, number of lamps and working hours decide the right model."],
     ["Light tower procurement","Solar (S), hybrid (H and M), skid (Q) and portable (P) models from GIDA, per official quotation."],
     ["Configuration choice","Manual or electric mast, battery capacity, external charging port and lamp rotation."],
     ["CCTV option on the tower","Several models offer an optional CCTV system, connected to your site network."],
     ["Network and CCTV support","Sentra can connect cameras to the site network, Starlink and central monitoring."],
     ["Usage guidance","Explaining how to raise the mast, charge batteries and basic care, following the manufacturer's guide."]],
 kits_h2="Model options", kits_lead="Eight models from the GIDA brochure. Prices follow the official quotation; request one via WhatsApp.",
 sectors=[["Mining","Haul roads, pits, disposal areas and stockpiles for night shifts."],
          ["Projects and construction","Temporary lighting that moves with work progress."],
          ["Government and emergency response","Disaster areas, events and sites without grid power."]],
 steps=["Define the area, mast height and working hours","Choose a model: solar, hybrid or portable","Request an official quotation for the configuration","Delivery and usage briefing","Regular care of batteries, panels and mast"],
 related=["Service: CCTV Procurement and Installation","Service: Starlink for Business","Service: IoT and Hardware"],
 faq=[["What is the difference between solar, hybrid and skid models?","S models use solar panels and batteries only. H and M models add a 5 kW generator as backup in bad weather or heavy load. Q models use a skid base to be lifted rather than towed. The P model is small and portable with removable batteries."],
      ["How many hours can the lights run?","According to the brochure, roughly 9 to 24 hours depending on model and configuration, and the portable model 8 to 30 hours depending on brightness level. Real results depend on weather, charging and load."],
      ["How much does a light tower cost?","Price depends on model, configuration and number of units, and follows the manufacturer's official quotation. Contact Sentra to request one."],
      ["Can a tower be fitted with CCTV?","Several models offer CCTV as an option. The configuration is discussed according to your site and existing network."],
      ["What about warranty and spare parts?","Warranty and after-sales follow the manufacturer's terms and are stated in the quotation."]],
 cta_h2="Need lighting for your site?", cta_p="Tell us the area, working hours and available power. The first discussion is free.",
 cta_trust=["Free first discussion","Official manufacturer quotation","Solar, hybrid and portable models"],
 card=dict(num="Field lighting", desc="Solar and hybrid light towers for mines, projects and sites without grid power.", tags=["Solar", "Hybrid", "LiFePO4", "CCTV option"], meta_after="laptop & server procurement, ", meta_add="solar light towers, "))
L["zh"] = dict(
 title="矿区与工地太阳能、混合动力移动灯塔 | Sentra",
 description="为矿区、施工和应急场景提供太阳能与混合动力移动灯塔：4 至 9 米灯杆、90,000 至 180,000 流明 LED、磷酸铁锂电池、可选 5 kW 发电机和 CCTV 选项。",
 name="太阳能与混合动力灯塔",
 h1="为黑暗作业区提供太阳能与混合动力灯塔。",
 lead="Sentra 与 PT GIDA International Trading Indonesia 合作供应移动灯塔：可移动的照明灯杆，配太阳能板、磷酸铁锂电池，混合型还配备备用发电机。适用于运输道路、采场、施工现场、港口和应急区域。",
 wa_text="您好 Sentra，我想咨询我们现场的太阳能灯塔。",
 btn_kits="查看型号",
 pains_h2="我们在现场常见的问题",
 pains=[["夜班照明不足","黑暗区域增加事故风险并拖慢工作。"],["柴油灯塔耗油且噪音大","发电机燃油、发动机维护和振动成为持续成本。"],["现场没有市电","临时项目和偏远区域需要可移动的照明。"],["照明与安防各自为政","明亮的区域仍需要摄像头监控。"]],
 do=[["照明需求咨询","区域大小、灯杆高度、灯具数量和工作时间决定合适的型号。"],["灯塔采购","GIDA 的太阳能（S）、混合（H、M）、底座式（Q）和便携（P）型号，以正式报价为准。"],["配置选择","手动或电动灯杆、电池容量、外部充电口和灯具旋转。"],["灯塔上的 CCTV 选项","部分型号提供 CCTV 选项，并接入现场网络。"],["网络与 CCTV 支持","Sentra 可将摄像头接入现场网络、Starlink 和集中监控。"],["使用指导","按制造商指南说明升杆、充电和基本保养。"]],
 kits_h2="型号选择", kits_lead="来自 GIDA 产品册的八个型号。价格以正式报价为准，请通过 WhatsApp 索取。",
 sectors=[["矿区","夜班的运输道路、采场、排土场和堆场。"],["项目与施工","随工程进度移动的临时照明。"],["政府与应急","灾区、活动和无市电场所。"]],
 steps=["确定区域、灯杆高度和工作时间","选择型号：太阳能、混合或便携","按配置索取正式报价","交付与使用说明","定期保养电池、光伏板和灯杆"],
 related=["服务：CCTV 采购与安装","服务：企业 Starlink","服务：IoT 与硬件"],
 faq=[["太阳能、混合和底座式型号有什么区别？","S 型只用光伏板和电池；H 和 M 型增加 5 kW 发电机，在恶劣天气或高负载时备用；Q 型为底座式，用吊装而非拖行；P 型小巧便携，电池可拆卸。"],["灯能亮多久？","根据产品册，约 9 至 24 小时，取决于型号和配置；便携型根据亮度档位为 8 至 30 小时。实际结果取决于天气、充电和负载。"],["灯塔多少钱？","价格取决于型号、配置和数量，以制造商正式报价为准，请联系 Sentra 索取。"],["灯塔可以加装 CCTV 吗？","部分型号提供 CCTV 选项，具体配置按现场和现有网络讨论。"],["保修和备件如何？","保修和售后遵循制造商条款，并写入报价单。"]],
 cta_h2="您的现场需要照明吗？", cta_p="告诉我们区域、工作时间和可用电源。首次沟通免费。",
 cta_trust=["首次沟通免费","制造商正式报价","太阳能、混合和便携型号"],
 card=dict(num="现场照明", desc="适用于矿区、工程和无市电场所的太阳能与混合动力灯塔。", tags=["太阳能", "混合动力", "磷酸铁锂", "CCTV 选项"], meta_after="笔记本与服务器采购、", meta_add="太阳能灯塔、"))
L["ko"] = dict(
 title="광산·건설 현장용 태양광·하이브리드 이동식 조명탑 | Sentra",
 description="광산, 건설, 긴급 대응을 위한 태양광·하이브리드 이동식 조명탑 조달: 4~9m 마스트, 90,000~180,000 루멘 LED, LiFePO4 배터리, 선택형 5kW 발전기와 CCTV 옵션.",
 name="태양광·하이브리드 조명탑",
 h1="어두운 작업 현장을 위한 태양광·하이브리드 조명탑.",
 lead="Sentra는 PT GIDA International Trading Indonesia와 협력해 이동식 조명탑을 공급합니다. 태양광 패널과 LiFePO4 배터리를 쓰고, 하이브리드형은 예비 발전기를 갖춥니다. 운반로, 채굴장, 건설 현장, 항만, 긴급 구역에서 사용합니다.",
 wa_text="안녕하세요 Sentra, 저희 현장의 태양광 조명탑 상담을 원합니다.",
 btn_kits="모델 보기",
 pains_h2="현장에서 자주 보는 문제",
 pains=[["야간 작업의 부족한 조명","어두운 구역은 사고 위험을 높이고 작업을 늦춥니다."],["디젤 조명탑은 연료를 많이 쓰고 시끄럽다","발전기 연료, 엔진 정비, 진동이 반복 비용이 됩니다."],["전력망이 없는 현장","임시 프로젝트와 외진 지역은 옮길 수 있는 조명이 필요합니다."],["조명과 보안이 따로 운영됨","밝은 구역에도 감시용 카메라가 필요합니다."]],
 do=[["조명 요구 상담","구역 크기, 마스트 높이, 등 수, 작업 시간이 모델을 정합니다."],["조명탑 조달","GIDA의 태양광(S), 하이브리드(H, M), 스키드(Q), 휴대형(P) 모델을 공식 견적에 따라 공급합니다."],["구성 선택","수동·전동 마스트, 배터리 용량, 외부 충전 포트, 조명 회전."],["조명탑 CCTV 옵션","일부 모델은 CCTV 옵션을 제공하며 현장 네트워크에 연결됩니다."],["네트워크·CCTV 지원","Sentra가 카메라를 현장 네트워크, Starlink, 통합 관제에 연결할 수 있습니다."],["사용 안내","제조사 가이드에 따라 마스트 올리기, 충전, 기본 관리를 설명합니다."]],
 kits_h2="모델 선택", kits_lead="GIDA 브로셔의 8개 모델입니다. 가격은 공식 견적에 따르며 WhatsApp으로 요청하세요.",
 sectors=[["광산","야간 작업용 운반로, 채굴장, 배토장, 야적장."],["프로젝트·건설","공정에 따라 옮기는 임시 조명."],["정부·긴급 대응","재난 지역, 행사, 전력망이 없는 곳."]],
 steps=["구역, 마스트 높이, 작업 시간 정하기","모델 선택: 태양광, 하이브리드, 휴대형","구성에 맞는 공식 견적 요청","배송 및 사용 안내","배터리, 패널, 마스트 정기 관리"],
 related=["서비스: CCTV 조달·설치","서비스: 기업용 Starlink","서비스: IoT 및 하드웨어"],
 faq=[["태양광, 하이브리드, 스키드 모델의 차이는?","S 모델은 태양광 패널과 배터리만 씁니다. H와 M 모델은 악천후나 고부하에 대비한 5kW 발전기를 더합니다. Q 모델은 견인이 아니라 들어 올리는 스키드 베이스이고, P 모델은 탈착식 배터리의 소형 휴대형입니다."],["조명은 몇 시간 켜지나요?","브로셔 기준 모델과 구성에 따라 약 9~24시간이며, 휴대형은 밝기 단계에 따라 8~30시간입니다. 실제는 날씨, 충전, 부하에 따라 달라집니다."],["가격은 얼마인가요?","모델, 구성, 수량에 따라 다르며 제조사의 공식 견적에 따릅니다. Sentra에 견적을 요청하세요."],["조명탑에 CCTV를 달 수 있나요?","일부 모델이 CCTV를 옵션으로 제공합니다. 현장과 기존 네트워크에 맞춰 구성을 논의합니다."],["보증과 부품은 어떻게 되나요?","보증과 사후 서비스는 제조사 조건에 따르며 견적서에 명시됩니다."]],
 cta_h2="현장에 조명이 필요하신가요?", cta_p="구역, 작업 시간, 사용 가능한 전원을 알려 주세요. 첫 상담은 무료입니다.",
 cta_trust=["첫 상담 무료","제조사 공식 견적","태양광·하이브리드·휴대형 모델"],
 card=dict(num="현장 조명", desc="광산, 프로젝트, 전력망이 없는 곳을 위한 태양광·하이브리드 조명탑.", tags=["태양광", "하이브리드", "LiFePO4", "CCTV 옵션"], meta_after="노트북·서버 조달, ", meta_add="태양광 조명탑, "))
L["ms"] = dict(
 title="Menara Lampu Suria & Hibrid untuk Lombong & Pembinaan | Sentra",
 description="Perolehan menara lampu mudah alih suria dan hibrid untuk lombong, pembinaan dan tindak balas kecemasan: tiang 4 hingga 9 meter, LED 90,000 hingga 180,000 lumen, bateri LiFePO4, penjana 5 kW pilihan dan pilihan CCTV.",
 name="Menara Lampu Suria & Hibrid",
 h1="Menara lampu suria dan hibrid untuk kawasan kerja yang gelap.",
 lead="Sentra bekerjasama dengan PT GIDA International Trading Indonesia untuk membekalkan menara lampu mudah alih: tiang pencahayaan boleh alih dengan panel suria, bateri LiFePO4 dan, pada versi hibrid, penjana sandaran. Digunakan di jalan angkut, pit, tapak pembinaan, pelabuhan dan kawasan kecemasan.",
 wa_text="Hai Sentra, saya ingin berunding tentang menara lampu suria untuk lokasi kami.",
 btn_kits="Lihat pilihan model",
 pains_h2="Masalah yang sering ada di lapangan",
 pains=[["Syif malam dengan pencahayaan lemah","Kawasan gelap meningkatkan risiko kemalangan dan melambatkan kerja."],["Menara lampu diesel boros bahan api dan bising","Bahan api penjana, penyelenggaraan enjin dan getaran menjadi kos berulang."],["Lokasi tanpa elektrik grid","Projek sementara dan kawasan terpencil memerlukan pencahayaan yang boleh dialihkan."],["Pencahayaan dan keselamatan berasingan","Kawasan terang tetap memerlukan kamera."]],
 do=[["Perundingan keperluan pencahayaan","Keluasan kawasan, ketinggian tiang, bilangan lampu dan waktu kerja menentukan model."],["Perolehan menara lampu","Model suria (S), hibrid (H dan M), skid (Q) dan mudah alih (P) daripada GIDA, mengikut sebut harga rasmi."],["Pilihan konfigurasi","Tiang manual atau elektrik, kapasiti bateri, port pengecasan luar dan putaran lampu."],["Pilihan CCTV pada menara","Beberapa model menyediakan pilihan CCTV, disambungkan ke rangkaian tapak."],["Sokongan rangkaian dan CCTV","Sentra boleh menyambungkan kamera ke rangkaian tapak, Starlink dan pemantauan pusat."],["Bimbingan penggunaan","Penerangan menaikkan tiang, mengecas bateri dan penjagaan asas mengikut panduan pengilang."]],
 kits_h2="Pilihan model", kits_lead="Lapan model daripada risalah GIDA. Harga mengikut sebut harga rasmi; mohon melalui WhatsApp.",
 sectors=[["Perlombongan","Jalan angkut, pit, kawasan pelupusan dan stokpail untuk syif malam."],["Projek dan pembinaan","Pencahayaan sementara yang berpindah mengikut kemajuan kerja."],["Kerajaan dan tindak balas kecemasan","Kawasan bencana, acara dan lokasi tanpa elektrik grid."]],
 steps=["Tentukan kawasan, ketinggian tiang dan waktu kerja","Pilih model: suria, hibrid atau mudah alih","Mohon sebut harga rasmi mengikut konfigurasi","Penghantaran dan taklimat penggunaan","Penjagaan berkala bateri, panel dan tiang"],
 related=["Perkhidmatan: Perolehan dan Pemasangan CCTV","Perkhidmatan: Starlink untuk Perniagaan","Perkhidmatan: IoT dan Perkakasan"],
 faq=[["Apakah beza model suria, hibrid dan skid?","Model S hanya menggunakan panel suria dan bateri. Model H dan M menambah penjana 5 kW sebagai sandaran. Model Q menggunakan pangkalan skid untuk diangkat, bukan ditunda. Model P kecil dan mudah alih dengan bateri boleh tanggal."],["Berapa jam lampu boleh menyala?","Menurut risalah, kira-kira 9 hingga 24 jam bergantung pada model dan konfigurasi, dan model mudah alih 8 hingga 30 jam mengikut tahap kecerahan. Hasil sebenar bergantung pada cuaca, pengecasan dan beban."],["Berapakah harga menara lampu?","Harga bergantung pada model, konfigurasi dan bilangan unit, dan mengikut sebut harga rasmi pengilang."],["Bolehkah menara dipasang CCTV?","Beberapa model menyediakan CCTV sebagai pilihan."],["Bagaimana dengan waranti dan alat ganti?","Waranti dan khidmat lepas jualan mengikut syarat pengilang dan dinyatakan dalam sebut harga."]],
 cta_h2="Perlukan pencahayaan untuk lokasi anda?", cta_p="Beritahu kami kawasan, waktu kerja dan sumber kuasa yang ada. Perbincangan awal percuma.",
 cta_trust=["Perbincangan awal percuma","Sebut harga rasmi pengilang","Model suria, hibrid dan mudah alih"],
 card=dict(num="Pencahayaan lapangan", desc="Menara lampu suria dan hibrid untuk lombong, projek dan lokasi tanpa elektrik grid.", tags=["Suria", "Hibrid", "LiFePO4", "Pilihan CCTV"], meta_after="perolehan komputer riba & pelayan, ", meta_add="menara lampu suria, "))

langs = {}
for k, t in L.items():
    b = base[k]
    d = {x: b[x] for x in ("crumb_home", "crumb_services", "btn_consult", "do_h2", "sectors_h2", "sector_link", "steps_h2", "related_h2", "faq_h2", "cta_wa", "cta_msg")}
    d.update(t); d["kits_html"] = table(k)
    langs[k] = d
out = {"slug": "menara-lampu-surya", "date": "2026-11-02", "template": "instalasi-infrastruktur", "list_after": "pengadaan-it", "card_icon": "sun",
       "hero_img": "/assets/img/art/menara-lampu.webp", "og_img": "/assets/og/art-menara-lampu.jpg",
       "do_icons": ["sun", "box", "wrench", "cam", "wifi", "pin"], "sector_icons": ["pick", "crane", "gov"],
       "sector_links": ["/industri/pertambangan", "/services/instalasi-infrastruktur", "/industri/pemerintahan"],
       "related_links": ["/services/pengadaan-cctv", "/services/starlink", "/services/iot-hardware"],
       "llms": "- [Solar & Hybrid Light Towers](https://www.sentratechnology.com/en/services/menara-lampu-surya): mobile solar and hybrid light towers from partner PT GIDA International Trading Indonesia for mines, construction, ports and emergency response: 4 to 9 metre masts, 90,000 to 180,000 lumen LED, LiFePO4 batteries, optional 5 kW generator and optional CCTV; prices follow the manufacturer's official quotation.",
       "langs": langs}
json.dump(out, open(os.path.join(here, "menara-lampu-surya.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
