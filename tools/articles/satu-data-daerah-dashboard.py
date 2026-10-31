SLUG = "satu-data-daerah-dashboard"
DATE = "2026-10-31"
COVER = "/assets/img/art/blog-satu-data.webp"
OG_IMAGE = "/assets/og/art-blog-satu-data.jpg"

LANGS = {
    "": {
        "title": "Satu Data Daerah: Langkah Membangun Dashboard untuk Pimpinan",
        "description": "Langkah pemda membangun Satu Data Daerah dan dashboard pimpinan: inventaris data, pemilik data, metadata, portal, pembaruan, dan perlindungan data pribadi.",
        "category": "Pemerintahan & data",
        "lead": "Dashboard pimpinan hanya sebaik datanya. Ini urutan kerja yang biasanya berhasil, dari mengumpulkan data sampai menampilkannya.",
        "wa_text": "Halo Sentra, saya baru membaca artikel Satu Data Daerah dan ingin berdiskusi untuk instansi kami.",
        "aside": [("/services/data-analytics", "Data & Analytics"), ("/industri/pemerintahan", "Solusi pemerintahan"), ("/portfolio/pompy-batara", "Proyek POMPy BATARA")],
        "body": """<p>Satu Data Daerah adalah upaya menjadikan data pemerintah daerah akurat, mutakhir, terpadu, dan mudah dibagikan antar perangkat daerah. Landasannya adalah kebijakan Satu Data Indonesia (Perpres Nomor 39 Tahun 2019), yang meminta data memiliki standar, metadata, dan interoperabilitas, serta pembagian peran antara produsen dan pengelola data.</p>
<p>Dashboard pimpinan adalah wajah yang terlihat dari upaya itu. Namun dashboard yang dibangun lebih dulu daripada rapinya data biasanya cepat ditinggalkan, karena angkanya berbeda dari laporan dinas.</p>
<h2 id="mulai-dari-pertanyaan">Mulai dari pertanyaan pimpinan</h2>
<p>Tanyakan apa yang ingin diketahui pimpinan setiap pagi atau setiap rapat. Dari sana, tentukan 10 sampai 20 indikator prioritas, misalnya realisasi anggaran, capaian program, jumlah penduduk miskin, kondisi infrastruktur, dan angka layanan publik. Jangan mulai dari semua data yang ada.</p>
<h2 id="langkah-membangun">Langkah membangun</h2>
<ol><li><strong>Inventaris data.</strong> Catat data apa yang dimiliki tiap perangkat daerah, formatnya, dan seberapa sering diperbarui.</li><li><strong>Tetapkan indikator prioritas</strong> dari pertanyaan pimpinan.</li><li><strong>Tetapkan peran.</strong> Siapa produsen data di tiap dinas, dan siapa yang mengelola portal data secara keseluruhan.</li><li><strong>Samakan definisi dan standar</strong>: satuan, periode, kode wilayah, dan rumus tiap indikator, ditulis dalam metadata singkat.</li><li><strong>Kumpulkan data ke satu tempat</strong> lewat unggah terjadwal atau integrasi langsung dari aplikasi dinas.</li><li><strong>Validasi.</strong> Bandingkan angka dengan laporan resmi, dan catat siapa yang menyetujuinya.</li><li><strong>Bangun dashboard</strong> dengan tampilan ringkas: angka utama, tren, dan perbandingan antar wilayah, lalu rincian bila diklik.</li><li><strong>Jadwalkan pembaruan</strong> dan tentukan siapa yang bertanggung jawab bila data terlambat.</li></ol>
<h2 id="peta-dan-wilayah">Menambah dimensi wilayah</h2>
<p>Banyak indikator lebih mudah dibaca di peta. Bila data sudah rapi, lapisan peta bisa ditambahkan di atasnya. Contohnya ada di artikel <a href="/blog/webgis-peta-tematik-pemda">WebGIS dan peta tematik untuk pemda</a>.</p>
<h2 id="perlindungan-data">Perlindungan data pribadi</h2>
<p>Tidak semua data boleh dibuka. Data yang memuat identitas perorangan tunduk pada Undang-Undang Pelindungan Data Pribadi (UU Nomor 27 Tahun 2022). Tampilkan data yang sudah diagregasi pada dashboard, batasi akses ke data rinci, dan catat siapa yang membukanya.</p>
<h2 id="kesalahan-umum">Kesalahan yang sering terjadi</h2>
<ul><li>Membangun dashboard dulu, merapikan data belakangan.</li><li>Terlalu banyak indikator sehingga pimpinan tidak membukanya.</li><li>Tidak ada yang bertanggung jawab atas pembaruan, sehingga angka basi.</li><li>Tiap dinas memakai definisi berbeda untuk istilah yang sama.</li></ul>
<h2 id="berapa-lama">Berapa lama dan siapa yang terlibat</h2>
<p>Versi pertama dengan 10 sampai 20 indikator bisa disiapkan lebih cepat daripada seluruh portal data. Libatkan perangkat daerah yang mengelola data perencanaan, statistik, dan teknologi informasi, karena merekalah yang biasanya memegang data dan standar.</p>
<p>Lihat layanan <a href="/services/data-analytics">Data &amp; Analytics</a> dan <a href="/industri/pemerintahan">solusi pemerintahan</a> dari Sentra, serta persiapan yang lebih luas di <a href="/blog/spbe-pemda-persiapan">artikel SPBE untuk pemda</a>.</p>""",
    },
    "en": {
        "title": "Regional One Data: Steps to Build a Dashboard for Leaders",
        "description": "Steps for local governments building Regional One Data and a leadership dashboard: data inventory, data owners, metadata, a portal, updates, and personal data protection.",
        "category": "Government & data",
        "lead": "A leadership dashboard is only as good as its data. Here is the order of work that usually succeeds, from collecting data to displaying it.",
        "wa_text": "Hello Sentra, I just read your Regional One Data article and would like to discuss it for our agency.",
        "aside": [("/services/data-analytics", "Data & Analytics"), ("/industri/pemerintahan", "Government solutions"), ("/portfolio/pompy-batara", "POMPy BATARA project")],
        "body": """<p>Regional One Data is the effort to make a local government's data accurate, current, integrated, and easy to share between regional agencies. Its basis is Indonesia's One Data policy (Presidential Regulation No. 39 of 2019), which asks data to have standards, metadata, and interoperability, and divides roles between data producers and data managers.</p>
<p>The leadership dashboard is the visible face of that effort. But a dashboard built before the data is in order is usually abandoned quickly, because its numbers differ from agency reports.</p>
<h2 id="start-from-questions">Start from the leader's questions</h2>
<p>Ask what the leader wants to know every morning or in every meeting. From there, choose 10 to 20 priority indicators, such as budget realization, program achievement, number of residents in poverty, infrastructure condition, and public service figures. Do not start from all the data that exists.</p>
<h2 id="steps">Steps to build it</h2>
<ol><li><strong>Inventory the data.</strong> Record what data each regional agency holds, its format, and how often it is updated.</li><li><strong>Set the priority indicators</strong> from the leader's questions.</li><li><strong>Assign roles.</strong> Who produces the data in each agency, and who manages the data portal overall.</li><li><strong>Align definitions and standards</strong>: units, periods, region codes, and the formula for each indicator, written in short metadata.</li><li><strong>Collect the data in one place</strong> through scheduled uploads or direct integration from agency applications.</li><li><strong>Validate.</strong> Compare the numbers with official reports and record who approved them.</li><li><strong>Build the dashboard</strong> with a concise view: headline numbers, trends, and comparison across areas, with detail on click.</li><li><strong>Schedule updates</strong> and decide who is responsible when data is late.</li></ol>
<h2 id="maps">Adding the place dimension</h2>
<p>Many indicators are easier to read on a map. Once the data is tidy, a map layer can be added on top. An example is in the article on <a href="/en/blog/webgis-peta-tematik-pemda">WebGIS and thematic maps for local governments</a>.</p>
<h2 id="data-protection">Personal data protection</h2>
<p>Not all data may be opened. Data containing personal identity is subject to the Personal Data Protection Law (Law No. 27 of 2022). Show aggregated data on the dashboard, restrict access to detailed data, and record who opens it.</p>
<h2 id="common-mistakes">Common mistakes</h2>
<ul><li>Building the dashboard first and tidying the data later.</li><li>Too many indicators, so leaders never open it.</li><li>No one responsible for updates, so the numbers go stale.</li><li>Each agency uses a different definition for the same term.</li></ul>
<h2 id="how-long">How long and who is involved</h2>
<p>A first version with 10 to 20 indicators can be ready much sooner than a whole data portal. Involve the agencies that handle planning data, statistics, and information technology, because they usually hold the data and the standards.</p>
<p>See Sentra's <a href="/en/services/data-analytics">Data &amp; Analytics</a> service and <a href="/en/industri/pemerintahan">government solutions</a>, and the broader preparation in the <a href="/en/blog/spbe-pemda-persiapan">SPBE article for local governments</a>.</p>""",
    },
    "zh": {
        "title": "地方统一数据：为领导搭建仪表板的步骤",
        "description": "地方政府搭建地方统一数据和领导仪表板的步骤：数据盘点、数据负责人、元数据、门户、更新和个人数据保护。",
        "category": "政务与数据",
        "lead": "领导仪表板的价值取决于数据。这是通常行之有效的工作顺序，从收集数据到展示数据。",
        "wa_text": "你好 Sentra，我刚读了地方统一数据文章，想为我们单位咨询。",
        "aside": [("/services/data-analytics", "数据与分析"), ("/industri/pemerintahan", "政府行业方案"), ("/portfolio/pompy-batara", "POMPy BATARA 项目")],
        "body": """<p>地方统一数据，是让地方政府的数据准确、及时、整合并便于各部门共享的努力。其依据是印尼的统一数据政策（2019 年第 39 号总统条例），要求数据具备标准、元数据和互操作性，并划分数据生产者与数据管理者的角色。</p>
<p>领导仪表板是这项工作可见的门面。但在数据整理好之前就先做的仪表板，通常很快被弃用，因为它的数字和部门报告对不上。</p>
<h2 id="start-from-questions">从领导的问题出发</h2>
<p>先问领导每天早上或每次会议想知道什么。据此选定 10 到 20 个重点指标，例如预算执行、项目完成、贫困人口数、基础设施状况和公共服务数据。不要从所有现有数据开始。</p>
<h2 id="steps">建设步骤</h2>
<ol><li><strong>盘点数据。</strong>记录各地方部门持有什么数据、格式以及更新频率。</li><li><strong>确定重点指标</strong>，来自领导的问题。</li><li><strong>明确角色。</strong>各部门谁是数据生产者，谁负责整体的数据门户。</li><li><strong>统一定义和标准</strong>：单位、周期、行政区划代码和每个指标的计算公式，写成简短的元数据。</li><li><strong>把数据汇集到一处</strong>，通过定时上传或与部门应用直接对接。</li><li><strong>验证。</strong>把数字与官方报告对照，并记录由谁批准。</li><li><strong>搭建仪表板</strong>，视图简洁：核心数字、趋势和地区对比，点击后查看明细。</li><li><strong>安排更新</strong>，并确定数据延迟时由谁负责。</li></ol>
<h2 id="maps">加入地域维度</h2>
<p>许多指标在地图上更容易读懂。数据整理好之后，可以在其上叠加地图图层。示例见文章<a href="/zh/blog/webgis-peta-tematik-pemda">地方政府的 WebGIS 与专题地图</a>。</p>
<h2 id="data-protection">个人数据保护</h2>
<p>并非所有数据都能公开。含有个人身份的数据受《个人数据保护法》（2022 年第 27 号法律）约束。仪表板上展示汇总数据，限制对明细数据的访问，并记录谁打开过。</p>
<h2 id="common-mistakes">常见错误</h2>
<ul><li>先做仪表板，后整理数据。</li><li>指标太多，领导根本不打开。</li><li>没有人负责更新，数字很快过时。</li><li>各部门对同一个术语使用不同的定义。</li></ul>
<h2 id="how-long">需要多久、涉及哪些人</h2>
<p>包含 10 到 20 个指标的第一版，比整个数据门户能更快准备好。请让管理规划数据、统计和信息技术的部门参与，因为数据和标准通常掌握在他们手里。</p>
<p>了解 Sentra 的<a href="/zh/services/data-analytics">数据与分析</a>服务和<a href="/zh/industri/pemerintahan">政府行业方案</a>，以及更广泛的准备工作，见<a href="/zh/blog/spbe-pemda-persiapan">面向地方政府的 SPBE 文章</a>。</p>""",
    },
    "ko": {
        "title": "지역 단일 데이터: 지도부용 대시보드를 만드는 단계",
        "description": "지방정부가 지역 단일 데이터와 지도부용 대시보드를 만드는 단계: 데이터 목록화, 데이터 담당자, 메타데이터, 포털, 갱신, 개인정보 보호.",
        "category": "정부 및 데이터",
        "lead": "지도부용 대시보드는 데이터만큼만 좋습니다. 데이터를 모으는 일부터 보여 주는 일까지, 보통 성공하는 작업 순서를 소개합니다.",
        "wa_text": "안녕하세요 Sentra, 지역 단일 데이터 글을 읽고 저희 기관에 대해 상담하고 싶습니다.",
        "aside": [("/services/data-analytics", "데이터 및 분석"), ("/industri/pemerintahan", "정부 솔루션"), ("/portfolio/pompy-batara", "POMPy BATARA 프로젝트")],
        "body": """<p>지역 단일 데이터는 지방정부의 데이터를 정확하고, 최신이며, 통합되고, 지방 부서 간에 쉽게 공유되도록 만드는 노력입니다. 그 근거는 인도네시아의 단일 데이터 정책(2019년 대통령령 제39호)으로, 데이터에 표준, 메타데이터, 상호운용성을 갖추도록 하고 데이터 생산자와 관리자의 역할을 나눕니다.</p>
<p>지도부용 대시보드는 그 노력의 눈에 보이는 얼굴입니다. 하지만 데이터가 정리되기 전에 만든 대시보드는 숫자가 부서 보고서와 달라서 금세 외면받는 경우가 많습니다.</p>
<h2 id="start-from-questions">지도부의 질문에서 시작</h2>
<p>지도부가 매일 아침이나 회의마다 무엇을 알고 싶은지 먼저 물으세요. 거기서 예산 집행, 사업 성과, 빈곤 인구, 인프라 상태, 공공 서비스 수치처럼 10~20개의 우선 지표를 정합니다. 있는 모든 데이터에서 시작하지 마세요.</p>
<h2 id="steps">구축 단계</h2>
<ol><li><strong>데이터 목록화.</strong> 각 지방 부서가 어떤 데이터를 갖고 있는지, 형식, 갱신 주기를 기록합니다.</li><li><strong>우선 지표 확정</strong>: 지도부의 질문에서 출발합니다.</li><li><strong>역할 지정.</strong> 부서별 데이터 생산자는 누구이고 데이터 포털 전체를 누가 관리하는지.</li><li><strong>정의와 표준 통일</strong>: 단위, 기간, 지역 코드, 지표별 산식을 짧은 메타데이터로 기록합니다.</li><li><strong>한곳에 데이터 수집</strong>: 정기 업로드나 부서 애플리케이션과의 직접 연동으로 합니다.</li><li><strong>검증.</strong> 숫자를 공식 보고서와 비교하고 누가 승인했는지 기록합니다.</li><li><strong>대시보드 구축</strong>: 핵심 수치, 추세, 지역 비교를 간결하게 보여 주고 클릭하면 세부 내용을 봅니다.</li><li><strong>갱신 일정 수립</strong>과 데이터가 늦어질 때 책임자 지정.</li></ol>
<h2 id="maps">지역 차원 더하기</h2>
<p>많은 지표는 지도에서 더 읽기 쉽습니다. 데이터가 정리되면 그 위에 지도 레이어를 얹을 수 있습니다. 사례는 <a href="/ko/blog/webgis-peta-tematik-pemda">지방정부를 위한 WebGIS와 주제도</a> 글에 있습니다.</p>
<h2 id="data-protection">개인정보 보호</h2>
<p>모든 데이터를 공개할 수는 없습니다. 개인 식별 정보가 담긴 데이터는 개인정보보호법(2022년 법률 제27호)의 적용을 받습니다. 대시보드에는 집계된 데이터를 보여 주고, 세부 데이터 접근을 제한하며, 누가 열람했는지 기록하세요.</p>
<h2 id="common-mistakes">흔한 실수</h2>
<ul><li>대시보드를 먼저 만들고 데이터 정리는 나중에 합니다.</li><li>지표가 너무 많아 지도부가 열어 보지 않습니다.</li><li>갱신 책임자가 없어 숫자가 낡습니다.</li><li>부서마다 같은 용어를 다르게 정의합니다.</li></ul>
<h2 id="how-long">기간과 관련 부서</h2>
<p>지표 10~20개의 첫 버전은 전체 데이터 포털보다 훨씬 빨리 준비할 수 있습니다. 계획 데이터, 통계, 정보기술을 담당하는 부서를 참여시키세요. 데이터와 표준을 보통 그들이 갖고 있기 때문입니다.</p>
<p>Sentra의 <a href="/ko/services/data-analytics">데이터 및 분석</a> 서비스와 <a href="/ko/industri/pemerintahan">정부 솔루션</a>, 그리고 더 넓은 준비 사항은 <a href="/ko/blog/spbe-pemda-persiapan">지방정부용 SPBE 글</a>을 참고하세요.</p>""",
    },
    "ms": {
        "title": "Satu Data Daerah: Langkah Membina Papan Pemuka untuk Pimpinan",
        "description": "Langkah kerajaan daerah membina Satu Data Daerah dan papan pemuka pimpinan: inventori data, pemilik data, metadata, portal, kemas kini, dan perlindungan data peribadi.",
        "category": "Kerajaan & data",
        "lead": "Papan pemuka pimpinan hanya sebaik datanya. Ini urutan kerja yang biasanya berjaya, daripada mengumpul data hingga memaparkannya.",
        "wa_text": "Hai Sentra, saya baru membaca artikel Satu Data Daerah dan ingin berbincang untuk agensi kami.",
        "aside": [("/services/data-analytics", "Data & Analitik"), ("/industri/pemerintahan", "Penyelesaian kerajaan"), ("/portfolio/pompy-batara", "Projek POMPy BATARA")],
        "body": """<p>Satu Data Daerah ialah usaha menjadikan data kerajaan daerah tepat, terkini, bersepadu, dan mudah dikongsi antara jabatan daerah. Asasnya ialah dasar Satu Data Indonesia (Peraturan Presiden No. 39 Tahun 2019), yang mahu data mempunyai standard, metadata, dan kebolehoperasian, serta pembahagian peranan antara pengeluar dan pengurus data.</p>
<p>Papan pemuka pimpinan ialah wajah yang kelihatan bagi usaha itu. Namun papan pemuka yang dibina sebelum data teratur biasanya cepat ditinggalkan, kerana angkanya berbeza daripada laporan jabatan.</p>
<h2 id="start-from-questions">Mulakan daripada soalan pimpinan</h2>
<p>Tanya apa yang ingin diketahui pimpinan setiap pagi atau setiap mesyuarat. Daripada situ, tetapkan 10 hingga 20 penunjuk keutamaan, contohnya realisasi bajet, pencapaian program, bilangan penduduk miskin, keadaan infrastruktur, dan angka perkhidmatan awam. Jangan bermula daripada semua data yang ada.</p>
<h2 id="steps">Langkah membina</h2>
<ol><li><strong>Inventori data.</strong> Rekodkan data apa yang dimiliki setiap jabatan daerah, formatnya, dan berapa kerap dikemas kini.</li><li><strong>Tetapkan penunjuk keutamaan</strong> daripada soalan pimpinan.</li><li><strong>Tetapkan peranan.</strong> Siapa pengeluar data di setiap jabatan, dan siapa yang mengurus portal data secara keseluruhan.</li><li><strong>Samakan definisi dan standard</strong>: unit, tempoh, kod wilayah, dan formula setiap penunjuk, ditulis dalam metadata ringkas.</li><li><strong>Kumpulkan data di satu tempat</strong> melalui muat naik berjadual atau integrasi terus daripada aplikasi jabatan.</li><li><strong>Sahkan.</strong> Banding angka dengan laporan rasmi dan rekodkan siapa yang meluluskannya.</li><li><strong>Bina papan pemuka</strong> dengan paparan ringkas: angka utama, aliran, dan perbandingan antara kawasan, dengan butiran apabila diklik.</li><li><strong>Jadualkan kemas kini</strong> dan tentukan siapa yang bertanggungjawab apabila data lewat.</li></ol>
<h2 id="maps">Menambah dimensi wilayah</h2>
<p>Banyak penunjuk lebih mudah dibaca pada peta. Apabila data sudah teratur, lapisan peta boleh ditambah di atasnya. Contohnya ada dalam artikel <a href="/ms/blog/webgis-peta-tematik-pemda">WebGIS dan peta tematik untuk kerajaan daerah</a>.</p>
<h2 id="data-protection">Perlindungan data peribadi</h2>
<p>Tidak semua data boleh dibuka. Data yang mengandungi identiti individu tertakluk kepada Undang-Undang Perlindungan Data Peribadi (Undang-Undang No. 27 Tahun 2022). Paparkan data yang sudah dikumpulkan pada papan pemuka, hadkan akses kepada data terperinci, dan rekodkan siapa yang membukanya.</p>
<h2 id="common-mistakes">Kesilapan yang kerap berlaku</h2>
<ul><li>Membina papan pemuka dahulu, menyusun data kemudian.</li><li>Terlalu banyak penunjuk sehingga pimpinan tidak membukanya.</li><li>Tiada yang bertanggungjawab atas kemas kini, jadi angka lapuk.</li><li>Setiap jabatan menggunakan definisi berbeza untuk istilah yang sama.</li></ul>
<h2 id="how-long">Berapa lama dan siapa yang terlibat</h2>
<p>Versi pertama dengan 10 hingga 20 penunjuk boleh disiapkan lebih awal berbanding seluruh portal data. Libatkan jabatan yang mengurus data perancangan, statistik, dan teknologi maklumat, kerana merekalah yang biasanya memegang data dan standard.</p>
<p>Lihat perkhidmatan <a href="/ms/services/data-analytics">Data &amp; Analitik</a> dan <a href="/ms/industri/pemerintahan">penyelesaian kerajaan</a> daripada Sentra, serta persediaan yang lebih luas dalam <a href="/ms/blog/spbe-pemda-persiapan">artikel SPBE untuk kerajaan daerah</a>.</p>""",
    },
}
