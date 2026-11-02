EXTRA = {
"": {"extra": """<h2 id="format-data">Data peta datang dalam format apa saja?</h2>
<p>Sebelum membangun, cek dulu bentuk data yang ada. Yang paling umum: berkas shapefile atau GeoJSON dari dinas teknis, tabel Excel yang punya kolom koordinat atau nama desa, citra satelit atau foto udara, dan basis data aplikasi yang hanya menyimpan alamat. Data tabel tanpa koordinat masih bisa dipetakan bila nama desa atau kecamatannya seragam dan cocok dengan batas wilayah administrasi.</p>
<p>Siapkan juga satu sistem koordinat yang disepakati. Data dari dua dinas yang memakai sistem berbeda akan tampak bergeser puluhan sampai ratusan meter bila digabung tanpa konversi.</p>
<h2 id="data-sensitif">Data mana yang sebaiknya tidak dibuka ke publik?</h2>
<p>Peta untuk publik dan peta untuk pimpinan sebaiknya dipisah. Data yang perlu dipikirkan ulang sebelum ditampilkan: lokasi tepat fasilitas vital, data pribadi penerima bantuan, dan batas lahan yang masih bersengketa. Tampilkan agregat per desa atau kecamatan untuk publik, dan simpan detail di tampilan yang memerlukan masuk akun. Aturan perlindungan data pribadi berlaku, jadi libatkan bagian hukum bila ragu.</p>
<h2 id="ukuran-berhasil">Bagaimana tahu portal peta ini berhasil?</h2>
<ul><li>Berapa lapisan data yang diperbarui tepat waktu oleh pemiliknya.</li><li>Berapa perangkat daerah yang benar-benar membuka peta tiap bulan.</li><li>Apakah pimpinan memakainya saat rapat, bukan hanya saat peluncuran.</li><li>Berapa permintaan data lewat surat atau pesan yang berkurang karena sudah bisa dilihat di portal.</li></ul>
""",
"faq":[("Apakah WebGIS sama dengan Google Maps?","Bukan. Google Maps menampilkan peta umum. WebGIS menampilkan peta dasar ditambah lapisan data milik instansi Anda, misalnya sekolah, jalan rusak, atau lahan, yang bisa disaring dan dianalisis."),
("Apakah perlu data koordinat lengkap sebelum mulai?","Tidak harus. Mulailah dari satu atau dua tema yang datanya paling rapi, lalu tambah lapisan bertahap. Data tanpa koordinat bisa dipetakan lewat nama desa atau kecamatan."),
("Berapa lama versi pertama bisa jadi?","Bergantung pada kesiapan data. Dengan dua sampai tiga lapisan yang sudah rapi, versi awal untuk uji internal biasanya bisa disiapkan dalam hitungan minggu, bukan bulan. Pastikan estimasi dikonfirmasi setelah data diperiksa."),
("Siapa yang memperbarui data setelah portal jadi?","Pemilik data di tiap dinas. Tetapkan nama penanggung jawab dan jadwal pembaruan per lapisan sejak awal, karena peta yang datanya basi cepat ditinggalkan.")]},
"en": {"extra": """<h2 id="format-data">What formats does map data come in?</h2>
<p>Check what you have before building. The most common: shapefile or GeoJSON from technical offices, Excel tables with coordinate columns or village names, satellite imagery or aerial photos, and application databases that only store addresses. Tabular data without coordinates can still be mapped when village or district names are consistent and match the administrative boundaries.</p>
<p>Also agree on one coordinate system. Data from two offices using different systems will appear shifted by tens to hundreds of metres if merged without conversion.</p>
<h2 id="data-sensitif">Which data should not be opened to the public?</h2>
<p>Keep the public map and the leadership map separate. Think twice before showing the exact location of vital facilities, personal data of aid recipients, and disputed land boundaries. Show aggregates per village or district to the public, and keep detail in views that require login. Personal data protection rules apply, so involve your legal office when in doubt.</p>
<h2 id="ukuran-berhasil">How do you know the portal is working?</h2>
<ul><li>How many data layers are updated on time by their owners.</li><li>How many agencies actually open the map each month.</li><li>Whether leadership uses it in meetings, not only at launch.</li><li>How many data requests by letter or message drop because the answer is visible on the portal.</li></ul>
""",
"faq":[("Is WebGIS the same as Google Maps?","No. Google Maps shows a general map. WebGIS shows a base map plus your agency's own data layers, such as schools, damaged roads or land parcels, which can be filtered and analysed."),
("Do we need complete coordinate data before starting?","No. Start with one or two themes whose data is cleanest, then add layers step by step. Data without coordinates can be mapped by village or district name."),
("How long does a first version take?","It depends on data readiness. With two or three clean layers, an initial version for internal testing can usually be ready in weeks, not months. Confirm the estimate once the data has been checked."),
("Who updates the data after launch?","The data owner at each office. Name a responsible person and an update schedule per layer from the start, because a map with stale data is quickly abandoned.")]},
"ms": {"extra": """<h2 id="format-data">Data peta datang dalam format apa?</h2>
<p>Semak bentuk data yang ada sebelum membina. Yang paling biasa: fail shapefile atau GeoJSON daripada jabatan teknikal, jadual Excel dengan lajur koordinat atau nama kampung, imej satelit atau foto udara, dan pangkalan data aplikasi yang hanya menyimpan alamat. Data jadual tanpa koordinat masih boleh dipetakan jika nama kampung atau daerah seragam.</p>
<h2 id="data-sensitif">Data mana yang tidak sesuai dibuka kepada umum?</h2>
<p>Asingkan peta untuk umum dan peta untuk pimpinan. Fikir semula sebelum memaparkan lokasi tepat kemudahan penting, data peribadi penerima bantuan dan sempadan tanah yang dipertikaikan. Papar data agregat untuk umum dan simpan butiran dalam paparan yang memerlukan log masuk.</p>
""",
"faq":[("Adakah WebGIS sama dengan Google Maps?","Tidak. WebGIS memaparkan peta asas ditambah lapisan data milik agensi anda yang boleh ditapis dan dianalisis."),
("Adakah perlu data koordinat lengkap sebelum bermula?","Tidak. Mulakan dengan satu atau dua tema yang datanya paling kemas, kemudian tambah lapisan secara berperingkat."),
("Siapa mengemas kini data selepas portal siap?","Pemilik data di setiap jabatan. Tetapkan penanggungjawab dan jadual kemas kini bagi setiap lapisan sejak awal.")]},
"zh": {"extra": """<h2 id="format-data">地图数据有哪些常见格式？</h2>
<p>开工前先看看手头有什么：技术部门的 shapefile 或 GeoJSON、带坐标列或村名的 Excel 表、卫星影像或航拍照片，以及只存地址的应用数据库。没有坐标的表格数据，只要村或县名称统一，也可以对应到行政边界上绘制。</p>
<h2 id="data-sensitif">哪些数据不宜对公众开放？</h2>
<p>面向公众的地图与面向领导的地图应分开。关键设施的精确位置、受助人个人信息和有争议的土地边界需要慎重。对公众只展示按村或县汇总的数据，细节放在需要登录的视图中。</p>
""",
"faq":[("WebGIS 和谷歌地图一样吗？","不一样。谷歌地图是通用地图；WebGIS 是在底图上叠加本机构自己的数据图层，如学校、受损道路或地块，并可筛选分析。"),
("开始前需要完整的坐标数据吗？","不需要。先从数据最整齐的一两个主题开始，再逐步增加图层。"),
("上线后由谁更新数据？","各部门的数据负责人。从一开始就为每个图层指定负责人和更新时间表。")]},
"ko": {"extra": """<h2 id="format-data">지도 데이터는 어떤 형식으로 있나요?</h2>
<p>구축 전에 가진 데이터를 확인하세요. 기술 부서의 shapefile 또는 GeoJSON, 좌표 열이나 마을 이름이 있는 엑셀 표, 위성·항공 사진, 주소만 저장한 앱 데이터베이스가 흔합니다. 좌표가 없는 표도 마을·군 이름이 일관되면 행정 경계에 맞춰 표시할 수 있습니다.</p>
<h2 id="data-sensitif">공개하면 안 되는 데이터는 무엇인가요?</h2>
<p>대중용 지도와 지도부용 지도는 분리하세요. 주요 시설의 정확한 위치, 지원 대상자의 개인정보, 분쟁 중인 토지 경계는 신중해야 합니다. 대중에게는 마을·군 단위 집계만 보여주고 세부 정보는 로그인 화면에 두세요.</p>
""",
"faq":[("WebGIS는 구글 지도와 같은가요?","아니요. WebGIS는 기본 지도 위에 기관의 자체 데이터 레이어(학교, 파손된 도로, 토지 등)를 올려 필터링과 분석을 할 수 있습니다."),
("시작 전에 좌표 데이터가 모두 필요한가요?","아니요. 가장 정리된 주제 한두 개로 시작해 레이어를 단계적으로 추가하세요."),
("출시 후 데이터는 누가 갱신하나요?","각 부서의 데이터 담당자입니다. 처음부터 레이어별 담당자와 갱신 일정을 정하세요.")]},
}
