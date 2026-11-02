"""Builds energi-surya-container.json and kamera-surya-4g.json (service pages, 5 languages) from the GIDA brochure
(PT GIDA International Trading Indonesia). No prices: the distributor price list is for partners only."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(here, "starlink.json")))["langs"]
BOILER = ("crumb_home", "crumb_services", "btn_consult", "do_h2", "sectors_h2", "sector_link", "steps_h2", "related_h2", "faq_h2", "cta_wa", "cta_msg")
TH = 'style="text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);white-space:nowrap"'
TD = 'style="padding:10px 12px;border-bottom:1px solid var(--line)'

def table(head, rows, foot):
    th = "".join(f"<th {TH}>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f'<td {TD}{";font-weight:700" if i == 0 else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return (f'<div class="rv" style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.92rem"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'
            f'<p class="lead" style="margin-top:14px;font-size:.9rem">{foot}</p>')

# ---------- container PV + storage ----------
ESS = [("GD-8GP-P20K", "20 kWp", "–"), ("GD-10GP-P40K", "25 kWp", "–"), ("GD-20HQ-P70K", "76 kWp", "–"), ("GD-20HQ-P110K", "135 kWp", "–"),
       ("GD-40GP-P150K", "150 kWp", "–"), ("GD-40HQ-P270K", "270 kWp", "–"), ("GD-08GP-P20K/30", "20 kWp", "30 kWh"), ("GD-08GP-P25K/60", "25 kWp", "60 kWh"),
       ("GD-20HQ-P80K/260", "80 kWp", "260 kWh"), ("GD-40HQ-P190K/260", "190 kWp", "260 kWh"), ("GD-40HQ-P200K/520", "200 kWp", "520 kWh")]
ESS_HEAD = {"": ("Model container", "Daya panel surya", "Kapasitas baterai"), "en": ("Container model", "Solar panel power", "Battery capacity"),
            "zh": ("集装箱型号", "光伏功率", "电池容量"), "ko": ("컨테이너 모델", "태양광 출력", "배터리 용량"), "ms": ("Model kontena", "Kuasa panel suria", "Kapasiti bateri")}
ESS_FOOT = {"": "Dari brosur GIDA. Angka \"KP\" di brosur dibaca sebagai kWp. Kapasitas baterai tidak dicantumkan untuk enam model pertama; ketersediaan dan konfigurasi mengikuti penawaran resmi.",
            "en": "From the GIDA brochure. The \"KP\" figures in the brochure are read as kWp. Battery capacity is not stated for the first six models; availability and configuration follow the official quotation.",
            "zh": "来自 GIDA 产品册。册中的“KP”按 kWp 理解。前六个型号未标明电池容量；供货与配置以正式报价为准。",
            "ko": "GIDA 브로셔 기준입니다. 브로셔의 \"KP\"는 kWp로 해석했습니다. 앞의 여섯 모델은 배터리 용량이 명시되지 않았으며 공급 및 구성은 공식 견적에 따릅니다.",
            "ms": "Daripada risalah GIDA. Angka \"KP\" dalam risalah dibaca sebagai kWp. Kapasiti bateri tidak dinyatakan untuk enam model pertama; ketersediaan dan konfigurasi mengikut sebut harga rasmi."}
E1 = {}
E1[""] = dict(
 title="Kontainer Tenaga Surya & Penyimpanan Energi (PV + Baterai) | Sentra",
 description="Pengadaan kontainer tenaga surya dengan penyimpanan baterai untuk industri, tambang, proyek, dan cadangan darurat: panel 20 sampai 270 kWp, baterai hingga 520 kWh, bisa beroperasi off-grid.",
 name="Kontainer Surya & Penyimpanan Energi",
 h1="Kontainer tenaga surya dan baterai untuk lokasi yang butuh listrik mandiri.",
 lead="Sentra adalah mitra resmi PT GIDA International Trading Indonesia dan menyediakan GD-MES: kontainer yang menyatukan panel surya, penyimpanan baterai, dan sistem kontrol dalam satu paket yang bisa dipindah. Dirancang untuk keperluan komersial dan industri, termasuk lokasi tanpa jaringan listrik.",
 wa_text="Halo Sentra, saya ingin konsultasi kontainer tenaga surya dan penyimpanan energi untuk lokasi kami.",
 btn_kits="Lihat pilihan model",
 pains_h2="Masalah yang sering ada di lapangan",
 pains=[["Lokasi tanpa listrik jaringan atau jaringannya tidak stabil","Kamp, proyek, dan area remote bergantung pada genset diesel."],
        ["Biaya BBM genset terus berulang","Solar, pengiriman, dan perawatan mesin menumpuk dari bulan ke bulan."],
        ["Listrik padam mengganggu operasi","Server, CCTV, jaringan, dan peralatan penting butuh cadangan daya."],
        ["Instalasi panel dan baterai terpisah rumit","Fondasi, penempatan, dan integrasi sering memakan waktu di lokasi."]],
 do=[["Konsultasi kebutuhan daya","Daftar beban, jam pakai, dan target cadangan menentukan kapasitas panel dan baterai."],
     ["Pengadaan kontainer PV dan baterai","Model GD-MES dari 20 sampai 270 kWp dan baterai hingga 520 kWh, sesuai penawaran resmi."],
     ["Pemilihan konfigurasi","Ukuran kontainer, daya panel, kapasitas baterai, dan kebutuhan off-grid atau cadangan."],
     ["Integrasi dengan CCTV dan jaringan","Daya untuk kamera, Starlink, dan perangkat jaringan di site Anda."],
     ["Perencanaan lokasi","Penempatan, akses, dan kebutuhan pondasi ringan mengikuti panduan pabrikan."],
     ["Dukungan setelah pembelian","Pertanyaan teknis dan perawatan diteruskan sesuai ketentuan pabrikan."]],
 kits_h2="Pilihan model", kits_lead="Sebelas konfigurasi dari brosur GIDA. Harga mengikuti penawaran resmi, silakan minta lewat WhatsApp.",
 sectors=[["Tambang dan kamp","Kantor site, mess, dan fasilitas di area remote tanpa jaringan listrik."],["Proyek dan konstruksi","Daya sementara untuk lokasi kerja yang berpindah."],["Industri dan cadangan darurat","Sumber listrik mandiri atau cadangan untuk pabrik dan fasilitas penting."]],
 steps=["Catat beban listrik dan jam pakai","Tentukan kapasitas panel dan baterai","Pilih konfigurasi dan minta penawaran resmi","Pengiriman, penempatan, dan serah terima","Pemantauan dan perawatan berkala"],
 related=["Layanan: Menara Lampu Surya dan Hybrid","Layanan: Starlink untuk Bisnis","Layanan: Pengadaan dan Instalasi CCTV"],
 faq=[["Apakah bisa beroperasi tanpa jaringan listrik?","Menurut brosur pabrikan, sistem dapat beroperasi sepenuhnya mandiri (off-grid). Kecocokan untuk beban Anda perlu dihitung dari daftar beban dan jam pakai."],
      ["Berapa lama pemasangannya?","Brosur menyebut instalasi tidak memerlukan pondasi yang rumit. Waktu nyata bergantung pada lokasi dan model, dan dikonfirmasi dalam penawaran."],
      ["Berapa harganya?","Harga bergantung pada konfigurasi dan jumlah, dan mengikuti penawaran resmi dari pabrikan. Hubungi Sentra untuk meminta penawaran."],
      ["Apakah bisa menghidupkan peralatan berat?","Tergantung daya inverter dan kapasitas baterai. Perlu hitung beban puncak dan arus awal peralatan sebelum memilih model."],
      ["Bagaimana dengan garansi?","Garansi dan layanan purna jual mengikuti ketentuan pabrikan dan dicantumkan di penawaran."]],
 cta_h2="Butuh listrik mandiri untuk lokasi Anda?", cta_p="Ceritakan beban listrik, jam pakai, dan lokasi. Diskusi awal gratis.",
 cta_trust=["Diskusi awal gratis","Penawaran resmi dari pabrikan","Panel 20 sampai 270 kWp"],
 card=dict(num="Energi surya", desc="Kontainer panel surya dan baterai untuk lokasi tanpa listrik jaringan atau butuh cadangan daya.", tags=["Panel surya", "Baterai", "Off-grid", "Kontainer"], meta_after="menara lampu surya, ", meta_add="penyimpanan energi surya, "))
E1["en"] = dict(
 title="Solar Container & Energy Storage (PV + Battery) | Sentra",
 description="Procurement of solar containers with battery storage for industry, mines, projects and emergency backup: 20 to 270 kWp of panels, batteries up to 520 kWh, able to run off-grid.",
 name="Solar Container & Energy Storage",
 h1="Solar and battery containers for sites that need their own power.",
 lead="Sentra is an official partner of PT GIDA International Trading Indonesia and supplies GD-MES: a container that combines solar panels, battery storage and controls in one movable package. Designed for commercial and industrial use, including sites without grid power.",
 wa_text="Hello Sentra, I would like advice on a solar container and energy storage for our site.",
 btn_kits="See model options",
 pains_h2="Problems we see in the field",
 pains=[["Sites with no grid power or an unstable grid","Camps, projects and remote areas depend on diesel generators."],["Generator fuel costs keep recurring","Diesel, delivery and engine maintenance pile up month after month."],["Power cuts disrupt operations","Servers, CCTV, networks and key equipment need backup power."],["Installing panels and batteries separately is complex","Foundations, placement and integration often eat time on site."]],
 do=[["Power needs consultation","The load list, hours of use and backup target decide panel and battery capacity."],["Procurement of PV and battery containers","GD-MES models from 20 to 270 kWp and batteries up to 520 kWh, per official quotation."],["Configuration choice","Container size, panel power, battery capacity, and off-grid or backup needs."],["Integration with CCTV and networks","Power for cameras, Starlink and network equipment at your site."],["Site planning","Placement, access and light foundation needs follow the manufacturer's guide."],["Support after purchase","Technical questions and maintenance are passed on under the manufacturer's terms."]],
 kits_h2="Model options", kits_lead="Eleven configurations from the GIDA brochure. Prices follow the official quotation; request one via WhatsApp.",
 sectors=[["Mines and camps","Site offices, mess halls and facilities in remote areas without grid power."],["Projects and construction","Temporary power for work sites that move."],["Industry and emergency backup","Independent or backup power for factories and critical facilities."]],
 steps=["Record electrical loads and hours of use","Determine panel and battery capacity","Choose a configuration and request an official quotation","Delivery, placement and handover","Monitoring and regular maintenance"],
 related=["Service: Solar & Hybrid Light Towers","Service: Starlink for Business","Service: CCTV Procurement and Installation"],
 faq=[["Can it run without grid power?","According to the manufacturer's brochure, the system can run fully independently (off-grid). Suitability for your load must be calculated from the load list and hours of use."],["How long does installation take?","The brochure says no complex foundation is needed. Real time depends on site and model, and is confirmed in the quotation."],["How much does it cost?","Price depends on configuration and quantity, and follows the manufacturer's official quotation. Contact Sentra to request one."],["Can it run heavy equipment?","It depends on inverter power and battery capacity. Peak load and starting current must be calculated before choosing a model."],["What about warranty?","Warranty and after-sales follow the manufacturer's terms and are stated in the quotation."]],
 cta_h2="Need independent power for your site?", cta_p="Tell us the electrical load, hours of use and location. The first discussion is free.",
 cta_trust=["Free first discussion","Official manufacturer quotation","20 to 270 kWp of panels"],
 card=dict(num="Solar energy", desc="Solar panel and battery containers for sites without grid power or needing backup.", tags=["Solar panels", "Battery", "Off-grid", "Container"], meta_after="solar light towers, ", meta_add="solar energy storage, "))
E1["zh"] = dict(
 title="太阳能集装箱与储能系统（光伏＋电池）| Sentra",
 description="为工业、矿区、工程和应急备用提供带电池储能的太阳能集装箱：光伏 20 至 270 kWp，电池最高 520 kWh，可离网运行。",
 name="太阳能集装箱与储能",
 h1="为需要自主供电的现场提供太阳能与电池集装箱。",
 lead="Sentra 是 PT GIDA International Trading Indonesia 的官方合作伙伴，供应 GD-MES：把光伏板、电池储能和控制系统集成在一个可移动的集装箱里，面向商业和工业场景，包括没有市电的场所。",
 wa_text="您好 Sentra，我想咨询我们现场的太阳能集装箱和储能系统。",
 btn_kits="查看型号",
 pains_h2="我们在现场常见的问题",
 pains=[["现场没有市电或电网不稳定","营地、项目和偏远区域依赖柴油发电机。"],["发电机燃油成本不断重复","柴油、运输和发动机维护逐月累积。"],["停电影响运营","服务器、CCTV、网络和关键设备需要备用电源。"],["光伏板和电池分开安装很复杂","基础、摆放和集成常占用现场时间。"]],
 do=[["用电需求咨询","负载清单、使用时间和备用目标决定光伏和电池容量。"],["光伏与电池集装箱采购","GD-MES 型号从 20 至 270 kWp，电池最高 520 kWh，以正式报价为准。"],["配置选择","集装箱尺寸、光伏功率、电池容量，以及离网或备用需求。"],["与 CCTV 和网络集成","为现场的摄像头、Starlink 和网络设备供电。"],["现场规划","摆放、通道和轻型基础要求遵循制造商指南。"],["购买后的支持","技术问题和维护按制造商条款转达。"]],
 kits_h2="型号选择", kits_lead="来自 GIDA 产品册的十一种配置。价格以正式报价为准，请通过 WhatsApp 索取。",
 sectors=[["矿区与营地","偏远无市电区域的现场办公室、宿舍和设施。"],["项目与施工","为流动的作业现场提供临时电力。"],["工业与应急备用","工厂和关键设施的独立或备用电源。"]],
 steps=["记录用电负载和使用时间","确定光伏和电池容量","选择配置并索取正式报价","交付、就位与交接","监控与定期维护"],
 related=["服务：太阳能与混合动力灯塔","服务：企业 Starlink","服务：CCTV 采购与安装"],
 faq=[["可以离网运行吗？","根据制造商产品册，系统可完全独立（离网）运行。是否适合您的负载，需要根据负载清单和使用时间计算。"],["安装需要多久？","产品册称无需复杂基础。实际时间取决于现场和型号，并在报价中确认。"],["价格是多少？","价格取决于配置和数量，以制造商正式报价为准，请联系 Sentra 索取。"],["能带动大型设备吗？","取决于逆变器功率和电池容量。选型前需计算峰值负载和启动电流。"],["保修如何？","保修和售后遵循制造商条款，并写入报价单。"]],
 cta_h2="您的现场需要自主供电吗？", cta_p="告诉我们用电负载、使用时间和地点。首次沟通免费。",
 cta_trust=["首次沟通免费","制造商正式报价","光伏 20 至 270 kWp"],
 card=dict(num="太阳能", desc="适用于无市电或需要备用电源场所的太阳能板与电池集装箱。", tags=["光伏板", "电池", "离网", "集装箱"], meta_after="太阳能灯塔、", meta_add="太阳能储能、"))
E1["ko"] = dict(
 title="태양광 컨테이너·에너지 저장 시스템(PV+배터리) | Sentra",
 description="산업, 광산, 프로젝트, 비상 백업을 위한 배터리 저장형 태양광 컨테이너 조달: 태양광 20~270kWp, 배터리 최대 520kWh, 오프그리드 운영 가능.",
 name="태양광 컨테이너·에너지 저장",
 h1="자체 전력이 필요한 현장을 위한 태양광·배터리 컨테이너.",
 lead="Sentra는 PT GIDA International Trading Indonesia의 공식 파트너로서 GD-MES를 공급합니다. 태양광 패널, 배터리 저장, 제어 시스템을 하나의 이동 가능한 컨테이너에 통합한 제품으로, 전력망이 없는 현장을 포함한 상업·산업용입니다.",
 wa_text="안녕하세요 Sentra, 저희 현장의 태양광 컨테이너와 에너지 저장 시스템 상담을 원합니다.",
 btn_kits="모델 보기",
 pains_h2="현장에서 자주 보는 문제",
 pains=[["전력망이 없거나 불안정한 현장","캠프, 프로젝트, 외진 지역은 디젤 발전기에 의존합니다."],["발전기 연료비가 계속 반복됨","경유, 운송, 엔진 정비가 매달 쌓입니다."],["정전이 운영을 방해함","서버, CCTV, 네트워크, 핵심 장비에는 예비 전원이 필요합니다."],["패널과 배터리를 따로 설치하기 복잡함","기초, 배치, 연동에 현장 시간이 많이 듭니다."]],
 do=[["전력 수요 상담","부하 목록, 사용 시간, 백업 목표가 패널과 배터리 용량을 정합니다."],["PV·배터리 컨테이너 조달","20~270kWp GD-MES 모델과 최대 520kWh 배터리를 공식 견적에 따라 공급합니다."],["구성 선택","컨테이너 크기, 패널 출력, 배터리 용량, 오프그리드 또는 백업 요구."],["CCTV·네트워크 연동","현장의 카메라, Starlink, 네트워크 장비에 전력을 공급합니다."],["현장 계획","배치, 접근, 가벼운 기초 요건은 제조사 가이드를 따릅니다."],["구매 후 지원","기술 문의와 유지보수는 제조사 조건에 따라 전달됩니다."]],
 kits_h2="모델 선택", kits_lead="GIDA 브로셔의 11개 구성입니다. 가격은 공식 견적에 따르며 WhatsApp으로 요청하세요.",
 sectors=[["광산·캠프","전력망이 없는 외진 지역의 현장 사무실, 숙소, 시설."],["프로젝트·건설","이동하는 작업 현장의 임시 전력."],["산업·비상 백업","공장과 핵심 시설의 독립 또는 백업 전원."]],
 steps=["전기 부하와 사용 시간 기록","패널과 배터리 용량 결정","구성 선택 및 공식 견적 요청","배송, 설치 위치 선정, 인도","모니터링과 정기 유지보수"],
 related=["서비스: 태양광·하이브리드 조명탑","서비스: 기업용 Starlink","서비스: CCTV 조달·설치"],
 faq=[["전력망 없이 운영할 수 있나요?","제조사 브로셔에 따르면 완전 독립(오프그리드) 운영이 가능합니다. 귀사의 부하에 맞는지는 부하 목록과 사용 시간으로 계산해야 합니다."],["설치에는 얼마나 걸리나요?","브로셔는 복잡한 기초가 필요 없다고 합니다. 실제 시간은 현장과 모델에 따라 다르며 견적에서 확인합니다."],["가격은 얼마인가요?","구성과 수량에 따라 다르며 제조사의 공식 견적에 따릅니다. Sentra에 견적을 요청하세요."],["중장비도 가동할 수 있나요?","인버터 출력과 배터리 용량에 따라 다릅니다. 모델 선택 전에 피크 부하와 기동 전류를 계산해야 합니다."],["보증은 어떻게 되나요?","보증과 사후 서비스는 제조사 조건에 따르며 견적서에 명시됩니다."]],
 cta_h2="현장에 자체 전력이 필요하신가요?", cta_p="전기 부하, 사용 시간, 위치를 알려 주세요. 첫 상담은 무료입니다.",
 cta_trust=["첫 상담 무료","제조사 공식 견적","태양광 20~270kWp"],
 card=dict(num="태양광 에너지", desc="전력망이 없거나 백업이 필요한 곳을 위한 태양광 패널·배터리 컨테이너.", tags=["태양광 패널", "배터리", "오프그리드", "컨테이너"], meta_after="태양광 조명탑, ", meta_add="태양광 에너지 저장, "))
E1["ms"] = dict(
 title="Kontena Suria & Storan Tenaga (PV + Bateri) | Sentra",
 description="Perolehan kontena suria dengan storan bateri untuk industri, lombong, projek dan sandaran kecemasan: panel 20 hingga 270 kWp, bateri sehingga 520 kWh, boleh beroperasi luar grid.",
 name="Kontena Suria & Storan Tenaga",
 h1="Kontena suria dan bateri untuk lokasi yang memerlukan kuasa sendiri.",
 lead="Sentra ialah rakan kongsi rasmi PT GIDA International Trading Indonesia dan membekalkan GD-MES: kontena yang menggabungkan panel suria, storan bateri dan kawalan dalam satu pakej boleh alih. Direka untuk kegunaan komersial dan industri, termasuk lokasi tanpa grid elektrik.",
 wa_text="Hai Sentra, saya ingin berunding tentang kontena suria dan storan tenaga untuk lokasi kami.",
 btn_kits="Lihat pilihan model",
 pains_h2="Masalah yang sering ada di lapangan",
 pains=[["Lokasi tanpa grid elektrik atau grid tidak stabil","Kem, projek dan kawasan terpencil bergantung pada penjana diesel."],["Kos bahan api penjana berulang","Diesel, penghantaran dan penyelenggaraan enjin terkumpul setiap bulan."],["Gangguan bekalan menjejaskan operasi","Pelayan, CCTV, rangkaian dan peralatan penting memerlukan kuasa sandaran."],["Pemasangan panel dan bateri berasingan rumit","Asas, penempatan dan integrasi memakan masa di lokasi."]],
 do=[["Perundingan keperluan kuasa","Senarai beban, waktu guna dan sasaran sandaran menentukan kapasiti panel dan bateri."],["Perolehan kontena PV dan bateri","Model GD-MES 20 hingga 270 kWp dan bateri sehingga 520 kWh, mengikut sebut harga rasmi."],["Pilihan konfigurasi","Saiz kontena, kuasa panel, kapasiti bateri dan keperluan luar grid atau sandaran."],["Integrasi dengan CCTV dan rangkaian","Kuasa untuk kamera, Starlink dan peranti rangkaian di tapak anda."],["Perancangan lokasi","Penempatan, akses dan keperluan asas ringan mengikut panduan pengilang."],["Sokongan selepas pembelian","Soalan teknikal dan penyelenggaraan disalurkan mengikut syarat pengilang."]],
 kits_h2="Pilihan model", kits_lead="Sebelas konfigurasi daripada risalah GIDA. Harga mengikut sebut harga rasmi; mohon melalui WhatsApp.",
 sectors=[["Lombong dan kem","Pejabat tapak, asrama dan kemudahan di kawasan terpencil tanpa grid elektrik."],["Projek dan pembinaan","Kuasa sementara untuk tapak kerja yang berpindah."],["Industri dan sandaran kecemasan","Kuasa bebas atau sandaran untuk kilang dan kemudahan penting."]],
 steps=["Catat beban elektrik dan waktu guna","Tentukan kapasiti panel dan bateri","Pilih konfigurasi dan mohon sebut harga rasmi","Penghantaran, penempatan dan serah terima","Pemantauan dan penyelenggaraan berkala"],
 related=["Perkhidmatan: Menara Lampu Suria & Hibrid","Perkhidmatan: Starlink untuk Perniagaan","Perkhidmatan: Perolehan dan Pemasangan CCTV"],
 faq=[["Bolehkah beroperasi tanpa grid elektrik?","Menurut risalah pengilang, sistem boleh beroperasi sepenuhnya bebas (luar grid). Kesesuaian untuk beban anda perlu dikira daripada senarai beban dan waktu guna."],["Berapa lama pemasangan?","Risalah menyatakan tiada asas rumit diperlukan. Masa sebenar bergantung pada lokasi dan model."],["Berapakah harganya?","Harga mengikut sebut harga rasmi pengilang."],["Bolehkah ia menghidupkan peralatan berat?","Bergantung pada kuasa penyongsang dan kapasiti bateri."],["Bagaimana dengan waranti?","Waranti mengikut syarat pengilang dan dinyatakan dalam sebut harga."]],
 cta_h2="Perlukan kuasa sendiri untuk lokasi anda?", cta_p="Beritahu kami beban elektrik, waktu guna dan lokasi. Perbincangan awal percuma.",
 cta_trust=["Perbincangan awal percuma","Sebut harga rasmi pengilang","Panel 20 hingga 270 kWp"],
 card=dict(num="Tenaga suria", desc="Kontena panel suria dan bateri untuk lokasi tanpa grid elektrik atau memerlukan kuasa sandaran.", tags=["Panel suria", "Bateri", "Luar grid", "Kontena"], meta_after="menara lampu suria, ", meta_add="storan tenaga suria, "))

# ---------- solar 4G camera ----------
CAM = {
 "": [("Resolusi", "2560×1440 (2K), kompresi H.265"), ("Lensa", "Dua lensa fix 4 mm + 4 mm, sudut pandang 80°"), ("PTZ", "Horizontal 355°, vertikal 90°"),
      ("Penglihatan malam", "Berwarna penuh (0,1 Lux) dan hitam-putih (0,01 Lux); lampu IR dan LED putih jangkauan 30 m"), ("Deteksi", "Sensor PIR dan deteksi bentuk manusia, jarak 0 sampai 12 m, sudut 120°"),
      ("Audio", "Speaker 1 W dan mikrofon, jangkauan sekitar 20 m"), ("Jaringan", "4G, pita FDD B1/B3/B5/B8 (termasuk Indonesia)"), ("Penyimpanan", "Cloud (video alarm) dan kartu TF hingga 128 GB"),
      ("Daya", "Panel surya 7,5 W dan baterai 8000 mAh"), ("Ketahanan", "IP66, suhu kerja -30 sampai 50 °C"), ("Aplikasi", "iCam365 (Android dan iOS)")],
 "en": [("Resolution", "2560×1440 (2K), H.265 compression"), ("Lens", "Dual fixed lens 4 mm + 4 mm, 80° viewing angle"), ("PTZ", "Horizontal 355°, vertical 90°"),
        ("Night vision", "Full colour (0.1 Lux) and black-and-white (0.01 Lux); IR and white LED range 30 m"), ("Detection", "PIR sensor and human-shape detection, 0 to 12 m, 120° angle"),
        ("Audio", "1 W speaker and microphone, about 20 m pickup"), ("Network", "4G, FDD bands B1/B3/B5/B8 (including Indonesia)"), ("Storage", "Cloud (alarm videos) and TF card up to 128 GB"),
        ("Power", "7.5 W solar panel and 8000 mAh battery"), ("Durability", "IP66, operating temperature -30 to 50 °C"), ("App", "iCam365 (Android and iOS)")],
 "zh": [("分辨率", "2560×1440（2K），H.265 压缩"), ("镜头", "双定焦 4 mm + 4 mm，视角 80°"), ("云台", "水平 355°，垂直 90°"),
        ("夜视", "全彩（0.1 Lux）和黑白（0.01 Lux）；红外和白光 LED 距离 30 米"), ("检测", "PIR 传感器和人形检测，0 至 12 米，120° 角度"),
        ("音频", "1 W 扬声器和麦克风，拾音约 20 米"), ("网络", "4G，FDD 频段 B1/B3/B5/B8（含印尼）"), ("存储", "云端（报警视频）和最高 128 GB TF 卡"),
        ("供电", "7.5 W 太阳能板和 8000 mAh 电池"), ("耐用性", "IP66，工作温度 -30 至 50 °C"), ("应用", "iCam365（Android 和 iOS）")],
 "ko": [("해상도", "2560×1440(2K), H.265 압축"), ("렌즈", "4 mm + 4 mm 이중 고정 렌즈, 시야각 80°"), ("PTZ", "수평 355°, 수직 90°"),
        ("야간 시야", "풀컬러(0.1 Lux)와 흑백(0.01 Lux), 적외선·백색 LED 30 m"), ("감지", "PIR 센서와 사람 형태 감지, 0~12 m, 120° 각도"),
        ("오디오", "1 W 스피커와 마이크, 수음 약 20 m"), ("네트워크", "4G, FDD 대역 B1/B3/B5/B8(인도네시아 포함)"), ("저장", "클라우드(경보 영상)와 최대 128 GB TF 카드"),
        ("전원", "7.5 W 태양광 패널과 8000 mAh 배터리"), ("내구성", "IP66, 작동 온도 -30~50 °C"), ("앱", "iCam365(Android, iOS)")],
 "ms": [("Resolusi", "2560×1440 (2K), mampatan H.265"), ("Kanta", "Dua kanta tetap 4 mm + 4 mm, sudut pandangan 80°"), ("PTZ", "Mendatar 355°, menegak 90°"),
        ("Penglihatan malam", "Berwarna penuh (0.1 Lux) dan hitam putih (0.01 Lux); jarak IR dan LED putih 30 m"), ("Pengesanan", "Penderia PIR dan pengesanan bentuk manusia, 0 hingga 12 m, sudut 120°"),
        ("Audio", "Pembesar suara 1 W dan mikrofon, jarak sekitar 20 m"), ("Rangkaian", "4G, jalur FDD B1/B3/B5/B8 (termasuk Indonesia)"), ("Storan", "Awan (video penggera) dan kad TF sehingga 128 GB"),
        ("Kuasa", "Panel suria 7.5 W dan bateri 8000 mAh"), ("Ketahanan", "IP66, suhu operasi -30 hingga 50 °C"), ("Aplikasi", "iCam365 (Android dan iOS)")]}
CAM_HEAD = {"": ("Spesifikasi", "Nilai"), "en": ("Specification", "Value"), "zh": ("规格", "参数"), "ko": ("사양", "값"), "ms": ("Spesifikasi", "Nilai")}
CAM_FOOT = {"": "Model GDKJ-D440 dari brosur GIDA. Kebutuhan kartu SIM atau paket data, ketersediaan, dan konfigurasi mengikuti penawaran resmi.",
            "en": "Model GDKJ-D440 from the GIDA brochure. SIM card or data plan needs, availability and configuration follow the official quotation.",
            "zh": "GDKJ-D440 型号，来自 GIDA 产品册。SIM 卡或流量套餐需求、供货和配置以正式报价为准。",
            "ko": "GIDA 브로셔의 GDKJ-D440 모델입니다. SIM 카드·데이터 요금제 요건, 공급, 구성은 공식 견적에 따릅니다.",
            "ms": "Model GDKJ-D440 daripada risalah GIDA. Keperluan kad SIM atau pelan data, ketersediaan dan konfigurasi mengikut sebut harga rasmi."}
C = {}
C[""] = dict(
 title="Kamera CCTV Tenaga Surya 4G Tanpa Kabel (GDKJ-D440) | Sentra",
 description="Pengadaan kamera CCTV tenaga surya 4G untuk lokasi tanpa listrik dan WiFi: resolusi 2K, putar 355°, deteksi manusia PIR, penglihatan malam berwarna, pantau dari ponsel.",
 name="Kamera CCTV Surya 4G",
 h1="Kamera CCTV tenaga surya 4G untuk lokasi tanpa listrik dan WiFi.",
 lead="Sentra adalah mitra resmi PT GIDA International Trading Indonesia dan menyediakan kamera GDKJ-D440: kamera ganda 2K yang ditenagai panel surya dan baterai, terhubung lewat jaringan 4G, dan dipantau dari ponsel. Cocok untuk kebun, proyek, gudang, dan lokasi sementara.",
 wa_text="Halo Sentra, saya ingin konsultasi kamera CCTV surya 4G untuk lokasi kami.",
 btn_kits="Lihat spesifikasi",
 pains_h2="Masalah yang sering ada di lapangan",
 pains=[["Lokasi tanpa listrik dan tanpa kabel jaringan","Menarik kabel ke kebun, proyek, atau gudang jauh terlalu mahal."],["Kamera berhenti saat listrik padam","Kamera yang bergantung pada listrik atau WiFi mati saat dibutuhkan."],["Pencurian di lokasi sementara","Material, alat, dan hasil panen butuh pengawasan tanpa pemasangan permanen."],["Tidak tahu kejadian saat tidak di lokasi","Pemilik butuh peringatan dan rekaman yang bisa dibuka dari ponsel."]],
 do=[["Konsultasi lokasi","Sudut pandang, paparan matahari, dan sinyal 4G di lokasi menentukan kecocokan."],["Pengadaan kamera surya 4G","Model GDKJ-D440 dengan panel surya, baterai, dan konektivitas 4G, sesuai penawaran resmi."],["Pengaturan aplikasi dan peringatan","Penyambungan ke aplikasi iCam365 dan pengaturan notifikasi deteksi manusia."],["Penempatan dan mounting","Posisi dan tinggi yang menangkap area penting dan menerima sinar matahari."],["Kombinasi dengan CCTV kabel","Dipadukan dengan sistem kamera VIGI dan NVR Sentra di titik yang terjangkau kabel."],["Dukungan setelah pembelian","Pertanyaan teknis diteruskan sesuai ketentuan pabrikan."]],
 kits_h2="Spesifikasi", kits_lead="Spesifikasi utama GDKJ-D440 dari brosur GIDA. Harga mengikuti penawaran resmi, silakan minta lewat WhatsApp.",
 sectors=[["Perkebunan dan lahan","Pos jaga, gudang panen, dan akses jauh dari jaringan listrik."],["Proyek dan konstruksi","Pengawasan material dan alat di lokasi sementara."],["Gudang, toko, dan rumah","Titik tanpa kabel yang sulit dijangkau instalasi biasa."]],
 steps=["Tentukan titik dan area yang diawasi","Cek paparan matahari dan sinyal 4G","Pilih jumlah kamera dan minta penawaran resmi","Pemasangan dan pengaturan aplikasi","Pemeriksaan panel dan baterai secara berkala"],
 related=["Layanan: Pengadaan dan Instalasi CCTV","Layanan: Kontainer Surya dan Penyimpanan Energi","Layanan: Starlink untuk Bisnis"],
 faq=[["Apakah perlu WiFi atau listrik di lokasi?","Menurut brosur, kamera ditenagai panel surya dan baterai serta terhubung lewat 4G, sehingga tidak butuh WiFi atau listrik jaringan. Cakupan sinyal 4G di lokasi tetap harus dicek."],["Apakah rekaman tersimpan?","Kamera mendukung penyimpanan cloud untuk video alarm dan kartu TF hingga 128 GB. Rekaman penuh sepanjang waktu tidak dijadwalkan dalam brosur; sistem mengutamakan perekaman saat ada deteksi."],["Bagaimana jika cuaca mendung berhari-hari?","Baterai 8000 mAh menyimpan cadangan, tetapi pengisian bergantung pada sinar matahari. Lokasi yang terlalu teduh atau sering mendung mungkin butuh solusi lain."],["Apakah perlu kartu SIM?","Kamera terhubung lewat 4G, sehingga kartu SIM dan paket data kemungkinan diperlukan. Konfirmasi dalam penawaran."],["Berapa harganya?","Harga mengikuti penawaran resmi dari pabrikan. Hubungi Sentra untuk meminta penawaran."]],
 cta_h2="Butuh kamera untuk lokasi tanpa listrik?", cta_p="Ceritakan lokasi, area yang diawasi, dan sinyal seluler yang ada. Diskusi awal gratis.",
 cta_trust=["Diskusi awal gratis","Penawaran resmi dari pabrikan","Pantau dari ponsel"],
 card=dict(num="Kamera tanpa kabel", desc="Kamera CCTV surya 4G 2K untuk lokasi tanpa listrik dan WiFi, dipantau dari ponsel.", tags=["Surya", "4G", "2K", "Deteksi manusia"], meta_after="penyimpanan energi surya, ", meta_add="kamera CCTV surya 4G, "))
C["en"] = dict(
 title="Solar 4G Wireless CCTV Camera (GDKJ-D440) | Sentra",
 description="Procurement of solar-powered 4G CCTV cameras for sites without power or WiFi: 2K resolution, 355° pan, PIR human detection, colour night vision, monitoring from a phone.",
 name="Solar 4G CCTV Camera",
 h1="Solar-powered 4G CCTV cameras for sites without power or WiFi.",
 lead="Sentra is an official partner of PT GIDA International Trading Indonesia and supplies the GDKJ-D440 camera: a dual-lens 2K camera powered by a solar panel and battery, connected over 4G and monitored from a phone. Suited to plantations, projects, warehouses and temporary sites.",
 wa_text="Hello Sentra, I would like advice on solar 4G CCTV cameras for our site.",
 btn_kits="See specifications",
 pains_h2="Problems we see in the field",
 pains=[["Sites with no power and no network cable","Running cable to a plantation, project or remote warehouse is too costly."],["Cameras stop when power fails","Cameras that depend on mains power or WiFi go dark when needed."],["Theft at temporary sites","Materials, tools and harvest need watching without permanent installation."],["No idea what happened while away","Owners need alerts and recordings that open from a phone."]],
 do=[["Site consultation","Viewing angle, sun exposure and 4G signal at the site decide suitability."],["Procurement of solar 4G cameras","The GDKJ-D440 with solar panel, battery and 4G connectivity, per official quotation."],["App and alert setup","Connection to the iCam365 app and human-detection notification settings."],["Placement and mounting","Position and height that capture the key area and receive sunlight."],["Combination with wired CCTV","Paired with Sentra's VIGI cameras and NVR at points cable can reach."],["Support after purchase","Technical questions are passed on under the manufacturer's terms."]],
 kits_h2="Specifications", kits_lead="Key GDKJ-D440 specifications from the GIDA brochure. Prices follow the official quotation; request one via WhatsApp.",
 sectors=[["Plantations and land","Guard posts, harvest stores and access far from the power grid."],["Projects and construction","Watching materials and tools at temporary sites."],["Warehouses, shops and homes","Cable-free points that ordinary installation cannot easily reach."]],
 steps=["Define the points and areas to watch","Check sun exposure and 4G signal","Choose the number of cameras and request an official quotation","Installation and app setup","Regular check of panel and battery"],
 related=["Service: CCTV Procurement and Installation","Service: Solar Container & Energy Storage","Service: Starlink for Business"],
 faq=[["Does the site need WiFi or power?","According to the brochure, the camera runs on a solar panel and battery and connects over 4G, so it needs neither WiFi nor grid power. 4G coverage at the site must still be checked."],["Is footage recorded?","The camera supports cloud storage for alarm videos and a TF card up to 128 GB. The brochure does not describe round-the-clock recording; the system prioritises recording on detection."],["What about several cloudy days?","The 8000 mAh battery stores a reserve, but charging depends on sunlight. A very shaded or often cloudy site may need another solution."],["Is a SIM card needed?","The camera connects over 4G, so a SIM card and data plan are likely needed. Confirm in the quotation."],["How much does it cost?","Price follows the manufacturer's official quotation. Contact Sentra to request one."]],
 cta_h2="Need a camera for a site without power?", cta_p="Tell us the location, the area to watch and the mobile signal available. The first discussion is free.",
 cta_trust=["Free first discussion","Official manufacturer quotation","Monitor from your phone"],
 card=dict(num="Wireless camera", desc="2K solar 4G CCTV cameras for sites without power or WiFi, monitored from a phone.", tags=["Solar", "4G", "2K", "Human detection"], meta_after="solar energy storage, ", meta_add="solar 4G CCTV camera, "))
C["zh"] = dict(
 title="太阳能 4G 无线 CCTV 摄像头（GDKJ-D440）| Sentra",
 description="为无电源、无 WiFi 的场所提供太阳能 4G CCTV 摄像头：2K 分辨率、355° 转动、PIR 人形检测、彩色夜视，可用手机查看。",
 name="太阳能 4G CCTV 摄像头",
 h1="为无电无 WiFi 的场所提供太阳能 4G CCTV 摄像头。",
 lead="Sentra 是 PT GIDA International Trading Indonesia 的官方合作伙伴，供应 GDKJ-D440 摄像头：双镜头 2K，由太阳能板和电池供电，通过 4G 联网，用手机查看。适用于种植园、工程、仓库和临时场所。",
 wa_text="您好 Sentra，我想咨询我们现场的太阳能 4G CCTV 摄像头。",
 btn_kits="查看规格",
 pains_h2="我们在现场常见的问题",
 pains=[["现场没有电也没有网线","给种植园、项目或偏远仓库拉线成本太高。"],["断电时摄像头停止工作","依赖市电或 WiFi 的摄像头在需要时失灵。"],["临时场所被盗","材料、工具和收成需要监控，又不想做永久安装。"],["不在现场时不知道发生了什么","业主需要能用手机查看的提醒和录像。"]],
 do=[["现场咨询","现场的视角、日照和 4G 信号决定是否适合。"],["太阳能 4G 摄像头采购","带太阳能板、电池和 4G 连接的 GDKJ-D440，以正式报价为准。"],["应用与提醒设置","连接 iCam365 应用并设置人形检测通知。"],["位置与安装","选择能拍到重点区域并接收阳光的位置和高度。"],["与有线 CCTV 组合","在线缆可达的点位与 Sentra 的 VIGI 摄像头和 NVR 搭配。"],["购买后的支持","技术问题按制造商条款转达。"]],
 kits_h2="规格", kits_lead="来自 GIDA 产品册的 GDKJ-D440 主要规格。价格以正式报价为准，请通过 WhatsApp 索取。",
 sectors=[["种植园与土地","远离电网的岗亭、收获仓库和通道。"],["项目与施工","临时场所的材料和工具监控。"],["仓库、商店与住宅","普通安装难以到达的无线点位。"]],
 steps=["确定要监控的点位和区域","检查日照和 4G 信号","确定摄像头数量并索取正式报价","安装与应用设置","定期检查太阳能板和电池"],
 related=["服务：CCTV 采购与安装","服务：太阳能集装箱与储能","服务：企业 Starlink"],
 faq=[["现场需要 WiFi 或电源吗？","根据产品册，摄像头由太阳能板和电池供电，并通过 4G 联网，因此无需 WiFi 或市电。现场的 4G 覆盖仍需确认。"],["会录像吗？","摄像头支持报警视频的云存储和最高 128 GB 的 TF 卡。产品册未描述全天候录像，系统以检测触发录像为主。"],["连续几天阴天怎么办？","8000 mAh 电池可储备电量，但充电依赖阳光。过于阴暗或常阴天的场所可能需要其他方案。"],["需要 SIM 卡吗？","摄像头通过 4G 联网，可能需要 SIM 卡和流量套餐，请在报价中确认。"],["价格是多少？","价格以制造商正式报价为准，请联系 Sentra 索取。"]],
 cta_h2="需要为无电场所安装摄像头吗？", cta_p="告诉我们地点、监控区域和可用的移动信号。首次沟通免费。",
 cta_trust=["首次沟通免费","制造商正式报价","手机查看"],
 card=dict(num="无线摄像头", desc="适用于无电无 WiFi 场所的 2K 太阳能 4G CCTV 摄像头，用手机查看。", tags=["太阳能", "4G", "2K", "人形检测"], meta_after="太阳能储能、", meta_add="太阳能 4G CCTV 摄像头、"))
C["ko"] = dict(
 title="태양광 4G 무선 CCTV 카메라(GDKJ-D440) | Sentra",
 description="전기와 WiFi가 없는 곳을 위한 태양광 4G CCTV 카메라 조달: 2K 해상도, 355° 회전, PIR 사람 감지, 컬러 야간 시야, 휴대폰 모니터링.",
 name="태양광 4G CCTV 카메라",
 h1="전기와 WiFi가 없는 현장을 위한 태양광 4G CCTV 카메라.",
 lead="Sentra는 PT GIDA International Trading Indonesia의 공식 파트너로서 GDKJ-D440 카메라를 공급합니다. 태양광 패널과 배터리로 작동하는 듀얼 렌즈 2K 카메라로, 4G로 연결되어 휴대폰으로 확인합니다. 농장, 프로젝트, 창고, 임시 현장에 적합합니다.",
 wa_text="안녕하세요 Sentra, 저희 현장의 태양광 4G CCTV 카메라 상담을 원합니다.",
 btn_kits="사양 보기",
 pains_h2="현장에서 자주 보는 문제",
 pains=[["전기도 네트워크 케이블도 없는 현장","농장, 프로젝트, 외진 창고까지 케이블을 까는 비용이 너무 큽니다."],["정전되면 카메라가 멈춤","상용 전원이나 WiFi에 의존하는 카메라는 필요할 때 꺼집니다."],["임시 현장의 도난","자재, 공구, 수확물을 영구 설치 없이 감시해야 합니다."],["자리를 비웠을 때 무슨 일이 있었는지 모름","휴대폰으로 열 수 있는 알림과 녹화가 필요합니다."]],
 do=[["현장 상담","현장의 시야각, 일조량, 4G 신호가 적합성을 정합니다."],["태양광 4G 카메라 조달","태양광 패널, 배터리, 4G 연결을 갖춘 GDKJ-D440을 공식 견적에 따라 공급합니다."],["앱·알림 설정","iCam365 앱 연결과 사람 감지 알림 설정."],["위치와 설치","주요 구역을 비추고 햇빛을 받는 위치와 높이."],["유선 CCTV와의 조합","케이블이 닿는 지점에는 Sentra의 VIGI 카메라와 NVR을 함께 사용합니다."],["구매 후 지원","기술 문의는 제조사 조건에 따라 전달됩니다."]],
 kits_h2="사양", kits_lead="GIDA 브로셔의 GDKJ-D440 주요 사양입니다. 가격은 공식 견적에 따르며 WhatsApp으로 요청하세요.",
 sectors=[["농장·토지","전력망에서 먼 초소, 수확물 창고, 진입로."],["프로젝트·건설","임시 현장의 자재와 공구 감시."],["창고·상점·주택","일반 설치가 어려운 무선 지점."]],
 steps=["감시할 지점과 구역 정하기","일조량과 4G 신호 확인","카메라 수 결정 및 공식 견적 요청","설치와 앱 설정","패널과 배터리 정기 점검"],
 related=["서비스: CCTV 조달·설치","서비스: 태양광 컨테이너·에너지 저장","서비스: 기업용 Starlink"],
 faq=[["현장에 WiFi나 전기가 필요한가요?","브로셔에 따르면 카메라는 태양광 패널과 배터리로 작동하고 4G로 연결되므로 WiFi나 상용 전원이 필요 없습니다. 현장의 4G 커버리지는 확인해야 합니다."],["영상이 저장되나요?","경보 영상용 클라우드 저장과 최대 128GB TF 카드를 지원합니다. 브로셔는 24시간 상시 녹화를 설명하지 않으며 감지 시 녹화를 우선합니다."],["며칠 동안 흐리면 어떻게 되나요?","8000mAh 배터리가 예비 전력을 저장하지만 충전은 햇빛에 달려 있습니다. 그늘이 많거나 자주 흐린 곳은 다른 방법이 필요할 수 있습니다."],["SIM 카드가 필요한가요?","4G로 연결되므로 SIM 카드와 데이터 요금제가 필요할 수 있습니다. 견적에서 확인하세요."],["가격은 얼마인가요?","제조사의 공식 견적에 따릅니다. Sentra에 견적을 요청하세요."]],
 cta_h2="전기가 없는 곳에 카메라가 필요하신가요?", cta_p="위치, 감시 구역, 사용 가능한 이동통신 신호를 알려 주세요. 첫 상담은 무료입니다.",
 cta_trust=["첫 상담 무료","제조사 공식 견적","휴대폰으로 확인"],
 card=dict(num="무선 카메라", desc="전기와 WiFi가 없는 곳을 위한 2K 태양광 4G CCTV 카메라, 휴대폰으로 확인.", tags=["태양광", "4G", "2K", "사람 감지"], meta_after="태양광 에너지 저장, ", meta_add="태양광 4G CCTV 카메라, "))
C["ms"] = dict(
 title="Kamera CCTV Suria 4G Tanpa Wayar (GDKJ-D440) | Sentra",
 description="Perolehan kamera CCTV suria 4G untuk lokasi tanpa elektrik dan WiFi: resolusi 2K, putaran 355°, pengesanan manusia PIR, penglihatan malam berwarna, pantau dari telefon.",
 name="Kamera CCTV Suria 4G",
 h1="Kamera CCTV suria 4G untuk lokasi tanpa elektrik dan WiFi.",
 lead="Sentra ialah rakan kongsi rasmi PT GIDA International Trading Indonesia dan membekalkan kamera GDKJ-D440: kamera dua kanta 2K berkuasa panel suria dan bateri, bersambung melalui 4G dan dipantau dari telefon. Sesuai untuk ladang, projek, gudang dan lokasi sementara.",
 wa_text="Hai Sentra, saya ingin berunding tentang kamera CCTV suria 4G untuk lokasi kami.",
 btn_kits="Lihat spesifikasi",
 pains_h2="Masalah yang sering ada di lapangan",
 pains=[["Lokasi tanpa elektrik dan tanpa kabel rangkaian","Menarik kabel ke ladang, projek atau gudang terpencil terlalu mahal."],["Kamera berhenti apabila elektrik terputus","Kamera yang bergantung pada elektrik atau WiFi mati ketika diperlukan."],["Kecurian di lokasi sementara","Bahan, alatan dan hasil tuaian perlu dipantau tanpa pemasangan kekal."],["Tidak tahu kejadian semasa tiada di lokasi","Pemilik memerlukan amaran dan rakaman yang boleh dibuka dari telefon."]],
 do=[["Perundingan lokasi","Sudut pandangan, pendedahan matahari dan isyarat 4G menentukan kesesuaian."],["Perolehan kamera suria 4G","GDKJ-D440 dengan panel suria, bateri dan sambungan 4G, mengikut sebut harga rasmi."],["Tetapan aplikasi dan amaran","Sambungan ke aplikasi iCam365 dan tetapan pemberitahuan pengesanan manusia."],["Penempatan dan pemasangan","Kedudukan dan ketinggian yang menangkap kawasan penting dan menerima cahaya matahari."],["Gabungan dengan CCTV berwayar","Digabungkan dengan kamera VIGI dan NVR Sentra di titik yang dicapai kabel."],["Sokongan selepas pembelian","Soalan teknikal disalurkan mengikut syarat pengilang."]],
 kits_h2="Spesifikasi", kits_lead="Spesifikasi utama GDKJ-D440 daripada risalah GIDA. Harga mengikut sebut harga rasmi; mohon melalui WhatsApp.",
 sectors=[["Ladang dan tanah","Pondok pengawal, stor tuaian dan akses jauh dari grid elektrik."],["Projek dan pembinaan","Pemantauan bahan dan alatan di lokasi sementara."],["Gudang, kedai dan rumah","Titik tanpa wayar yang sukar dicapai pemasangan biasa."]],
 steps=["Tentukan titik dan kawasan yang dipantau","Semak pendedahan matahari dan isyarat 4G","Pilih bilangan kamera dan mohon sebut harga rasmi","Pemasangan dan tetapan aplikasi","Semakan berkala panel dan bateri"],
 related=["Perkhidmatan: Perolehan dan Pemasangan CCTV","Perkhidmatan: Kontena Suria & Storan Tenaga","Perkhidmatan: Starlink untuk Perniagaan"],
 faq=[["Adakah lokasi memerlukan WiFi atau elektrik?","Menurut risalah, kamera berkuasa panel suria dan bateri serta bersambung melalui 4G, jadi tidak memerlukan WiFi atau elektrik grid. Liputan 4G di lokasi tetap perlu disemak."],["Adakah rakaman disimpan?","Kamera menyokong storan awan untuk video penggera dan kad TF sehingga 128 GB."],["Bagaimana jika mendung beberapa hari?","Bateri 8000 mAh menyimpan simpanan, tetapi pengecasan bergantung pada cahaya matahari."],["Adakah kad SIM diperlukan?","Kamera bersambung melalui 4G, jadi kad SIM dan pelan data mungkin diperlukan."],["Berapakah harganya?","Harga mengikut sebut harga rasmi pengilang."]],
 cta_h2="Perlukan kamera untuk lokasi tanpa elektrik?", cta_p="Beritahu kami lokasi, kawasan yang dipantau dan isyarat selular yang ada. Perbincangan awal percuma.",
 cta_trust=["Perbincangan awal percuma","Sebut harga rasmi pengilang","Pantau dari telefon"],
 card=dict(num="Kamera tanpa wayar", desc="Kamera CCTV suria 4G 2K untuk lokasi tanpa elektrik dan WiFi, dipantau dari telefon.", tags=["Suria", "4G", "2K", "Pengesanan manusia"], meta_after="storan tenaga suria, ", meta_add="kamera CCTV suria 4G, "))

def build(slug, T, kits, listafter, icon, hero, og, doi, soi, sol, rel, llms):
    langs = {}
    for k, t in T.items():
        d = {x: base[k][x] for x in BOILER}; d.update(t); d["kits_html"] = kits(k); langs[k] = d
    out = dict(slug=slug, date="2026-11-02", template="instalasi-infrastruktur", list_after=listafter, card_icon=icon, hero_img=hero, og_img=og,
               do_icons=doi, sector_icons=soi, sector_links=sol, related_links=rel, llms=llms, langs=langs)
    json.dump(out, open(os.path.join(here, slug + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

build("energi-surya-container", E1, lambda k: table(ESS_HEAD[k], ESS, ESS_FOOT[k]), "menara-lampu-surya", "sun", "/assets/img/art/energi-surya.webp", "/assets/og/art-energi-surya.jpg",
      ["sun", "box", "wrench", "wifi", "pin", "shuffle"], ["pick", "crane", "factory"], ["/industri/pertambangan", "/services/instalasi-infrastruktur", "/industri/korporasi"],
      ["/services/menara-lampu-surya", "/services/starlink", "/services/pengadaan-cctv"],
      "- [Solar Container & Energy Storage](https://www.sentratechnology.com/en/services/energi-surya-container): GD-MES containers combining solar panels (20 to 270 kWp), battery storage (up to 520 kWh) and controls from official partner PT GIDA International Trading Indonesia, for commercial and industrial sites, mines, projects and emergency backup, able to run off-grid; prices follow the manufacturer's official quotation.")
build("kamera-surya-4g", C, lambda k: table(CAM_HEAD[k], CAM[k], CAM_FOOT[k]), "energi-surya-container", "cam", "/assets/img/art/kamera-surya-4g.webp", "/assets/og/art-kamera-surya-4g.jpg",
      ["cam", "sun", "phone", "pin", "nvr", "wrench"], ["leaf", "crane", "shop"], ["/industri/pertambangan", "/services/instalasi-infrastruktur", "/industri/korporasi"],
      ["/services/pengadaan-cctv", "/services/energi-surya-container", "/services/starlink"],
      "- [Solar 4G CCTV Camera](https://www.sentratechnology.com/en/services/kamera-surya-4g): GDKJ-D440 solar-powered 4G wireless cameras from official partner PT GIDA International Trading Indonesia: dual-lens 2K, 355° pan, PIR human detection, colour night vision, cloud and TF card storage, phone app, for sites without power or WiFi; prices follow the manufacturer's official quotation.")
print("ok")
