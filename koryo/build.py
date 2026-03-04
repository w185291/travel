import os
import re

LAYOUT_HTML = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@300;400;500;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script>
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#B91C1C",
                        "primary-dark": "#991B1B",
                        "background-light": "#fcfcfc",
                        "background-dark": "#121212",
                        "text-main": "#222222",
                        "text-muted": "#666666",
                        "accent": "#d4af37",
                        "line-green": "#06C755",
                        "wechat-green": "#07C160",
                    },
                    fontFamily: {
                        "display": ["Noto Serif TC", "serif"],
                        "sans": ["Noto Sans TC", "sans-serif"],
                        "serif": ["Noto Serif TC", "serif"],
                        "serif-title": ["Noto Serif TC", "serif"],
                        "serif-text": ["Noto Serif TC", "serif"]
                    },
                    backgroundImage: {
                        'texture': "url('https://www.transparenttextures.com/patterns/paper.png')",
                    }
                },
            },
        }
    </script>
    <style>
        body { font-family: 'Noto Sans TC', sans-serif; background-color: #fcfcfc; }
        h1, h2, h3, h4, h5, h6 { font-family: 'Noto Serif TC', serif; }
        .text-vertical { writing-mode: vertical-rl; text-orientation: mixed; }
        .fade-in-up { animation: fadeInUp 1s ease-out forwards; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .magazine-shadow { box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.1), 0 10px 20px -5px rgba(0, 0, 0, 0.04); }
        .serif-text, .serif-title { font-family: 'Noto Serif TC', serif; }
        :root { --primary-blue: #B91C1C; --primary-red: #B91C1C; --elegant-gray: #4B5563; } /* Unified to Red */
        .text-vertical-rl { writing-mode: vertical-rl; text-orientation: mixed; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        details > summary { list-style: none; }
        details > summary::-webkit-details-marker { display: none; }
        .bg-background-light { background-color: #fcfcfc; }
        .bg-background-dark { background-color: #1a1a1a; }
        .text-text-main { color: #222222; }
        .text-text-secondary { color: #666666; }
    </style>
</head>
<body class="bg-stone-50 text-gray-800 antialiased overflow-x-hidden selection:bg-primary selection:text-white flex flex-col min-h-screen">

<!-- Mobile Menu Toggle & Overlay -->
<input class="peer hidden" id="mobile-menu-toggle" type="checkbox"/>
<div class="fixed inset-0 bg-black/50 z-40 hidden peer-checked:block lg:hidden transition-opacity"></div>
<div class="fixed top-0 right-0 w-[70%] h-full bg-white z-50 transform translate-x-full peer-checked:translate-x-0 transition-transform duration-300 lg:hidden shadow-2xl flex flex-col p-6 overflow-y-auto">
    <div class="flex justify-end mb-8">
        <label class="cursor-pointer p-2 rounded-full hover:bg-gray-100" for="mobile-menu-toggle">
            <span class="material-symbols-outlined text-3xl text-gray-800">close</span>
        </label>
    </div>
    <nav class="flex flex-col gap-6 text-lg font-medium text-gray-700">
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="index.html">首頁</a>
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="about.html">關於朝鮮</a>
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="nature.html">自然人文</a>
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="landmarks.html">經典地標</a>
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="experience.html">深度體驗</a>
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="itinerary.html">行程攻略</a>
        <a class="border-b border-gray-100 pb-2 hover:text-primary transition-colors" href="visa.html">簽證資訊</a>
    </nav>
    <div class="mt-auto pt-8 border-t border-gray-200">
        <div class="flex flex-col gap-2 text-sm text-gray-500">
            <span>台北總代理</span>
            <span>(02) 2515-8500</span>
        </div>
    </div>
</div>

<!-- Header -->
<header class="w-full z-30 bg-white/95 backdrop-blur-sm border-b border-stone-200 transition-all duration-300 sticky top-0">
    <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
            <a href="index.html" class="flex items-center gap-4 group cursor-pointer">
                <div class="w-10 h-10 bg-primary rounded-full flex items-center justify-center text-white shrink-0 shadow-sm group-hover:bg-primary-dark transition-colors duration-500">
                    <span class="material-symbols-outlined text-2xl">flight_takeoff</span>
                </div>
                <div class="flex flex-col">
                    <span class="text-lg md:text-xl font-bold tracking-widest text-gray-900 leading-none group-hover:text-primary transition-colors">朝鮮假期</span>
                    <span class="text-[10px] md:text-xs text-gray-500 tracking-wider uppercase mt-1">Air Koryo Taiwan Agent</span>
                </div>
            </a>
            
            <nav class="hidden lg:flex items-center gap-6 xl:gap-8">
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="index.html">首頁</a>
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="about.html">關於朝鮮</a>
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="nature.html">自然人文</a>
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="landmarks.html">經典地標</a>
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="experience.html">深度體驗</a>
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="itinerary.html">行程攻略</a>
                <a class="text-sm font-medium tracking-widest hover:text-primary relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-0 after:h-[2px] after:bg-primary after:transition-all hover:after:w-full" href="visa.html">簽證資訊</a>
            </nav>
            
            <div class="lg:hidden">
                <label class="cursor-pointer p-2 rounded-md hover:bg-gray-100 flex items-center justify-center" for="mobile-menu-toggle">
                    <span class="material-symbols-outlined text-3xl text-gray-800">menu</span>
                </label>
            </div>
            <div class="hidden lg:block">
                <a href="#contact-footer" class="bg-gray-900 text-white px-6 py-2 text-sm tracking-widest hover:bg-primary transition-colors duration-300 rounded shadow-lg">
                    立即預訂
                </a>
            </div>
        </div>
    </div>
</header>
<div class="flex-grow flex flex-col w-full relative">
{main_content}
</div>
<footer id="contact-footer" class="bg-gray-900 text-white pt-16 md:pt-24 pb-8 border-t border-gray-800 mt-auto">
    <div class="max-w-[1400px] mx-auto px-6 md:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
            <div class="col-span-1 md:col-span-2 lg:col-span-1">
                <div class="flex items-center gap-3 mb-6">
                    <span class="material-symbols-outlined text-3xl text-primary">flight_takeoff</span>
                    <div class="flex flex-col">
                        <span class="text-xl font-bold tracking-widest">朝鮮假期</span>
                        <span class="text-[10px] text-gray-400 tracking-wider uppercase">Air Koryo Taiwan Agent</span>
                    </div>
                </div>
                <p class="text-gray-400 text-sm leading-relaxed mb-6 font-light">
                    高麗航空台灣總代理，專注於朝鮮旅遊二十餘年。致力於提供最專業、安全、深度的旅遊體驗。
                </p>
                <div class="flex gap-4">
                    <a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors">
                        <span class="font-bold text-xs">FB</span>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors">
                        <span class="font-bold text-xs">IG</span>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors">
                        <span class="font-bold text-xs">LINE</span>
                    </a>
                </div>
            </div>
            <div>
                <h4 class="text-lg font-bold mb-6 tracking-widest border-b border-gray-700 pb-2 inline-block">關於我們</h4>
                <ul class="space-y-4 text-sm text-gray-400 font-light">
                    <li><a href="about.html" class="hover:text-white transition-colors">品牌故事</a></li>
                    <li><a href="itinerary.html" class="hover:text-white transition-colors">精選行程</a></li>
                    <li><a href="visa.html" class="hover:text-white transition-colors">簽證辦理</a></li>
                    <li><a href="metro.html" class="hover:text-white transition-colors">平壤地鐵特別企划</a></li>
                </ul>
            </div>
            <div class="lg:col-span-2">
                <h4 class="text-lg font-bold mb-6 tracking-widest border-b border-gray-700 pb-2 inline-block">聯絡與代理資訊</h4>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 text-sm text-gray-400 font-light">
                    <div class="flex flex-col gap-2">
                        <span class="text-white font-medium">台北總公司</span>
                        <span class="flex items-center gap-2"><span class="material-symbols-outlined text-base">location_on</span> 台北市中山區南京東路</span>
                        <span class="flex items-center gap-2"><span class="material-symbols-outlined text-base">call</span> (02) 2515-8500</span>
                    </div>
                    <div class="flex flex-col gap-2">
                        <span class="text-white font-medium">高雄分公司</span>
                        <span class="flex items-center gap-2"><span class="material-symbols-outlined text-base">location_on</span> 高雄市前金區中正四路</span>
                        <span class="flex items-center gap-2"><span class="material-symbols-outlined text-base">call</span> (07) 215-6788</span>
                    </div>
                    <div class="flex flex-col gap-2 border-t pt-6 sm:border-t-0 sm:pt-0 sm:border-l sm:border-gray-800 sm:pl-6">
                        <span class="text-white font-medium">指定代理商</span>
                        <ul class="space-y-1 text-xs">
                            <li>東南旅遊</li>
                            <li>雄獅旅遊</li>
                            <li>可樂旅遊</li>
                            <li>鳳凰旅遊</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
            <p class="text-xs text-gray-500 font-light tracking-wide">
                © 2024 Air Koryo Taiwan Agent. All rights reserved. 交觀甲第0000號 品保北0000號
            </p>
            <div class="flex gap-6 text-xs text-gray-500">
                <a href="#" class="hover:text-white transition-colors">網站地圖</a>
                <a href="#" class="hover:text-white transition-colors">免責聲明</a>
                <a href="#" class="hover:text-white transition-colors">隱私權政策</a>
            </div>
        </div>
    </div>
</footer>
</body>
</html>
"""

pages_mapping = {
    "_7": ("index.html", "朝鮮假期 - 首頁"),
    "_1": ("about.html", "關於朝鮮 - 朝鮮假期"),
    "_2": ("nature.html", "自然人文 - 朝鮮假期"),
    "_6": ("landmarks.html", "經典地標 - 朝鮮假期"),
    "_4": ("experience.html", "深度體驗 - 朝鮮假期"),
    "_8": ("itinerary.html", "行程攻略 - 朝鮮假期"),
    "_3": ("visa.html", "簽證資訊 - 朝鮮假期"),
    "_5": ("metro.html", "平壤地鐵 - 朝鮮假期")
}

for folder, (filename, title) in pages_mapping.items():
    filepath = os.path.join(folder, "code.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Try to extract <main>
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
    if main_match:
        main_content = main_match.group(0) # Keep <main> tag itself
    else:
        # Some are wrapped differently, like _4 and _6
        header_end = content.find('</header>')
        footer_start = content.find('<footer')
        if header_end != -1 and footer_start != -1:
            main_content = content[header_end+9:footer_start]
        else:
            main_content = "<!-- Failed to extract main content -->"
            
    out_html = LAYOUT_HTML.replace("{title}", title).replace("{main_content}", main_content)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(out_html)

print("HTML combination completed.")
