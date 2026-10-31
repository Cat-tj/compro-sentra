SLUG = "webgis-peta-tematik-pemda"
DATE = "2026-10-31"
COVER = "/assets/img/art/blog-webgis.webp"
OG_IMAGE = "/assets/og/art-blog-webgis.jpg"

LANGS = {
    "": {
        "title": "WebGIS dan Peta Tematik untuk Pemda: Belajar dari POMPy BATARA Barito Utara",
        "description": "Cara pemda membangun WebGIS dan peta tematik: lapisan data yang umum, langkah membangun, kesalahan yang sering terjadi, dengan contoh POMPy BATARA di Kabupaten Barito Utara.",
        "category": "Pemerintahan & data",
        "lead": "Data daerah tersebar di banyak dinas dan format. Peta tematik menyatukannya dalam satu tampilan yang bisa dibaca pimpinan dan masyarakat. Ini langkahnya, dengan contoh nyata dari Barito Utara.",
        "wa_text": "Halo Sentra, saya baru membaca artikel WebGIS dan peta tematik untuk pemda dan ingin berdiskusi untuk daerah kami.",
        "aside": [("/portfolio/pompy-batara", "Proyek POMPy BATARA"), ("/services/data-analytics", "Data & Analytics"), ("/industri/pemerintahan", "Solusi pemerintahan")],
        "body": """<p>WebGIS adalah sistem informasi geografis yang diakses lewat browser. Peta tematik adalah peta yang menampilkan satu tema data di atas wilayah, misalnya sebaran sekolah, fasilitas kesehatan, atau proyek pembangunan. Bagi pemda, keduanya berguna karena hampir semua keputusan pembangunan menyangkut tempat.</p>
<h2 id="masalah-data-tersebar">Masalah: data ada, tetapi tersebar</h2>
<p>Setiap dinas biasanya menyimpan datanya sendiri dalam spreadsheet, aplikasi sektoral, atau laporan PDF. Ketika pimpinan butuh gambaran wilayah, tim harus mengumpulkan dan menggabungkannya manual. Hasilnya lambat dan sering berbeda antar sumber.</p>
<h2 id="contoh-pompy-batara">Contoh: POMPy BATARA di Barito Utara</h2>
<p>POMPy BATARA adalah portal peta tematik (One Map) dan dashboard daerah milik Kabupaten Barito Utara. Portal ini mengintegrasikan data spasial dan tematik dari berbagai perangkat daerah ke dalam satu tampilan, sehingga informasi pembangunan lebih mudah dibuka dan dibaca dalam konteks wilayah. Sentra Technology terlibat dalam pengembangannya bersama Diskominfosandi Kabupaten Barito Utara, dan Kabupaten Barito Utara meraih Digital Innovation Award 2026 melalui portal ini, sebagaimana diberitakan ANTARA. Portalnya dapat dilihat di pompy.baritoutarakab.go.id.</p>
<h2 id="lapisan-data">Lapisan data yang umum</h2>
<ul><li><strong>Batas wilayah</strong> kecamatan dan desa sebagai dasar semua lapisan lain.</li><li><strong>Fasilitas pendidikan dan kesehatan</strong> beserta lokasinya.</li><li><strong>Infrastruktur</strong> seperti jalan, jembatan, dan jaringan.</li><li><strong>Proyek pembangunan</strong> dan statusnya.</li><li><strong>Penggunaan lahan</strong> dan rencana tata ruang.</li><li><strong>Data sosial</strong> yang sudah diagregasi per wilayah.</li></ul>
<h2 id="langkah-membangun">Langkah membangun</h2>
<ol><li><strong>Mulai dari data yang sudah ada</strong> di perangkat daerah, jangan menunggu data baru.</li><li><strong>Tetapkan pemilik tiap lapisan</strong>: siapa yang memperbarui, seberapa sering, dan dari sumber apa.</li><li><strong>Samakan standar</strong>: sistem koordinat, kode wilayah, dan metadata singkat tiap lapisan.</li><li><strong>Satukan bertahap</strong>: tampilkan 3 sampai 5 lapisan prioritas lebih dulu, lalu tambah.</li><li><strong>Rancang dua tampilan</strong>: dashboard ringkas untuk pimpinan dan peta publik yang mudah dibaca warga.</li><li><strong>Atur akses</strong>: data sensitif atau belum final tidak otomatis menjadi publik.</li><li><strong>Siapkan perawatan</strong>: jadwal pembaruan data, cadangan, dan tim yang bertanggung jawab.</li></ol>
<h2 id="kesalahan-umum">Kesalahan yang sering terjadi</h2>
<ul><li>Peta bagus tetapi datanya tidak diperbarui, sehingga cepat ditinggalkan.</li><li>Terlalu banyak lapisan sejak awal sampai pengguna bingung.</li><li>Tidak ada pemilik data, sehingga tiap dinas saling menunggu.</li><li>Dibangun hanya untuk tim teknis, bukan untuk pimpinan dan publik.</li></ul>
<h2 id="hubungan-dengan-spbe">Hubungan dengan SPBE dan Satu Data</h2>
<p>Peta tematik memperlihatkan data yang sudah rapi. Karena itu ia biasanya muncul sebagai hasil dari upaya menyatukan data di bawah <a href="/blog/spbe-pemda-persiapan">SPBE</a> dan Satu Data Daerah, bukan sebagai pengganti upaya itu.</p>
<p>Lihat dokumentasi proyek <a href="/portfolio/pompy-batara">POMPy BATARA</a>, layanan <a href="/services/data-analytics">Data &amp; Analytics</a>, dan <a href="/industri/pemerintahan">solusi pemerintahan</a> dari Sentra.</p>""",
    },
    "en": {
        "title": "WebGIS and Thematic Maps for Local Governments: Lessons from POMPy BATARA in Barito Utara",
        "description": "How local governments build WebGIS and thematic maps: common data layers, the steps, frequent mistakes, with the POMPy BATARA example from Barito Utara Regency.",
        "category": "Government & data",
        "lead": "Regional data is scattered across many agencies and formats. A thematic map brings it into one view that leaders and residents can read. Here are the steps, with a real example from Barito Utara.",
        "wa_text": "Hello Sentra, I just read your WebGIS and thematic map article for local governments and would like to discuss it for our region.",
        "aside": [("/portfolio/pompy-batara", "POMPy BATARA project"), ("/services/data-analytics", "Data & Analytics"), ("/industri/pemerintahan", "Government solutions")],
        "body": """<p>WebGIS is a geographic information system accessed through a browser. A thematic map shows one theme of data over a territory, such as the spread of schools, health facilities, or development projects. For local governments both are useful because almost every development decision is about a place.</p>
<h2 id="scattered-data">The problem: the data exists, but it is scattered</h2>
<p>Each agency usually keeps its data in spreadsheets, sector-specific apps, or PDF reports. When leaders need a picture of the region, staff collect and combine it by hand. The result is slow and often differs between sources.</p>
<h2 id="pompy-batara-example">Example: POMPy BATARA in Barito Utara</h2>
<p>POMPy BATARA is the thematic map (One Map) portal and regional dashboard of Barito Utara Regency. It integrates spatial and thematic data from several regional agencies into one view, so development information is easier to open and read in the context of the territory. Sentra Technology took part in its development together with the Barito Utara Regency communications and informatics office (Diskominfosandi), and the regency won the Digital Innovation Award 2026 through the portal, as reported by ANTARA. The portal is at pompy.baritoutarakab.go.id.</p>
<h2 id="data-layers">Common data layers</h2>
<ul><li><strong>Administrative boundaries</strong> of districts and villages as the base for every other layer.</li><li><strong>Education and health facilities</strong> with their locations.</li><li><strong>Infrastructure</strong> such as roads, bridges, and networks.</li><li><strong>Development projects</strong> and their status.</li><li><strong>Land use</strong> and spatial plans.</li><li><strong>Social data</strong> already aggregated per area.</li></ul>
<h2 id="steps">Steps to build it</h2>
<ol><li><strong>Start from data that already exists</strong> in regional agencies instead of waiting for new data.</li><li><strong>Name an owner for every layer</strong>: who updates it, how often, and from what source.</li><li><strong>Align standards</strong>: coordinate system, region codes, and a short metadata note per layer.</li><li><strong>Combine gradually</strong>: show 3 to 5 priority layers first, then add more.</li><li><strong>Design two views</strong>: a concise dashboard for leaders and a public map that residents can read easily.</li><li><strong>Control access</strong>: sensitive or unfinished data does not become public automatically.</li><li><strong>Plan upkeep</strong>: data update schedule, backups, and a team that is responsible.</li></ol>
<h2 id="common-mistakes">Common mistakes</h2>
<ul><li>A good-looking map with data that is never updated, so it is quickly abandoned.</li><li>Too many layers from the start, which confuses users.</li><li>No data owner, so every agency waits for the others.</li><li>Built only for the technical team, not for leaders and the public.</li></ul>
<h2 id="relation-to-spbe">Relation to SPBE and One Data</h2>
<p>A thematic map shows data that is already in order. That is why it usually appears as a result of efforts to unify data under <a href="/en/blog/spbe-pemda-persiapan">SPBE</a> and regional One Data, not as a replacement for them.</p>
<p>See the <a href="/en/portfolio/pompy-batara">POMPy BATARA</a> project page, Sentra's <a href="/en/services/data-analytics">Data &amp; Analytics</a> service, and <a href="/en/industri/pemerintahan">government solutions</a>.</p>""",
    },
    "zh": {
        "title": "地方政府的 WebGIS 与专题地图：北巴里托县 POMPy BATARA 的启示",
        "description": "地方政府如何建设 WebGIS 与专题地图：常见数据图层、建设步骤、常见错误，并以北巴里托县的 POMPy BATARA 为例。",
        "category": "政务与数据",
        "lead": "地方数据分散在许多部门和格式里。专题地图把它们汇成一个领导和居民都能看懂的视图。下面是步骤，并附北巴里托县的真实案例。",
        "wa_text": "你好 Sentra，我刚读了面向地方政府的 WebGIS 与专题地图文章，想为我们地区咨询。",
        "aside": [("/portfolio/pompy-batara", "POMPy BATARA 项目"), ("/services/data-analytics", "数据与分析"), ("/industri/pemerintahan", "政府行业方案")],
        "body": """<p>WebGIS 是通过浏览器访问的地理信息系统。专题地图是在地域上展示某一主题数据的地图，例如学校、医疗设施或建设项目的分布。对地方政府来说两者都很有用，因为几乎所有发展决策都与地点有关。</p>
<h2 id="scattered-data">问题：数据有，但很分散</h2>
<p>每个部门通常把数据存在电子表格、专业应用或 PDF 报告里。领导需要了解全区概况时，工作人员只能手工收集和合并，结果既慢，来源之间还常常对不上。</p>
<h2 id="pompy-batara-example">案例：北巴里托县的 POMPy BATARA</h2>
<p>POMPy BATARA 是北巴里托县的专题地图（One Map）门户和地区仪表板。它把多个地方部门的空间数据和专题数据整合到一个视图中，让发展信息更容易打开，并能结合地域来解读。Sentra Technology 与北巴里托县通信信息局（Diskominfosandi）共同参与了开发，据 ANTARA 报道，该县凭借这个门户获得了 2026 年数字创新奖。门户网址为 pompy.baritoutarakab.go.id。</p>
<h2 id="data-layers">常见数据图层</h2>
<ul><li><strong>行政边界</strong>：区和村，作为所有其他图层的基础。</li><li><strong>教育与医疗设施</strong>及其位置。</li><li><strong>基础设施</strong>：道路、桥梁和网络。</li><li><strong>建设项目</strong>及其状态。</li><li><strong>土地利用</strong>和空间规划。</li><li><strong>社会数据</strong>：已按区域汇总。</li></ul>
<h2 id="steps">建设步骤</h2>
<ol><li><strong>从已有数据开始</strong>，不要等待新数据。</li><li><strong>为每个图层指定负责人</strong>：谁更新、多久更新、数据来源是什么。</li><li><strong>统一标准</strong>：坐标系、行政区划代码和每个图层的简短元数据。</li><li><strong>逐步整合</strong>：先展示 3 到 5 个重点图层，再逐步增加。</li><li><strong>设计两种视图</strong>：给领导的简洁仪表板，以及居民容易读懂的公开地图。</li><li><strong>控制访问</strong>：敏感或未定稿的数据不会自动公开。</li><li><strong>规划维护</strong>：数据更新计划、备份和负责的团队。</li></ol>
<h2 id="common-mistakes">常见错误</h2>
<ul><li>地图好看但数据不更新，很快就被弃用。</li><li>一开始图层太多，用户看不明白。</li><li>没有数据负责人，各部门互相等待。</li><li>只为技术团队构建，而不是为领导和公众。</li></ul>
<h2 id="relation-to-spbe">与 SPBE 和统一数据的关系</h2>
<p>专题地图展示的是已经整理好的数据。所以它通常是在 <a href="/zh/blog/spbe-pemda-persiapan">SPBE</a> 和地方统一数据推进整合之后出现的成果，而不是替代这些工作。</p>
<p>了解 <a href="/zh/portfolio/pompy-batara">POMPy BATARA</a> 项目页、Sentra 的<a href="/zh/services/data-analytics">数据与分析</a>服务和<a href="/zh/industri/pemerintahan">政府行业方案</a>。</p>""",
    },
    "ko": {
        "title": "지방정부를 위한 WebGIS와 주제도: 북바리토군 POMPy BATARA에서 배우기",
        "description": "지방정부가 WebGIS와 주제도를 만드는 방법: 흔한 데이터 레이어, 구축 단계, 자주 하는 실수, 북바리토군 POMPy BATARA 사례.",
        "category": "정부 및 데이터",
        "lead": "지역 데이터는 여러 부서와 형식에 흩어져 있습니다. 주제도는 이를 지도부와 주민이 읽을 수 있는 하나의 화면으로 모읍니다. 북바리토군의 실제 사례와 함께 단계를 소개합니다.",
        "wa_text": "안녕하세요 Sentra, 지방정부용 WebGIS와 주제도 글을 읽고 저희 지역에 대해 상담하고 싶습니다.",
        "aside": [("/portfolio/pompy-batara", "POMPy BATARA 프로젝트"), ("/services/data-analytics", "데이터 및 분석"), ("/industri/pemerintahan", "정부 솔루션")],
        "body": """<p>WebGIS는 브라우저로 접속하는 지리정보시스템입니다. 주제도는 학교, 보건 시설, 개발 사업의 분포처럼 하나의 주제를 지역 위에 보여 주는 지도입니다. 거의 모든 개발 결정이 장소와 관련되기 때문에 지방정부에 둘 다 유용합니다.</p>
<h2 id="scattered-data">문제: 데이터는 있지만 흩어져 있다</h2>
<p>각 부서는 보통 스프레드시트, 분야별 앱, PDF 보고서에 데이터를 보관합니다. 지도부가 지역 전체 그림이 필요할 때 직원이 손으로 모아 합칩니다. 결과는 느리고 출처마다 다른 경우가 많습니다.</p>
<h2 id="pompy-batara-example">사례: 북바리토군의 POMPy BATARA</h2>
<p>POMPy BATARA는 북바리토군의 주제도(One Map) 포털이자 지역 대시보드입니다. 여러 지방 부서의 공간 및 주제 데이터를 하나의 화면으로 통합해, 개발 정보를 더 쉽게 열어 보고 지역 맥락에서 읽을 수 있게 합니다. Sentra Technology는 북바리토군 정보통신부서(Diskominfosandi)와 함께 개발에 참여했고, ANTARA 보도에 따르면 이 포털로 군이 2026년 디지털 혁신상을 받았습니다. 포털 주소는 pompy.baritoutarakab.go.id입니다.</p>
<h2 id="data-layers">흔한 데이터 레이어</h2>
<ul><li><strong>행정 경계</strong>: 면과 마을. 모든 레이어의 기반입니다.</li><li><strong>교육 및 보건 시설</strong>과 위치.</li><li><strong>인프라</strong>: 도로, 교량, 네트워크.</li><li><strong>개발 사업</strong>과 진행 상태.</li><li><strong>토지 이용</strong>과 공간 계획.</li><li><strong>사회 데이터</strong>: 지역별로 이미 집계된 것.</li></ul>
<h2 id="steps">구축 단계</h2>
<ol><li><strong>이미 있는 데이터에서 시작</strong>하고 새 데이터를 기다리지 않습니다.</li><li><strong>레이어마다 담당자 지정</strong>: 누가, 얼마나 자주, 어떤 출처로 갱신하는지.</li><li><strong>표준 통일</strong>: 좌표계, 지역 코드, 레이어별 짧은 메타데이터.</li><li><strong>단계적으로 통합</strong>: 우선 3~5개 레이어를 먼저 보여 주고 늘려 갑니다.</li><li><strong>화면 두 가지 설계</strong>: 지도부용 간결한 대시보드와 주민이 쉽게 읽는 공개 지도.</li><li><strong>접근 제어</strong>: 민감하거나 확정되지 않은 데이터는 자동으로 공개되지 않습니다.</li><li><strong>유지관리 계획</strong>: 데이터 갱신 일정, 백업, 책임 팀.</li></ol>
<h2 id="common-mistakes">흔한 실수</h2>
<ul><li>지도는 멋지지만 데이터가 갱신되지 않아 곧 외면받습니다.</li><li>처음부터 레이어가 너무 많아 사용자가 혼란스러워합니다.</li><li>데이터 담당자가 없어 부서끼리 서로 기다립니다.</li><li>기술 팀만을 위해 만들고 지도부와 대중은 고려하지 않습니다.</li></ul>
<h2 id="relation-to-spbe">SPBE 및 단일 데이터와의 관계</h2>
<p>주제도는 이미 정리된 데이터를 보여 줍니다. 그래서 보통 <a href="/ko/blog/spbe-pemda-persiapan">SPBE</a>와 지역 단일 데이터로 데이터를 통합하려는 노력의 결과로 나타나며, 그 노력을 대체하지는 않습니다.</p>
<p><a href="/ko/portfolio/pompy-batara">POMPy BATARA</a> 프로젝트 페이지, Sentra의 <a href="/ko/services/data-analytics">데이터 및 분석</a> 서비스, <a href="/ko/industri/pemerintahan">정부 솔루션</a>을 참고하세요.</p>""",
    },
    "ms": {
        "title": "WebGIS dan Peta Tematik untuk Kerajaan Daerah: Pengajaran daripada POMPy BATARA Barito Utara",
        "description": "Cara kerajaan daerah membina WebGIS dan peta tematik: lapisan data lazim, langkah membina, kesilapan yang kerap berlaku, dengan contoh POMPy BATARA di Daerah Barito Utara.",
        "category": "Kerajaan & data",
        "lead": "Data daerah bertaburan di banyak jabatan dan format. Peta tematik menyatukannya dalam satu paparan yang boleh dibaca pimpinan dan penduduk. Ini langkahnya, dengan contoh sebenar dari Barito Utara.",
        "wa_text": "Hai Sentra, saya baru membaca artikel WebGIS dan peta tematik untuk kerajaan daerah dan ingin berbincang untuk daerah kami.",
        "aside": [("/portfolio/pompy-batara", "Projek POMPy BATARA"), ("/services/data-analytics", "Data & Analitik"), ("/industri/pemerintahan", "Penyelesaian kerajaan")],
        "body": """<p>WebGIS ialah sistem maklumat geografi yang diakses melalui pelayar. Peta tematik ialah peta yang memaparkan satu tema data di atas wilayah, contohnya taburan sekolah, kemudahan kesihatan, atau projek pembangunan. Bagi kerajaan daerah kedua-duanya berguna kerana hampir semua keputusan pembangunan berkait dengan tempat.</p>
<h2 id="scattered-data">Masalah: data ada, tetapi bertaburan</h2>
<p>Setiap jabatan biasanya menyimpan data dalam hamparan, aplikasi sektor, atau laporan PDF. Apabila pimpinan memerlukan gambaran wilayah, pasukan mengumpul dan menggabungkannya secara manual. Hasilnya perlahan dan sering berbeza antara sumber.</p>
<h2 id="pompy-batara-example">Contoh: POMPy BATARA di Barito Utara</h2>
<p>POMPy BATARA ialah portal peta tematik (One Map) dan papan pemuka daerah milik Daerah Barito Utara. Portal ini menyepadukan data spatial dan tematik daripada beberapa jabatan daerah ke dalam satu paparan, supaya maklumat pembangunan lebih mudah dibuka dan dibaca dalam konteks wilayah. Sentra Technology terlibat dalam pembangunannya bersama Diskominfosandi Daerah Barito Utara, dan daerah itu memenangi Digital Innovation Award 2026 melalui portal ini, seperti dilaporkan ANTARA. Portal boleh dilihat di pompy.baritoutarakab.go.id.</p>
<h2 id="data-layers">Lapisan data yang lazim</h2>
<ul><li><strong>Sempadan wilayah</strong> daerah kecil dan kampung sebagai asas semua lapisan lain.</li><li><strong>Kemudahan pendidikan dan kesihatan</strong> beserta lokasinya.</li><li><strong>Infrastruktur</strong> seperti jalan, jambatan, dan rangkaian.</li><li><strong>Projek pembangunan</strong> dan statusnya.</li><li><strong>Guna tanah</strong> dan rancangan tata ruang.</li><li><strong>Data sosial</strong> yang sudah dikumpulkan mengikut kawasan.</li></ul>
<h2 id="steps">Langkah membina</h2>
<ol><li><strong>Mulakan dengan data yang sudah ada</strong> di jabatan daerah, jangan menunggu data baharu.</li><li><strong>Tetapkan pemilik setiap lapisan</strong>: siapa yang mengemas kini, berapa kerap, dan daripada sumber mana.</li><li><strong>Samakan standard</strong>: sistem koordinat, kod wilayah, dan metadata ringkas setiap lapisan.</li><li><strong>Satukan secara berperingkat</strong>: paparkan 3 hingga 5 lapisan keutamaan dahulu, kemudian tambah.</li><li><strong>Reka dua paparan</strong>: papan pemuka ringkas untuk pimpinan dan peta awam yang mudah dibaca penduduk.</li><li><strong>Atur akses</strong>: data sensitif atau belum muktamad tidak menjadi awam secara automatik.</li><li><strong>Sediakan penyelenggaraan</strong>: jadual kemas kini data, sandaran, dan pasukan yang bertanggungjawab.</li></ol>
<h2 id="common-mistakes">Kesilapan yang kerap berlaku</h2>
<ul><li>Peta cantik tetapi datanya tidak dikemas kini, lalu cepat ditinggalkan.</li><li>Terlalu banyak lapisan sejak awal sehingga pengguna keliru.</li><li>Tiada pemilik data, jadi setiap jabatan saling menunggu.</li><li>Dibina untuk pasukan teknikal sahaja, bukan untuk pimpinan dan orang awam.</li></ul>
<h2 id="relation-to-spbe">Kaitan dengan SPBE dan Satu Data</h2>
<p>Peta tematik memaparkan data yang sudah teratur. Sebab itu ia biasanya muncul sebagai hasil usaha menyatukan data di bawah <a href="/ms/blog/spbe-pemda-persiapan">SPBE</a> dan Satu Data Daerah, bukan sebagai pengganti usaha itu.</p>
<p>Lihat halaman projek <a href="/ms/portfolio/pompy-batara">POMPy BATARA</a>, perkhidmatan <a href="/ms/services/data-analytics">Data &amp; Analitik</a>, dan <a href="/ms/industri/pemerintahan">penyelesaian kerajaan</a> daripada Sentra.</p>""",
    },
}
