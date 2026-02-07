document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('btn-generate-scenario');

    if (btn) {
        btn.addEventListener('click', async () => {
            if (!CONFIG.API_ENDPOINT || !CONFIG.API_KEY || CONFIG.API_KEY === "YOUR_API_KEY_HERE") {
                alert('Please configure the API_ENDPOINT and API_KEY in js/config.js');
                return;
            }

            const originalText = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = `
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                生成中...
            `;

            try {
                // Example Payload - modify as needed
                const payload = {
                    prompt: "Generate a travel scenario image for Yunnan",
                    // Add other parameters required by your API
                };

                // Mock API call structure
                /*
                const response = await fetch(CONFIG.API_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${CONFIG.API_KEY}`,
                        // 'X-API-KEY': CONFIG.API_KEY // depending on API requirement
                    },
                    body: JSON.stringify(payload)
                });
                
                if (!response.ok) {
                    throw new Error(`API Error: ${response.statusText}`);
                }
                
                const data = await response.json();
                console.log("Scenario Generated:", data);
                */

                // Simulation for now
                console.log(`Calling API at ${CONFIG.API_ENDPOINT} with Key ${CONFIG.API_KEY}`);
                await new Promise(resolve => setTimeout(resolve, 2000));

                alert('API Request Sent! (Check console for details). Implement actual response handling in js/script.js');

            } catch (error) {
                console.error("Error generating scenario:", error);
                alert("生成失敗，請檢查 console 錯誤訊息");
            } finally {
                btn.disabled = false;
                btn.innerHTML = originalText;
            }
        });
    } else {
        console.warn("Generate Scenario button not found!");
    }
});
// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Close mobile menu when clicking a link
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });
});

// Smooth Scroll for Anchor Links (Optional, CSS scroll-behavior: smooth is often enough)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            e.preventDefault();
            // Offset for fixed header (20rem is about 80px)
            const headerOffset = 80;
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: "smooth"
            });
        }
    });
});

