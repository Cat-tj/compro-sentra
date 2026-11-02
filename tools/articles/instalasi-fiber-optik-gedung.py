SLUG = "instalasi-fiber-optik-gedung"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-fiber-gedung.webp"
OG_IMAGE = "/assets/og/art-blog-fiber-gedung.jpg"

LANGS = {
"": {
"title": "Instalasi Fiber Optik Gedung: Tahapan, Alat, dan Komponen Biaya",
"description": "Tahapan memasang fiber optik di gedung atau kampus: survei jalur, jenis kabel single-mode dan multimode, splicing, terminasi, pengukuran OTDR, dan komponen biaya.",
"category": "Jaringan",
"lead": "Fiber optik di dalam gedung bukan sekadar menarik kabel. Hasilnya bergantung pada jalur, kualitas sambungan, dan pengukuran sebelum serah terima.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"Instalasi Fiber Optik Gedung\" dan ingin minta survei jalur untuk gedung kami.",
"aside": [("/services/instalasi-infrastruktur", "Instalasi infrastruktur jaringan"), ("/blog/starlink-vs-vsat-vs-fiber", "Starlink vs VSAT vs Fiber"), ("/services/pengadaan-it", "Pengadaan perangkat IT")],
"body": """<p>Fiber optik dipakai di gedung dan kampus untuk menghubungkan lantai atau bangunan yang jaraknya melebihi batas kabel jaringan tembaga (sekitar 100 meter), untuk kecepatan tinggi, dan agar kebal terhadap gangguan listrik. Pemasangan yang baik terlihat pada hasil ukurnya, bukan hanya pada lampu yang menyala.</p>
<h2 id="jenis-kabel">Single-mode atau multimode?</h2>
<ul><li><strong>Single-mode</strong>: untuk jarak jauh (kilometer) dan antar gedung. Pilihan umum untuk backbone kampus dan proyek yang ingin tahan lama.</li><li><strong>Multimode</strong> (OM3, OM4): untuk jarak pendek di dalam gedung. Untuk 10 Gbps, jangkauannya sekitar 300 meter (OM3) sampai 400 meter (OM4).</li></ul>
<p>Modul transceiver di switch harus cocok dengan jenis kabel. Salah pilih jenis adalah kesalahan umum yang baru ketahuan saat perangkat datang.</p>
<h2 id="tahapan">Apa saja tahapan pemasangan?</h2>
<ol><li><strong>Survei jalur.</strong> Periksa shaft, kolom kabel, pipa, ruang server per lantai, dan titik yang perlu menembus dinding atau lantai.</li><li><strong>Desain.</strong> Tentukan topologi, jumlah core (dengan cadangan), titik distribusi (ODF), dan jenis kabel dalam atau luar ruangan.</li><li><strong>Penarikan kabel.</strong> Perhatikan radius tekuk dan tarikan maksimum, serta pisahkan dari kabel listrik berdaya besar.</li><li><strong>Terminasi dan splicing.</strong> Inti serat disambung dengan fusion splicer atau dihubungkan lewat pigtail ke konektor di ODF.</li><li><strong>Pengukuran.</strong> Uji redaman dengan power meter dan OTDR, lalu catat hasilnya per core.</li><li><strong>Dokumentasi.</strong> Label, diagram jalur, dan laporan ukur diserahkan bersama.</li></ol>
<h2 id="alat">Alat dan material apa yang dipakai?</h2>
<ul><li>Fusion splicer, cleaver, stripper, dan tray splice.</li><li>OTDR dan optical power meter dengan light source.</li><li>ODF, patch cord, pigtail, adapter, dan penutup sambungan.</li><li>Pipa pelindung, ladder atau tray kabel, dan penanda jalur.</li></ul>
<h2 id="komponen-biaya">Komponen apa yang menentukan biaya?</h2>
<p>Tidak ada satu angka per meter yang jujur, karena biaya dipengaruhi: panjang dan kerumitan jalur (apakah perlu galian atau membobok dinding), jumlah core, jumlah titik sambungan, kualitas ODF dan konektor, perangkat transceiver, serta pengukuran dan dokumentasi. Minta penawaran yang merinci material, jasa penarikan, jasa splicing per sambungan, dan laporan ukur.</p>
<h2 id="redaman">Berapa redaman yang wajar?</h2>
<p>Redaman total adalah jumlah redaman kabel per kilometer, sambungan, dan konektor. Sambungan fusion yang baik biasanya hanya beberapa persepuluh dB atau kurang, sedangkan konektor memberi redaman lebih besar. Bandingkan hasil ukur dengan anggaran redaman (loss budget) modul yang akan dipakai, bukan dengan angka umum.</p>
<p>Perbandingan fiber dengan opsi lain untuk kantor cabang ada di <a href="/blog/starlink-vs-vsat-vs-fiber">Starlink vs VSAT vs Fiber</a>. Sentra mengerjakan survei, pemasangan, dan pengukuran. Lihat <a href="/services/instalasi-infrastruktur">instalasi infrastruktur jaringan</a> dan <a href="/services/pengadaan-it">pengadaan perangkat IT</a>.</p>""",
"faq": [("Berapa jarak maksimum fiber optik?","Single-mode bisa menjangkau puluhan kilometer tergantung modul, sedangkan multimode di dalam gedung terbatas ratusan meter untuk kecepatan tinggi."),
("Apakah perlu core cadangan?","Sebaiknya ya. Menarik kabel dengan core lebih banyak biayanya relatif kecil dibanding menarik ulang kemudian."),
("Apa itu OTDR dan apakah wajib?","OTDR adalah alat yang memetakan redaman sepanjang serat dan menunjukkan lokasi sambungan bermasalah. Untuk proyek serius, laporan ukur sebaiknya diminta sebagai bagian serah terima."),
("Bisakah serat yang putus diperbaiki?","Bisa disambung ulang dengan splicing, tetapi jalur yang terlindungi sejak awal jauh mengurangi risiko putus.")]},
"en": {
"title": "Building Fibre Optic Installation: Stages, Tools and Cost Components",
"description": "Stages of installing fibre optic in a building or campus: route survey, single-mode vs multimode, splicing, termination, OTDR testing, and cost components.",
"category": "Networking",
"lead": "Fibre inside a building is more than pulling cable. The result depends on the route, the quality of the joints, and testing before handover.",
"wa_text": "Hello Sentra, I just read \"Building Fibre Optic Installation\" and would like a route survey for our building.",
"aside": [("/services/instalasi-infrastruktur", "Network infrastructure installation"), ("/blog/starlink-vs-vsat-vs-fiber", "Starlink vs VSAT vs Fibre"), ("/services/pengadaan-it", "IT procurement")],
"body": """<p>Fibre is used in buildings and campuses to link floors or buildings beyond the reach of copper network cable (about 100 metres), for high speed, and for immunity to electrical interference. A good installation shows in its test results, not just in a lit-up port.</p>
<h2 id="jenis-kabel">Single-mode or multimode?</h2>
<ul><li><strong>Single-mode</strong>: for long distances (kilometres) and between buildings. The usual choice for campus backbones and projects meant to last.</li><li><strong>Multimode</strong> (OM3, OM4): for short runs inside a building. At 10 Gbps the reach is about 300 metres (OM3) to 400 metres (OM4).</li></ul>
<p>The transceiver modules in the switches must match the cable type. Choosing the wrong type is a common mistake discovered only when the equipment arrives.</p>
<h2 id="tahapan">What are the installation stages?</h2>
<ol><li><strong>Route survey.</strong> Check shafts, cable risers, conduits, per-floor equipment rooms, and points that need to penetrate walls or floors.</li><li><strong>Design.</strong> Decide topology, core count (with spares), distribution points (ODF), and indoor or outdoor cable type.</li><li><strong>Cable pulling.</strong> Respect bend radius and maximum pull tension, and separate from high-power electrical cable.</li><li><strong>Termination and splicing.</strong> Fibres are joined with a fusion splicer or connected through pigtails to connectors at the ODF.</li><li><strong>Testing.</strong> Measure loss with a power meter and OTDR, and record results per core.</li><li><strong>Documentation.</strong> Labels, route diagrams and test reports are handed over together.</li></ol>
<h2 id="alat">What tools and materials are used?</h2>
<ul><li>Fusion splicer, cleaver, stripper and splice trays.</li><li>OTDR and optical power meter with light source.</li><li>ODF, patch cords, pigtails, adapters and splice closures.</li><li>Protective conduit, cable ladder or tray, and route markers.</li></ul>
<h2 id="komponen-biaya">What determines the cost?</h2>
<p>No honest single per-metre figure exists, because cost is affected by route length and difficulty (trenching or wall penetration), core count, number of splice points, quality of ODF and connectors, transceivers, and testing and documentation. Ask for a quote that itemises material, pulling labour, splicing per joint, and the test report.</p>
<h2 id="redaman">What loss is reasonable?</h2>
<p>Total loss is the sum of cable loss per kilometre, splices and connectors. A good fusion splice is usually a few tenths of a dB or less, while connectors add more. Compare test results against the loss budget of the modules you will use, not against generic numbers.</p>
<p>Comparing fibre with other options for branch offices is in <a href="/en/blog/starlink-vs-vsat-vs-fiber">Starlink vs VSAT vs Fibre</a>. Sentra handles survey, installation and testing. See <a href="/en/services/instalasi-infrastruktur">network infrastructure installation</a> and <a href="/en/services/pengadaan-it">IT procurement</a>.</p>""",
"faq": [("What is the maximum fibre distance?","Single-mode can reach tens of kilometres depending on the module, while multimode inside a building is limited to hundreds of metres at high speed."),
("Are spare cores needed?","Preferably yes. Pulling a cable with more cores costs relatively little compared with re-pulling later."),
("What is an OTDR and is it mandatory?","An OTDR maps loss along the fibre and shows where a bad joint is. For serious projects, ask for the test report as part of handover."),
("Can a broken fibre be repaired?","It can be re-spliced, but a route protected from the start greatly reduces the risk of breaks.")]},
"ms": {
"title": "Pemasangan Gentian Optik Bangunan: Peringkat dan Komponen Kos",
"description": "Peringkat memasang gentian optik di bangunan atau kampus: tinjauan laluan, single-mode lawan multimode, penyambungan, ujian OTDR dan komponen kos.",
"category": "Rangkaian",
"lead": "Gentian optik dalam bangunan bukan sekadar menarik kabel.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"Pemasangan Gentian Optik Bangunan\" dan ingin meminta tinjauan laluan.",
"aside": [("/services/instalasi-infrastruktur", "Pemasangan infrastruktur rangkaian"), ("/blog/starlink-vs-vsat-vs-fiber", "Starlink vs VSAT vs Fiber"), ("/services/pengadaan-it", "Perolehan IT")],
"body": """<p>Gentian optik digunakan untuk menghubungkan tingkat atau bangunan yang melebihi had kabel tembaga (sekitar 100 meter) dan kebal terhadap gangguan elektrik.</p>
<h2 id="jenis-kabel">Single-mode atau multimode?</h2>
<p>Single-mode untuk jarak jauh dan antara bangunan; multimode (OM3, OM4) untuk jarak pendek dalam bangunan, sekitar 300 hingga 400 meter pada 10 Gbps. Modul pemancar-penerima mesti sepadan dengan jenis kabel.</p>
<h2 id="tahapan">Peringkat pemasangan</h2>
<p>Tinjauan laluan, reka bentuk, penarikan kabel, penamatan dan penyambungan, pengukuran dengan OTDR, kemudian dokumentasi. Lihat <a href="/ms/blog/starlink-vs-vsat-vs-fiber">Starlink vs VSAT vs Fiber</a> dan <a href="/ms/services/instalasi-infrastruktur">pemasangan infrastruktur rangkaian</a>.</p>""",
"faq": [("Berapa jarak maksimum gentian optik?","Single-mode boleh mencapai puluhan kilometer; multimode dalam bangunan terhad kepada ratusan meter."),
("Perlukah teras simpanan?","Sebaiknya ya, kerana kosnya kecil berbanding menarik semula.")]},
"zh": {
"title": "楼宇光纤安装：阶段、工具与成本构成",
"description": "在楼宇或园区安装光纤的阶段：路由勘察、单模与多模、熔接、端接、OTDR 测试和成本构成。",
"category": "网络",
"lead": "楼内光纤不只是拉线，结果取决于路由、熔接质量和交付前的测试。",
"wa_text": "您好 Sentra，我刚读了《楼宇光纤安装》，想请你们为我们的大楼勘察路由。",
"aside": [("/services/instalasi-infrastruktur", "网络基础设施安装"), ("/blog/starlink-vs-vsat-vs-fiber", "Starlink、VSAT 与光纤"), ("/services/pengadaan-it", "IT 设备采购")],
"body": """<p>光纤用于连接超出铜缆距离（约 100 米）的楼层或建筑，速率高且不受电气干扰。</p>
<h2 id="jenis-kabel">单模还是多模？</h2>
<p>单模用于长距离和楼宇之间；多模（OM3、OM4）用于楼内短距离，10 Gbps 下约 300 至 400 米。交换机光模块必须与光缆类型匹配。</p>
<h2 id="tahapan">安装阶段</h2>
<p>路由勘察、设计、布线、端接与熔接、用 OTDR 测试，最后交付文档。参见 <a href="/zh/blog/starlink-vs-vsat-vs-fiber">Starlink、VSAT 与光纤</a>和<a href="/zh/services/instalasi-infrastruktur">网络基础设施安装</a>。</p>""",
"faq": [("光纤最远能多远？","单模可达数十公里，楼内多模高速时限于数百米。"),
("需要备用纤芯吗？","建议要，多拉几芯的成本相对重拉很低。")]},
"ko": {
"title": "건물 광케이블 설치: 단계, 장비, 비용 구성",
"description": "건물이나 캠퍼스에 광케이블을 설치하는 단계: 경로 조사, 싱글모드와 멀티모드, 융착, 종단, OTDR 측정, 비용 구성.",
"category": "네트워크",
"lead": "건물 내 광케이블은 케이블을 당기는 것 이상입니다. 경로, 접속 품질, 인도 전 측정이 결과를 좌우합니다.",
"wa_text": "안녕하세요 Sentra, \"건물 광케이블 설치\" 글을 읽고 우리 건물의 경로 조사를 요청하고 싶습니다.",
"aside": [("/services/instalasi-infrastruktur", "네트워크 인프라 설치"), ("/blog/starlink-vs-vsat-vs-fiber", "Starlink·VSAT·광케이블 비교"), ("/services/pengadaan-it", "IT 장비 조달")],
"body": """<p>광케이블은 구리 케이블 한계(약 100m)를 넘는 층이나 건물을 연결하고 전기적 간섭에 강합니다.</p>
<h2 id="jenis-kabel">싱글모드와 멀티모드</h2>
<p>싱글모드는 장거리와 건물 간, 멀티모드(OM3, OM4)는 건물 내 단거리용이며 10Gbps에서 약 300~400m입니다. 스위치의 트랜시버 모듈은 케이블 종류와 맞아야 합니다.</p>
<h2 id="tahapan">설치 단계</h2>
<p>경로 조사, 설계, 포설, 종단과 융착, OTDR 측정, 문서화 순입니다. <a href="/ko/blog/starlink-vs-vsat-vs-fiber">Starlink·VSAT·광케이블 비교</a>와 <a href="/ko/services/instalasi-infrastruktur">네트워크 인프라 설치</a>를 확인하세요.</p>""",
"faq": [("광케이블 최대 거리는?","싱글모드는 모듈에 따라 수십 km, 건물 내 멀티모드는 고속에서 수백 m입니다."),
("여유 코어가 필요한가요?","가급적 필요합니다. 코어를 더 넣는 비용은 나중에 다시 포설하는 것보다 적습니다.")]},
}
