SLUG = "fleet-management-tambang"
DATE = "2026-10-30"
COVER = "/assets/img/art/products-fleet.webp"
OG_IMAGE = "/assets/og/art-products-fleet.jpg"

LANGS = {
    "": {
        "title": "Fleet Management Tambang Batubara: Cara Kerja GPS, Sensor BBM, dan Laporan",
        "description": "Cara kerja fleet management untuk tambang dan hauling batubara: GPS dan replay, sensor BBM, data CAN-Bus alat berat, geofence, perilaku operator, pengingat servis, dan laporan harian.",
        "category": "Armada & IoT",
        "lead": "Di tambang, setiap unit hauling dan alat berat adalah biaya besar yang bergerak. Fleet management membuat posisinya, BBM-nya, dan cara mengoperasikannya terlihat dari satu dashboard. Ini cara kerjanya dan apa yang perlu disiapkan.",
        "wa_text": "Halo Sentra, saya baru membaca artikel \"Fleet Management Tambang\" dan ingin konsultasi untuk armada kami.",
        "aside": [("/produk/fleet", "Produk Fleet"), ("/portfolio/fleet-management", "Proyek FMS kontraktor tambang"), ("/industri/pertambangan", "Solusi pertambangan")],
        "body": """<p>Kontraktor tambang dan hauling batubara biasanya mengelola puluhan sampai ratusan unit: dump truck, excavator, light vehicle, dan sarana penunjang. Tanpa data yang akurat, pertanyaan sederhana seperti "unit mana yang sedang menganggur" atau "kenapa solar minggu ini naik" sulit dijawab.</p>
<h2 id="cara-kerja-fleet-management">Cara kerja fleet management</h2>
<ol><li><strong>Perangkat di unit</strong>: GPS tracker industrial dipasang di setiap kendaraan atau alat berat, ditambah sensor sesuai kebutuhan.</li><li><strong>Pengiriman data</strong>: posisi dan status dikirim lewat jaringan seluler. Di area tanpa sinyal, data disimpan di perangkat lalu dikirim saat sinyal kembali.</li><li><strong>Dashboard</strong>: semua unit tampil di peta, lengkap dengan riwayat perjalanan, alert, dan laporan.</li></ol>
<h2 id="data-yang-bisa-dipantau">Data yang bisa dipantau</h2>
<ul><li><strong>Posisi real-time dan replay</strong>: di mana unit berada dan rute yang dilalui per shift.</li><li><strong>Konsumsi BBM</strong>: sensor BBM membaca level tangki, sehingga pengisian dan penurunan tidak wajar bisa terdeteksi.</li><li><strong>Data mesin lewat CAN-Bus</strong>: untuk unit yang mendukung, seperti jam operasi, RPM, dan suhu mesin. Kendaraan berat umumnya memakai standar J1939/FMS.</li><li><strong>Geofence</strong>: alert saat unit keluar area, masuk zona terlarang, atau berhenti terlalu lama.</li><li><strong>Perilaku operator</strong>: kecepatan, pengereman keras, dan idle berlebihan dalam bentuk skor.</li><li><strong>Pengingat servis</strong>: berdasarkan jarak tempuh atau jam operasi.</li></ul>
<h2 id="masalah-yang-biasanya-terlihat">Masalah yang biasanya mulai terlihat</h2>
<ul><li>Unit yang idle lama dengan mesin menyala dan menghabiskan solar.</li><li>Selisih antara catatan pengisian BBM dan penurunan level tangki.</li><li>Rute hauling yang lebih panjang dari seharusnya.</li><li>Servis yang terlambat sehingga kerusakan lebih besar.</li><li>Kecepatan berlebih di jalan tambang yang berisiko kecelakaan.</li></ul>
<h2 id="keselamatan-operator">Keselamatan operator</h2>
<p>Selain GPS, kabin bisa dilengkapi kamera yang memperingatkan operator saat mengantuk atau terdistraksi, dan pekerja lapangan bisa membawa tracker personal dengan tombol SOS dan deteksi jatuh. Data ini membantu tim HSE bertindak sebelum insiden terjadi.</p>
<h2 id="langkah-implementasi">Langkah implementasi</h2>
<ol><li><strong>Survei armada</strong>: jenis dan jumlah unit, ketersediaan CAN-Bus, dan sinyal di area kerja.</li><li><strong>Pemasangan perangkat</strong> per unit, sebaiknya terjadwal di sela shift supaya produksi tidak terganggu.</li><li><strong>Atur geofence dan alert</strong>: pit, disposal, jalan hauling, workshop, dan area terlarang.</li><li><strong>Laporan berjalan</strong>: rekap harian untuk pengawas dan pimpinan, lalu disesuaikan dengan kebutuhan operasional.</li></ol>
<h2 id="checklist-sebelum-mulai">Checklist sebelum mulai</h2>
<ul><li>Daftar unit: jenis, merek, tahun, dan pemiliknya (sendiri atau rental).</li><li>Data apa yang paling dibutuhkan: posisi, BBM, jam operasi, atau keselamatan.</li><li>Kondisi sinyal di area kerja dan apakah perlu Starlink di kantor site.</li><li>Siapa yang memantau dashboard dan menindaklanjuti alert.</li><li>Laporan yang sudah dipakai sekarang dan format yang diinginkan.</li></ul>
<p>Sentra menjalankan sistem fleet management untuk kontraktor tambang di Kalimantan Timur. Lihat <a href="/portfolio/fleet-management">proyek FMS</a> dan <a href="/produk/fleet">produk Fleet</a>.</p>""",
    },
    "en": {
        "title": "Fleet Management for Coal Mining: How GPS, Fuel Sensors, and Reports Work",
        "description": "How fleet management works for coal mining and hauling: GPS and replay, fuel sensors, heavy equipment CAN-Bus data, geofences, operator behavior, service reminders, and daily reports.",
        "category": "Fleet & IoT",
        "lead": "At a mine, every hauling unit and piece of heavy equipment is a large moving cost. Fleet management makes its position, fuel, and operation visible from one dashboard. Here is how it works and what to prepare.",
        "wa_text": "Hello Sentra, I just read the article \"Fleet Management for Mining\" and would like to discuss our fleet.",
        "aside": [("/produk/fleet", "Fleet product"), ("/portfolio/fleet-management", "FMS project for a mining contractor"), ("/industri/pertambangan", "Mining solutions")],
        "body": """<p>Mining and coal hauling contractors typically manage tens to hundreds of units: dump trucks, excavators, light vehicles, and support equipment. Without accurate data, simple questions like "which unit is idle" or "why did diesel use rise this week" are hard to answer.</p>
<h2 id="how-it-works">How fleet management works</h2>
<ol><li><strong>Device on the unit</strong>: an industrial GPS tracker is fitted to each vehicle or machine, plus sensors as needed.</li><li><strong>Data transmission</strong>: position and status are sent over the cellular network. Where there is no signal, data is stored on the device and sent once signal returns.</li><li><strong>Dashboard</strong>: every unit appears on the map, with trip history, alerts, and reports.</li></ol>
<h2 id="what-can-be-monitored">What can be monitored</h2>
<ul><li><strong>Real-time position and replay</strong>: where a unit is and the route it took each shift.</li><li><strong>Fuel consumption</strong>: a fuel sensor reads tank level, so unusual refills and drops can be detected.</li><li><strong>Engine data via CAN-Bus</strong>: for supported units, such as operating hours, RPM, and engine temperature. Heavy vehicles generally use the J1939/FMS standard.</li><li><strong>Geofences</strong>: alerts when a unit leaves an area, enters a restricted zone, or stops too long.</li><li><strong>Operator behavior</strong>: speed, harsh braking, and excessive idling as a score.</li><li><strong>Service reminders</strong>: by distance or operating hours.</li></ul>
<h2 id="problems-that-surface">Problems that usually surface</h2>
<ul><li>Units idling for long periods with the engine on, burning diesel.</li><li>Gaps between fuel refill records and the drop in tank level.</li><li>Hauling routes longer than they should be.</li><li>Late servicing that turns small faults into big repairs.</li><li>Speeding on mine roads that raises accident risk.</li></ul>
<h2 id="operator-safety">Operator safety</h2>
<p>Beyond GPS, cabins can be fitted with cameras that warn operators when drowsy or distracted, and field workers can carry personal trackers with an SOS button and fall detection. This data helps the HSE team act before an incident happens.</p>
<h2 id="implementation-steps">Implementation steps</h2>
<ol><li><strong>Fleet survey</strong>: unit types and count, CAN-Bus availability, and signal in work areas.</li><li><strong>Device installation</strong> per unit, ideally scheduled between shifts so production is not disrupted.</li><li><strong>Set geofences and alerts</strong>: pits, disposal, haul roads, workshops, and restricted areas.</li><li><strong>Live reporting</strong>: daily summaries for supervisors and leadership, then tuned to operational needs.</li></ol>
<h2 id="checklist-before-starting">Checklist before starting</h2>
<ul><li>A unit list: type, brand, year, and owner (own or rental).</li><li>Which data matters most: position, fuel, operating hours, or safety.</li><li>Signal conditions in work areas and whether the site office needs Starlink.</li><li>Who watches the dashboard and follows up on alerts.</li><li>Reports in use today and the format you want.</li></ul>
<p>Sentra runs a fleet management system for a mining contractor in East Kalimantan. See the <a href="/en/portfolio/fleet-management">FMS project</a> and the <a href="/en/produk/fleet">Fleet product</a>.</p>""",
    },
    "zh": {
        "title": "煤矿车队管理：GPS、油量传感器与报表如何运作",
        "description": "煤矿与运输车队管理的工作原理：GPS 与轨迹回放、油量传感器、重型设备 CAN 总线数据、电子围栏、驾驶行为、保养提醒和每日报表。",
        "category": "车队与物联网",
        "lead": "在矿区，每台运输车辆和重型设备都是一笔流动的大成本。车队管理让它们的位置、油耗和操作方式在一个看板上一目了然。以下是工作原理和准备事项。",
        "wa_text": "您好 Sentra，我刚读了文章“煤矿车队管理”，想咨询我们的车队。",
        "aside": [("/produk/fleet", "Fleet 产品"), ("/portfolio/fleet-management", "矿业承包商 FMS 项目"), ("/industri/pertambangan", "矿业解决方案")],
        "body": """<p>矿业和煤炭运输承包商通常管理几十到几百台设备：自卸车、挖掘机、轻型车辆和辅助设备。没有准确的数据，“哪台车在闲置”或“这周柴油为什么增加”这样的简单问题也很难回答。</p>
<h2 id="how-it-works">车队管理如何运作</h2>
<ol><li><strong>车载设备</strong>：每台车辆或设备安装工业级 GPS 定位器，并按需加装传感器。</li><li><strong>数据传输</strong>：位置和状态通过蜂窝网络发送。无信号区域的数据先存储在设备中，恢复信号后再上传。</li><li><strong>看板</strong>：所有设备显示在地图上，附带行程记录、告警和报表。</li></ol>
<h2 id="what-can-be-monitored">可以监控的数据</h2>
<ul><li><strong>实时位置与轨迹回放</strong>：设备在哪里，以及每个班次的行驶路线。</li><li><strong>油耗</strong>：油量传感器读取油箱液位，可发现异常加油和油量下降。</li><li><strong>通过 CAN 总线读取发动机数据</strong>：支持的设备可读取工作小时、转速和发动机温度。重型车辆一般采用 J1939/FMS 标准。</li><li><strong>电子围栏</strong>：设备离开区域、进入禁区或停留过久时告警。</li><li><strong>驾驶行为</strong>：车速、急刹车和过度怠速以评分呈现。</li><li><strong>保养提醒</strong>：按里程或工作小时。</li></ul>
<h2 id="problems-that-surface">通常会暴露的问题</h2>
<ul><li>设备长时间怠速、发动机空转耗油。</li><li>加油记录与油箱液位下降之间存在差额。</li><li>运输路线比应有的更长。</li><li>保养延误，小故障变成大修。</li><li>矿区道路超速，增加事故风险。</li></ul>
<h2 id="operator-safety">驾驶员安全</h2>
<p>除 GPS 外，驾驶室还可加装在驾驶员疲劳或分心时报警的摄像头，现场人员也可携带带 SOS 按钮和跌倒检测的个人定位器。这些数据帮助 HSE 团队在事故发生前采取行动。</p>
<h2 id="implementation-steps">实施步骤</h2>
<ol><li><strong>车队勘查</strong>：设备类型与数量、是否支持 CAN 总线以及作业区信号情况。</li><li><strong>逐台安装设备</strong>：最好安排在换班间隙，避免影响生产。</li><li><strong>设置电子围栏和告警</strong>：采坑、排土场、运输道路、维修车间和禁区。</li><li><strong>报表上线</strong>：为主管和管理层提供每日汇总，再按运营需要调整。</li></ol>
<h2 id="checklist-before-starting">开始前的清单</h2>
<ul><li>设备清单：类型、品牌、年份以及归属（自有或租赁）。</li><li>最需要的数据：位置、油耗、工作小时还是安全。</li><li>作业区信号情况，以及现场办公室是否需要 Starlink。</li><li>谁负责查看看板并跟进告警。</li><li>目前使用的报表和期望的格式。</li></ul>
<p>Sentra 为东加里曼丹的矿业承包商运行车队管理系统。了解 <a href="/zh/portfolio/fleet-management">FMS 项目</a>和 <a href="/zh/produk/fleet">Fleet 产品</a>。</p>""",
    },
    "ko": {
        "title": "석탄 광산 차량 관리: GPS, 연료 센서, 보고서의 작동 방식",
        "description": "석탄 광산과 운반 차량 관리의 작동 방식: GPS와 경로 재생, 연료 센서, 중장비 CAN-Bus 데이터, 지오펜스, 운전 행태, 정비 알림, 일일 보고서.",
        "category": "차량 관리 및 IoT",
        "lead": "광산에서 운반 차량과 중장비 한 대 한 대는 움직이는 큰 비용입니다. 차량 관리 시스템은 위치, 연료, 운용 방식을 하나의 대시보드에서 보여 줍니다. 작동 방식과 준비할 사항을 정리했습니다.",
        "wa_text": "안녕하세요 Sentra, \"광산 차량 관리\" 아티클을 읽고 저희 차량에 대해 상담받고 싶습니다.",
        "aside": [("/produk/fleet", "Fleet 제품"), ("/portfolio/fleet-management", "광산 협력사 FMS 프로젝트"), ("/industri/pertambangan", "광업 솔루션")],
        "body": """<p>광산 및 석탄 운반 협력사는 보통 덤프트럭, 굴착기, 소형 차량, 지원 장비 등 수십에서 수백 대를 관리합니다. 정확한 데이터가 없으면 "어느 장비가 놀고 있나" "이번 주 경유가 왜 늘었나" 같은 간단한 질문에도 답하기 어렵습니다.</p>
<h2 id="how-it-works">차량 관리의 작동 방식</h2>
<ol><li><strong>장비 단말기</strong>: 각 차량이나 장비에 산업용 GPS 트래커를 달고 필요에 따라 센서를 추가합니다.</li><li><strong>데이터 전송</strong>: 위치와 상태는 이동통신망으로 전송됩니다. 신호가 없는 구역에서는 단말기에 저장했다가 신호가 돌아오면 보냅니다.</li><li><strong>대시보드</strong>: 모든 장비가 지도에 표시되고 운행 기록, 알림, 보고서를 함께 봅니다.</li></ol>
<h2 id="what-can-be-monitored">모니터링할 수 있는 데이터</h2>
<ul><li><strong>실시간 위치와 경로 재생</strong>: 장비 위치와 교대별 이동 경로.</li><li><strong>연료 소비</strong>: 연료 센서가 탱크 수위를 읽어 비정상적인 주유와 감소를 찾아냅니다.</li><li><strong>CAN-Bus 엔진 데이터</strong>: 지원 장비는 가동 시간, RPM, 엔진 온도 등을 읽습니다. 중차량은 보통 J1939/FMS 표준을 씁니다.</li><li><strong>지오펜스</strong>: 장비가 구역을 벗어나거나 금지 구역에 들어가거나 오래 멈추면 알림.</li><li><strong>운전 행태</strong>: 속도, 급제동, 과도한 공회전을 점수로.</li><li><strong>정비 알림</strong>: 주행 거리나 가동 시간 기준.</li></ul>
<h2 id="problems-that-surface">보통 드러나는 문제</h2>
<ul><li>엔진을 켠 채 오래 공회전하며 경유를 쓰는 장비.</li><li>주유 기록과 탱크 수위 감소량의 차이.</li><li>필요 이상으로 긴 운반 경로.</li><li>정비 지연으로 작은 고장이 큰 수리로 커짐.</li><li>광산 도로 과속으로 인한 사고 위험.</li></ul>
<h2 id="operator-safety">운전자 안전</h2>
<p>GPS 외에도 운전석에 졸음이나 주의 분산을 경고하는 카메라를 달 수 있고, 현장 작업자는 SOS 버튼과 낙상 감지가 있는 개인 트래커를 휴대할 수 있습니다. 이 데이터는 HSE 팀이 사고 전에 조치하도록 돕습니다.</p>
<h2 id="implementation-steps">도입 절차</h2>
<ol><li><strong>차량 조사</strong>: 장비 종류와 수, CAN-Bus 지원 여부, 작업 구역 신호.</li><li><strong>장비별 단말기 설치</strong>: 생산에 지장이 없도록 교대 사이에 일정을 잡는 것이 좋습니다.</li><li><strong>지오펜스와 알림 설정</strong>: 피트, 적치장, 운반 도로, 정비소, 금지 구역.</li><li><strong>보고서 운영</strong>: 감독자와 경영진용 일일 요약을 만들고 운영 필요에 맞게 조정합니다.</li></ol>
<h2 id="checklist-before-starting">시작 전 체크리스트</h2>
<ul><li>장비 목록: 종류, 브랜드, 연식, 소유 형태(자가 또는 임차).</li><li>가장 필요한 데이터: 위치, 연료, 가동 시간, 안전 중 무엇인지.</li><li>작업 구역 신호 상태와 현장 사무실의 Starlink 필요 여부.</li><li>대시보드를 보고 알림에 대응할 담당자.</li><li>현재 쓰는 보고서와 원하는 형식.</li></ul>
<p>Sentra는 동칼리만탄의 광산 협력사를 위한 차량 관리 시스템을 운영하고 있습니다. <a href="/ko/portfolio/fleet-management">FMS 프로젝트</a>와 <a href="/ko/produk/fleet">Fleet 제품</a>을 확인하십시오.</p>""",
    },
    "ms": {
        "title": "Pengurusan Armada Lombong Arang Batu: Cara GPS, Sensor Bahan Api dan Laporan Berfungsi",
        "description": "Cara pengurusan armada berfungsi untuk lombong dan pengangkutan arang batu: GPS dan main semula, sensor bahan api, data CAN-Bus jentera berat, geofence, tingkah laku pengendali, peringatan servis dan laporan harian.",
        "category": "Armada & IoT",
        "lead": "Di lombong, setiap unit pengangkutan dan jentera berat ialah kos besar yang bergerak. Pengurusan armada menjadikan kedudukan, bahan api dan cara pengendaliannya kelihatan dari satu papan pemuka. Ini cara kerjanya dan apa yang perlu disediakan.",
        "wa_text": "Hai Sentra, saya baru membaca artikel \"Pengurusan Armada Lombong\" dan ingin berbincang tentang armada kami.",
        "aside": [("/produk/fleet", "Produk Fleet"), ("/portfolio/fleet-management", "Projek FMS kontraktor lombong"), ("/industri/pertambangan", "Penyelesaian perlombongan")],
        "body": """<p>Kontraktor lombong dan pengangkutan arang batu biasanya mengurus berpuluh hingga beratus unit: trak sampah, jengkaut, kenderaan ringan dan peralatan sokongan. Tanpa data yang tepat, soalan mudah seperti "unit mana yang terbiar" atau "mengapa diesel minggu ini meningkat" sukar dijawab.</p>
<h2 id="how-it-works">Cara pengurusan armada berfungsi</h2>
<ol><li><strong>Peranti pada unit</strong>: penjejak GPS industri dipasang pada setiap kenderaan atau jentera, ditambah sensor mengikut keperluan.</li><li><strong>Penghantaran data</strong>: kedudukan dan status dihantar melalui rangkaian selular. Di kawasan tanpa isyarat, data disimpan dalam peranti lalu dihantar apabila isyarat kembali.</li><li><strong>Papan pemuka</strong>: semua unit dipaparkan di peta, lengkap dengan sejarah perjalanan, amaran dan laporan.</li></ol>
<h2 id="what-can-be-monitored">Data yang boleh dipantau</h2>
<ul><li><strong>Kedudukan masa nyata dan main semula</strong>: di mana unit berada dan laluan setiap syif.</li><li><strong>Penggunaan bahan api</strong>: sensor bahan api membaca paras tangki, jadi pengisian dan penurunan luar biasa boleh dikesan.</li><li><strong>Data enjin melalui CAN-Bus</strong>: untuk unit yang menyokong, seperti jam operasi, RPM dan suhu enjin. Kenderaan berat umumnya menggunakan piawaian J1939/FMS.</li><li><strong>Geofence</strong>: amaran apabila unit keluar kawasan, memasuki zon larangan atau berhenti terlalu lama.</li><li><strong>Tingkah laku pengendali</strong>: kelajuan, brek mengejut dan melahu berlebihan dalam bentuk skor.</li><li><strong>Peringatan servis</strong>: berdasarkan jarak atau jam operasi.</li></ul>
<h2 id="problems-that-surface">Masalah yang biasanya mula kelihatan</h2>
<ul><li>Unit yang lama melahu dengan enjin hidup dan menghabiskan diesel.</li><li>Perbezaan antara rekod pengisian bahan api dan penurunan paras tangki.</li><li>Laluan pengangkutan yang lebih panjang daripada sepatutnya.</li><li>Servis yang lewat sehingga kerosakan menjadi lebih besar.</li><li>Kelajuan berlebihan di jalan lombong yang berisiko kemalangan.</li></ul>
<h2 id="operator-safety">Keselamatan pengendali</h2>
<p>Selain GPS, kabin boleh dilengkapi kamera yang memberi amaran apabila pengendali mengantuk atau terganggu, dan pekerja lapangan boleh membawa penjejak peribadi dengan butang SOS dan pengesanan jatuh. Data ini membantu pasukan HSE bertindak sebelum insiden berlaku.</p>
<h2 id="implementation-steps">Langkah pelaksanaan</h2>
<ol><li><strong>Tinjauan armada</strong>: jenis dan bilangan unit, ketersediaan CAN-Bus dan isyarat di kawasan kerja.</li><li><strong>Pemasangan peranti</strong> bagi setiap unit, sebaiknya dijadualkan di antara syif supaya pengeluaran tidak terganggu.</li><li><strong>Tetapkan geofence dan amaran</strong>: lubang lombong, tapak pembuangan, jalan pengangkutan, bengkel dan kawasan larangan.</li><li><strong>Laporan berjalan</strong>: rekap harian untuk penyelia dan pimpinan, kemudian disesuaikan dengan keperluan operasi.</li></ol>
<h2 id="checklist-before-starting">Senarai semak sebelum bermula</h2>
<ul><li>Senarai unit: jenis, jenama, tahun dan pemilik (sendiri atau sewa).</li><li>Data yang paling diperlukan: kedudukan, bahan api, jam operasi atau keselamatan.</li><li>Keadaan isyarat di kawasan kerja dan sama ada pejabat tapak memerlukan Starlink.</li><li>Siapa yang memantau papan pemuka dan menindaklanjuti amaran.</li><li>Laporan yang digunakan sekarang dan format yang dikehendaki.</li></ul>
<p>Sentra menjalankan sistem pengurusan armada untuk kontraktor lombong di Kalimantan Timur. Lihat <a href="/ms/portfolio/fleet-management">projek FMS</a> dan <a href="/ms/produk/fleet">produk Fleet</a>.</p>""",
    },
}
