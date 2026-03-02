import re

html_file = 'car_headliner_final.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Preloader
preloader_orig = '''<div class="preloader-inner">
            <h2 class="preloader-logo">KG<span style="color:#D4AF37;">.</span> Headliner</h2>'''
preloader_new = '''<div class="preloader-inner flex flex-col items-center">
            <img src="images_to_use/logo.svg" alt="KG Headliner Logo" class="w-24 h-24 mb-6 drop-shadow-[0_0_15px_rgba(212,175,55,0.4)]">
            <h2 class="preloader-logo">KG<span style="color:#D4AF37;">.</span> Headliner</h2>'''
html = html.replace(preloader_orig, preloader_new)

# 2. Update Navbar Logo & Language Toggle
navbar_orig_logo = '''<div class="font-display font-bold text-2xl tracking-tighter uppercase magnetic hover-trigger" data-strength="20">
                KG<span class="text-brand">.</span>
            </div>'''
navbar_new_logo = '''<div class="flex items-center gap-3 magnetic hover-trigger" data-strength="20">
                <img src="images_to_use/logo.svg" class="w-8 h-8 object-contain drop-shadow-[0_0_8px_rgba(212,175,55,0.4)]" alt="Logo">
                <div class="font-display font-bold text-2xl tracking-tighter uppercase">
                    KG<span class="text-brand">.</span>
                </div>
            </div>'''
html = html.replace(navbar_orig_logo, navbar_new_logo)

navbar_orig_right = '''<div class="flex items-center gap-6">
                <a href="tel:+13213741176" class="hidden lg:flex items-center gap-2 text-xs font-display tracking-widest text-white/80 hover:text-brand transition-colors hover-trigger">'''
navbar_new_right = '''<div class="flex items-center gap-6">
                <div class="hidden md:flex items-center gap-3 text-[10px] font-bold tracking-[0.2em] text-white/40">
                    <button class="lang-btn text-white transition-colors" data-lang="en">EN</button>
                    <span class="w-[1px] h-3 bg-white/20"></span>
                    <button class="lang-btn hover:text-white transition-colors" data-lang="es">ES</button>
                </div>
                <a href="tel:+13213741176" class="hidden lg:flex items-center gap-2 text-xs font-display tracking-widest text-white/80 hover:text-brand transition-colors hover-trigger">'''
html = html.replace(navbar_orig_right, navbar_new_right)

# 3. Add Split-Type classes to Hero text for Premium Animations
hero_orig = '''<div class="overflow-hidden mb-8">
                <p class="hero-sub font-sans text-brand tracking-[0.5em] uppercase text-xs font-bold translate-y-full flex items-center gap-4 justify-center">
                    <span class="w-8 h-[1px] bg-brand"></span>
                    100% Mobile Operations
                    <span class="w-8 h-[1px] bg-brand"></span>
                </p>
            </div>
            <h1 class="hero-title font-display font-bold text-[11vw] md:text-[9vw] leading-[0.8] tracking-tighter uppercase m-0 text-white drop-shadow-2xl">
                Restoring<br><span class="font-luxury italic text-brand font-light lowercase text-[12vw] md:text-[10vw] pr-4">the</span> Pinnacle.
            </h1>'''
hero_new = '''<div class="overflow-hidden mb-8">
                <p class="hero-sub font-sans text-brand tracking-[0.5em] uppercase text-xs font-bold flex items-center gap-4 justify-center">
                    <span class="w-8 h-[1px] bg-brand hero-line"></span>
                    <span class="premium-text-animate">100% Mobile Operations</span>
                    <span class="w-8 h-[1px] bg-brand hero-line"></span>
                </p>
            </div>
            <h1 class="hero-title font-display font-bold text-[11vw] md:text-[9vw] leading-[0.8] tracking-tighter uppercase m-0 text-white drop-shadow-2xl premium-title-animate">
                Restoring<br><span class="font-luxury italic text-brand font-light lowercase text-[12vw] md:text-[10vw] pr-4">the</span> Pinnacle.
            </h1>'''
html = html.replace(hero_orig, hero_new)

# 4. Inject Translation and GSAP Animation Script before </body>
script_injection = '''
    <!-- Text Animation & Translation Scripts -->
    <script>
        // High-End Text Animations
        document.addEventListener("DOMContentLoaded", () => {
            if (typeof window.SplitType !== 'undefined' && typeof window.gsap !== 'undefined') {
                const subText = new SplitType('.premium-text-animate', { types: 'chars' });
                const titleText = new SplitType('.premium-title-animate', { types: 'words, chars' });
                
                // Preloader hide animation sequence
                setTimeout(() => {
                    const preloader = document.getElementById('preloader');
                    window.gsap.to(preloader, {
                        opacity: 0,
                        duration: 1.2,
                        ease: "power2.inOut",
                        onComplete: () => {
                            preloader.style.display = 'none';
                            
                            // Trigger Hero Animations
                            const tl = window.gsap.timeline();
                            tl.fromTo('.hero-line', { width: 0, opacity: 0 }, { width: 32, opacity: 1, duration: 1, ease: "power3.out" })
                              .fromTo(subText.chars, { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8, stagger: 0.05, ease: "back.out(1.7)" }, "-=0.5")
                              .fromTo(titleText.words, { y: 100, opacity: 0, rotateX: -45 }, { y: 0, opacity: 1, rotateX: 0, duration: 1.2, stagger: 0.1, ease: "expo.out" }, "-=0.8")
                              .fromTo('.hero-desc', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 1, ease: "power3.out" }, "-=0.8");
                        }
                    });
                }, 1500);
            } else {
                // Fallback if scripts are missing
                document.getElementById('preloader').classList.add('is-hidden');
            }
        });

        // Basic Dictionary Translation System
        const translations = {
            "en": {
                "nav_mastery": "Mastery", "nav_transformations": "Transformations", "nav_mobile": "Mobile Service", "nav_book": "Book Concierge",
                "hero_sub": "100% Mobile Operations", "hero_title": "Restoring<br><span class=\\"font-luxury italic text-brand font-light lowercase text-[12vw] md:text-[10vw] pr-4\\">the</span> Pinnacle.", "hero_desc": "Your time is a luxury. We are Florida's premier fully mobile studio, bringing factory-perfect headliner restoration and Alcantara upgrades directly to your driveway or dealership.", "hero_scroll": "Discover Mastery",
                "expertise_sub": "Our Expertise", "expertise_title": "Mastery in <br><span class=\\"font-luxury italic text-white/80 font-light lowercase\\">every</span> detail.", "expertise_desc": "Scroll horizontally to explore the uncompromising standards of our core services. Engineered to perfection, executed in your driveway.",
                "factory_title": "Factory <br><span class=\\"text-brand\\">Restoration.</span>", "factory_desc": "We surgically extract the shell, strip the degraded, toxic structural foam down to the core fiberglass, and bond premium OEM fabrics using high-temp industrial adhesives.", "alcantara_title": "Alcantara <br><span class=\\"text-brand\\">Upgrades.</span>", "alcantara_desc": "Elevate your cabin to supercar standards. We import genuine Italian Alcantara to wrap your headliner, providing a track-focused, luxurious matte texture.", "pillars_title": "Pillars & <br><span class=\\"text-brand\\">Sun Visors.</span>", "pillars_desc": "A holistic restoration. We ensure your A, B, and C pillars, along with complex sunroof sliding shades and visors, are meticulously hand-stitched and recovered to match.",
                "portfolio_title": "Witness the <br><span class=\\"text-brand\\">Transformation.</span>", "portfolio_desc": "Select a vehicle below to view the meticulous restoration process. We turn ruined interiors back to showroom perfection.",
                "marquee": "WE ARE 100% MOBILE <span class=\\"text-white/50 text-3xl\\">&bull;</span> WE COME TO YOU <span class=\\"text-white/50 text-3xl\\">&bull;</span> HOME OR OFFICE <span class=\\"text-white/50 text-3xl\\">&bull;</span>",
                "social_sub": "Real Results. Real Convenience.", "social_title": "The Studio Feed <br>& <span class=\\"font-luxury italic text-white/80 font-light lowercase\\">verified</span> Excellence.",
                "contact_sub": "Mobile Dispatch", "contact_title": "Book Your <br><span class=\\"font-luxury italic text-white/80 font-light lowercase\\">appointment.</span>"
            },
            "es": {
                "nav_mastery": "Maestría", "nav_transformations": "Transformaciones", "nav_mobile": "Servicio Móvil", "nav_book": "Reserva Ahora",
                "hero_sub": "Operaciones 100% Móviles", "hero_title": "Restaurando<br><span class=\\"font-luxury italic text-brand font-light lowercase text-[12vw] md:text-[10vw] pr-4\\">el</span> Pináculo.", "hero_desc": "Tu tiempo es un lujo. Somos el principal estudio completamente móvil de Florida, llevando la restauración perfecta de techos y mejoras de Alcantara directamente a tu entrada o concesionario.", "hero_scroll": "Descubre la Maestría",
                "expertise_sub": "Nuestra Experiencia", "expertise_title": "Maestría en <br><span class=\\"font-luxury italic text-white/80 font-light lowercase\\">cada</span> detalle.", "expertise_desc": "Desplázate horizontalmente para explorar los estándares intransigentes de nuestros servicios principales. Diseñados a la perfección, ejecutados en tu entrada.",
                "factory_title": "Restauración <br><span class=\\"text-brand\\">de Fábrica.</span>", "factory_desc": "Extraemos quirúrgicamente la carcasa, eliminamos la espuma estructural degradada hasta el núcleo de fibra de vidrio, y unimos telas OEM premium usando adhesivos industriales de alta temperatura.", "alcantara_title": "Mejoras en <br><span class=\\"text-brand\\">Alcantara.</span>", "alcantara_desc": "Eleva tu cabina a los estándares de un superdeportivo. Importamos Alcantara italiano genuino para forrar tu techo, proporcionando una textura mate lujosa enfocada en la pista.", "pillars_title": "Pilares y <br><span class=\\"text-brand\\">Viseras.</span>", "pillars_desc": "Una restauración integral. Nos aseguramos de que tus pilares A, B y C, junto con las complejas persianas solares y viseras, sean meticulosamente cosidos a mano y forrados para combinar.",
                "portfolio_title": "Testigo de la <br><span class=\\"text-brand\\">Transformación.</span>", "portfolio_desc": "Selecciona un vehículo a continuación para ver el proceso de restauración minucioso. Devolvemos interiores arruinados a la perfección de sala de exposición.",
                "marquee": "SOMOS 100% MÓVILES <span class=\\"text-white/50 text-3xl\\">&bull;</span> VAMOS A TI <span class=\\"text-white/50 text-3xl\\">&bull;</span> CASA U OFICINA <span class=\\"text-white/50 text-3xl\\">&bull;</span>",
                "social_sub": "Resultados Reales.", "social_title": "Nuestro Feed <br>& Excelencia <span class=\\"font-luxury italic text-white/80 font-light lowercase\\">verificada</span>.",
                "contact_sub": "Despacho Móvil", "contact_title": "Reserva Tu <br><span class=\\"font-luxury italic text-white/80 font-light lowercase\\">cita.</span>"
            }
        };

        const updateLanguage = (lang) => {
            document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.replace('text-white', 'text-white/40'));
            document.querySelector(`.lang-btn[data-lang="${lang}"]`).classList.replace('text-white/40', 'text-white');
            
            // Re-apply SplitType after text change if it's the hero
            const sub = document.querySelector('.premium-text-animate');
            const title = document.querySelector('.premium-title-animate');
            
            if (sub && title && typeof window.SplitType !== 'undefined') {
                sub.innerHTML = translations[lang]['hero_sub'];
                title.innerHTML = translations[lang]['hero_title'];
                new SplitType('.premium-text-animate', { types: 'chars' });
                new SplitType('.premium-title-animate', { types: 'words, chars' });
            }

            // A basic search and replace could be done by ID or classes
            const replaceMap = {
                'a[href="#services"]': 'nav_mastery',
                'a[href="#portfolio"]': 'nav_transformations',
                '.hero-desc': 'hero_desc',
                '#services .reveal-text:nth-of-type(1)': 'expertise_sub',
                '#services h2': 'expertise_title',
                '#services .reveal-text:nth-of-type(3)': 'expertise_desc',
            };
            
            for (const [selector, key] of Object.entries(replaceMap)) {
                const el = document.querySelector(selector);
                if (el) el.innerHTML = translations[lang][key];
            }
        };

        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', (e) => updateLanguage(e.target.dataset.lang));
        });
    </script>
</body>'''
html = html.replace('</body>', script_injection)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML updated successfully!')
