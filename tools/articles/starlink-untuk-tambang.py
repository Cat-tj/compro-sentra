SLUG = "starlink-untuk-tambang"
DATE = "2026-10-30"
COVER = "/assets/img/art/infra.webp"
OG_IMAGE = "/assets/og/art-infra.jpg"

LANGS = {
    "": {
        "title": "Starlink untuk Tambang: Memilih Kit, Instalasi, dan Jaringan di Site Remote",
        "description": "Panduan Starlink untuk site tambang: kit yang cocok, titik pasang, membawa WiFi ke mess dan workshop, sumber listrik, keamanan jaringan, dan komponen biaya.",
        "category": "Infrastruktur & konektivitas",
        "lead": "Site tambang jauh dari fiber, tetapi laporan produksi, GPS armada, CCTV, dan absensi tetap harus terkirim. Ini cara merencanakan Starlink supaya internetnya benar-benar sampai ke tempat kerja.",
        "wa_text": "Halo Sentra, saya baru membaca artikel \"Starlink untuk Tambang\" dan ingin konsultasi untuk site kami.",
        "aside": [("/services/starlink", "Layanan Starlink untuk Bisnis"), ("/industri/pertambangan", "Solusi pertambangan"), ("/produk/fleet", "Fleet management")],
        "body": """<p>Di banyak site tambang di Kalimantan, sinyal seluler hanya ada di titik tertentu dan fiber optik belum masuk. Starlink mengisi celah itu: internet satelit orbit rendah yang cukup cepat untuk video call, unggah laporan, dan memantau CCTV dari kantor pusat.</p>
<p>Tantangannya jarang ada di antena. Yang sering gagal justru hal di sekitarnya: titik pasang, listrik, dan jaringan yang membawa internet dari antena ke mess, workshop, dan pos jaga.</p>
<h2 id="untuk-apa-internet-di-site">Untuk apa internet di site tambang?</h2>
<ul><li><strong>Laporan produksi dan ritase</strong> yang dikirim per shift, bukan menunggu kurir ke kota.</li><li><strong>Fleet management</strong>: data GPS, sensor BBM, dan perilaku operator dari unit ke dashboard.</li><li><strong>CCTV dan deteksi APD</strong> yang dipantau tim HSE dari jarak jauh.</li><li><strong>Absensi dan roster</strong> karyawan yang tinggal di mess.</li><li><strong>Komunikasi</strong> dengan kantor pusat dan kebutuhan pribadi karyawan selama rotasi.</li></ul>
<p>Daftar ini menentukan berapa besar bandwidth dan berapa titik yang harus terhubung, jadi tuliskan dulu sebelum memilih kit.</p>
<h2 id="memilih-kit-starlink">Memilih kit Starlink</h2>
<ul><li><strong>Starlink Standard</strong>: untuk kantor site atau mess dengan pengguna terbatas.</li><li><strong>Starlink Enterprise</strong>: untuk lokasi bisnis tetap. Kabelnya lebih panjang dan bisa disambung ke router atau jaringan sendiri, cocok bila antena harus dipasang jauh dari ruang server.</li><li><strong>Starlink Performance</strong>: untuk kondisi ekstrem seperti angin kencang, panas, getaran, dan pemakaian di kendaraan. Pilihan untuk titik dekat pit atau unit bergerak.</li><li><strong>Starlink Mini</strong>: portabel dan bisa diberi daya dari aki, untuk survei, eksplorasi, atau pos sementara.</li></ul>
<p>Site besar biasanya memakai lebih dari satu kit: satu untuk kantor dan sistem operasional, satu lagi untuk mess, supaya pemakaian pribadi tidak mengganggu aplikasi kerja.</p>
<h2 id="menentukan-titik-pasang">Menentukan titik pasang</h2>
<ul><li><strong>Pandangan langit terbuka</strong>: pohon, tebing, dan bangunan tinggi bisa memutus koneksi. Cek dengan aplikasi Starlink saat survei.</li><li><strong>Ketinggian dan tiang</strong>: tiang yang kokoh dan dibaut lebih aman dibanding atap seng yang bergetar.</li><li><strong>Debu dan getaran</strong>: jauhkan dari jalur hauling dan area peledakan, atau pilih kit Performance.</li><li><strong>Petir dan grounding</strong>: site terbuka di Kalimantan rawan petir. Tiang dan perangkat perlu grounding yang benar.</li></ul>
<h2 id="membawa-internet-ke-mess-dan-workshop">Membawa internet ke mess, workshop, dan pos</h2>
<p>Router bawaan Starlink umumnya hanya menjangkau satu bangunan. Untuk site dengan beberapa bangunan, rancang jaringan seperti di kantor:</p>
<ul><li><strong>Router dan switch</strong> di ruang yang aman dan teduh.</li><li><strong>Access point outdoor</strong> di mess dan workshop.</li><li><strong>Radio link point-to-point</strong> atau kabel fiber untuk bangunan yang berjauhan.</li><li><strong>Jaringan terpisah</strong> (VLAN) untuk operasional, CCTV, dan karyawan, dengan prioritas bandwidth untuk aplikasi kerja.</li></ul>
<h2 id="sumber-listrik">Sumber listrik</h2>
<p>Banyak site mematikan genset di malam hari, padahal CCTV dan pengiriman data harus tetap jalan. Pilihannya:</p>
<ul><li><strong>UPS</strong> untuk menahan perangkat saat genset berpindah atau mati sebentar.</li><li><strong>Panel surya dan baterai</strong> untuk titik yang jauh dari genset atau harus menyala 24 jam.</li></ul>
<p>Kebutuhan baterai dihitung dari daya kit, router, dan access point dikali jam pemakaian tanpa genset.</p>
<h2 id="keamanan-jaringan">Keamanan jaringan</h2>
<ul><li>Ganti password bawaan router dan akun admin.</li><li>Pisahkan WiFi tamu dan karyawan dari jaringan CCTV dan sistem operasional.</li><li>Perbarui firmware perangkat secara berkala.</li><li>Catat siapa yang memegang akun Starlink dan akses pengaturannya.</li></ul>
<h2 id="komponen-biaya">Komponen biaya</h2>
<p>Biaya Starlink untuk tambang bukan hanya harga kit. Saat menyusun anggaran, masukkan komponen berikut:</p>
<ol><li>Perangkat Starlink sesuai jenis kit.</li><li>Mounting, tiang, kabel, dan material instalasi.</li><li>Jaringan site: router, switch, access point, radio link atau fiber.</li><li>Sistem daya: UPS, panel surya, baterai, dan inverter bila perlu.</li><li>Jasa survei, instalasi, dan mobilisasi tim ke lokasi.</li><li>Langganan bulanan Starlink sesuai paket yang dipilih.</li><li>Perawatan berkala dan suku cadang.</li></ol>
<h2 id="checklist-sebelum-survei">Checklist sebelum survei</h2>
<ul><li>Koordinat atau peta site dan daftar bangunan yang perlu internet.</li><li>Perkiraan jumlah pengguna dan perangkat per bangunan.</li><li>Aplikasi yang wajib jalan: laporan, fleet, CCTV, absensi.</li><li>Jadwal genset dan sumber listrik yang tersedia.</li><li>Kontak penanggung jawab di site dan aturan izin masuk area.</li></ul>
<p>Dengan data ini, survei bisa langsung menghasilkan desain jaringan dan rencana anggaran yang realistis. Lihat <a href="/services/starlink">layanan Starlink untuk Bisnis</a> dari Sentra untuk pilihan kit dan alur kerjanya.</p>""",
    },
    "en": {
        "title": "Starlink for Mining: Choosing Kits, Installation, and Networks at Remote Sites",
        "description": "A Starlink guide for mine sites: which kit fits, where to mount it, bringing WiFi to the mess and workshop, power, network security, and cost components.",
        "category": "Infrastructure & connectivity",
        "lead": "Mine sites are far from fiber, yet production reports, fleet GPS, CCTV, and attendance still have to get through. Here is how to plan Starlink so the internet actually reaches the work areas.",
        "wa_text": "Hello Sentra, I just read the article \"Starlink for Mining\" and would like to discuss our site.",
        "aside": [("/services/starlink", "Starlink for Business service"), ("/industri/pertambangan", "Mining solutions"), ("/produk/fleet", "Fleet management")],
        "body": """<p>At many mine sites in Kalimantan, mobile signal exists only at certain points and fiber has not arrived. Starlink fills that gap: low-orbit satellite internet fast enough for video calls, report uploads, and CCTV monitoring from head office.</p>
<p>The challenge is rarely the dish. What usually fails is everything around it: the mounting point, power, and the network that carries the internet from the dish to the mess, workshop, and guard posts.</p>
<h2 id="what-the-internet-is-for">What does a mine site need the internet for?</h2>
<ul><li><strong>Production and haul reports</strong> sent every shift instead of waiting for a courier to town.</li><li><strong>Fleet management</strong>: GPS, fuel sensor, and operator behavior data from units to the dashboard.</li><li><strong>CCTV and PPE detection</strong> monitored remotely by the HSE team.</li><li><strong>Attendance and rosters</strong> for employees living in the mess.</li><li><strong>Communication</strong> with head office and employees' personal needs during rotation.</li></ul>
<p>This list sets how much bandwidth you need and how many points must be connected, so write it down before choosing a kit.</p>
<h2 id="choosing-a-starlink-kit">Choosing a Starlink kit</h2>
<ul><li><strong>Starlink Standard</strong>: for a site office or mess with a limited number of users.</li><li><strong>Starlink Enterprise</strong>: for fixed business locations. A longer cable that connects to your own router or network, useful when the dish must sit far from the server room.</li><li><strong>Starlink Performance</strong>: for extreme conditions such as strong wind, heat, vibration, and use on vehicles. The choice for points near the pit or on moving units.</li><li><strong>Starlink Mini</strong>: portable and can run from a battery, for surveys, exploration, or temporary posts.</li></ul>
<p>Large sites usually use more than one kit: one for the office and operational systems, another for the mess, so personal use does not slow down work applications.</p>
<h2 id="choosing-the-mounting-point">Choosing the mounting point</h2>
<ul><li><strong>Clear sky view</strong>: trees, cliffs, and tall buildings can interrupt the connection. Check with the Starlink app during the survey.</li><li><strong>Height and pole</strong>: a sturdy bolted pole is safer than a vibrating metal roof.</li><li><strong>Dust and vibration</strong>: keep away from haul roads and blasting areas, or choose a Performance kit.</li><li><strong>Lightning and grounding</strong>: open sites in Kalimantan are lightning-prone. The pole and devices need proper grounding.</li></ul>
<h2 id="bringing-internet-to-the-mess-and-workshop">Bringing the internet to the mess, workshop, and posts</h2>
<p>The standard Starlink router usually covers one building. For a site with several buildings, design the network as you would for an office:</p>
<ul><li><strong>Router and switch</strong> in a safe, shaded room.</li><li><strong>Outdoor access points</strong> at the mess and workshop.</li><li><strong>Point-to-point radio links</strong> or fiber for distant buildings.</li><li><strong>Separate networks</strong> (VLANs) for operations, CCTV, and employees, with bandwidth priority for work applications.</li></ul>
<h2 id="power-supply">Power supply</h2>
<p>Many sites switch the generator off at night, yet CCTV and data transfer must keep running. The options:</p>
<ul><li><strong>UPS</strong> to hold devices while the generator switches over or stops briefly.</li><li><strong>Solar panels and batteries</strong> for points far from the generator or that must run 24 hours.</li></ul>
<p>Battery capacity is calculated from the power of the kit, router, and access points multiplied by the hours without the generator.</p>
<h2 id="network-security">Network security</h2>
<ul><li>Change the router's default password and admin account.</li><li>Separate guest and employee WiFi from the CCTV and operational network.</li><li>Update device firmware regularly.</li><li>Record who holds the Starlink account and its settings access.</li></ul>
<h2 id="cost-components">Cost components</h2>
<p>The cost of Starlink for a mine is not just the kit. When building the budget, include:</p>
<ol><li>Starlink hardware for the chosen kit type.</li><li>Mounts, poles, cables, and installation materials.</li><li>Site network: routers, switches, access points, radio links or fiber.</li><li>Power system: UPS, solar panels, batteries, and an inverter if needed.</li><li>Survey, installation, and team mobilization to the site.</li><li>The monthly Starlink subscription for the chosen plan.</li><li>Scheduled maintenance and spare parts.</li></ol>
<h2 id="checklist-before-the-survey">Checklist before the survey</h2>
<ul><li>Site coordinates or map and the list of buildings that need internet.</li><li>Estimated users and devices per building.</li><li>Applications that must run: reports, fleet, CCTV, attendance.</li><li>Generator schedule and available power sources.</li><li>The on-site contact person and area access rules.</li></ul>
<p>With this information, the survey can go straight to a network design and a realistic budget. See Sentra's <a href="/en/services/starlink">Starlink for Business service</a> for kit options and how we work.</p>""",
    },
    "zh": {
        "title": "矿区 Starlink：套件选择、安装与偏远站点网络",
        "description": "矿区 Starlink 指南：适合的套件、安装位置、把 WiFi 延伸到宿舍和车间、供电、网络安全以及成本构成。",
        "category": "基础设施与网络",
        "lead": "矿区远离光纤，但生产报表、车队 GPS、CCTV 和考勤仍然必须按时上传。下面介绍如何规划 Starlink，让网络真正覆盖到作业区域。",
        "wa_text": "您好 Sentra，我刚读了文章“矿区 Starlink”，想咨询我们站点的方案。",
        "aside": [("/services/starlink", "企业 Starlink 服务"), ("/industri/pertambangan", "矿业解决方案"), ("/produk/fleet", "车队管理")],
        "body": """<p>在加里曼丹的许多矿区，手机信号只覆盖部分地点，光纤也尚未接入。Starlink 正好弥补这一空白：低轨卫星网络的速度足以支持视频通话、上传报表以及从总部远程查看 CCTV。</p>
<p>难点很少出在天线本身，真正容易出问题的是周边环节：安装位置、供电，以及把网络从天线送到宿舍、车间和岗亭的现场网络。</p>
<h2 id="what-the-internet-is-for">矿区需要网络做什么？</h2>
<ul><li><strong>生产与运量报表</strong>：每个班次上传，不必等人送到城里。</li><li><strong>车队管理</strong>：GPS、油量传感器和驾驶行为数据从设备传到看板。</li><li><strong>CCTV 与 PPE 检测</strong>：由 HSE 团队远程监控。</li><li><strong>考勤与排班</strong>：针对住在宿舍的员工。</li><li><strong>通信</strong>：与总部沟通以及员工轮班期间的个人需求。</li></ul>
<p>这份清单决定所需带宽和需要联网的点位数量，因此在选择套件之前先把它写下来。</p>
<h2 id="choosing-a-starlink-kit">选择 Starlink 套件</h2>
<ul><li><strong>Starlink Standard</strong>：适合用户数量有限的现场办公室或宿舍。</li><li><strong>Starlink Enterprise</strong>：适合固定的业务地点。线缆更长，可接入自有路由器或网络，适合天线必须远离机房的情况。</li><li><strong>Starlink Performance</strong>：适合大风、高温、振动等极端环境以及车载使用，是靠近采坑或移动设备的首选。</li><li><strong>Starlink Mini</strong>：便携，可用电瓶供电，适合勘测、勘探或临时岗点。</li></ul>
<p>大型站点通常使用不止一套：一套用于办公室和生产系统，另一套用于宿舍，避免个人使用影响工作应用。</p>
<h2 id="choosing-the-mounting-point">选择安装位置</h2>
<ul><li><strong>开阔的天空视野</strong>：树木、山崖和高楼会中断连接。勘测时用 Starlink 应用检查。</li><li><strong>高度与立杆</strong>：牢固并用螺栓固定的立杆比会振动的铁皮屋顶更可靠。</li><li><strong>粉尘与振动</strong>：远离运输道路和爆破区域，或选择 Performance 套件。</li><li><strong>防雷与接地</strong>：加里曼丹的开阔站点雷电频繁，立杆和设备需要规范接地。</li></ul>
<h2 id="bringing-internet-to-the-mess-and-workshop">把网络送到宿舍、车间和岗点</h2>
<p>Starlink 自带路由器通常只覆盖一栋建筑。若站点有多栋建筑，应像办公室一样设计网络：</p>
<ul><li><strong>路由器和交换机</strong>放在安全、阴凉的房间。</li><li><strong>室外无线 AP</strong>安装在宿舍和车间。</li><li><strong>点对点无线网桥</strong>或光纤连接距离较远的建筑。</li><li><strong>独立网络</strong>（VLAN）分别用于生产、CCTV 和员工，并为工作应用设置带宽优先级。</li></ul>
<h2 id="power-supply">供电</h2>
<p>许多站点夜间会关闭发电机，但 CCTV 和数据传输必须持续运行。可选方案：</p>
<ul><li><strong>UPS</strong>：在发电机切换或短暂停机时维持设备供电。</li><li><strong>太阳能板与电池</strong>：用于远离发电机或需要 24 小时运行的点位。</li></ul>
<p>电池容量按套件、路由器和 AP 的功率乘以无发电机的时长来计算。</p>
<h2 id="network-security">网络安全</h2>
<ul><li>修改路由器默认密码和管理员账户。</li><li>将访客和员工 WiFi 与 CCTV 及生产网络隔离。</li><li>定期更新设备固件。</li><li>记录谁持有 Starlink 账户及其设置权限。</li></ul>
<h2 id="cost-components">成本构成</h2>
<p>矿区 Starlink 的费用不只是套件价格。编制预算时应包括：</p>
<ol><li>所选类型的 Starlink 设备。</li><li>支架、立杆、线缆和安装材料。</li><li>现场网络：路由器、交换机、AP、无线网桥或光纤。</li><li>供电系统：UPS、太阳能板、电池，必要时加逆变器。</li><li>勘测、安装以及团队进场费用。</li><li>所选套餐的 Starlink 月度订阅费。</li><li>定期维护与备件。</li></ol>
<h2 id="checklist-before-the-survey">勘测前清单</h2>
<ul><li>站点坐标或地图，以及需要联网的建筑清单。</li><li>每栋建筑的预计用户数和设备数。</li><li>必须运行的应用：报表、车队、CCTV、考勤。</li><li>发电机运行时间和可用电源。</li><li>现场负责人联系方式和进场规定。</li></ul>
<p>有了这些信息，勘测就能直接产出网络设计和切实可行的预算。了解 Sentra 的<a href="/zh/services/starlink">企业 Starlink 服务</a>，查看套件选择和工作流程。</p>""",
    },
    "ko": {
        "title": "광산용 Starlink: 키트 선택, 설치, 원격지 현장 네트워크",
        "description": "광산 현장을 위한 Starlink 가이드: 맞는 키트, 설치 위치, 숙소와 정비소까지 WiFi 연결, 전원, 네트워크 보안, 비용 구성.",
        "category": "인프라 및 연결",
        "lead": "광산 현장은 광케이블에서 멀지만 생산 보고, 차량 GPS, CCTV, 출퇴근 기록은 제때 전송되어야 합니다. 인터넷이 실제 작업 공간까지 닿도록 Starlink를 계획하는 방법을 정리했습니다.",
        "wa_text": "안녕하세요 Sentra, \"광산용 Starlink\" 아티클을 읽고 저희 현장에 대해 상담받고 싶습니다.",
        "aside": [("/services/starlink", "기업용 Starlink 서비스"), ("/industri/pertambangan", "광업 솔루션"), ("/produk/fleet", "차량 관리")],
        "body": """<p>칼리만탄의 많은 광산 현장에서는 이동통신 신호가 일부 지점에만 잡히고 광케이블도 아직 들어오지 않았습니다. Starlink는 이 빈틈을 메웁니다. 저궤도 위성 인터넷은 화상 통화, 보고서 업로드, 본사에서의 CCTV 모니터링에 충분한 속도를 제공합니다.</p>
<p>문제는 대개 안테나가 아닙니다. 자주 실패하는 것은 그 주변, 즉 설치 위치, 전원, 그리고 안테나에서 숙소, 정비소, 경비 초소까지 인터넷을 전달하는 네트워크입니다.</p>
<h2 id="what-the-internet-is-for">광산 현장에서 인터넷은 어디에 쓰일까?</h2>
<ul><li><strong>생산 및 운반 보고</strong>: 시내로 가는 인편을 기다리지 않고 교대마다 전송합니다.</li><li><strong>차량 관리</strong>: GPS, 연료 센서, 운전 행태 데이터를 장비에서 대시보드로 보냅니다.</li><li><strong>CCTV 및 PPE 감지</strong>: HSE 팀이 원격으로 모니터링합니다.</li><li><strong>출퇴근 및 근무표</strong>: 숙소에 거주하는 직원 대상입니다.</li><li><strong>소통</strong>: 본사와의 연락, 순환 근무 중 직원의 개인 용도.</li></ul>
<p>이 목록이 필요한 대역폭과 연결해야 할 지점 수를 결정하므로, 키트를 고르기 전에 먼저 정리하십시오.</p>
<h2 id="choosing-a-starlink-kit">Starlink 키트 선택</h2>
<ul><li><strong>Starlink Standard</strong>: 사용자가 많지 않은 현장 사무실이나 숙소용.</li><li><strong>Starlink Enterprise</strong>: 고정된 사업장용. 케이블이 더 길고 자체 라우터나 네트워크에 연결할 수 있어, 안테나를 서버실에서 멀리 설치해야 할 때 적합합니다.</li><li><strong>Starlink Performance</strong>: 강풍, 고온, 진동, 차량 사용 등 극한 환경용. 피트 인근 지점이나 이동 장비에 알맞습니다.</li><li><strong>Starlink Mini</strong>: 휴대형이며 배터리로 구동할 수 있어 조사, 탐사, 임시 초소에 쓰입니다.</li></ul>
<p>대형 현장은 보통 키트를 둘 이상 씁니다. 하나는 사무실과 운영 시스템용, 다른 하나는 숙소용으로 두어 개인 사용이 업무 애플리케이션을 방해하지 않게 합니다.</p>
<h2 id="choosing-the-mounting-point">설치 위치 정하기</h2>
<ul><li><strong>트인 하늘 시야</strong>: 나무, 절벽, 높은 건물은 연결을 끊을 수 있습니다. 조사 때 Starlink 앱으로 확인하십시오.</li><li><strong>높이와 기둥</strong>: 볼트로 고정한 튼튼한 기둥이 진동하는 함석 지붕보다 안전합니다.</li><li><strong>먼지와 진동</strong>: 운반 도로와 발파 구역에서 떨어뜨리거나 Performance 키트를 선택하십시오.</li><li><strong>낙뢰와 접지</strong>: 칼리만탄의 개활지 현장은 낙뢰가 잦습니다. 기둥과 장비는 올바르게 접지해야 합니다.</li></ul>
<h2 id="bringing-internet-to-the-mess-and-workshop">숙소, 정비소, 초소까지 인터넷 연결</h2>
<p>Starlink 기본 라우터는 보통 건물 하나만 커버합니다. 건물이 여러 동인 현장은 사무실처럼 네트워크를 설계하십시오.</p>
<ul><li><strong>라우터와 스위치</strong>는 안전하고 그늘진 실내에 둡니다.</li><li><strong>실외 AP</strong>를 숙소와 정비소에 설치합니다.</li><li><strong>점대점 무선 링크</strong> 또는 광케이블로 멀리 떨어진 건물을 연결합니다.</li><li><strong>분리된 네트워크</strong>(VLAN)를 운영, CCTV, 직원용으로 나누고 업무 애플리케이션에 대역폭 우선순위를 줍니다.</li></ul>
<h2 id="power-supply">전원</h2>
<p>많은 현장이 밤에 발전기를 끄지만 CCTV와 데이터 전송은 계속되어야 합니다. 선택지는 다음과 같습니다.</p>
<ul><li><strong>UPS</strong>: 발전기 전환이나 짧은 정지 동안 장비 전원을 유지합니다.</li><li><strong>태양광 패널과 배터리</strong>: 발전기에서 먼 지점이나 24시간 가동해야 하는 지점용.</li></ul>
<p>배터리 용량은 키트, 라우터, AP의 소비 전력에 발전기 없이 버텨야 하는 시간을 곱해 계산합니다.</p>
<h2 id="network-security">네트워크 보안</h2>
<ul><li>라우터 기본 비밀번호와 관리자 계정을 변경합니다.</li><li>방문자·직원 WiFi를 CCTV 및 운영 네트워크와 분리합니다.</li><li>장비 펌웨어를 정기적으로 업데이트합니다.</li><li>Starlink 계정과 설정 권한을 누가 가지고 있는지 기록합니다.</li></ul>
<h2 id="cost-components">비용 구성</h2>
<p>광산용 Starlink 비용은 키트 가격만이 아닙니다. 예산을 짤 때 다음 항목을 포함하십시오.</p>
<ol><li>선택한 유형의 Starlink 장비.</li><li>거치대, 기둥, 케이블, 설치 자재.</li><li>현장 네트워크: 라우터, 스위치, AP, 무선 링크 또는 광케이블.</li><li>전원 시스템: UPS, 태양광 패널, 배터리, 필요 시 인버터.</li><li>현장 조사, 설치, 팀 이동 비용.</li><li>선택한 요금제의 Starlink 월 구독료.</li><li>정기 유지보수와 예비 부품.</li></ol>
<h2 id="checklist-before-the-survey">현장 조사 전 체크리스트</h2>
<ul><li>현장 좌표 또는 지도, 인터넷이 필요한 건물 목록.</li><li>건물별 예상 사용자 수와 장비 수.</li><li>반드시 작동해야 할 애플리케이션: 보고, 차량 관리, CCTV, 출퇴근.</li><li>발전기 가동 일정과 사용 가능한 전원.</li><li>현장 담당자 연락처와 출입 규정.</li></ul>
<p>이 정보가 있으면 현장 조사에서 곧바로 네트워크 설계와 현실적인 예산을 도출할 수 있습니다. 키트 선택과 진행 절차는 Sentra의 <a href="/ko/services/starlink">기업용 Starlink 서비스</a>에서 확인하십시오.</p>""",
    },
    "ms": {
        "title": "Starlink untuk Perlombongan: Memilih Kit, Pemasangan dan Rangkaian di Tapak Terpencil",
        "description": "Panduan Starlink untuk tapak lombong: kit yang sesuai, titik pemasangan, membawa WiFi ke asrama dan bengkel, sumber kuasa, keselamatan rangkaian dan komponen kos.",
        "category": "Infrastruktur & kesambungan",
        "lead": "Tapak lombong jauh dari gentian optik, tetapi laporan pengeluaran, GPS armada, CCTV dan kehadiran tetap perlu dihantar. Begini cara merancang Starlink supaya internet benar-benar sampai ke kawasan kerja.",
        "wa_text": "Hai Sentra, saya baru membaca artikel \"Starlink untuk Perlombongan\" dan ingin berbincang tentang tapak kami.",
        "aside": [("/services/starlink", "Perkhidmatan Starlink untuk Perniagaan"), ("/industri/pertambangan", "Penyelesaian perlombongan"), ("/produk/fleet", "Pengurusan armada")],
        "body": """<p>Di banyak tapak lombong di Kalimantan, isyarat selular hanya ada di titik tertentu dan gentian optik belum sampai. Starlink mengisi jurang itu: internet satelit orbit rendah yang cukup laju untuk panggilan video, muat naik laporan dan memantau CCTV dari ibu pejabat.</p>
<p>Cabarannya jarang pada antena. Yang sering gagal ialah perkara di sekelilingnya: titik pemasangan, bekalan kuasa dan rangkaian yang membawa internet dari antena ke asrama, bengkel dan pondok pengawal.</p>
<h2 id="what-the-internet-is-for">Untuk apa internet di tapak lombong?</h2>
<ul><li><strong>Laporan pengeluaran dan trip</strong> yang dihantar setiap syif, bukan menunggu kurier ke bandar.</li><li><strong>Pengurusan armada</strong>: data GPS, sensor bahan api dan tingkah laku pengendali dari unit ke papan pemuka.</li><li><strong>CCTV dan pengesanan PPE</strong> yang dipantau pasukan HSE dari jauh.</li><li><strong>Kehadiran dan jadual giliran</strong> pekerja yang tinggal di asrama.</li><li><strong>Komunikasi</strong> dengan ibu pejabat dan keperluan peribadi pekerja semasa giliran.</li></ul>
<p>Senarai ini menentukan jumlah lebar jalur dan bilangan titik yang perlu disambung, jadi tuliskan dahulu sebelum memilih kit.</p>
<h2 id="choosing-a-starlink-kit">Memilih kit Starlink</h2>
<ul><li><strong>Starlink Standard</strong>: untuk pejabat tapak atau asrama dengan pengguna terhad.</li><li><strong>Starlink Enterprise</strong>: untuk lokasi perniagaan tetap. Kabelnya lebih panjang dan boleh disambung ke penghala atau rangkaian sendiri, sesuai jika antena perlu dipasang jauh dari bilik pelayan.</li><li><strong>Starlink Performance</strong>: untuk keadaan ekstrem seperti angin kencang, panas, getaran dan penggunaan pada kenderaan. Pilihan untuk titik berhampiran lubang lombong atau unit bergerak.</li><li><strong>Starlink Mini</strong>: mudah alih dan boleh dikuasakan bateri, untuk tinjauan, eksplorasi atau pos sementara.</li></ul>
<p>Tapak besar biasanya memakai lebih daripada satu kit: satu untuk pejabat dan sistem operasi, satu lagi untuk asrama, supaya penggunaan peribadi tidak mengganggu aplikasi kerja.</p>
<h2 id="choosing-the-mounting-point">Menentukan titik pemasangan</h2>
<ul><li><strong>Pandangan langit terbuka</strong>: pokok, tebing dan bangunan tinggi boleh memutuskan sambungan. Semak dengan aplikasi Starlink semasa tinjauan.</li><li><strong>Ketinggian dan tiang</strong>: tiang kukuh yang dibolt lebih selamat berbanding bumbung zink yang bergetar.</li><li><strong>Debu dan getaran</strong>: jauhkan dari laluan pengangkutan dan kawasan letupan, atau pilih kit Performance.</li><li><strong>Kilat dan pembumian</strong>: tapak terbuka di Kalimantan kerap dipanah kilat. Tiang dan peranti perlu pembumian yang betul.</li></ul>
<h2 id="bringing-internet-to-the-mess-and-workshop">Membawa internet ke asrama, bengkel dan pos</h2>
<p>Penghala asal Starlink biasanya hanya meliputi satu bangunan. Untuk tapak dengan beberapa bangunan, reka rangkaian seperti di pejabat:</p>
<ul><li><strong>Penghala dan suis</strong> di bilik yang selamat dan teduh.</li><li><strong>Titik akses luar</strong> di asrama dan bengkel.</li><li><strong>Pautan radio point-to-point</strong> atau gentian optik untuk bangunan yang berjauhan.</li><li><strong>Rangkaian berasingan</strong> (VLAN) untuk operasi, CCTV dan pekerja, dengan keutamaan lebar jalur untuk aplikasi kerja.</li></ul>
<h2 id="power-supply">Sumber kuasa</h2>
<p>Banyak tapak mematikan genset pada waktu malam, sedangkan CCTV dan penghantaran data mesti terus berjalan. Pilihannya:</p>
<ul><li><strong>UPS</strong> untuk mengekalkan peranti semasa genset bertukar atau terhenti seketika.</li><li><strong>Panel solar dan bateri</strong> untuk titik yang jauh dari genset atau perlu menyala 24 jam.</li></ul>
<p>Keperluan bateri dikira daripada kuasa kit, penghala dan titik akses didarab dengan jam penggunaan tanpa genset.</p>
<h2 id="network-security">Keselamatan rangkaian</h2>
<ul><li>Tukar kata laluan asal penghala dan akaun pentadbir.</li><li>Asingkan WiFi tetamu dan pekerja daripada rangkaian CCTV dan sistem operasi.</li><li>Kemas kini perisian tegar peranti secara berkala.</li><li>Rekod siapa yang memegang akaun Starlink dan akses tetapannya.</li></ul>
<h2 id="cost-components">Komponen kos</h2>
<p>Kos Starlink untuk lombong bukan sekadar harga kit. Semasa menyusun bajet, masukkan komponen berikut:</p>
<ol><li>Peranti Starlink mengikut jenis kit.</li><li>Pendakap, tiang, kabel dan bahan pemasangan.</li><li>Rangkaian tapak: penghala, suis, titik akses, pautan radio atau gentian optik.</li><li>Sistem kuasa: UPS, panel solar, bateri dan penyongsang jika perlu.</li><li>Tinjauan, pemasangan dan mobilisasi pasukan ke lokasi.</li><li>Langganan bulanan Starlink mengikut pelan yang dipilih.</li><li>Penyelenggaraan berkala dan alat ganti.</li></ol>
<h2 id="checklist-before-the-survey">Senarai semak sebelum tinjauan</h2>
<ul><li>Koordinat atau peta tapak dan senarai bangunan yang memerlukan internet.</li><li>Anggaran pengguna dan peranti bagi setiap bangunan.</li><li>Aplikasi yang wajib berjalan: laporan, armada, CCTV, kehadiran.</li><li>Jadual genset dan sumber kuasa yang ada.</li><li>Pegawai yang bertanggungjawab di tapak dan peraturan kebenaran masuk.</li></ul>
<p>Dengan maklumat ini, tinjauan boleh terus menghasilkan reka bentuk rangkaian dan bajet yang realistik. Lihat <a href="/ms/services/starlink">perkhidmatan Starlink untuk Perniagaan</a> Sentra untuk pilihan kit dan aliran kerjanya.</p>""",
    },
}
