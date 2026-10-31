SLUG = "starlink-vs-vsat-vs-fiber"
DATE = "2026-10-30"
COVER = "/assets/img/art/infra.webp"
OG_IMAGE = "/assets/og/art-infra.jpg"

LANGS = {
    "": {
        "title": "Starlink vs VSAT vs Fiber untuk Kantor Cabang dan Site di Kalimantan",
        "description": "Perbandingan Starlink, VSAT, fiber optik, dan seluler untuk kantor cabang, site tambang, dan kebun di Kalimantan: latensi, stabilitas, instalasi, dan kapan memakai kombinasi.",
        "category": "Infrastruktur & konektivitas",
        "lead": "Tidak ada satu koneksi yang terbaik untuk semua lokasi. Ini cara membandingkan Starlink, VSAT, fiber, dan seluler berdasarkan kebutuhan aplikasi dan kondisi site, termasuk kapan sebaiknya memakai dua jalur sekaligus.",
        "wa_text": "Halo Sentra, saya baru membaca artikel \"Starlink vs VSAT vs Fiber\" dan ingin konsultasi koneksi untuk lokasi kami.",
        "aside": [("/services/starlink", "Layanan Starlink untuk Bisnis"), ("/services/instalasi-infrastruktur", "Instalasi jaringan & fiber"), ("/blog/starlink-untuk-tambang", "Starlink untuk tambang")],
        "body": """<p>Kantor di kota besar biasanya cukup memakai fiber. Tantangannya muncul di kantor cabang kecamatan, site tambang, kebun, dan proyek yang jauh dari jaringan. Di sana pilihannya biasanya fiber (bila terjangkau), seluler 4G/5G, VSAT, atau Starlink.</p>
<h2 id="perbedaan-utama">Perbedaan utama</h2>
<ul><li><strong>Fiber optik</strong>: paling stabil dan latensinya paling rendah. Syaratnya kabel bisa ditarik sampai lokasi, dan untuk site terpencil biayanya bisa besar atau tidak tersedia.</li><li><strong>Seluler 4G/5G</strong>: cepat dipasang dan murah bila sinyalnya kuat. Di banyak site, sinyal tidak stabil atau tidak ada.</li><li><strong>VSAT</strong>: internet satelit geostasioner di ketinggian sekitar 36.000 km. Jangkauannya luas, tetapi jarak sejauh itu membuat latensi umumnya tinggi, di atas setengah detik.</li><li><strong>Starlink</strong>: satelit orbit rendah yang jauh lebih dekat ke bumi, sehingga latensinya umumnya puluhan milidetik. Pemasangannya relatif cepat, cukup pandangan langit yang terbuka.</li></ul>
<h2 id="kenapa-latensi-penting">Kenapa latensi penting</h2>
<p>Latensi adalah jeda waktu data pergi dan kembali. Untuk mengunduh file, latensi tinggi masih bisa ditoleransi. Untuk video call, remote desktop, aplikasi yang sering bolak-balik ke server, dan CCTV live, latensi tinggi terasa sebagai suara terputus, layar tersendat, dan aplikasi lambat. Karena itu, jumlah Mbps saja tidak cukup untuk membandingkan koneksi.</p>
<h2 id="pilih-berdasarkan-kebutuhan">Pilih berdasarkan kebutuhan</h2>
<ul><li><strong>Kantor cabang yang dilalui fiber</strong>: fiber sebagai jalur utama, Starlink atau seluler sebagai cadangan.</li><li><strong>Site tambang atau kebun tanpa fiber</strong>: Starlink sebagai jalur utama, seluler sebagai cadangan bila ada sinyal.</li><li><strong>Lokasi yang sudah lama memakai VSAT</strong>: pertimbangkan Starlink untuk aplikasi yang sensitif latensi, sementara VSAT tetap dipakai bila ada kontrak atau sistem yang bergantung padanya.</li><li><strong>Proyek sementara</strong>: Starlink atau seluler, karena bisa dipindah saat proyek selesai.</li></ul>
<h2 id="dua-jalur-lebih-aman">Dua jalur lebih aman dari satu</h2>
<p>Untuk operasional yang tidak boleh putus, pasang dua koneksi dengan router yang bisa memindahkan lalu lintas otomatis (failover). Bila jalur utama putus, aplikasi tetap jalan lewat jalur cadangan. Router yang sama juga bisa memprioritaskan aplikasi kerja di atas pemakaian pribadi.</p>
<h2 id="hal-di-luar-koneksi">Hal di luar koneksi yang sering menentukan</h2>
<ul><li><strong>Listrik</strong>: koneksi apa pun akan mati bila perangkat tidak punya UPS atau panel surya saat genset dimatikan.</li><li><strong>Jaringan lokal</strong>: koneksi cepat tidak berguna bila WiFi hanya menjangkau satu ruangan.</li><li><strong>Petir dan grounding</strong> untuk antena di lokasi terbuka.</li><li><strong>Dukungan teknis</strong>: siapa yang datang ke lokasi bila ada gangguan, dan berapa lama.</li></ul>
<h2 id="checklist-memilih-koneksi">Checklist memilih koneksi</h2>
<ul><li>Aplikasi apa yang wajib jalan, dan apakah sensitif latensi?</li><li>Berapa pengguna dan perangkat yang terhubung bersamaan?</li><li>Apakah fiber atau sinyal seluler tersedia di lokasi?</li><li>Apakah perlu jalur cadangan otomatis?</li><li>Bagaimana sumber listrik di titik pemasangan?</li></ul>
<p>Sentra memasang Starlink, jaringan site, dan fiber untuk kantor dan site di Kalimantan Timur. Lihat <a href="/services/starlink">layanan Starlink untuk Bisnis</a> dan <a href="/services/instalasi-infrastruktur">instalasi infrastruktur</a>.</p>""",
    },
    "en": {
        "title": "Starlink vs VSAT vs Fiber for Branch Offices and Sites in Kalimantan",
        "description": "Comparing Starlink, VSAT, fiber, and cellular for branch offices, mine sites, and estates in Kalimantan: latency, stability, installation, and when to combine them.",
        "category": "Infrastructure & connectivity",
        "lead": "No single connection is best for every location. Here is how to compare Starlink, VSAT, fiber, and cellular by application needs and site conditions, including when to run two links at once.",
        "wa_text": "Hello Sentra, I just read the article \"Starlink vs VSAT vs Fiber\" and would like advice on connectivity for our site.",
        "aside": [("/services/starlink", "Starlink for Business service"), ("/services/instalasi-infrastruktur", "Network & fiber installation"), ("/blog/starlink-untuk-tambang", "Starlink for mining")],
        "body": """<p>Offices in big cities can usually rely on fiber. The challenge is in district branch offices, mine sites, estates, and projects far from the network. There, the options are usually fiber (if it reaches), 4G/5G cellular, VSAT, or Starlink.</p>
<h2 id="key-differences">Key differences</h2>
<ul><li><strong>Fiber optics</strong>: the most stable, with the lowest latency. It requires a cable run to the site, which for remote sites can be expensive or unavailable.</li><li><strong>4G/5G cellular</strong>: quick and cheap to set up when the signal is strong. At many sites the signal is unstable or absent.</li><li><strong>VSAT</strong>: geostationary satellite internet at about 36,000 km altitude. Coverage is wide, but that distance makes latency generally high, above half a second.</li><li><strong>Starlink</strong>: low-orbit satellites much closer to Earth, so latency is generally tens of milliseconds. Installation is relatively fast and needs only a clear view of the sky.</li></ul>
<h2 id="why-latency-matters">Why latency matters</h2>
<p>Latency is the round-trip delay of data. For downloading files, high latency is tolerable. For video calls, remote desktop, apps that talk to the server often, and live CCTV, high latency shows up as broken audio, stuttering screens, and slow apps. That is why Mbps alone is not enough to compare connections.</p>
<h2 id="choose-by-need">Choose by need</h2>
<ul><li><strong>Branch office on a fiber route</strong>: fiber as the main link, Starlink or cellular as backup.</li><li><strong>Mine site or estate without fiber</strong>: Starlink as the main link, cellular as backup where there is signal.</li><li><strong>Sites long on VSAT</strong>: consider Starlink for latency-sensitive apps, keeping VSAT where contracts or systems depend on it.</li><li><strong>Temporary projects</strong>: Starlink or cellular, since they can move when the project ends.</li></ul>
<h2 id="two-links-are-safer">Two links are safer than one</h2>
<p>For operations that must not stop, install two connections with a router that moves traffic automatically (failover). If the main link drops, apps keep running over the backup. The same router can prioritize work apps over personal use.</p>
<h2 id="beyond-the-connection">What often matters beyond the connection</h2>
<ul><li><strong>Power</strong>: any connection dies if devices have no UPS or solar when the generator is off.</li><li><strong>Local network</strong>: a fast link is useless if WiFi reaches only one room.</li><li><strong>Lightning and grounding</strong> for antennas in open locations.</li><li><strong>Technical support</strong>: who comes to the site when something fails, and how fast.</li></ul>
<h2 id="connection-checklist">Connection checklist</h2>
<ul><li>Which applications must run, and are they latency-sensitive?</li><li>How many users and devices connect at the same time?</li><li>Is fiber or cellular signal available on site?</li><li>Is an automatic backup link needed?</li><li>What is the power source at the mounting point?</li></ul>
<p>Sentra installs Starlink, site networks, and fiber for offices and sites in East Kalimantan. See the <a href="/en/services/starlink">Starlink for Business service</a> and <a href="/en/services/instalasi-infrastruktur">infrastructure installation</a>.</p>""",
    },
    "zh": {
        "title": "加里曼丹分支机构与站点：Starlink、VSAT 与光纤对比",
        "description": "比较 Starlink、VSAT、光纤和蜂窝网络在加里曼丹分支机构、矿区和种植园的适用性：时延、稳定性、安装以及何时组合使用。",
        "category": "基础设施与网络",
        "lead": "没有一种连接适合所有地点。以下介绍如何按应用需求和站点条件比较 Starlink、VSAT、光纤和蜂窝网络，以及何时同时使用两条线路。",
        "wa_text": "您好 Sentra，我刚读了文章“Starlink、VSAT 与光纤对比”，想咨询我们站点的网络方案。",
        "aside": [("/services/starlink", "企业 Starlink 服务"), ("/services/instalasi-infrastruktur", "网络与光纤安装"), ("/blog/starlink-untuk-tambang", "矿区 Starlink")],
        "body": """<p>大城市的办公室通常用光纤就够了。难点在于县区分支机构、矿区、种植园以及远离网络的项目。在这些地方，可选的通常是光纤（如果能接入）、4G/5G 蜂窝网络、VSAT 或 Starlink。</p>
<h2 id="key-differences">主要区别</h2>
<ul><li><strong>光纤</strong>：最稳定、时延最低。前提是线缆能拉到现场，偏远站点的成本可能很高甚至无法接入。</li><li><strong>4G/5G 蜂窝网络</strong>：信号强时安装快、成本低。但许多站点信号不稳定或没有信号。</li><li><strong>VSAT</strong>：位于约 36,000 公里高度的静止轨道卫星网络。覆盖广，但距离太远，时延通常很高，超过半秒。</li><li><strong>Starlink</strong>：低轨卫星离地球近得多，时延通常为几十毫秒。安装相对快速，只需开阔的天空视野。</li></ul>
<h2 id="why-latency-matters">为什么时延很重要</h2>
<p>时延是数据往返所需的时间。下载文件时，高时延尚可接受；但视频通话、远程桌面、频繁访问服务器的应用以及 CCTV 实时画面，高时延会表现为声音断续、画面卡顿和应用变慢。因此只看 Mbps 不足以比较连接。</p>
<h2 id="choose-by-need">按需求选择</h2>
<ul><li><strong>有光纤经过的分支机构</strong>：光纤作为主线路，Starlink 或蜂窝网络作为备用。</li><li><strong>没有光纤的矿区或种植园</strong>：Starlink 作为主线路，有信号时以蜂窝网络作为备用。</li><li><strong>长期使用 VSAT 的站点</strong>：对时延敏感的应用可考虑 Starlink，有合同或系统依赖的部分继续使用 VSAT。</li><li><strong>临时项目</strong>：Starlink 或蜂窝网络，项目结束后可以搬走。</li></ul>
<h2 id="two-links-are-safer">两条线路比一条更可靠</h2>
<p>对于不能中断的业务，安装两条连接，并使用能自动切换流量的路由器（故障切换）。主线路中断时，应用通过备用线路继续运行。同一台路由器还可以让工作应用优先于个人使用。</p>
<h2 id="beyond-the-connection">连接之外常被忽视的因素</h2>
<ul><li><strong>供电</strong>：如果发电机关闭时设备没有 UPS 或太阳能，任何连接都会中断。</li><li><strong>本地网络</strong>：WiFi 只覆盖一个房间，线路再快也没用。</li><li><strong>防雷与接地</strong>：开阔地点的天线必须考虑。</li><li><strong>技术支持</strong>：出现故障时谁来现场、多久能到。</li></ul>
<h2 id="connection-checklist">选择连接的清单</h2>
<ul><li>哪些应用必须运行？是否对时延敏感？</li><li>同时连接的用户和设备有多少？</li><li>现场是否有光纤或蜂窝信号？</li><li>是否需要自动备用线路？</li><li>安装点的电源情况如何？</li></ul>
<p>Sentra 为东加里曼丹的办公室和站点安装 Starlink、现场网络和光纤。了解 <a href="/zh/services/starlink">企业 Starlink 服务</a>和<a href="/zh/services/instalasi-infrastruktur">基础设施安装</a>。</p>""",
    },
    "ko": {
        "title": "칼리만탄 지점과 현장을 위한 Starlink vs VSAT vs 광케이블",
        "description": "칼리만탄의 지점, 광산 현장, 농장을 위한 Starlink, VSAT, 광케이블, 이동통신 비교: 지연 시간, 안정성, 설치, 조합해서 쓰는 경우.",
        "category": "인프라 및 연결",
        "lead": "모든 장소에 가장 좋은 연결 하나는 없습니다. 애플리케이션 요구와 현장 조건에 따라 Starlink, VSAT, 광케이블, 이동통신을 비교하는 방법과 두 회선을 함께 쓰는 경우를 정리했습니다.",
        "wa_text": "안녕하세요 Sentra, \"Starlink vs VSAT vs 광케이블\" 아티클을 읽고 저희 현장 연결에 대해 상담받고 싶습니다.",
        "aside": [("/services/starlink", "기업용 Starlink 서비스"), ("/services/instalasi-infrastruktur", "네트워크·광케이블 설치"), ("/blog/starlink-untuk-tambang", "광산용 Starlink")],
        "body": """<p>대도시 사무실은 보통 광케이블이면 충분합니다. 문제는 군 단위 지점, 광산 현장, 농장, 네트워크에서 먼 프로젝트입니다. 이런 곳의 선택지는 보통 광케이블(닿는다면), 4G/5G 이동통신, VSAT, Starlink입니다.</p>
<h2 id="key-differences">주요 차이</h2>
<ul><li><strong>광케이블</strong>: 가장 안정적이고 지연 시간이 가장 짧습니다. 현장까지 케이블을 끌어와야 하며 원격지는 비용이 크거나 불가능할 수 있습니다.</li><li><strong>4G/5G 이동통신</strong>: 신호가 강하면 빠르고 저렴하게 설치됩니다. 많은 현장에서는 신호가 불안정하거나 없습니다.</li><li><strong>VSAT</strong>: 약 36,000 km 고도의 정지궤도 위성 인터넷입니다. 커버리지는 넓지만 거리 때문에 지연 시간이 보통 0.5초 이상으로 깁니다.</li><li><strong>Starlink</strong>: 지구에 훨씬 가까운 저궤도 위성이어서 지연 시간이 보통 수십 밀리초입니다. 하늘이 트여 있으면 비교적 빠르게 설치됩니다.</li></ul>
<h2 id="why-latency-matters">지연 시간이 중요한 이유</h2>
<p>지연 시간은 데이터가 갔다 돌아오는 데 걸리는 시간입니다. 파일 다운로드에는 긴 지연도 견딜 만합니다. 그러나 화상 통화, 원격 데스크톱, 서버와 자주 통신하는 앱, CCTV 실시간 영상에서는 끊기는 음성, 버벅이는 화면, 느린 앱으로 나타납니다. 그래서 Mbps만으로는 연결을 비교할 수 없습니다.</p>
<h2 id="choose-by-need">필요에 따라 선택</h2>
<ul><li><strong>광케이블이 지나는 지점</strong>: 광케이블을 주 회선으로, Starlink나 이동통신을 백업으로.</li><li><strong>광케이블이 없는 광산·농장</strong>: Starlink를 주 회선으로, 신호가 있으면 이동통신을 백업으로.</li><li><strong>오래 VSAT를 써 온 현장</strong>: 지연에 민감한 앱은 Starlink를 고려하고, 계약이나 시스템이 의존하는 부분은 VSAT를 유지합니다.</li><li><strong>임시 프로젝트</strong>: 프로젝트가 끝나면 옮길 수 있는 Starlink나 이동통신.</li></ul>
<h2 id="two-links-are-safer">회선 하나보다 둘이 안전하다</h2>
<p>멈추면 안 되는 운영에는 두 회선을 설치하고 트래픽을 자동으로 옮기는 라우터(페일오버)를 씁니다. 주 회선이 끊겨도 앱은 백업 회선으로 계속 동작합니다. 같은 라우터로 업무 앱을 개인 사용보다 우선할 수도 있습니다.</p>
<h2 id="beyond-the-connection">연결 외에 자주 결정적인 요소</h2>
<ul><li><strong>전원</strong>: 발전기를 끌 때 UPS나 태양광이 없으면 어떤 회선도 끊깁니다.</li><li><strong>로컬 네트워크</strong>: WiFi가 방 하나만 닿으면 빠른 회선도 소용없습니다.</li><li><strong>낙뢰와 접지</strong>: 개활지 안테나에 필요합니다.</li><li><strong>기술 지원</strong>: 장애 시 누가, 얼마나 빨리 현장에 오는지.</li></ul>
<h2 id="connection-checklist">연결 선택 체크리스트</h2>
<ul><li>반드시 돌아가야 할 앱은 무엇이며 지연에 민감합니까?</li><li>동시에 연결되는 사용자와 기기는 몇 대입니까?</li><li>현장에 광케이블이나 이동통신 신호가 있습니까?</li><li>자동 백업 회선이 필요합니까?</li><li>설치 지점의 전원은 어떻습니까?</li></ul>
<p>Sentra는 동칼리만탄의 사무실과 현장에 Starlink, 현장 네트워크, 광케이블을 설치합니다. <a href="/ko/services/starlink">기업용 Starlink 서비스</a>와 <a href="/ko/services/instalasi-infrastruktur">인프라 설치</a>를 확인하십시오.</p>""",
    },
    "ms": {
        "title": "Starlink vs VSAT vs Gentian Optik untuk Pejabat Cawangan dan Tapak di Kalimantan",
        "description": "Perbandingan Starlink, VSAT, gentian optik dan selular untuk pejabat cawangan, tapak lombong dan ladang di Kalimantan: latensi, kestabilan, pemasangan dan bila menggabungkannya.",
        "category": "Infrastruktur & kesambungan",
        "lead": "Tiada satu sambungan yang terbaik untuk semua lokasi. Begini cara membandingkan Starlink, VSAT, gentian optik dan selular berdasarkan keperluan aplikasi dan keadaan tapak, termasuk bila perlu menggunakan dua talian sekali gus.",
        "wa_text": "Hai Sentra, saya baru membaca artikel \"Starlink vs VSAT vs Gentian Optik\" dan ingin nasihat sambungan untuk lokasi kami.",
        "aside": [("/services/starlink", "Perkhidmatan Starlink untuk Perniagaan"), ("/services/instalasi-infrastruktur", "Pemasangan rangkaian & gentian optik"), ("/blog/starlink-untuk-tambang", "Starlink untuk perlombongan")],
        "body": """<p>Pejabat di bandar besar biasanya cukup menggunakan gentian optik. Cabarannya muncul di pejabat cawangan daerah, tapak lombong, ladang dan projek yang jauh dari rangkaian. Di sana pilihannya biasanya gentian optik (jika sampai), selular 4G/5G, VSAT atau Starlink.</p>
<h2 id="key-differences">Perbezaan utama</h2>
<ul><li><strong>Gentian optik</strong>: paling stabil dan latensinya paling rendah. Syaratnya kabel boleh ditarik ke lokasi, dan bagi tapak terpencil kosnya boleh tinggi atau tidak tersedia.</li><li><strong>Selular 4G/5G</strong>: cepat dipasang dan murah jika isyarat kuat. Di banyak tapak, isyarat tidak stabil atau tiada.</li><li><strong>VSAT</strong>: internet satelit geopegun pada ketinggian kira-kira 36,000 km. Liputannya luas, tetapi jarak sejauh itu menjadikan latensi umumnya tinggi, melebihi setengah saat.</li><li><strong>Starlink</strong>: satelit orbit rendah yang jauh lebih dekat ke bumi, jadi latensinya umumnya puluhan milisaat. Pemasangannya agak cepat, cukup dengan pandangan langit terbuka.</li></ul>
<h2 id="why-latency-matters">Mengapa latensi penting</h2>
<p>Latensi ialah masa data pergi dan kembali. Untuk memuat turun fail, latensi tinggi masih boleh diterima. Untuk panggilan video, desktop jauh, aplikasi yang kerap berhubung dengan pelayan dan CCTV langsung, latensi tinggi terasa sebagai suara terputus, skrin tersekat dan aplikasi perlahan. Oleh itu, Mbps sahaja tidak cukup untuk membandingkan sambungan.</p>
<h2 id="choose-by-need">Pilih mengikut keperluan</h2>
<ul><li><strong>Pejabat cawangan yang dilalui gentian optik</strong>: gentian optik sebagai talian utama, Starlink atau selular sebagai sandaran.</li><li><strong>Tapak lombong atau ladang tanpa gentian optik</strong>: Starlink sebagai talian utama, selular sebagai sandaran jika ada isyarat.</li><li><strong>Lokasi yang lama menggunakan VSAT</strong>: pertimbangkan Starlink untuk aplikasi yang sensitif latensi, sambil mengekalkan VSAT jika ada kontrak atau sistem yang bergantung padanya.</li><li><strong>Projek sementara</strong>: Starlink atau selular, kerana boleh dipindahkan apabila projek tamat.</li></ul>
<h2 id="two-links-are-safer">Dua talian lebih selamat daripada satu</h2>
<p>Untuk operasi yang tidak boleh terhenti, pasang dua sambungan dengan penghala yang boleh memindahkan trafik secara automatik (failover). Jika talian utama terputus, aplikasi terus berjalan melalui talian sandaran. Penghala yang sama juga boleh mengutamakan aplikasi kerja berbanding penggunaan peribadi.</p>
<h2 id="beyond-the-connection">Perkara di luar sambungan yang sering menentukan</h2>
<ul><li><strong>Bekalan kuasa</strong>: sebarang sambungan akan terputus jika peranti tiada UPS atau solar semasa genset dimatikan.</li><li><strong>Rangkaian setempat</strong>: sambungan laju tidak berguna jika WiFi hanya meliputi satu bilik.</li><li><strong>Kilat dan pembumian</strong> untuk antena di lokasi terbuka.</li><li><strong>Sokongan teknikal</strong>: siapa yang datang ke lokasi apabila berlaku gangguan, dan berapa lama.</li></ul>
<h2 id="connection-checklist">Senarai semak memilih sambungan</h2>
<ul><li>Aplikasi apa yang wajib berjalan, dan adakah ia sensitif latensi?</li><li>Berapa pengguna dan peranti yang bersambung serentak?</li><li>Adakah gentian optik atau isyarat selular tersedia di lokasi?</li><li>Adakah talian sandaran automatik diperlukan?</li><li>Bagaimana sumber kuasa di titik pemasangan?</li></ul>
<p>Sentra memasang Starlink, rangkaian tapak dan gentian optik untuk pejabat dan tapak di Kalimantan Timur. Lihat <a href="/ms/services/starlink">perkhidmatan Starlink untuk Perniagaan</a> dan <a href="/ms/services/instalasi-infrastruktur">pemasangan infrastruktur</a>.</p>""",
    },
}
