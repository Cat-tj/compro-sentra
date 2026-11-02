SLUG = "server-ai-on-premise"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-server-ai.webp"
OG_IMAGE = "/assets/og/art-blog-server-ai.jpg"

LANGS = {
"": {
"title": "Server AI On-Premise: GPU, RAM, dan Penyimpanan yang Dibutuhkan",
"description": "Cara memperkirakan kebutuhan GPU, VRAM, RAM, dan penyimpanan untuk menjalankan model bahasa di server sendiri, dengan rumus sederhana dan contoh ukuran model.",
"category": "AI & data",
"lead": "Kebutuhan server AI ditentukan hampir sepenuhnya oleh ukuran model dan jumlah pengguna serentak. Ini cara menghitungnya sebelum membeli perangkat.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"Server AI On-Premise\" dan ingin konsultasi kebutuhan server untuk perusahaan kami.",
"aside": [("/services/private-llm", "Private LLM untuk perusahaan"), ("/services/pengadaan-it", "Pengadaan perangkat IT"), ("/blog/chatgpt-untuk-perusahaan", "ChatGPT untuk perusahaan: risiko data dan alternatif")],
"body": """<p>Menjalankan model bahasa di server sendiri berarti Anda menyiapkan sendiri memori kartu grafis (VRAM), RAM, dan penyimpanan. Kesalahan paling umum adalah membeli perangkat sebelum tahu model dan beban kerjanya. Urutan yang benar: tentukan kasus penggunaan, pilih model, hitung memori, baru pilih perangkat.</p>
<h2 id="vram">Berapa VRAM yang dibutuhkan model?</h2>
<p>Pegangan kasar: jumlah parameter dikali byte per parameter. Model dengan presisi 16-bit memakai 2 byte per parameter, sedangkan versi terkuantisasi 4-bit memakai sekitar setengah byte. Ditambah ruang untuk konteks percakapan (KV cache) dan overhead, biasanya 10 sampai 30 persen lebih.</p>
<ul><li><strong>Model 7 miliar parameter</strong>: sekitar 14 GB di 16-bit, sekitar 4 sampai 5 GB di 4-bit.</li><li><strong>Model 13 miliar</strong>: sekitar 26 GB di 16-bit, sekitar 7 sampai 8 GB di 4-bit.</li><li><strong>Model 70 miliar</strong>: sekitar 140 GB di 16-bit, sekitar 35 sampai 40 GB di 4-bit.</li></ul>
<p>Angka di atas perkiraan; kebutuhan nyata berbeda per model dan per perangkat lunak penjalannya, jadi uji dulu sebelum memesan.</p>
<h2 id="pengguna-serentak">Bagaimana jumlah pengguna memengaruhi?</h2>
<p>Satu pengguna dan lima puluh pengguna serentak membutuhkan perangkat yang sangat berbeda. Tiap permintaan aktif memakai tambahan memori konteks dan waktu hitung. Tanyakan: berapa pengguna aktif pada jam sibuk, seberapa panjang dokumen rata-rata, dan berapa detik jawaban yang masih bisa diterima. Untuk pilot dengan 5 sampai 10 pengguna, satu server berkapasitas sedang sering cukup.</p>
<h2 id="ram-dan-penyimpanan">RAM, CPU, dan penyimpanan</h2>
<ul><li><strong>RAM sistem</strong>: sediakan minimal sebesar VRAM total agar model bisa dimuat dengan lancar, lebih baik dua kali lipat.</li><li><strong>CPU</strong>: tidak perlu mewah, tetapi cukup jalur PCIe untuk GPU dan NVMe.</li><li><strong>Penyimpanan</strong>: gunakan SSD NVMe untuk berkas model (puluhan GB per model) dan basis data vektor bila memakai pencarian dokumen. Siapkan juga ruang untuk dokumen sumber dan cadangan.</li><li><strong>Listrik dan pendingin</strong>: GPU server menarik daya besar dan menghasilkan panas. Cek kapasitas listrik dan pendingin ruangan sebelum perangkat datang.</li></ul>
<h2 id="satu-atau-banyak-gpu">Satu GPU besar atau beberapa GPU kecil?</h2>
<p>Model yang muat di satu GPU lebih sederhana dan lebih cepat. Membagi satu model ke beberapa GPU memungkinkan model lebih besar, tetapi menambah kerumitan dan butuh antarmuka yang cukup cepat. Untuk banyak kasus perusahaan, model menengah terkuantisasi di satu GPU sudah memadai.</p>
<h2 id="alternatif-sewa">Kapan sewa lebih masuk akal daripada beli?</h2>
<p>Bila beban kerja masih diuji atau pemakaian jarang, menyewa server GPU atau memakai server di pusat data lokal bisa lebih hemat sambil Anda belajar. Beli perangkat sendiri baru masuk akal setelah pilot menunjukkan beban yang stabil dan data memang harus tetap di gedung Anda.</p>
<p>Sentra membantu memilih model dan perangkat dari pilot sampai implementasi. Lihat <a href="/services/private-llm">layanan Private LLM</a>, <a href="/services/pengadaan-it">pengadaan perangkat IT</a>, dan pertimbangan data di artikel <a href="/blog/chatgpt-untuk-perusahaan">ChatGPT untuk perusahaan</a>.</p>""",
"faq": [("Berapa GPU minimum untuk asisten AI kantor?","Bergantung model. Model kecil terkuantisasi bisa jalan di satu GPU dengan VRAM belasan GB untuk pilot kecil. Untuk banyak pengguna atau model besar butuh VRAM jauh lebih besar. Hitung dari model dan beban, bukan dari angka umum."),
("Apakah bisa tanpa GPU?","Bisa untuk model kecil dengan jawaban yang lebih lambat. Untuk pemakaian bersama oleh banyak orang, GPU hampir selalu diperlukan."),
("Berapa lama pilot sebaiknya berjalan?","Beberapa minggu dengan pertanyaan uji yang sudah disiapkan, cukup untuk menilai ketepatan dan beban sebelum membeli perangkat."),
("Apakah data benar-benar tidak keluar dari kantor?","Itu tujuan on-premise, tetapi pastikan juga akses jaringan, pencadangan, dan pembaruan perangkat lunak tidak membuka jalur keluar yang tidak diinginkan.")]},
"en": {
"title": "On-Premise AI Server: GPU, RAM and Storage You Need",
"description": "How to estimate GPU, VRAM, RAM and storage needs for running a language model on your own server, with a simple formula and example model sizes.",
"category": "AI & data",
"lead": "An AI server's requirements are set almost entirely by model size and concurrent users. Here is how to calculate before buying hardware.",
"wa_text": "Hello Sentra, I just read \"On-Premise AI Server\" and would like advice on server needs for our company.",
"aside": [("/services/private-llm", "Private LLM for companies"), ("/services/pengadaan-it", "IT procurement"), ("/blog/chatgpt-untuk-perusahaan", "ChatGPT for business: data risks and alternatives")],
"body": """<p>Running a language model on your own server means you provide the graphics memory (VRAM), RAM and storage yourself. The most common mistake is buying hardware before knowing the model and workload. The right order: define the use case, choose the model, calculate memory, then pick hardware.</p>
<h2 id="vram">How much VRAM does a model need?</h2>
<p>Rule of thumb: parameter count times bytes per parameter. A 16-bit model uses 2 bytes per parameter, while a 4-bit quantised version uses about half a byte. Add room for conversation context (KV cache) and overhead, usually 10 to 30 percent more.</p>
<ul><li><strong>7 billion parameters</strong>: about 14 GB at 16-bit, about 4 to 5 GB at 4-bit.</li><li><strong>13 billion</strong>: about 26 GB at 16-bit, about 7 to 8 GB at 4-bit.</li><li><strong>70 billion</strong>: about 140 GB at 16-bit, about 35 to 40 GB at 4-bit.</li></ul>
<p>These are estimates; real needs differ by model and by the software running it, so test before ordering.</p>
<h2 id="pengguna-serentak">How do concurrent users affect this?</h2>
<p>One user and fifty concurrent users need very different hardware. Each active request uses extra context memory and compute time. Ask: how many active users at peak, how long are typical documents, and how many seconds of response time is acceptable. For a pilot with 5 to 10 users, one mid-range server is often enough.</p>
<h2 id="ram-dan-penyimpanan">RAM, CPU and storage</h2>
<ul><li><strong>System RAM</strong>: at least equal to total VRAM so the model loads smoothly, ideally double.</li><li><strong>CPU</strong>: no need for a fancy one, but enough PCIe lanes for GPUs and NVMe.</li><li><strong>Storage</strong>: NVMe SSD for model files (tens of GB each) and a vector database if you use document search. Add room for source documents and backups.</li><li><strong>Power and cooling</strong>: GPU servers draw a lot of power and make heat. Check room power and cooling before the hardware arrives.</li></ul>
<h2 id="satu-atau-banyak-gpu">One big GPU or several small ones?</h2>
<p>A model that fits on one GPU is simpler and faster. Splitting one model across several GPUs allows larger models but adds complexity and needs a fast enough interconnect. For many company cases, a mid-size quantised model on one GPU is adequate.</p>
<h2 id="alternatif-sewa">When is renting better than buying?</h2>
<p>If the workload is still being tested or use is occasional, renting a GPU server or using a local data centre can be cheaper while you learn. Buying makes sense once a pilot shows stable load and the data truly must stay in your building.</p>
<p>Sentra helps choose models and hardware from pilot to rollout. See the <a href="/en/services/private-llm">Private LLM service</a>, <a href="/en/services/pengadaan-it">IT procurement</a>, and data considerations in <a href="/en/blog/chatgpt-untuk-perusahaan">ChatGPT for business</a>.</p>""",
"faq": [("What is the minimum GPU for an office AI assistant?","It depends on the model. A small quantised model can run on one GPU with a dozen or so GB of VRAM for a small pilot. Many users or a large model need much more. Calculate from model and load, not from generic numbers."),
("Is it possible without a GPU?","For small models, yes, with slower answers. For shared use by many people, a GPU is almost always needed."),
("How long should a pilot run?","A few weeks with prepared test questions is enough to judge accuracy and load before buying hardware."),
("Does data really never leave the office?","That is the aim of on-premise, but also make sure network access, backups and software updates do not open unwanted outbound paths.")]},
"ms": {
"title": "Pelayan AI On-Premise: GPU, RAM dan Storan yang Diperlukan",
"description": "Cara menganggar keperluan GPU, VRAM, RAM dan storan untuk menjalankan model bahasa di pelayan sendiri.",
"category": "AI & data",
"lead": "Keperluan pelayan AI ditentukan hampir sepenuhnya oleh saiz model dan bilangan pengguna serentak.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"Pelayan AI On-Premise\" dan ingin berunding tentang keperluan pelayan.",
"aside": [("/services/private-llm", "Private LLM untuk syarikat"), ("/services/pengadaan-it", "Perolehan IT"), ("/blog/chatgpt-untuk-perusahaan", "ChatGPT untuk syarikat")],
"body": """<p>Menjalankan model bahasa di pelayan sendiri bermakna anda menyediakan VRAM, RAM dan storan. Kesilapan paling lazim ialah membeli perkakasan sebelum mengetahui model dan beban kerja. Susunan yang betul: tentukan kes penggunaan, pilih model, kira memori, kemudian pilih perkakasan.</p>
<h2 id="vram">Berapa VRAM diperlukan?</h2>
<p>Anggaran kasar: bilangan parameter didarab bait setiap parameter. Model 16-bit menggunakan 2 bait, versi terkuantiti 4-bit kira-kira setengah bait, ditambah 10 hingga 30 peratus untuk konteks. Model 7 bilion parameter kira-kira 14 GB pada 16-bit atau 4 hingga 5 GB pada 4-bit; model 70 bilion kira-kira 140 GB atau 35 hingga 40 GB. Ini anggaran, jadi uji sebelum membeli.</p>
<p>Lihat <a href="/ms/services/private-llm">perkhidmatan Private LLM</a> dan <a href="/ms/blog/chatgpt-untuk-perusahaan">ChatGPT untuk syarikat</a>.</p>""",
"faq": [("Adakah boleh tanpa GPU?","Boleh untuk model kecil dengan jawapan lebih perlahan. Untuk ramai pengguna, GPU hampir selalu perlu."),
("Berapa lama pilot patut berjalan?","Beberapa minggu dengan soalan ujian yang disediakan."),
("Bilakah sewa lebih sesuai daripada beli?","Apabila beban masih diuji atau penggunaan jarang.")]},
"zh": {
"title": "本地 AI 服务器：所需 GPU、内存与存储",
"description": "如何估算在自有服务器上运行语言模型所需的 GPU、显存、内存和存储。",
"category": "AI 与数据",
"lead": "AI 服务器的需求几乎完全由模型大小和并发用户数决定。",
"wa_text": "您好 Sentra，我刚读了《本地 AI 服务器》，想咨询公司服务器需求。",
"aside": [("/services/private-llm", "企业私有 LLM"), ("/services/pengadaan-it", "IT 设备采购"), ("/blog/chatgpt-untuk-perusahaan", "企业使用 ChatGPT")],
"body": """<p>在自有服务器上运行语言模型，意味着显存（VRAM）、内存和存储都要自己准备。最常见的错误是在不了解模型和负载前就采购硬件。正确顺序：确定用例、选择模型、计算内存、再选硬件。</p>
<h2 id="vram">模型需要多少显存？</h2>
<p>粗略估算：参数量乘以每个参数的字节数。16 位模型每参数 2 字节，4 位量化约半字节，再加上上下文缓存和开销，通常多 10% 到 30%。70 亿参数模型约 14 GB（16 位）或 4 到 5 GB（4 位）；700 亿参数约 140 GB 或 35 到 40 GB。以上为估算，采购前请先测试。</p>
<p>参见<a href="/zh/services/private-llm">私有 LLM 服务</a>和<a href="/zh/blog/chatgpt-untuk-perusahaan">企业使用 ChatGPT</a>。</p>""",
"faq": [("没有 GPU 可以吗？","小模型可以，但回答较慢；多人共用几乎总是需要 GPU。"),
("试点应进行多久？","几周，使用事先准备好的测试问题即可评估准确性和负载。"),
("什么时候租比买更合适？","负载仍在测试或使用不频繁时。")]},
"ko": {
"title": "온프레미스 AI 서버: 필요한 GPU, RAM, 저장소",
"description": "자체 서버에서 언어 모델을 돌리는 데 필요한 GPU, VRAM, RAM, 저장소를 추정하는 방법.",
"category": "AI·데이터",
"lead": "AI 서버 요구 사양은 거의 전적으로 모델 크기와 동시 사용자 수가 정합니다.",
"wa_text": "안녕하세요 Sentra, \"온프레미스 AI 서버\" 글을 읽고 우리 회사 서버 요구 사항을 상담하고 싶습니다.",
"aside": [("/services/private-llm", "기업용 프라이빗 LLM"), ("/services/pengadaan-it", "IT 장비 조달"), ("/blog/chatgpt-untuk-perusahaan", "기업의 ChatGPT 사용")],
"body": """<p>자체 서버에서 언어 모델을 돌린다는 것은 그래픽 메모리(VRAM), RAM, 저장소를 직접 마련한다는 뜻입니다. 가장 흔한 실수는 모델과 작업량을 알기 전에 장비를 사는 것입니다. 올바른 순서는 사용 사례, 모델, 메모리 계산, 장비 선택입니다.</p>
<h2 id="vram">모델에 VRAM이 얼마나 필요한가요?</h2>
<p>대략 파라미터 수에 파라미터당 바이트를 곱합니다. 16비트는 2바이트, 4비트 양자화는 약 0.5바이트이며 컨텍스트 캐시와 오버헤드로 보통 10~30% 더 필요합니다. 70억 파라미터는 16비트 약 14GB, 4비트 약 4~5GB이고, 700억 파라미터는 약 140GB 또는 35~40GB입니다. 추정치이므로 구매 전에 테스트하세요.</p>
<p><a href="/ko/services/private-llm">프라이빗 LLM 서비스</a>와 <a href="/ko/blog/chatgpt-untuk-perusahaan">기업의 ChatGPT 사용</a>을 참고하세요.</p>""",
"faq": [("GPU 없이도 가능한가요?","작은 모델은 가능하지만 느립니다. 여러 사람이 함께 쓰려면 거의 항상 GPU가 필요합니다."),
("파일럿은 얼마나 해야 하나요?","준비한 테스트 질문으로 몇 주면 정확도와 부하를 판단할 수 있습니다."),
("언제 구매보다 임대가 나은가요?","작업량을 아직 시험 중이거나 사용이 드물 때입니다.")]},
}
