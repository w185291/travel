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
