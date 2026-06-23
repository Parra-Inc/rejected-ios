#!/usr/bin/env python3
"""Generate Localizable.xcstrings with translations for all 37 App Store localizations.

Modeled on Tax Days' generate_strings.py. Every user-facing English string in the
app's SwiftUI sources is registered with t(); plural / count-interpolated strings
use stringsDict variations via p(). Run from this directory:

    python3 generate_strings.py
"""

import json
import os

LANGUAGES = [
    "ar", "ca", "cs", "da", "de", "el", "en-AU", "en-GB", "es", "es-419",
    "fi", "fr", "fr-CA", "he", "hi", "hr", "hu", "id", "it", "ja", "ko",
    "ms", "nb", "nl", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sv",
    "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant"
]

# Plural categories required per language (CLDR). Languages not listed use
# the default {one, other}. Arabic, Polish, Russian, etc. need more.
PLURAL_CATEGORIES = {
    "ar": ["zero", "one", "two", "few", "many", "other"],
    "cs": ["one", "few", "many", "other"],
    "sk": ["one", "few", "many", "other"],
    "pl": ["one", "few", "many", "other"],
    "ru": ["one", "few", "many", "other"],
    "uk": ["one", "few", "many", "other"],
    "hr": ["one", "few", "other"],
    "ro": ["one", "few", "other"],
    "lt": ["one", "few", "other"],
    "he": ["one", "two", "many", "other"],
    # CJK / no-plural languages collapse to "other" only
    "ja": ["other"], "ko": ["other"], "zh-Hans": ["other"], "zh-Hant": ["other"],
    "th": ["other"], "vi": ["other"], "id": ["other"], "ms": ["other"],
}

# Format: { "english_key": { "lang_code": "translation", ... } }
T = {}
# Plural strings: { "english_key": { "format": "...%lld...", lang: {cat: value} } }
P = {}


def t(key, translations):
    """Register a flat (non-plural) string."""
    T[key] = translations


def p(key, en_one, en_other, variations):
    """Register a plural string.

    en_one / en_other are the English source forms. `variations` maps each
    language to a dict of {plural_category: value}. The %lld placeholder is
    substituted into each form.
    """
    P[key] = {"en_one": en_one, "en_other": en_other, "variations": variations}


# ============================================================
# NAVIGATION / TAB BAR
# ============================================================
t("Rejections", {
    "ar": "حالات الرفض", "ca": "Rebutjos", "cs": "Odmítnutí", "da": "Afslag", "de": "Absagen",
    "el": "Απορρίψεις", "es": "Rechazos", "es-419": "Rechazos", "fi": "Hylkäykset", "fr": "Refus",
    "fr-CA": "Refus", "he": "דחיות", "hi": "अस्वीकृतियाँ", "hr": "Odbijanja", "hu": "Elutasítások",
    "id": "Penolakan", "it": "Rifiuti", "ja": "不採用", "ko": "거절", "ms": "Penolakan",
    "nb": "Avslag", "nl": "Afwijzingen", "pl": "Odrzucenia", "pt-BR": "Rejeições", "pt-PT": "Rejeições",
    "ro": "Respingeri", "ru": "Отказы", "sk": "Odmietnutia", "sv": "Avslag", "th": "การถูกปฏิเสธ",
    "tr": "Retler", "uk": "Відмови", "vi": "Từ chối", "zh-Hans": "拒绝", "zh-Hant": "拒絕"
})
t("Settings", {
    "ar": "الإعدادات", "ca": "Configuració", "cs": "Nastavení", "da": "Indstillinger", "de": "Einstellungen",
    "el": "Ρυθμίσεις", "es": "Ajustes", "es-419": "Configuración", "fi": "Asetukset", "fr": "Réglages",
    "fr-CA": "Paramètres", "he": "הגדרות", "hi": "सेटिंग्स", "hr": "Postavke", "hu": "Beállítások",
    "id": "Pengaturan", "it": "Impostazioni", "ja": "設定", "ko": "설정", "ms": "Tetapan",
    "nb": "Innstillinger", "nl": "Instellingen", "pl": "Ustawienia", "pt-BR": "Configurações", "pt-PT": "Definições",
    "ro": "Setări", "ru": "Настройки", "sk": "Nastavenia", "sv": "Inställningar", "th": "การตั้งค่า",
    "tr": "Ayarlar", "uk": "Налаштування", "vi": "Cài đặt", "zh-Hans": "设置", "zh-Hant": "設定"
})
t("Search", {
    "ar": "بحث", "ca": "Cerca", "cs": "Hledat", "da": "Søg", "de": "Suche",
    "el": "Αναζήτηση", "es": "Buscar", "es-419": "Buscar", "fi": "Haku", "fr": "Rechercher",
    "fr-CA": "Rechercher", "he": "חיפוש", "hi": "खोजें", "hr": "Pretraži", "hu": "Keresés",
    "id": "Cari", "it": "Cerca", "ja": "検索", "ko": "검색", "ms": "Cari",
    "nb": "Søk", "nl": "Zoeken", "pl": "Szukaj", "pt-BR": "Buscar", "pt-PT": "Pesquisar",
    "ro": "Căutare", "ru": "Поиск", "sk": "Hľadať", "sv": "Sök", "th": "ค้นหา",
    "tr": "Ara", "uk": "Пошук", "vi": "Tìm kiếm", "zh-Hans": "搜索", "zh-Hant": "搜尋"
})

# ============================================================
# REJECTIONS HOME — SECTIONS / STATS
# ============================================================
t("Stats", {
    "ar": "الإحصائيات", "ca": "Estadístiques", "cs": "Statistiky", "da": "Statistik", "de": "Statistiken",
    "el": "Στατιστικά", "es": "Estadísticas", "es-419": "Estadísticas", "fi": "Tilastot", "fr": "Statistiques",
    "fr-CA": "Statistiques", "he": "סטטיסטיקות", "hi": "आँकड़े", "hr": "Statistike", "hu": "Statisztikák",
    "id": "Statistik", "it": "Statistiche", "ja": "統計", "ko": "통계", "ms": "Statistik",
    "nb": "Statistikk", "nl": "Statistieken", "pl": "Statystyki", "pt-BR": "Estatísticas", "pt-PT": "Estatísticas",
    "ro": "Statistici", "ru": "Статистика", "sk": "Štatistiky", "sv": "Statistik", "th": "สถิติ",
    "tr": "İstatistikler", "uk": "Статистика", "vi": "Thống kê", "zh-Hans": "统计", "zh-Hant": "統計"
})
t("History", {
    "ar": "السجل", "ca": "Historial", "cs": "Historie", "da": "Historik", "de": "Verlauf",
    "el": "Ιστορικό", "es": "Historial", "es-419": "Historial", "fi": "Historia", "fr": "Historique",
    "fr-CA": "Historique", "he": "היסטוריה", "hi": "इतिहास", "hr": "Povijest", "hu": "Előzmények",
    "id": "Riwayat", "it": "Cronologia", "ja": "履歴", "ko": "기록", "ms": "Sejarah",
    "nb": "Historikk", "nl": "Geschiedenis", "pl": "Historia", "pt-BR": "Histórico", "pt-PT": "Histórico",
    "ro": "Istoric", "ru": "История", "sk": "História", "sv": "Historik", "th": "ประวัติ",
    "tr": "Geçmiş", "uk": "Історія", "vi": "Lịch sử", "zh-Hans": "历史", "zh-Hant": "歷史"
})
t("Total Rejections", {
    "ar": "إجمالي حالات الرفض", "ca": "Rebutjos totals", "cs": "Celkem odmítnutí", "da": "Afslag i alt", "de": "Absagen gesamt",
    "el": "Σύνολο απορρίψεων", "es": "Rechazos totales", "es-419": "Rechazos totales", "fi": "Hylkäyksiä yhteensä", "fr": "Total des refus",
    "fr-CA": "Total des refus", "he": "סך הדחיות", "hi": "कुल अस्वीकृतियाँ", "hr": "Ukupno odbijanja", "hu": "Összes elutasítás",
    "id": "Total Penolakan", "it": "Rifiuti totali", "ja": "不採用の合計", "ko": "전체 거절", "ms": "Jumlah Penolakan",
    "nb": "Avslag totalt", "nl": "Totaal afwijzingen", "pl": "Łącznie odrzuceń", "pt-BR": "Total de rejeições", "pt-PT": "Total de rejeições",
    "ro": "Total respingeri", "ru": "Всего отказов", "sk": "Odmietnutí spolu", "sv": "Avslag totalt", "th": "การถูกปฏิเสธทั้งหมด",
    "tr": "Toplam Ret", "uk": "Усього відмов", "vi": "Tổng số từ chối", "zh-Hans": "拒绝总数", "zh-Hant": "拒絕總數"
})
t("Last Rejection", {
    "ar": "آخر رفض", "ca": "Últim rebuig", "cs": "Poslední odmítnutí", "da": "Seneste afslag", "de": "Letzte Absage",
    "el": "Τελευταία απόρριψη", "es": "Último rechazo", "es-419": "Último rechazo", "fi": "Viimeisin hylkäys", "fr": "Dernier refus",
    "fr-CA": "Dernier refus", "he": "הדחייה האחרונה", "hi": "अंतिम अस्वीकृति", "hr": "Zadnje odbijanje", "hu": "Utolsó elutasítás",
    "id": "Penolakan Terakhir", "it": "Ultimo rifiuto", "ja": "最後の不採用", "ko": "최근 거절", "ms": "Penolakan Terakhir",
    "nb": "Siste avslag", "nl": "Laatste afwijzing", "pl": "Ostatnie odrzucenie", "pt-BR": "Última rejeição", "pt-PT": "Última rejeição",
    "ro": "Ultima respingere", "ru": "Последний отказ", "sk": "Posledné odmietnutie", "sv": "Senaste avslaget", "th": "การถูกปฏิเสธล่าสุด",
    "tr": "Son Ret", "uk": "Остання відмова", "vi": "Lần từ chối gần nhất", "zh-Hans": "最近一次拒绝", "zh-Hant": "最近一次拒絕"
})
t("Top Categories", {
    "ar": "أهم الفئات", "ca": "Categories principals", "cs": "Hlavní kategorie", "da": "Topkategorier", "de": "Top-Kategorien",
    "el": "Κορυφαίες κατηγορίες", "es": "Categorías principales", "es-419": "Categorías principales", "fi": "Suosituimmat kategoriat", "fr": "Catégories principales",
    "fr-CA": "Catégories principales", "he": "קטגוריות מובילות", "hi": "शीर्ष श्रेणियाँ", "hr": "Glavne kategorije", "hu": "Fő kategóriák",
    "id": "Kategori Teratas", "it": "Categorie principali", "ja": "上位カテゴリ", "ko": "주요 카테고리", "ms": "Kategori Teratas",
    "nb": "Toppkategorier", "nl": "Topcategorieën", "pl": "Najczęstsze kategorie", "pt-BR": "Principais categorias", "pt-PT": "Principais categorias",
    "ro": "Categorii de top", "ru": "Топ-категории", "sk": "Hlavné kategórie", "sv": "Toppkategorier", "th": "หมวดหมู่ยอดนิยม",
    "tr": "En Çok Ret Alınan Kategoriler", "uk": "Топ-категорії", "vi": "Danh mục hàng đầu", "zh-Hans": "热门类别", "zh-Hant": "熱門類別"
})
t("Just now", {
    "ar": "الآن", "ca": "Ara mateix", "cs": "Právě teď", "da": "Lige nu", "de": "Gerade eben",
    "el": "Μόλις τώρα", "es": "Justo ahora", "es-419": "Recién", "fi": "Juuri nyt", "fr": "À l'instant",
    "fr-CA": "À l'instant", "he": "ממש עכשיו", "hi": "अभी-अभी", "hr": "Upravo sada", "hu": "Az imént",
    "id": "Baru saja", "it": "Proprio ora", "ja": "たった今", "ko": "방금", "ms": "Sebentar tadi",
    "nb": "Akkurat nå", "nl": "Zojuist", "pl": "Przed chwilą", "pt-BR": "Agora mesmo", "pt-PT": "Agora mesmo",
    "ro": "Chiar acum", "ru": "Только что", "sk": "Práve teraz", "sv": "Just nu", "th": "เมื่อสักครู่",
    "tr": "Az önce", "uk": "Щойно", "vi": "Vừa xong", "zh-Hans": "刚刚", "zh-Hant": "剛剛"
})
# "%@ ago" — DateComponentsFormatter output is substituted into %@
t("%@ ago", {
    "ar": "قبل %@", "ca": "fa %@", "cs": "před %@", "da": "for %@ siden", "de": "vor %@",
    "el": "πριν από %@", "es": "hace %@", "es-419": "hace %@", "fi": "%@ sitten", "fr": "il y a %@",
    "fr-CA": "il y a %@", "he": "לפני %@", "hi": "%@ पहले", "hr": "prije %@", "hu": "%@ ezelőtt",
    "id": "%@ yang lalu", "it": "%@ fa", "ja": "%@前", "ko": "%@ 전", "ms": "%@ yang lalu",
    "nb": "%@ siden", "nl": "%@ geleden", "pl": "%@ temu", "pt-BR": "há %@", "pt-PT": "há %@",
    "ro": "acum %@", "ru": "%@ назад", "sk": "pred %@", "sv": "för %@ sedan", "th": "%@ ที่แล้ว",
    "tr": "%@ önce", "uk": "%@ тому", "vi": "%@ trước", "zh-Hans": "%@前", "zh-Hant": "%@前"
})

# ============================================================
# CREATE REJECTION SHEET
# ============================================================
t("Add Rejection", {
    "ar": "إضافة رفض", "ca": "Afegir rebuig", "cs": "Přidat odmítnutí", "da": "Tilføj afslag", "de": "Absage hinzufügen",
    "el": "Προσθήκη απόρριψης", "es": "Añadir rechazo", "es-419": "Agregar rechazo", "fi": "Lisää hylkäys", "fr": "Ajouter un refus",
    "fr-CA": "Ajouter un refus", "he": "הוספת דחייה", "hi": "अस्वीकृति जोड़ें", "hr": "Dodaj odbijanje", "hu": "Elutasítás hozzáadása",
    "id": "Tambah Penolakan", "it": "Aggiungi rifiuto", "ja": "不採用を追加", "ko": "거절 추가", "ms": "Tambah Penolakan",
    "nb": "Legg til avslag", "nl": "Afwijzing toevoegen", "pl": "Dodaj odrzucenie", "pt-BR": "Adicionar rejeição", "pt-PT": "Adicionar rejeição",
    "ro": "Adaugă respingere", "ru": "Добавить отказ", "sk": "Pridať odmietnutie", "sv": "Lägg till avslag", "th": "เพิ่มการถูกปฏิเสธ",
    "tr": "Ret Ekle", "uk": "Додати відмову", "vi": "Thêm lần từ chối", "zh-Hans": "添加拒绝", "zh-Hant": "新增拒絕"
})
t("Category", {
    "ar": "الفئة", "ca": "Categoria", "cs": "Kategorie", "da": "Kategori", "de": "Kategorie",
    "el": "Κατηγορία", "es": "Categoría", "es-419": "Categoría", "fi": "Kategoria", "fr": "Catégorie",
    "fr-CA": "Catégorie", "he": "קטגוריה", "hi": "श्रेणी", "hr": "Kategorija", "hu": "Kategória",
    "id": "Kategori", "it": "Categoria", "ja": "カテゴリ", "ko": "카테고리", "ms": "Kategori",
    "nb": "Kategori", "nl": "Categorie", "pl": "Kategoria", "pt-BR": "Categoria", "pt-PT": "Categoria",
    "ro": "Categorie", "ru": "Категория", "sk": "Kategória", "sv": "Kategori", "th": "หมวดหมู่",
    "tr": "Kategori", "uk": "Категорія", "vi": "Danh mục", "zh-Hans": "类别", "zh-Hant": "類別"
})
t("Title", {
    "ar": "العنوان", "ca": "Títol", "cs": "Název", "da": "Titel", "de": "Titel",
    "el": "Τίτλος", "es": "Título", "es-419": "Título", "fi": "Otsikko", "fr": "Titre",
    "fr-CA": "Titre", "he": "כותרת", "hi": "शीर्षक", "hr": "Naslov", "hu": "Cím",
    "id": "Judul", "it": "Titolo", "ja": "タイトル", "ko": "제목", "ms": "Tajuk",
    "nb": "Tittel", "nl": "Titel", "pl": "Tytuł", "pt-BR": "Título", "pt-PT": "Título",
    "ro": "Titlu", "ru": "Название", "sk": "Názov", "sv": "Titel", "th": "ชื่อ",
    "tr": "Başlık", "uk": "Назва", "vi": "Tiêu đề", "zh-Hans": "标题", "zh-Hant": "標題"
})
t("Note", {
    "ar": "ملاحظة", "ca": "Nota", "cs": "Poznámka", "da": "Note", "de": "Notiz",
    "el": "Σημείωση", "es": "Nota", "es-419": "Nota", "fi": "Muistiinpano", "fr": "Note",
    "fr-CA": "Note", "he": "הערה", "hi": "नोट", "hr": "Bilješka", "hu": "Jegyzet",
    "id": "Catatan", "it": "Nota", "ja": "メモ", "ko": "메모", "ms": "Nota",
    "nb": "Notat", "nl": "Notitie", "pl": "Notatka", "pt-BR": "Nota", "pt-PT": "Nota",
    "ro": "Notă", "ru": "Заметка", "sk": "Poznámka", "sv": "Anteckning", "th": "บันทึก",
    "tr": "Not", "uk": "Нотатка", "vi": "Ghi chú", "zh-Hans": "备注", "zh-Hant": "備註"
})
t("Enter a title", {
    "ar": "أدخل عنوانًا", "ca": "Introdueix un títol", "cs": "Zadejte název", "da": "Indtast en titel", "de": "Titel eingeben",
    "el": "Εισαγάγετε έναν τίτλο", "es": "Introduce un título", "es-419": "Ingresa un título", "fi": "Anna otsikko", "fr": "Saisissez un titre",
    "fr-CA": "Saisissez un titre", "he": "הזן כותרת", "hi": "शीर्षक दर्ज करें", "hr": "Unesite naslov", "hu": "Adjon meg egy címet",
    "id": "Masukkan judul", "it": "Inserisci un titolo", "ja": "タイトルを入力", "ko": "제목 입력", "ms": "Masukkan tajuk",
    "nb": "Skriv inn en tittel", "nl": "Voer een titel in", "pl": "Wprowadź tytuł", "pt-BR": "Digite um título", "pt-PT": "Introduza um título",
    "ro": "Introdu un titlu", "ru": "Введите название", "sk": "Zadajte názov", "sv": "Ange en titel", "th": "ป้อนชื่อ",
    "tr": "Bir başlık girin", "uk": "Введіть назву", "vi": "Nhập tiêu đề", "zh-Hans": "输入标题", "zh-Hant": "輸入標題"
})
t("Please select a category", {
    "ar": "يرجى اختيار فئة", "ca": "Selecciona una categoria", "cs": "Vyberte kategorii", "da": "Vælg en kategori", "de": "Bitte wähle eine Kategorie",
    "el": "Επιλέξτε μια κατηγορία", "es": "Selecciona una categoría", "es-419": "Selecciona una categoría", "fi": "Valitse kategoria", "fr": "Veuillez sélectionner une catégorie",
    "fr-CA": "Veuillez sélectionner une catégorie", "he": "בחר קטגוריה", "hi": "कृपया एक श्रेणी चुनें", "hr": "Odaberite kategoriju", "hu": "Válasszon kategóriát",
    "id": "Silakan pilih kategori", "it": "Seleziona una categoria", "ja": "カテゴリを選択してください", "ko": "카테고리를 선택하세요", "ms": "Sila pilih kategori",
    "nb": "Velg en kategori", "nl": "Selecteer een categorie", "pl": "Wybierz kategorię", "pt-BR": "Selecione uma categoria", "pt-PT": "Selecione uma categoria",
    "ro": "Selectează o categorie", "ru": "Выберите категорию", "sk": "Vyberte kategóriu", "sv": "Välj en kategori", "th": "กรุณาเลือกหมวดหมู่",
    "tr": "Lütfen bir kategori seçin", "uk": "Виберіть категорію", "vi": "Vui lòng chọn danh mục", "zh-Hans": "请选择一个类别", "zh-Hant": "請選擇一個類別"
})
t("Please enter a title", {
    "ar": "يرجى إدخال عنوان", "ca": "Introdueix un títol", "cs": "Zadejte název", "da": "Indtast en titel", "de": "Bitte gib einen Titel ein",
    "el": "Εισαγάγετε έναν τίτλο", "es": "Introduce un título", "es-419": "Ingresa un título", "fi": "Anna otsikko", "fr": "Veuillez saisir un titre",
    "fr-CA": "Veuillez saisir un titre", "he": "הזן כותרת", "hi": "कृपया एक शीर्षक दर्ज करें", "hr": "Unesite naslov", "hu": "Adjon meg egy címet",
    "id": "Silakan masukkan judul", "it": "Inserisci un titolo", "ja": "タイトルを入力してください", "ko": "제목을 입력하세요", "ms": "Sila masukkan tajuk",
    "nb": "Skriv inn en tittel", "nl": "Voer een titel in", "pl": "Wprowadź tytuł", "pt-BR": "Digite um título", "pt-PT": "Introduza um título",
    "ro": "Introdu un titlu", "ru": "Введите название", "sk": "Zadajte názov", "sv": "Ange en titel", "th": "กรุณาป้อนชื่อ",
    "tr": "Lütfen bir başlık girin", "uk": "Введіть назву", "vi": "Vui lòng nhập tiêu đề", "zh-Hans": "请输入标题", "zh-Hant": "請輸入標題"
})
t("Save Rejection", {
    "ar": "حفظ الرفض", "ca": "Desar rebuig", "cs": "Uložit odmítnutí", "da": "Gem afslag", "de": "Absage speichern",
    "el": "Αποθήκευση απόρριψης", "es": "Guardar rechazo", "es-419": "Guardar rechazo", "fi": "Tallenna hylkäys", "fr": "Enregistrer le refus",
    "fr-CA": "Enregistrer le refus", "he": "שמירת דחייה", "hi": "अस्वीकृति सहेजें", "hr": "Spremi odbijanje", "hu": "Elutasítás mentése",
    "id": "Simpan Penolakan", "it": "Salva rifiuto", "ja": "不採用を保存", "ko": "거절 저장", "ms": "Simpan Penolakan",
    "nb": "Lagre avslag", "nl": "Afwijzing opslaan", "pl": "Zapisz odrzucenie", "pt-BR": "Salvar rejeição", "pt-PT": "Guardar rejeição",
    "ro": "Salvează respingerea", "ru": "Сохранить отказ", "sk": "Uložiť odmietnutie", "sv": "Spara avslag", "th": "บันทึกการถูกปฏิเสธ",
    "tr": "Reti Kaydet", "uk": "Зберегти відмову", "vi": "Lưu lần từ chối", "zh-Hans": "保存拒绝", "zh-Hant": "儲存拒絕"
})

# ============================================================
# CATEGORY PICKER / CREATE CATEGORY
# ============================================================
t("Add Category", {
    "ar": "إضافة فئة", "ca": "Afegir categoria", "cs": "Přidat kategorii", "da": "Tilføj kategori", "de": "Kategorie hinzufügen",
    "el": "Προσθήκη κατηγορίας", "es": "Añadir categoría", "es-419": "Agregar categoría", "fi": "Lisää kategoria", "fr": "Ajouter une catégorie",
    "fr-CA": "Ajouter une catégorie", "he": "הוספת קטגוריה", "hi": "श्रेणी जोड़ें", "hr": "Dodaj kategoriju", "hu": "Kategória hozzáadása",
    "id": "Tambah Kategori", "it": "Aggiungi categoria", "ja": "カテゴリを追加", "ko": "카테고리 추가", "ms": "Tambah Kategori",
    "nb": "Legg til kategori", "nl": "Categorie toevoegen", "pl": "Dodaj kategorię", "pt-BR": "Adicionar categoria", "pt-PT": "Adicionar categoria",
    "ro": "Adaugă categorie", "ru": "Добавить категорию", "sk": "Pridať kategóriu", "sv": "Lägg till kategori", "th": "เพิ่มหมวดหมู่",
    "tr": "Kategori Ekle", "uk": "Додати категорію", "vi": "Thêm danh mục", "zh-Hans": "添加类别", "zh-Hant": "新增類別"
})
t("Save Category", {
    "ar": "حفظ الفئة", "ca": "Desar categoria", "cs": "Uložit kategorii", "da": "Gem kategori", "de": "Kategorie speichern",
    "el": "Αποθήκευση κατηγορίας", "es": "Guardar categoría", "es-419": "Guardar categoría", "fi": "Tallenna kategoria", "fr": "Enregistrer la catégorie",
    "fr-CA": "Enregistrer la catégorie", "he": "שמירת קטגוריה", "hi": "श्रेणी सहेजें", "hr": "Spremi kategoriju", "hu": "Kategória mentése",
    "id": "Simpan Kategori", "it": "Salva categoria", "ja": "カテゴリを保存", "ko": "카테고리 저장", "ms": "Simpan Kategori",
    "nb": "Lagre kategori", "nl": "Categorie opslaan", "pl": "Zapisz kategorię", "pt-BR": "Salvar categoria", "pt-PT": "Guardar categoria",
    "ro": "Salvează categoria", "ru": "Сохранить категорию", "sk": "Uložiť kategóriu", "sv": "Spara kategori", "th": "บันทึกหมวดหมู่",
    "tr": "Kategoriyi Kaydet", "uk": "Зберегти категорію", "vi": "Lưu danh mục", "zh-Hans": "保存类别", "zh-Hant": "儲存類別"
})
t("Name", {
    "ar": "الاسم", "ca": "Nom", "cs": "Název", "da": "Navn", "de": "Name",
    "el": "Όνομα", "es": "Nombre", "es-419": "Nombre", "fi": "Nimi", "fr": "Nom",
    "fr-CA": "Nom", "he": "שם", "hi": "नाम", "hr": "Naziv", "hu": "Név",
    "id": "Nama", "it": "Nome", "ja": "名前", "ko": "이름", "ms": "Nama",
    "nb": "Navn", "nl": "Naam", "pl": "Nazwa", "pt-BR": "Nome", "pt-PT": "Nome",
    "ro": "Nume", "ru": "Имя", "sk": "Názov", "sv": "Namn", "th": "ชื่อ",
    "tr": "Ad", "uk": "Назва", "vi": "Tên", "zh-Hans": "名称", "zh-Hant": "名稱"
})
t("Name is required", {
    "ar": "الاسم مطلوب", "ca": "El nom és obligatori", "cs": "Název je povinný", "da": "Navn er påkrævet", "de": "Name ist erforderlich",
    "el": "Το όνομα είναι υποχρεωτικό", "es": "El nombre es obligatorio", "es-419": "El nombre es obligatorio", "fi": "Nimi vaaditaan", "fr": "Le nom est requis",
    "fr-CA": "Le nom est requis", "he": "שם הוא שדה חובה", "hi": "नाम आवश्यक है", "hr": "Naziv je obavezan", "hu": "A név megadása kötelező",
    "id": "Nama wajib diisi", "it": "Il nome è obbligatorio", "ja": "名前は必須です", "ko": "이름은 필수입니다", "ms": "Nama diperlukan",
    "nb": "Navn er påkrevd", "nl": "Naam is verplicht", "pl": "Nazwa jest wymagana", "pt-BR": "O nome é obrigatório", "pt-PT": "O nome é obrigatório",
    "ro": "Numele este obligatoriu", "ru": "Имя обязательно", "sk": "Názov je povinný", "sv": "Namn krävs", "th": "ต้องระบุชื่อ",
    "tr": "Ad gereklidir", "uk": "Назва обов’язкова", "vi": "Tên là bắt buộc", "zh-Hans": "名称为必填项", "zh-Hant": "名稱為必填項"
})
t("Enter category name", {
    "ar": "أدخل اسم الفئة", "ca": "Introdueix el nom de la categoria", "cs": "Zadejte název kategorie", "da": "Indtast kategorinavn", "de": "Kategorienamen eingeben",
    "el": "Εισαγάγετε όνομα κατηγορίας", "es": "Introduce el nombre de la categoría", "es-419": "Ingresa el nombre de la categoría", "fi": "Anna kategorian nimi", "fr": "Saisissez le nom de la catégorie",
    "fr-CA": "Saisissez le nom de la catégorie", "he": "הזן שם קטגוריה", "hi": "श्रेणी का नाम दर्ज करें", "hr": "Unesite naziv kategorije", "hu": "Adja meg a kategória nevét",
    "id": "Masukkan nama kategori", "it": "Inserisci il nome della categoria", "ja": "カテゴリ名を入力", "ko": "카테고리 이름 입력", "ms": "Masukkan nama kategori",
    "nb": "Skriv inn kategorinavn", "nl": "Voer categorienaam in", "pl": "Wprowadź nazwę kategorii", "pt-BR": "Digite o nome da categoria", "pt-PT": "Introduza o nome da categoria",
    "ro": "Introdu numele categoriei", "ru": "Введите название категории", "sk": "Zadajte názov kategórie", "sv": "Ange kategorinamn", "th": "ป้อนชื่อหมวดหมู่",
    "tr": "Kategori adını girin", "uk": "Введіть назву категорії", "vi": "Nhập tên danh mục", "zh-Hans": "输入类别名称", "zh-Hant": "輸入類別名稱"
})
t("Select category", {
    "ar": "اختر فئة", "ca": "Selecciona una categoria", "cs": "Vyberte kategorii", "da": "Vælg kategori", "de": "Kategorie auswählen",
    "el": "Επιλέξτε κατηγορία", "es": "Selecciona una categoría", "es-419": "Selecciona una categoría", "fi": "Valitse kategoria", "fr": "Sélectionner une catégorie",
    "fr-CA": "Sélectionner une catégorie", "he": "בחר קטגוריה", "hi": "श्रेणी चुनें", "hr": "Odaberite kategoriju", "hu": "Kategória kiválasztása",
    "id": "Pilih kategori", "it": "Seleziona categoria", "ja": "カテゴリを選択", "ko": "카테고리 선택", "ms": "Pilih kategori",
    "nb": "Velg kategori", "nl": "Selecteer categorie", "pl": "Wybierz kategorię", "pt-BR": "Selecionar categoria", "pt-PT": "Selecionar categoria",
    "ro": "Selectează categoria", "ru": "Выберите категорию", "sk": "Vyberte kategóriu", "sv": "Välj kategori", "th": "เลือกหมวดหมู่",
    "tr": "Kategori seçin", "uk": "Виберіть категорію", "vi": "Chọn danh mục", "zh-Hans": "选择类别", "zh-Hant": "選擇類別"
})
t("Emoji", {
    "ar": "إيموجي", "ca": "Emoji", "cs": "Emoji", "da": "Emoji", "de": "Emoji",
    "el": "Emoji", "es": "Emoji", "es-419": "Emoji", "fi": "Emoji", "fr": "Emoji",
    "fr-CA": "Émoji", "he": "אימוג'י", "hi": "इमोजी", "hr": "Emoji", "hu": "Emodzsi",
    "id": "Emoji", "it": "Emoji", "ja": "絵文字", "ko": "이모지", "ms": "Emoji",
    "nb": "Emoji", "nl": "Emoji", "pl": "Emoji", "pt-BR": "Emoji", "pt-PT": "Emoji",
    "ro": "Emoji", "ru": "Эмодзи", "sk": "Emodži", "sv": "Emoji", "th": "อิโมจิ",
    "tr": "Emoji", "uk": "Емодзі", "vi": "Biểu tượng cảm xúc", "zh-Hans": "表情符号", "zh-Hant": "表情符號"
})
t("Emojis", {
    "ar": "الإيموجي", "ca": "Emojis", "cs": "Emoji", "da": "Emojis", "de": "Emojis",
    "el": "Emoji", "es": "Emojis", "es-419": "Emojis", "fi": "Emojit", "fr": "Émojis",
    "fr-CA": "Émojis", "he": "אימוג'ים", "hi": "इमोजी", "hr": "Emojiji", "hu": "Emodzsik",
    "id": "Emoji", "it": "Emoji", "ja": "絵文字", "ko": "이모지", "ms": "Emoji",
    "nb": "Emojier", "nl": "Emoji's", "pl": "Emoji", "pt-BR": "Emojis", "pt-PT": "Emojis",
    "ro": "Emoji-uri", "ru": "Эмодзи", "sk": "Emodži", "sv": "Emojier", "th": "อิโมจิ",
    "tr": "Emojiler", "uk": "Емодзі", "vi": "Biểu tượng cảm xúc", "zh-Hans": "表情符号", "zh-Hant": "表情符號"
})
t("Image", {
    "ar": "صورة", "ca": "Imatge", "cs": "Obrázek", "da": "Billede", "de": "Bild",
    "el": "Εικόνα", "es": "Imagen", "es-419": "Imagen", "fi": "Kuva", "fr": "Image",
    "fr-CA": "Image", "he": "תמונה", "hi": "छवि", "hr": "Slika", "hu": "Kép",
    "id": "Gambar", "it": "Immagine", "ja": "画像", "ko": "이미지", "ms": "Imej",
    "nb": "Bilde", "nl": "Afbeelding", "pl": "Obraz", "pt-BR": "Imagem", "pt-PT": "Imagem",
    "ro": "Imagine", "ru": "Изображение", "sk": "Obrázok", "sv": "Bild", "th": "รูปภาพ",
    "tr": "Görsel", "uk": "Зображення", "vi": "Hình ảnh", "zh-Hans": "图片", "zh-Hant": "圖片"
})
t("Remove", {
    "ar": "إزالة", "ca": "Eliminar", "cs": "Odebrat", "da": "Fjern", "de": "Entfernen",
    "el": "Αφαίρεση", "es": "Eliminar", "es-419": "Quitar", "fi": "Poista", "fr": "Supprimer",
    "fr-CA": "Retirer", "he": "הסר", "hi": "हटाएँ", "hr": "Ukloni", "hu": "Eltávolítás",
    "id": "Hapus", "it": "Rimuovi", "ja": "削除", "ko": "제거", "ms": "Buang",
    "nb": "Fjern", "nl": "Verwijderen", "pl": "Usuń", "pt-BR": "Remover", "pt-PT": "Remover",
    "ro": "Elimină", "ru": "Удалить", "sk": "Odstrániť", "sv": "Ta bort", "th": "ลบ",
    "tr": "Kaldır", "uk": "Видалити", "vi": "Xóa", "zh-Hans": "移除", "zh-Hant": "移除"
})
t("Enter URL", {
    "ar": "أدخل عنوان URL", "ca": "Introdueix l'URL", "cs": "Zadejte adresu URL", "da": "Indtast URL", "de": "URL eingeben",
    "el": "Εισαγάγετε URL", "es": "Introduce la URL", "es-419": "Ingresa la URL", "fi": "Anna URL-osoite", "fr": "Saisissez l'URL",
    "fr-CA": "Saisissez l'URL", "he": "הזן כתובת URL", "hi": "URL दर्ज करें", "hr": "Unesite URL", "hu": "Adja meg az URL-t",
    "id": "Masukkan URL", "it": "Inserisci l'URL", "ja": "URLを入力", "ko": "URL 입력", "ms": "Masukkan URL",
    "nb": "Skriv inn URL", "nl": "Voer URL in", "pl": "Wprowadź adres URL", "pt-BR": "Digite a URL", "pt-PT": "Introduza o URL",
    "ro": "Introdu URL-ul", "ru": "Введите URL", "sk": "Zadajte URL", "sv": "Ange URL", "th": "ป้อน URL",
    "tr": "URL girin", "uk": "Введіть URL", "vi": "Nhập URL", "zh-Hans": "输入网址", "zh-Hant": "輸入網址"
})
t("Please enter a valid URL", {
    "ar": "يرجى إدخال عنوان URL صالح", "ca": "Introdueix un URL vàlid", "cs": "Zadejte platnou adresu URL", "da": "Indtast en gyldig URL", "de": "Bitte gib eine gültige URL ein",
    "el": "Εισαγάγετε ένα έγκυρο URL", "es": "Introduce una URL válida", "es-419": "Ingresa una URL válida", "fi": "Anna kelvollinen URL-osoite", "fr": "Veuillez saisir une URL valide",
    "fr-CA": "Veuillez saisir une URL valide", "he": "הזן כתובת URL תקינה", "hi": "कृपया एक मान्य URL दर्ज करें", "hr": "Unesite valjani URL", "hu": "Adjon meg egy érvényes URL-t",
    "id": "Silakan masukkan URL yang valid", "it": "Inserisci un URL valido", "ja": "有効なURLを入力してください", "ko": "유효한 URL을 입력하세요", "ms": "Sila masukkan URL yang sah",
    "nb": "Skriv inn en gyldig URL", "nl": "Voer een geldige URL in", "pl": "Wprowadź prawidłowy adres URL", "pt-BR": "Digite uma URL válida", "pt-PT": "Introduza um URL válido",
    "ro": "Introdu un URL valid", "ru": "Введите действительный URL", "sk": "Zadajte platnú adresu URL", "sv": "Ange en giltig URL", "th": "กรุณาป้อน URL ที่ถูกต้อง",
    "tr": "Lütfen geçerli bir URL girin", "uk": "Введіть дійсний URL", "vi": "Vui lòng nhập URL hợp lệ", "zh-Hans": "请输入有效的网址", "zh-Hant": "請輸入有效的網址"
})

# ============================================================
# EMPTY STATE
# ============================================================
t("Oh no!", {
    "ar": "يا للأسف!", "ca": "Oh, no!", "cs": "Ale ne!", "da": "Åh nej!", "de": "Oh nein!",
    "el": "Ωχ όχι!", "es": "¡Oh, no!", "es-419": "¡Oh, no!", "fi": "Voi ei!", "fr": "Oh non !",
    "fr-CA": "Oh non !", "he": "אוי לא!", "hi": "अरे नहीं!", "hr": "O, ne!", "hu": "Jaj, ne!",
    "id": "Oh tidak!", "it": "Oh no!", "ja": "あらら！", "ko": "이런!", "ms": "Alamak!",
    "nb": "Å nei!", "nl": "O nee!", "pl": "O nie!", "pt-BR": "Ah, não!", "pt-PT": "Oh, não!",
    "ro": "O, nu!", "ru": "О нет!", "sk": "Ale nie!", "sv": "Åh nej!", "th": "ไม่นะ!",
    "tr": "Olamaz!", "uk": "О ні!", "vi": "Ôi không!", "zh-Hans": "糟糕！", "zh-Hant": "糟糕！"
})
t("We're sorry you found us.\nAdd your rejection to get started!", {
    "ar": "نأسف لأنك وجدتنا.\nأضف رفضك للبدء!",
    "ca": "Lamentem que ens hagis trobat.\nAfegeix el teu rebuig per començar!",
    "cs": "Mrzí nás, že jste nás našli.\nPřidejte své odmítnutí a začněte!",
    "da": "Vi er kede af, at du fandt os.\nTilføj dit afslag for at komme i gang!",
    "de": "Schade, dass du uns gefunden hast.\nFüge deine Absage hinzu, um loszulegen!",
    "el": "Λυπόμαστε που μας βρήκες.\nΠρόσθεσε την απόρριψή σου για να ξεκινήσεις!",
    "es": "Sentimos que nos hayas encontrado.\nAñade tu rechazo para empezar.",
    "es-419": "Lamentamos que nos hayas encontrado.\nAgrega tu rechazo para empezar.",
    "fi": "Harmi, että löysit meidät.\nLisää hylkäyksesi ja aloita!",
    "fr": "Nous sommes désolés que vous nous ayez trouvés.\nAjoutez votre refus pour commencer !",
    "fr-CA": "Nous sommes désolés que vous nous ayez trouvés.\nAjoutez votre refus pour commencer !",
    "he": "מצטערים שמצאת אותנו.\nהוסף את הדחייה שלך כדי להתחיל!",
    "hi": "हमें खेद है कि आपको हमारी ज़रूरत पड़ी।\nशुरू करने के लिए अपनी अस्वीकृति जोड़ें!",
    "hr": "Žao nam je što si nas pronašao.\nDodaj svoje odbijanje za početak!",
    "hu": "Sajnáljuk, hogy ránk találtál.\nAdd hozzá az elutasításodat, és kezdjük!",
    "id": "Maaf Anda menemukan kami.\nTambahkan penolakan Anda untuk memulai!",
    "it": "Ci dispiace che tu ci abbia trovati.\nAggiungi il tuo rifiuto per iniziare!",
    "ja": "ここにたどり着いてしまったのは残念です。\n不採用を追加して始めましょう！",
    "ko": "여기까지 오게 되어 안타깝네요.\n거절을 추가해 시작하세요!",
    "ms": "Maaf anda menemui kami.\nTambah penolakan anda untuk bermula!",
    "nb": "Vi er lei for at du fant oss.\nLegg til avslaget ditt for å komme i gang!",
    "nl": "Jammer dat je ons gevonden hebt.\nVoeg je afwijzing toe om te beginnen!",
    "pl": "Przykro nam, że nas znalazłeś.\nDodaj swoje odrzucenie, aby zacząć!",
    "pt-BR": "Lamentamos que você tenha nos encontrado.\nAdicione sua rejeição para começar!",
    "pt-PT": "Lamentamos que nos tenha encontrado.\nAdicione a sua rejeição para começar!",
    "ro": "Ne pare rău că ne-ai găsit.\nAdaugă respingerea ta ca să începi!",
    "ru": "Жаль, что вы нас нашли.\nДобавьте свой отказ, чтобы начать!",
    "sk": "Mrzí nás, že ste nás našli.\nPridajte svoje odmietnutie a začnite!",
    "sv": "Vi är ledsna att du hittade oss.\nLägg till ditt avslag för att komma igång!",
    "th": "เสียใจด้วยที่คุณมาเจอเรา\nเพิ่มการถูกปฏิเสธของคุณเพื่อเริ่มต้น!",
    "tr": "Bizi bulduğun için üzgünüz.\nBaşlamak için retini ekle!",
    "uk": "Шкода, що ви нас знайшли.\nДодайте свою відмову, щоб почати!",
    "vi": "Rất tiếc vì bạn đã tìm đến chúng tôi.\nThêm lần từ chối của bạn để bắt đầu!",
    "zh-Hans": "很遗憾你需要找到我们。\n添加你的拒绝记录，开始吧！",
    "zh-Hant": "很遺憾你需要找到我們。\n新增你的拒絕記錄，開始吧！"
})

# ============================================================
# SHARE / CELEBRATION SHEET
# ============================================================
t("Now it's time to turn that frown upside down, get back out there and grind harder!", {
    "ar": "حان الوقت الآن لتحويل عبوسك إلى ابتسامة، عُد إلى الميدان واجتهد أكثر!",
    "ca": "Ara és el moment de fer un somriure, tornar a sortir-hi i esforçar-te encara més!",
    "cs": "Teď je čas vyměnit zamračení za úsměv, vrátit se do hry a makat ještě víc!",
    "da": "Nu er det tid til at vende den sure mine til et smil, komme tilbage og knokle endnu hårdere!",
    "de": "Jetzt ist es Zeit, das Stirnrunzeln in ein Lächeln zu verwandeln, weiterzumachen und noch härter zu kämpfen!",
    "el": "Τώρα είναι η ώρα να γυρίσεις το συνοφρύωμα ανάποδα, να ξαναβγείς εκεί έξω και να παλέψεις πιο σκληρά!",
    "es": "Ahora es el momento de cambiar esa cara larga por una sonrisa, salir de nuevo y darlo todo con más ganas.",
    "es-419": "Ahora es momento de cambiar esa cara larga por una sonrisa, salir de nuevo y darle con más ganas.",
    "fi": "Nyt on aika kääntää murjotus hymyksi, palata kentälle ja painaa entistä kovemmin!",
    "fr": "Il est temps de transformer cette grimace en sourire, de repartir au combat et de bosser encore plus dur !",
    "fr-CA": "Il est temps de transformer cette grimace en sourire, de repartir au combat et de bosser encore plus fort !",
    "he": "עכשיו הזמן להפוך את הזעף לחיוך, לחזור לזירה ולעבוד קשה יותר!",
    "hi": "अब समय है उस उदासी को मुस्कान में बदलने का, फिर से मैदान में उतरने और और भी मेहनत करने का!",
    "hr": "Sad je vrijeme da namrgođenost pretvoriš u osmijeh, vratiš se u igru i još jače zagriziš!",
    "hu": "Itt az idő, hogy mosolyra fordítsd a búsképet, visszatérj a ringbe és még keményebben hajts!",
    "id": "Sekarang saatnya mengubah cemberut jadi senyum, kembali ke gelanggang, dan berjuang lebih keras!",
    "it": "Ora è il momento di trasformare quel broncio in un sorriso, tornare in pista e impegnarti ancora di più!",
    "ja": "さあ、しかめっ面を笑顔に変えて、もう一度立ち上がって、もっと頑張ろう！",
    "ko": "이제 찡그린 얼굴을 활짝 펴고, 다시 도전해서 더 열심히 달려봐요!",
    "ms": "Kini masanya tukar muka masam jadi senyuman, kembali ke gelanggang dan berusaha lebih gigih!",
    "nb": "Nå er det på tide å snu sutringen til et smil, komme deg ut igjen og stå på enda hardere!",
    "nl": "Tijd om die frons om te draaien, er weer tegenaan te gaan en nóg harder te knallen!",
    "pl": "Teraz czas zamienić grymas w uśmiech, wrócić do gry i zaharować się jeszcze bardziej!",
    "pt-BR": "Agora é hora de transformar essa carranca em sorriso, voltar à ativa e ralar ainda mais!",
    "pt-PT": "Agora é hora de transformar esse esgar num sorriso, voltar à carga e dar ainda mais de ti!",
    "ro": "Acum e momentul să transformi încruntarea în zâmbet, să revii în arenă și să muncești și mai mult!",
    "ru": "Самое время сменить хмурый взгляд на улыбку, снова выйти на поле и работать ещё усерднее!",
    "sk": "Teraz je čas vymeniť zamračenie za úsmev, vrátiť sa do hry a makať ešte tvrdšie!",
    "sv": "Nu är det dags att byta rynkan mot ett leende, ge dig ut igen och kämpa ännu hårdare!",
    "th": "ถึงเวลาเปลี่ยนหน้าบึ้งเป็นรอยยิ้ม กลับออกไปลุยและพยายามให้หนักกว่าเดิม!",
    "tr": "Şimdi o asık suratı gülümsemeye çevirme, yeniden sahaya çıkıp daha çok çalışma zamanı!",
    "uk": "Тепер час перетворити похмурий вираз на усмішку, повернутися в гру й працювати ще завзятіше!",
    "vi": "Giờ là lúc đổi cái cau mày thành nụ cười, trở lại đường đua và cố gắng hơn nữa!",
    "zh-Hans": "现在是时候把愁眉转成笑脸，重新出发，更拼一点！",
    "zh-Hant": "現在是時候把愁眉轉成笑臉，重新出發，更拼一點！"
})
t("Remember: doing something nice for others when you're down is the best way to help you feel better :)", {
    "ar": "تذكّر: فعل شيء لطيف للآخرين حين تكون محبطًا هو أفضل طريقة لتحسين شعورك :)",
    "ca": "Recorda: fer alguna cosa bona pels altres quan estàs baix és la millor manera de sentir-te millor :)",
    "cs": "Pamatuj: udělat něco hezkého pro druhé, když je ti mizerně, je nejlepší způsob, jak si zvednout náladu :)",
    "da": "Husk: at gøre noget godt for andre, når du er nede, er den bedste måde at få det bedre på :)",
    "de": "Denk dran: Anderen etwas Gutes zu tun, wenn du am Boden bist, ist der beste Weg, dich besser zu fühlen :)",
    "el": "Θυμήσου: το να κάνεις κάτι όμορφο για τους άλλους όταν είσαι πεσμένος είναι ο καλύτερος τρόπος να νιώσεις καλύτερα :)",
    "es": "Recuerda: hacer algo bueno por los demás cuando estás mal es la mejor manera de sentirte mejor :)",
    "es-419": "Recuerda: hacer algo lindo por los demás cuando estás mal es la mejor forma de sentirte mejor :)",
    "fi": "Muista: jonkin mukavan tekeminen muille, kun olet maassa, on paras tapa piristyä :)",
    "fr": "Souviens-toi : faire quelque chose de gentil pour les autres quand tu as le moral à plat est le meilleur moyen d'aller mieux :)",
    "fr-CA": "Souviens-toi : faire quelque chose de gentil pour les autres quand tu as le moral à plat est le meilleur moyen d'aller mieux :)",
    "he": "זכור: לעשות משהו טוב לאחרים כשאתה בשפל זו הדרך הטובה ביותר להרגיש טוב יותר :)",
    "hi": "याद रखें: जब आप उदास हों तो दूसरों के लिए कुछ अच्छा करना खुद को बेहतर महसूस कराने का सबसे अच्छा तरीका है :)",
    "hr": "Zapamti: učiniti nešto lijepo za druge kad si na dnu najbolji je način da se osjećaš bolje :)",
    "hu": "Ne feledd: ha másoknak teszel valami jót, amikor padlón vagy, az a legjobb módja, hogy jobban érezd magad :)",
    "id": "Ingat: melakukan hal baik untuk orang lain saat sedang terpuruk adalah cara terbaik agar merasa lebih baik :)",
    "it": "Ricorda: fare qualcosa di bello per gli altri quando sei giù è il modo migliore per sentirti meglio :)",
    "ja": "覚えておいて：落ち込んだときこそ誰かに親切にするのが、自分の気分を上げる一番の方法だよ :)",
    "ko": "기억하세요: 힘들 때 남에게 좋은 일을 하는 것이 기분을 회복하는 가장 좋은 방법이에요 :)",
    "ms": "Ingat: melakukan sesuatu yang baik untuk orang lain ketika sedih ialah cara terbaik untuk rasa lebih baik :)",
    "nb": "Husk: å gjøre noe hyggelig for andre når du er nedfor er den beste måten å få det bedre på :)",
    "nl": "Onthoud: iets aardigs doen voor anderen als je in de put zit is de beste manier om je beter te voelen :)",
    "pl": "Pamiętaj: zrobienie czegoś miłego dla innych, gdy jesteś na dnie, to najlepszy sposób, by poczuć się lepiej :)",
    "pt-BR": "Lembre-se: fazer algo legal pelos outros quando você está pra baixo é a melhor forma de se sentir melhor :)",
    "pt-PT": "Lembra-te: fazer algo bom pelos outros quando estás em baixo é a melhor forma de te sentires melhor :)",
    "ro": "Ține minte: să faci ceva frumos pentru ceilalți când ești la pământ e cel mai bun mod să te simți mai bine :)",
    "ru": "Помни: сделать что-то доброе для других, когда тебе плохо, — лучший способ почувствовать себя лучше :)",
    "sk": "Pamätaj: urobiť niečo pekné pre druhých, keď ti je ťažko, je najlepší spôsob, ako sa cítiť lepšie :)",
    "sv": "Kom ihåg: att göra något snällt för andra när du är nere är det bästa sättet att må bättre :)",
    "th": "จำไว้: การทำสิ่งดีๆ ให้คนอื่นตอนที่คุณท้อ คือวิธีที่ดีที่สุดที่จะทำให้รู้สึกดีขึ้น :)",
    "tr": "Unutma: kötü hissettiğinde başkalarına iyilik yapmak, kendini daha iyi hissetmenin en güzel yoludur :)",
    "uk": "Пам’ятай: зробити щось добре для інших, коли тобі зле, — найкращий спосіб почуватися краще :)",
    "vi": "Hãy nhớ: làm điều tốt cho người khác khi bạn buồn là cách tuyệt nhất để thấy khá hơn :)",
    "zh-Hans": "记住：心情低落时为别人做点好事，是让自己感觉变好的最佳方式 :)",
    "zh-Hant": "記住：心情低落時為別人做點好事，是讓自己感覺變好的最佳方式 :)"
})
t("Share", {
    "ar": "مشاركة", "ca": "Comparteix", "cs": "Sdílet", "da": "Del", "de": "Teilen",
    "el": "Κοινοποίηση", "es": "Compartir", "es-419": "Compartir", "fi": "Jaa", "fr": "Partager",
    "fr-CA": "Partager", "he": "שיתוף", "hi": "साझा करें", "hr": "Podijeli", "hu": "Megosztás",
    "id": "Bagikan", "it": "Condividi", "ja": "シェア", "ko": "공유", "ms": "Kongsi",
    "nb": "Del", "nl": "Delen", "pl": "Udostępnij", "pt-BR": "Compartilhar", "pt-PT": "Partilhar",
    "ro": "Distribuie", "ru": "Поделиться", "sk": "Zdieľať", "sv": "Dela", "th": "แชร์",
    "tr": "Paylaş", "uk": "Поділитися", "vi": "Chia sẻ", "zh-Hans": "分享", "zh-Hant": "分享"
})
t("Karma", {
    "ar": "كارما", "ca": "Karma", "cs": "Karma", "da": "Karma", "de": "Karma",
    "el": "Κάρμα", "es": "Karma", "es-419": "Karma", "fi": "Karma", "fr": "Karma",
    "fr-CA": "Karma", "he": "קארמה", "hi": "कर्म", "hr": "Karma", "hu": "Karma",
    "id": "Karma", "it": "Karma", "ja": "カルマ", "ko": "카르마", "ms": "Karma",
    "nb": "Karma", "nl": "Karma", "pl": "Karma", "pt-BR": "Karma", "pt-PT": "Karma",
    "ro": "Karma", "ru": "Карма", "sk": "Karma", "sv": "Karma", "th": "กรรม",
    "tr": "Karma", "uk": "Карма", "vi": "Nghiệp", "zh-Hans": "因果", "zh-Hant": "因果"
})

# ============================================================
# TIP JAR
# ============================================================
t("Karma is a 😸", {
    "ar": "الكارما قطة لطيفة 😸", "ca": "El karma és un 😸", "cs": "Karma je 😸", "da": "Karma er en 😸", "de": "Karma ist eine 😸",
    "el": "Το κάρμα είναι μια 😸", "es": "El karma es un 😸", "es-419": "El karma es un 😸", "fi": "Karma on 😸", "fr": "Le karma est un 😸",
    "fr-CA": "Le karma est un 😸", "he": "קארמה היא 😸", "hi": "कर्म एक 😸 है", "hr": "Karma je 😸", "hu": "A karma egy 😸",
    "id": "Karma itu 😸", "it": "Il karma è un 😸", "ja": "カルマは😸", "ko": "카르마는 😸", "ms": "Karma ialah 😸",
    "nb": "Karma er en 😸", "nl": "Karma is een 😸", "pl": "Karma to 😸", "pt-BR": "O karma é um 😸", "pt-PT": "O karma é um 😸",
    "ro": "Karma e o 😸", "ru": "Карма — это 😸", "sk": "Karma je 😸", "sv": "Karma är en 😸", "th": "กรรมคือ 😸",
    "tr": "Karma bir 😸", "uk": "Карма — це 😸", "vi": "Nghiệp là một chú 😸", "zh-Hans": "因果就是一只 😸", "zh-Hant": "因果就是一隻 😸"
})
t("If this stupid little app put a smile on your face please consider tipping. Every contribution, no matter how small, makes a big difference!", {
    "ar": "إذا رسم هذا التطبيق الصغير السخيف ابتسامة على وجهك، ففكّر في ترك إكرامية. كل مساهمة، مهما كانت صغيرة، تُحدث فرقًا كبيرًا!",
    "ca": "Si aquesta petita aplicació ximple t'ha fet somriure, considera deixar una propina. Cada aportació, per petita que sigui, marca una gran diferència!",
    "cs": "Jestli ti tahle hloupá aplikace vykouzlila úsměv, zvaž drobné spropitné. Každý příspěvek, i ten nejmenší, znamená velký rozdíl!",
    "da": "Hvis denne lille fjollede app fik dig til at smile, så overvej at give drikkepenge. Ethvert bidrag, uanset hvor lille, gør en stor forskel!",
    "de": "Wenn dir diese kleine, alberne App ein Lächeln entlockt hat, denk über ein Trinkgeld nach. Jeder Beitrag, egal wie klein, macht einen großen Unterschied!",
    "el": "Αν αυτή η χαζή μικρή εφαρμογή σου έφερε ένα χαμόγελο, σκέψου να αφήσεις ένα φιλοδώρημα. Κάθε συνεισφορά, όσο μικρή κι αν είναι, κάνει μεγάλη διαφορά!",
    "es": "Si esta pequeña y tonta app te ha sacado una sonrisa, plantéate dejar una propina. Cada aportación, por pequeña que sea, marca una gran diferencia.",
    "es-419": "Si esta pequeña y tonta app te sacó una sonrisa, considera dejar una propina. ¡Cada aporte, por pequeño que sea, hace una gran diferencia!",
    "fi": "Jos tämä typerä pieni sovellus sai sinut hymyilemään, harkitse tippiä. Jokainen lahjoitus, olipa se kuinka pieni tahansa, merkitsee paljon!",
    "fr": "Si cette petite appli idiote t'a fait sourire, pense à laisser un pourboire. Chaque contribution, aussi petite soit-elle, fait une grande différence !",
    "fr-CA": "Si cette petite appli niaise t'a fait sourire, pense à laisser un pourboire. Chaque contribution, aussi petite soit-elle, fait une grande différence !",
    "he": "אם האפליקציה הקטנה והטיפשית הזו גרמה לך לחייך, שקול להשאיר טיפ. כל תרומה, קטנה ככל שתהיה, עושה הבדל גדול!",
    "hi": "अगर इस छोटे-से बेवकूफ़ ऐप ने आपके चेहरे पर मुस्कान लाई, तो टिप देने पर विचार करें। हर योगदान, चाहे कितना भी छोटा हो, बड़ा फ़र्क डालता है!",
    "hr": "Ako ti je ova glupava aplikacijica izmamila osmijeh, razmisli o napojnici. Svaki doprinos, koliko god malen, čini veliku razliku!",
    "hu": "Ha ez a buta kis app mosolyt csalt az arcodra, fontold meg a borravalót. Minden hozzájárulás, bármilyen kicsi is, nagy különbséget jelent!",
    "id": "Jika aplikasi kecil konyol ini membuatmu tersenyum, pertimbangkan memberi tip. Setiap kontribusi, sekecil apa pun, sangat berarti!",
    "it": "Se questa stupida appicina ti ha strappato un sorriso, valuta di lasciare una mancia. Ogni contributo, per quanto piccolo, fa una grande differenza!",
    "ja": "このちっぽけでおバカなアプリで笑顔になれたなら、チップを検討してね。どんなに小さな支援でも、大きな違いになるんだ！",
    "ko": "이 작고 엉뚱한 앱이 미소를 줬다면 팁을 고려해 주세요. 아무리 작은 후원이라도 큰 힘이 됩니다!",
    "ms": "Jika aplikasi kecil yang kelakar ini buat anda tersenyum, pertimbangkan untuk memberi tip. Setiap sumbangan, sekecil mana pun, amat bermakna!",
    "nb": "Hvis denne lille tullete appen fikk deg til å smile, vurder å gi tips. Hvert bidrag, uansett hvor lite, utgjør en stor forskjell!",
    "nl": "Als deze stomme kleine app je een glimlach bezorgde, overweeg dan een fooi. Elke bijdrage, hoe klein ook, maakt een groot verschil!",
    "pl": "Jeśli ta głupiutka aplikacja wywołała uśmiech na twojej twarzy, rozważ napiwek. Każdy datek, choćby najmniejszy, robi wielką różnicę!",
    "pt-BR": "Se esse appzinho bobo te fez sorrir, considere deixar uma gorjeta. Cada contribuição, por menor que seja, faz uma grande diferença!",
    "pt-PT": "Se esta aplicaçãozinha tonta te fez sorrir, considera deixar uma gorjeta. Cada contribuição, por mais pequena que seja, faz uma grande diferença!",
    "ro": "Dacă această aplicație mică și caraghioasă te-a făcut să zâmbești, ia în calcul un bacșiș. Orice contribuție, oricât de mică, face o mare diferență!",
    "ru": "Если это глупое маленькое приложение вызвало у вас улыбку, подумайте о чаевых. Любой вклад, каким бы малым он ни был, имеет огромное значение!",
    "sk": "Ak ti táto hlúpučká aplikácia vyčarila úsmev, zváž prepitné. Každý príspevok, akokoľvek malý, znamená veľký rozdiel!",
    "sv": "Om den här lilla fåniga appen fick dig att le, överväg en dricks. Varje bidrag, hur litet det än är, gör stor skillnad!",
    "th": "ถ้าแอปเล็กๆ งี่เง่านี้ทำให้คุณยิ้มได้ ลองพิจารณาให้ทิปดูนะ ทุกการสนับสนุน ไม่ว่าน้อยแค่ไหน ก็สร้างความเปลี่ยนแปลงที่ยิ่งใหญ่!",
    "tr": "Bu küçük, saçma uygulama yüzünü güldürdüyse bahşiş bırakmayı düşün. Ne kadar küçük olursa olsun her katkı büyük fark yaratır!",
    "uk": "Якщо цей дурненький маленький застосунок викликав у тебе усмішку, подумай про чайові. Будь-який внесок, хай навіть найменший, має велике значення!",
    "vi": "Nếu ứng dụng nhỏ ngớ ngẩn này khiến bạn mỉm cười, hãy cân nhắc tặng một chút. Mỗi đóng góp, dù nhỏ đến đâu, đều tạo nên khác biệt lớn!",
    "zh-Hans": "如果这个又小又傻的应用让你会心一笑，欢迎打赏。每一份心意，无论多小，都意义非凡！",
    "zh-Hant": "如果這個又小又傻的應用讓你會心一笑，歡迎打賞。每一份心意，無論多小，都意義非凡！"
})
t("Buy some karma!", {
    "ar": "اشترِ بعض الكارما!", "ca": "Compra una mica de karma!", "cs": "Kupte si trochu karmy!", "da": "Køb lidt karma!", "de": "Kauf dir etwas Karma!",
    "el": "Αγόρασε λίγο κάρμα!", "es": "¡Compra un poco de karma!", "es-419": "¡Compra un poco de karma!", "fi": "Osta vähän karmaa!", "fr": "Achète un peu de karma !",
    "fr-CA": "Achète un peu de karma !", "he": "קנה קצת קארמה!", "hi": "थोड़ा कर्म खरीदें!", "hr": "Kupi malo karme!", "hu": "Vegyél egy kis karmát!",
    "id": "Beli sedikit karma!", "it": "Comprati un po' di karma!", "ja": "カルマを買おう！", "ko": "카르마를 좀 사세요!", "ms": "Beli sedikit karma!",
    "nb": "Kjøp litt karma!", "nl": "Koop wat karma!", "pl": "Kup trochę karmy!", "pt-BR": "Compre um pouco de karma!", "pt-PT": "Compra um pouco de karma!",
    "ro": "Cumpără niște karma!", "ru": "Купи немного кармы!", "sk": "Kúp si trochu karmy!", "sv": "Köp lite karma!", "th": "ซื้อกรรมดีสักหน่อย!",
    "tr": "Biraz karma satın al!", "uk": "Купи трохи карми!", "vi": "Mua một chút nghiệp lành!", "zh-Hans": "买点因果吧！", "zh-Hant": "買點因果吧！"
})
t("Something went wrong: %@", {
    "ar": "حدث خطأ ما: %@", "ca": "Alguna cosa ha anat malament: %@", "cs": "Něco se pokazilo: %@", "da": "Noget gik galt: %@", "de": "Etwas ist schiefgelaufen: %@",
    "el": "Κάτι πήγε στραβά: %@", "es": "Algo salió mal: %@", "es-419": "Algo salió mal: %@", "fi": "Jokin meni pieleen: %@", "fr": "Une erreur s'est produite : %@",
    "fr-CA": "Une erreur s'est produite : %@", "he": "משהו השתבש: %@", "hi": "कुछ गलत हो गया: %@", "hr": "Nešto je pošlo po zlu: %@", "hu": "Valami hiba történt: %@",
    "id": "Terjadi kesalahan: %@", "it": "Qualcosa è andato storto: %@", "ja": "問題が発生しました：%@", "ko": "문제가 발생했습니다: %@", "ms": "Sesuatu tidak kena: %@",
    "nb": "Noe gikk galt: %@", "nl": "Er is iets misgegaan: %@", "pl": "Coś poszło nie tak: %@", "pt-BR": "Algo deu errado: %@", "pt-PT": "Algo correu mal: %@",
    "ro": "Ceva nu a mers bine: %@", "ru": "Что-то пошло не так: %@", "sk": "Niečo sa pokazilo: %@", "sv": "Något gick fel: %@", "th": "เกิดข้อผิดพลาด: %@",
    "tr": "Bir şeyler ters gitti: %@", "uk": "Щось пішло не так: %@", "vi": "Đã xảy ra lỗi: %@", "zh-Hans": "出了点问题：%@", "zh-Hant": "出了點問題：%@"
})
t("Maybe Later", {
    "ar": "ربما لاحقًا", "ca": "Potser més tard", "cs": "Možná později", "da": "Måske senere", "de": "Vielleicht später",
    "el": "Ίσως αργότερα", "es": "Quizá más tarde", "es-419": "Tal vez después", "fi": "Ehkä myöhemmin", "fr": "Peut-être plus tard",
    "fr-CA": "Peut-être plus tard", "he": "אולי מאוחר יותר", "hi": "शायद बाद में", "hr": "Možda kasnije", "hu": "Talán később",
    "id": "Mungkin Nanti", "it": "Forse più tardi", "ja": "あとで", "ko": "나중에", "ms": "Mungkin Nanti",
    "nb": "Kanskje senere", "nl": "Misschien later", "pl": "Może później", "pt-BR": "Talvez depois", "pt-PT": "Talvez mais tarde",
    "ro": "Poate mai târziu", "ru": "Может, позже", "sk": "Možno neskôr", "sv": "Kanske senare", "th": "ไว้ทีหลัง",
    "tr": "Belki Sonra", "uk": "Можливо, пізніше", "vi": "Để sau", "zh-Hans": "稍后再说", "zh-Hant": "稍後再說"
})

# ============================================================
# SETTINGS — SECTION HEADERS
# ============================================================
t("Appearance", {
    "ar": "المظهر", "ca": "Aparença", "cs": "Vzhled", "da": "Udseende", "de": "Erscheinungsbild",
    "el": "Εμφάνιση", "es": "Apariencia", "es-419": "Apariencia", "fi": "Ulkoasu", "fr": "Apparence",
    "fr-CA": "Apparence", "he": "מראה", "hi": "रूप", "hr": "Izgled", "hu": "Megjelenés",
    "id": "Tampilan", "it": "Aspetto", "ja": "外観", "ko": "디스플레이", "ms": "Penampilan",
    "nb": "Utseende", "nl": "Weergave", "pl": "Wygląd", "pt-BR": "Aparência", "pt-PT": "Aspeto",
    "ro": "Aspect", "ru": "Оформление", "sk": "Vzhľad", "sv": "Utseende", "th": "ลักษณะที่ปรากฏ",
    "tr": "Görünüm", "uk": "Вигляд", "vi": "Giao diện", "zh-Hans": "外观", "zh-Hant": "外觀"
})
t("General", {
    "ar": "عام", "ca": "General", "cs": "Obecné", "da": "Generelt", "de": "Allgemein",
    "el": "Γενικά", "es": "General", "es-419": "General", "fi": "Yleiset", "fr": "Général",
    "fr-CA": "Général", "he": "כללי", "hi": "सामान्य", "hr": "Općenito", "hu": "Általános",
    "id": "Umum", "it": "Generali", "ja": "一般", "ko": "일반", "ms": "Umum",
    "nb": "Generelt", "nl": "Algemeen", "pl": "Ogólne", "pt-BR": "Geral", "pt-PT": "Geral",
    "ro": "General", "ru": "Основные", "sk": "Všeobecné", "sv": "Allmänt", "th": "ทั่วไป",
    "tr": "Genel", "uk": "Загальні", "vi": "Chung", "zh-Hans": "通用", "zh-Hant": "一般"
})
t("Legal", {
    "ar": "قانوني", "ca": "Legal", "cs": "Právní informace", "da": "Juridisk", "de": "Rechtliches",
    "el": "Νομικά", "es": "Legal", "es-419": "Legal", "fi": "Lakiasiat", "fr": "Mentions légales",
    "fr-CA": "Mentions légales", "he": "משפטי", "hi": "कानूनी", "hr": "Pravno", "hu": "Jogi információk",
    "id": "Hukum", "it": "Note legali", "ja": "法的事項", "ko": "법적 고지", "ms": "Undang-undang",
    "nb": "Juridisk", "nl": "Juridisch", "pl": "Informacje prawne", "pt-BR": "Jurídico", "pt-PT": "Informação legal",
    "ro": "Aspecte juridice", "ru": "Юридическая информация", "sk": "Právne informácie", "sv": "Juridiskt", "th": "ข้อมูลทางกฎหมาย",
    "tr": "Yasal", "uk": "Юридична інформація", "vi": "Pháp lý", "zh-Hans": "法律", "zh-Hant": "法律"
})
t("Security", {
    "ar": "الأمان", "ca": "Seguretat", "cs": "Zabezpečení", "da": "Sikkerhed", "de": "Sicherheit",
    "el": "Ασφάλεια", "es": "Seguridad", "es-419": "Seguridad", "fi": "Suojaus", "fr": "Sécurité",
    "fr-CA": "Sécurité", "he": "אבטחה", "hi": "सुरक्षा", "hr": "Sigurnost", "hu": "Biztonság",
    "id": "Keamanan", "it": "Sicurezza", "ja": "セキュリティ", "ko": "보안", "ms": "Keselamatan",
    "nb": "Sikkerhet", "nl": "Beveiliging", "pl": "Bezpieczeństwo", "pt-BR": "Segurança", "pt-PT": "Segurança",
    "ro": "Securitate", "ru": "Безопасность", "sk": "Zabezpečenie", "sv": "Säkerhet", "th": "ความปลอดภัย",
    "tr": "Güvenlik", "uk": "Безпека", "vi": "Bảo mật", "zh-Hans": "安全", "zh-Hant": "安全"
})
t("Login Methods", {
    "ar": "طرق تسجيل الدخول", "ca": "Mètodes d'inici de sessió", "cs": "Způsoby přihlášení", "da": "Loginmetoder", "de": "Anmeldemethoden",
    "el": "Μέθοδοι σύνδεσης", "es": "Métodos de inicio de sesión", "es-419": "Métodos de inicio de sesión", "fi": "Kirjautumistavat", "fr": "Méthodes de connexion",
    "fr-CA": "Méthodes de connexion", "he": "שיטות התחברות", "hi": "लॉगिन विधियाँ", "hr": "Načini prijave", "hu": "Bejelentkezési módok",
    "id": "Metode Masuk", "it": "Metodi di accesso", "ja": "ログイン方法", "ko": "로그인 방법", "ms": "Kaedah Log Masuk",
    "nb": "Innloggingsmetoder", "nl": "Inlogmethoden", "pl": "Metody logowania", "pt-BR": "Métodos de login", "pt-PT": "Métodos de início de sessão",
    "ro": "Metode de autentificare", "ru": "Способы входа", "sk": "Spôsoby prihlásenia", "sv": "Inloggningsmetoder", "th": "วิธีเข้าสู่ระบบ",
    "tr": "Giriş Yöntemleri", "uk": "Способи входу", "vi": "Phương thức đăng nhập", "zh-Hans": "登录方式", "zh-Hant": "登入方式"
})
t("Danger Zone", {
    "ar": "منطقة الخطر", "ca": "Zona de perill", "cs": "Nebezpečná zóna", "da": "Farezone", "de": "Gefahrenzone",
    "el": "Ζώνη κινδύνου", "es": "Zona de peligro", "es-419": "Zona de peligro", "fi": "Vaaravyöhyke", "fr": "Zone à risque",
    "fr-CA": "Zone à risque", "he": "אזור מסוכן", "hi": "खतरे का क्षेत्र", "hr": "Opasna zona", "hu": "Veszélyzóna",
    "id": "Zona Berbahaya", "it": "Zona pericolosa", "ja": "危険な操作", "ko": "위험 구역", "ms": "Zon Bahaya",
    "nb": "Faresone", "nl": "Gevarenzone", "pl": "Strefa zagrożenia", "pt-BR": "Zona de perigo", "pt-PT": "Zona de perigo",
    "ro": "Zonă periculoasă", "ru": "Опасная зона", "sk": "Nebezpečná zóna", "sv": "Farozon", "th": "โซนอันตราย",
    "tr": "Tehlikeli Bölge", "uk": "Небезпечна зона", "vi": "Vùng nguy hiểm", "zh-Hans": "危险区域", "zh-Hant": "危險區域"
})
t("Personal Info", {
    "ar": "معلومات شخصية", "ca": "Informació personal", "cs": "Osobní údaje", "da": "Personlige oplysninger", "de": "Persönliche Daten",
    "el": "Προσωπικά στοιχεία", "es": "Información personal", "es-419": "Información personal", "fi": "Henkilötiedot", "fr": "Informations personnelles",
    "fr-CA": "Renseignements personnels", "he": "פרטים אישיים", "hi": "व्यक्तिगत जानकारी", "hr": "Osobni podaci", "hu": "Személyes adatok",
    "id": "Info Pribadi", "it": "Informazioni personali", "ja": "個人情報", "ko": "개인 정보", "ms": "Maklumat Peribadi",
    "nb": "Personlig informasjon", "nl": "Persoonlijke gegevens", "pl": "Dane osobowe", "pt-BR": "Informações pessoais", "pt-PT": "Informações pessoais",
    "ro": "Informații personale", "ru": "Личные данные", "sk": "Osobné údaje", "sv": "Personlig information", "th": "ข้อมูลส่วนตัว",
    "tr": "Kişisel Bilgiler", "uk": "Особиста інформація", "vi": "Thông tin cá nhân", "zh-Hans": "个人信息", "zh-Hant": "個人資訊"
})

# ============================================================
# SETTINGS — CELLS
# ============================================================
t("Theme", {
    "ar": "السمة", "ca": "Tema", "cs": "Motiv", "da": "Tema", "de": "Design",
    "el": "Θέμα", "es": "Tema", "es-419": "Tema", "fi": "Teema", "fr": "Thème",
    "fr-CA": "Thème", "he": "ערכת נושא", "hi": "थीम", "hr": "Tema", "hu": "Téma",
    "id": "Tema", "it": "Tema", "ja": "テーマ", "ko": "테마", "ms": "Tema",
    "nb": "Tema", "nl": "Thema", "pl": "Motyw", "pt-BR": "Tema", "pt-PT": "Tema",
    "ro": "Temă", "ru": "Тема", "sk": "Motív", "sv": "Tema", "th": "ธีม",
    "tr": "Tema", "uk": "Тема", "vi": "Giao diện", "zh-Hans": "主题", "zh-Hant": "主題"
})
t("Roadmap", {
    "ar": "خارطة الطريق", "ca": "Full de ruta", "cs": "Plán vývoje", "da": "Køreplan", "de": "Roadmap",
    "el": "Χάρτης πορείας", "es": "Hoja de ruta", "es-419": "Hoja de ruta", "fi": "Tiekartta", "fr": "Feuille de route",
    "fr-CA": "Feuille de route", "he": "מפת דרכים", "hi": "रोडमैप", "hr": "Plan razvoja", "hu": "Ütemterv",
    "id": "Peta Jalan", "it": "Roadmap", "ja": "ロードマップ", "ko": "로드맵", "ms": "Peta Jalan",
    "nb": "Veikart", "nl": "Roadmap", "pl": "Plan rozwoju", "pt-BR": "Roadmap", "pt-PT": "Roteiro",
    "ro": "Foaie de parcurs", "ru": "Дорожная карта", "sk": "Plán vývoja", "sv": "Färdplan", "th": "แผนพัฒนา",
    "tr": "Yol Haritası", "uk": "Дорожня карта", "vi": "Lộ trình", "zh-Hans": "路线图", "zh-Hant": "路線圖"
})
t("Changelog", {
    "ar": "سجل التغييرات", "ca": "Registre de canvis", "cs": "Seznam změn", "da": "Ændringslog", "de": "Änderungsprotokoll",
    "el": "Αρχείο αλλαγών", "es": "Registro de cambios", "es-419": "Registro de cambios", "fi": "Muutosloki", "fr": "Journal des modifications",
    "fr-CA": "Journal des modifications", "he": "יומן שינויים", "hi": "बदलाव लॉग", "hr": "Zapisnik promjena", "hu": "Változásnapló",
    "id": "Catatan Perubahan", "it": "Registro modifiche", "ja": "変更履歴", "ko": "변경 사항", "ms": "Log Perubahan",
    "nb": "Endringslogg", "nl": "Wijzigingslogboek", "pl": "Lista zmian", "pt-BR": "Registro de alterações", "pt-PT": "Registo de alterações",
    "ro": "Jurnal de modificări", "ru": "История изменений", "sk": "Zoznam zmien", "sv": "Ändringslogg", "th": "บันทึกการเปลี่ยนแปลง",
    "tr": "Değişiklik Günlüğü", "uk": "Журнал змін", "vi": "Nhật ký thay đổi", "zh-Hans": "更新日志", "zh-Hant": "更新日誌"
})
t("Update Available", {
    "ar": "يتوفر تحديث", "ca": "Actualització disponible", "cs": "Dostupná aktualizace", "da": "Opdatering tilgængelig", "de": "Update verfügbar",
    "el": "Διαθέσιμη ενημέρωση", "es": "Actualización disponible", "es-419": "Actualización disponible", "fi": "Päivitys saatavilla", "fr": "Mise à jour disponible",
    "fr-CA": "Mise à jour disponible", "he": "עדכון זמין", "hi": "अपडेट उपलब्ध", "hr": "Dostupno ažuriranje", "hu": "Frissítés érhető el",
    "id": "Pembaruan Tersedia", "it": "Aggiornamento disponibile", "ja": "アップデートあり", "ko": "업데이트 가능", "ms": "Kemas Kini Tersedia",
    "nb": "Oppdatering tilgjengelig", "nl": "Update beschikbaar", "pl": "Dostępna aktualizacja", "pt-BR": "Atualização disponível", "pt-PT": "Atualização disponível",
    "ro": "Actualizare disponibilă", "ru": "Доступно обновление", "sk": "Dostupná aktualizácia", "sv": "Uppdatering tillgänglig", "th": "มีอัปเดต",
    "tr": "Güncelleme Mevcut", "uk": "Доступне оновлення", "vi": "Có bản cập nhật", "zh-Hans": "有可用更新", "zh-Hant": "有可用更新"
})
t("Leave Feedback", {
    "ar": "إرسال ملاحظات", "ca": "Deixar comentaris", "cs": "Zanechat zpětnou vazbu", "da": "Giv feedback", "de": "Feedback geben",
    "el": "Αφήστε σχόλια", "es": "Enviar comentarios", "es-419": "Dejar comentarios", "fi": "Anna palautetta", "fr": "Laisser un avis",
    "fr-CA": "Laisser un commentaire", "he": "השאר משוב", "hi": "प्रतिक्रिया दें", "hr": "Ostavite povratnu informaciju", "hu": "Visszajelzés küldése",
    "id": "Beri Masukan", "it": "Lascia un feedback", "ja": "フィードバックを送る", "ko": "피드백 남기기", "ms": "Tinggalkan Maklum Balas",
    "nb": "Gi tilbakemelding", "nl": "Feedback geven", "pl": "Zostaw opinię", "pt-BR": "Deixar feedback", "pt-PT": "Deixar feedback",
    "ro": "Lasă feedback", "ru": "Оставить отзыв", "sk": "Zanechať spätnú väzbu", "sv": "Lämna feedback", "th": "ส่งความคิดเห็น",
    "tr": "Geri Bildirim Bırak", "uk": "Залишити відгук", "vi": "Để lại phản hồi", "zh-Hans": "提交反馈", "zh-Hant": "提供意見回饋"
})
t("Write a Review", {
    "ar": "اكتب مراجعة", "ca": "Escriu una ressenya", "cs": "Napsat recenzi", "da": "Skriv en anmeldelse", "de": "Bewertung schreiben",
    "el": "Γράψτε μια κριτική", "es": "Escribir una reseña", "es-419": "Escribir una reseña", "fi": "Kirjoita arvostelu", "fr": "Rédiger un avis",
    "fr-CA": "Rédiger un avis", "he": "כתוב ביקורת", "hi": "समीक्षा लिखें", "hr": "Napišite recenziju", "hu": "Értékelés írása",
    "id": "Tulis Ulasan", "it": "Scrivi una recensione", "ja": "レビューを書く", "ko": "리뷰 작성", "ms": "Tulis Ulasan",
    "nb": "Skriv en anmeldelse", "nl": "Schrijf een review", "pl": "Napisz recenzję", "pt-BR": "Escrever avaliação", "pt-PT": "Escrever avaliação",
    "ro": "Scrie o recenzie", "ru": "Написать отзыв", "sk": "Napísať recenziu", "sv": "Skriv ett omdöme", "th": "เขียนรีวิว",
    "tr": "Değerlendirme Yaz", "uk": "Написати відгук", "vi": "Viết đánh giá", "zh-Hans": "撰写评价", "zh-Hant": "撰寫評論"
})
t("Share this App", {
    "ar": "شارك هذا التطبيق", "ca": "Comparteix aquesta app", "cs": "Sdílet tuto aplikaci", "da": "Del denne app", "de": "Diese App teilen",
    "el": "Κοινοποίηση αυτής της εφαρμογής", "es": "Compartir esta app", "es-419": "Compartir esta app", "fi": "Jaa tämä sovellus", "fr": "Partager cette app",
    "fr-CA": "Partager cette appli", "he": "שתף את האפליקציה", "hi": "यह ऐप साझा करें", "hr": "Podijeli ovu aplikaciju", "hu": "Az alkalmazás megosztása",
    "id": "Bagikan Aplikasi Ini", "it": "Condividi questa app", "ja": "このアプリをシェア", "ko": "이 앱 공유", "ms": "Kongsi Apl Ini",
    "nb": "Del denne appen", "nl": "Deel deze app", "pl": "Udostępnij tę aplikację", "pt-BR": "Compartilhar este app", "pt-PT": "Partilhar esta app",
    "ro": "Distribuie această aplicație", "ru": "Поделиться приложением", "sk": "Zdieľať túto aplikáciu", "sv": "Dela den här appen", "th": "แชร์แอปนี้",
    "tr": "Bu Uygulamayı Paylaş", "uk": "Поділитися застосунком", "vi": "Chia sẻ ứng dụng này", "zh-Hans": "分享此应用", "zh-Hant": "分享此應用程式"
})

# ============================================================
# ACCOUNT SCREEN / AUTH
# ============================================================
t("Account", {
    "ar": "الحساب", "ca": "Compte", "cs": "Účet", "da": "Konto", "de": "Account",
    "el": "Λογαριασμός", "es": "Cuenta", "es-419": "Cuenta", "fi": "Tili", "fr": "Compte",
    "fr-CA": "Compte", "he": "חשבון", "hi": "खाता", "hr": "Račun", "hu": "Fiók",
    "id": "Akun", "it": "Account", "ja": "アカウント", "ko": "계정", "ms": "Akaun",
    "nb": "Konto", "nl": "Account", "pl": "Konto", "pt-BR": "Conta", "pt-PT": "Conta",
    "ro": "Cont", "ru": "Аккаунт", "sk": "Účet", "sv": "Konto", "th": "บัญชี",
    "tr": "Hesap", "uk": "Обліковий запис", "vi": "Tài khoản", "zh-Hans": "账户", "zh-Hant": "帳戶"
})
t("Anonymous", {
    "ar": "مجهول", "ca": "Anònim", "cs": "Anonymní", "da": "Anonym", "de": "Anonym",
    "el": "Ανώνυμος", "es": "Anónimo", "es-419": "Anónimo", "fi": "Nimetön", "fr": "Anonyme",
    "fr-CA": "Anonyme", "he": "אנונימי", "hi": "अनाम", "hr": "Anonimno", "hu": "Névtelen",
    "id": "Anonim", "it": "Anonimo", "ja": "匿名", "ko": "익명", "ms": "Tanpa Nama",
    "nb": "Anonym", "nl": "Anoniem", "pl": "Anonimowy", "pt-BR": "Anônimo", "pt-PT": "Anónimo",
    "ro": "Anonim", "ru": "Аноним", "sk": "Anonymný", "sv": "Anonym", "th": "ไม่ระบุชื่อ",
    "tr": "Anonim", "uk": "Анонім", "vi": "Ẩn danh", "zh-Hans": "匿名", "zh-Hant": "匿名"
})
t("Sign in", {
    "ar": "تسجيل الدخول", "ca": "Inicia la sessió", "cs": "Přihlásit se", "da": "Log ind", "de": "Anmelden",
    "el": "Σύνδεση", "es": "Iniciar sesión", "es-419": "Iniciar sesión", "fi": "Kirjaudu sisään", "fr": "Se connecter",
    "fr-CA": "Se connecter", "he": "התחברות", "hi": "साइन इन करें", "hr": "Prijava", "hu": "Bejelentkezés",
    "id": "Masuk", "it": "Accedi", "ja": "サインイン", "ko": "로그인", "ms": "Log Masuk",
    "nb": "Logg inn", "nl": "Inloggen", "pl": "Zaloguj się", "pt-BR": "Entrar", "pt-PT": "Iniciar sessão",
    "ro": "Conectează-te", "ru": "Войти", "sk": "Prihlásiť sa", "sv": "Logga in", "th": "เข้าสู่ระบบ",
    "tr": "Giriş Yap", "uk": "Увійти", "vi": "Đăng nhập", "zh-Hans": "登录", "zh-Hant": "登入"
})
t("Link an email", {
    "ar": "ربط بريد إلكتروني", "ca": "Vincula un correu electrònic", "cs": "Propojit e-mail", "da": "Tilknyt en e-mail", "de": "E-Mail verknüpfen",
    "el": "Σύνδεση email", "es": "Vincular un correo", "es-419": "Vincular un correo", "fi": "Liitä sähköposti", "fr": "Associer un e-mail",
    "fr-CA": "Associer un courriel", "he": "קישור אימייל", "hi": "एक ईमेल लिंक करें", "hr": "Poveži e-poštu", "hu": "E-mail összekapcsolása",
    "id": "Tautkan email", "it": "Collega un'email", "ja": "メールを連携", "ko": "이메일 연결", "ms": "Pautkan e-mel",
    "nb": "Koble til en e-post", "nl": "Een e-mail koppelen", "pl": "Połącz e-mail", "pt-BR": "Vincular um e-mail", "pt-PT": "Associar um e-mail",
    "ro": "Asociază un e-mail", "ru": "Привязать почту", "sk": "Prepojiť e-mail", "sv": "Länka en e-post", "th": "เชื่อมต่ออีเมล",
    "tr": "E-posta bağla", "uk": "Прив’язати email", "vi": "Liên kết email", "zh-Hans": "关联邮箱", "zh-Hant": "連結電子郵件"
})
t("Edit Profile", {
    "ar": "تعديل الملف الشخصي", "ca": "Edita el perfil", "cs": "Upravit profil", "da": "Rediger profil", "de": "Profil bearbeiten",
    "el": "Επεξεργασία προφίλ", "es": "Editar perfil", "es-419": "Editar perfil", "fi": "Muokkaa profiilia", "fr": "Modifier le profil",
    "fr-CA": "Modifier le profil", "he": "עריכת פרופיל", "hi": "प्रोफ़ाइल संपादित करें", "hr": "Uredi profil", "hu": "Profil szerkesztése",
    "id": "Edit Profil", "it": "Modifica profilo", "ja": "プロフィールを編集", "ko": "프로필 편집", "ms": "Edit Profil",
    "nb": "Rediger profil", "nl": "Profiel bewerken", "pl": "Edytuj profil", "pt-BR": "Editar perfil", "pt-PT": "Editar perfil",
    "ro": "Editează profilul", "ru": "Изменить профиль", "sk": "Upraviť profil", "sv": "Redigera profil", "th": "แก้ไขโปรไฟล์",
    "tr": "Profili Düzenle", "uk": "Редагувати профіль", "vi": "Chỉnh sửa hồ sơ", "zh-Hans": "编辑个人资料", "zh-Hant": "編輯個人資料"
})
t("Change Password", {
    "ar": "تغيير كلمة المرور", "ca": "Canvia la contrasenya", "cs": "Změnit heslo", "da": "Skift adgangskode", "de": "Passwort ändern",
    "el": "Αλλαγή κωδικού", "es": "Cambiar contraseña", "es-419": "Cambiar contraseña", "fi": "Vaihda salasana", "fr": "Modifier le mot de passe",
    "fr-CA": "Modifier le mot de passe", "he": "שינוי סיסמה", "hi": "पासवर्ड बदलें", "hr": "Promijeni lozinku", "hu": "Jelszó módosítása",
    "id": "Ubah Kata Sandi", "it": "Cambia password", "ja": "パスワードを変更", "ko": "비밀번호 변경", "ms": "Tukar Kata Laluan",
    "nb": "Endre passord", "nl": "Wachtwoord wijzigen", "pl": "Zmień hasło", "pt-BR": "Alterar senha", "pt-PT": "Alterar palavra-passe",
    "ro": "Schimbă parola", "ru": "Изменить пароль", "sk": "Zmeniť heslo", "sv": "Ändra lösenord", "th": "เปลี่ยนรหัสผ่าน",
    "tr": "Şifreyi Değiştir", "uk": "Змінити пароль", "vi": "Đổi mật khẩu", "zh-Hans": "更改密码", "zh-Hant": "變更密碼"
})
t("Logout", {
    "ar": "تسجيل الخروج", "ca": "Tanca la sessió", "cs": "Odhlásit se", "da": "Log ud", "de": "Abmelden",
    "el": "Αποσύνδεση", "es": "Cerrar sesión", "es-419": "Cerrar sesión", "fi": "Kirjaudu ulos", "fr": "Se déconnecter",
    "fr-CA": "Se déconnecter", "he": "התנתקות", "hi": "लॉग आउट", "hr": "Odjava", "hu": "Kijelentkezés",
    "id": "Keluar", "it": "Esci", "ja": "ログアウト", "ko": "로그아웃", "ms": "Log Keluar",
    "nb": "Logg ut", "nl": "Uitloggen", "pl": "Wyloguj się", "pt-BR": "Sair", "pt-PT": "Terminar sessão",
    "ro": "Deconectare", "ru": "Выйти", "sk": "Odhlásiť sa", "sv": "Logga ut", "th": "ออกจากระบบ",
    "tr": "Çıkış Yap", "uk": "Вийти", "vi": "Đăng xuất", "zh-Hans": "退出登录", "zh-Hant": "登出"
})
t("Delete Account", {
    "ar": "حذف الحساب", "ca": "Elimina el compte", "cs": "Smazat účet", "da": "Slet konto", "de": "Account löschen",
    "el": "Διαγραφή λογαριασμού", "es": "Eliminar cuenta", "es-419": "Eliminar cuenta", "fi": "Poista tili", "fr": "Supprimer le compte",
    "fr-CA": "Supprimer le compte", "he": "מחיקת חשבון", "hi": "खाता हटाएँ", "hr": "Izbriši račun", "hu": "Fiók törlése",
    "id": "Hapus Akun", "it": "Elimina account", "ja": "アカウントを削除", "ko": "계정 삭제", "ms": "Padam Akaun",
    "nb": "Slett konto", "nl": "Account verwijderen", "pl": "Usuń konto", "pt-BR": "Excluir conta", "pt-PT": "Eliminar conta",
    "ro": "Șterge contul", "ru": "Удалить аккаунт", "sk": "Odstrániť účet", "sv": "Radera konto", "th": "ลบบัญชี",
    "tr": "Hesabı Sil", "uk": "Видалити обліковий запис", "vi": "Xóa tài khoản", "zh-Hans": "删除账户", "zh-Hant": "刪除帳戶"
})

# ============================================================
# EDIT PROFILE SCREEN
# ============================================================
t("First Name", {
    "ar": "الاسم الأول", "ca": "Nom", "cs": "Jméno", "da": "Fornavn", "de": "Vorname",
    "el": "Όνομα", "es": "Nombre", "es-419": "Nombre", "fi": "Etunimi", "fr": "Prénom",
    "fr-CA": "Prénom", "he": "שם פרטי", "hi": "पहला नाम", "hr": "Ime", "hu": "Keresztnév",
    "id": "Nama Depan", "it": "Nome", "ja": "名", "ko": "이름", "ms": "Nama Pertama",
    "nb": "Fornavn", "nl": "Voornaam", "pl": "Imię", "pt-BR": "Nome", "pt-PT": "Nome próprio",
    "ro": "Prenume", "ru": "Имя", "sk": "Meno", "sv": "Förnamn", "th": "ชื่อจริง",
    "tr": "Ad", "uk": "Ім’я", "vi": "Tên", "zh-Hans": "名字", "zh-Hant": "名字"
})
t("Last Name", {
    "ar": "اسم العائلة", "ca": "Cognoms", "cs": "Příjmení", "da": "Efternavn", "de": "Nachname",
    "el": "Επώνυμο", "es": "Apellidos", "es-419": "Apellido", "fi": "Sukunimi", "fr": "Nom",
    "fr-CA": "Nom", "he": "שם משפחה", "hi": "उपनाम", "hr": "Prezime", "hu": "Vezetéknév",
    "id": "Nama Belakang", "it": "Cognome", "ja": "姓", "ko": "성", "ms": "Nama Akhir",
    "nb": "Etternavn", "nl": "Achternaam", "pl": "Nazwisko", "pt-BR": "Sobrenome", "pt-PT": "Apelido",
    "ro": "Nume", "ru": "Фамилия", "sk": "Priezvisko", "sv": "Efternamn", "th": "นามสกุล",
    "tr": "Soyad", "uk": "Прізвище", "vi": "Họ", "zh-Hans": "姓氏", "zh-Hant": "姓氏"
})
t("Display Name", {
    "ar": "الاسم المعروض", "ca": "Nom visible", "cs": "Zobrazované jméno", "da": "Vist navn", "de": "Anzeigename",
    "el": "Εμφανιζόμενο όνομα", "es": "Nombre visible", "es-419": "Nombre para mostrar", "fi": "Näyttönimi", "fr": "Nom affiché",
    "fr-CA": "Nom affiché", "he": "שם תצוגה", "hi": "प्रदर्शन नाम", "hr": "Prikazano ime", "hu": "Megjelenített név",
    "id": "Nama Tampilan", "it": "Nome visualizzato", "ja": "表示名", "ko": "표시 이름", "ms": "Nama Paparan",
    "nb": "Visningsnavn", "nl": "Weergavenaam", "pl": "Wyświetlana nazwa", "pt-BR": "Nome de exibição", "pt-PT": "Nome a apresentar",
    "ro": "Nume afișat", "ru": "Отображаемое имя", "sk": "Zobrazované meno", "sv": "Visningsnamn", "th": "ชื่อที่แสดง",
    "tr": "Görünen Ad", "uk": "Відображуване ім’я", "vi": "Tên hiển thị", "zh-Hans": "显示名称", "zh-Hant": "顯示名稱"
})
t("Birthday", {
    "ar": "تاريخ الميلاد", "ca": "Data de naixement", "cs": "Datum narození", "da": "Fødselsdag", "de": "Geburtstag",
    "el": "Γενέθλια", "es": "Cumpleaños", "es-419": "Cumpleaños", "fi": "Syntymäpäivä", "fr": "Date de naissance",
    "fr-CA": "Date de naissance", "he": "יום הולדת", "hi": "जन्मदिन", "hr": "Rođendan", "hu": "Születésnap",
    "id": "Ulang Tahun", "it": "Compleanno", "ja": "誕生日", "ko": "생일", "ms": "Hari Lahir",
    "nb": "Bursdag", "nl": "Verjaardag", "pl": "Urodziny", "pt-BR": "Aniversário", "pt-PT": "Data de nascimento",
    "ro": "Zi de naștere", "ru": "День рождения", "sk": "Dátum narodenia", "sv": "Födelsedag", "th": "วันเกิด",
    "tr": "Doğum Günü", "uk": "День народження", "vi": "Ngày sinh", "zh-Hans": "生日", "zh-Hant": "生日"
})

# ============================================================
# COMMON UI WORDS (shared with Tax Days — reused verbatim where applicable)
# ============================================================
t("Save", {
    "ar": "حفظ", "ca": "Desa", "cs": "Uložit", "da": "Gem", "de": "Speichern",
    "el": "Αποθήκευση", "es": "Guardar", "es-419": "Guardar", "fi": "Tallenna", "fr": "Enregistrer",
    "fr-CA": "Enregistrer", "he": "שמירה", "hi": "सहेजें", "hr": "Spremi", "hu": "Mentés",
    "id": "Simpan", "it": "Salva", "ja": "保存", "ko": "저장", "ms": "Simpan",
    "nb": "Lagre", "nl": "Opslaan", "pl": "Zapisz", "pt-BR": "Salvar", "pt-PT": "Guardar",
    "ro": "Salvează", "ru": "Сохранить", "sk": "Uložiť", "sv": "Spara", "th": "บันทึก",
    "tr": "Kaydet", "uk": "Зберегти", "vi": "Lưu", "zh-Hans": "保存", "zh-Hant": "儲存"
})
t("Cancel", {
    "ar": "إلغاء", "ca": "Cancel·la", "cs": "Zrušit", "da": "Annuller", "de": "Abbrechen",
    "el": "Ακύρωση", "es": "Cancelar", "es-419": "Cancelar", "fi": "Peruuta", "fr": "Annuler",
    "fr-CA": "Annuler", "he": "ביטול", "hi": "रद्द करें", "hr": "Odustani", "hu": "Mégse",
    "id": "Batal", "it": "Annulla", "ja": "キャンセル", "ko": "취소", "ms": "Batal",
    "nb": "Avbryt", "nl": "Annuleren", "pl": "Anuluj", "pt-BR": "Cancelar", "pt-PT": "Cancelar",
    "ro": "Anulează", "ru": "Отмена", "sk": "Zrušiť", "sv": "Avbryt", "th": "ยกเลิก",
    "tr": "İptal", "uk": "Скасувати", "vi": "Hủy", "zh-Hans": "取消", "zh-Hant": "取消"
})
t("OK", {
    "ar": "موافق", "ca": "D'acord", "cs": "OK", "da": "OK", "de": "OK",
    "el": "OK", "es": "Aceptar", "es-419": "Aceptar", "fi": "OK", "fr": "OK",
    "fr-CA": "OK", "he": "אישור", "hi": "ठीक है", "hr": "U redu", "hu": "OK",
    "id": "OK", "it": "OK", "ja": "OK", "ko": "확인", "ms": "OK",
    "nb": "OK", "nl": "OK", "pl": "OK", "pt-BR": "OK", "pt-PT": "OK",
    "ro": "OK", "ru": "ОК", "sk": "OK", "sv": "OK", "th": "ตกลง",
    "tr": "Tamam", "uk": "OK", "vi": "OK", "zh-Hans": "好", "zh-Hant": "好"
})

# ============================================================
# PLURAL STRINGS (stringsDict) — count-interpolated copy
# Not currently emitted by an interpolated literal in the app, but the
# History total reads as "N rejections"; provided so the catalog covers the
# pluralized count when used.
# ============================================================
p(
    "%lld rejections",
    "%lld rejection", "%lld rejections",
    {
        "ar": {"zero": "%lld رفض", "one": "رفض واحد", "two": "رفضان", "few": "%lld حالات رفض", "many": "%lld حالة رفض", "other": "%lld حالة رفض"},
        "ca": {"one": "%lld rebuig", "other": "%lld rebutjos"},
        "cs": {"one": "%lld odmítnutí", "few": "%lld odmítnutí", "many": "%lld odmítnutí", "other": "%lld odmítnutí"},
        "da": {"one": "%lld afslag", "other": "%lld afslag"},
        "de": {"one": "%lld Absage", "other": "%lld Absagen"},
        "el": {"one": "%lld απόρριψη", "other": "%lld απορρίψεις"},
        "en-AU": {"one": "%lld rejection", "other": "%lld rejections"},
        "en-GB": {"one": "%lld rejection", "other": "%lld rejections"},
        "es": {"one": "%lld rechazo", "other": "%lld rechazos"},
        "es-419": {"one": "%lld rechazo", "other": "%lld rechazos"},
        "fi": {"one": "%lld hylkäys", "other": "%lld hylkäystä"},
        "fr": {"one": "%lld refus", "other": "%lld refus"},
        "fr-CA": {"one": "%lld refus", "other": "%lld refus"},
        "he": {"one": "דחייה אחת", "two": "שתי דחיות", "many": "%lld דחיות", "other": "%lld דחיות"},
        "hi": {"one": "%lld अस्वीकृति", "other": "%lld अस्वीकृतियाँ"},
        "hr": {"one": "%lld odbijanje", "few": "%lld odbijanja", "other": "%lld odbijanja"},
        "hu": {"one": "%lld elutasítás", "other": "%lld elutasítás"},
        "id": {"other": "%lld penolakan"},
        "it": {"one": "%lld rifiuto", "other": "%lld rifiuti"},
        "ja": {"other": "%lld 件の不採用"},
        "ko": {"other": "거절 %lld건"},
        "ms": {"other": "%lld penolakan"},
        "nb": {"one": "%lld avslag", "other": "%lld avslag"},
        "nl": {"one": "%lld afwijzing", "other": "%lld afwijzingen"},
        "pl": {"one": "%lld odrzucenie", "few": "%lld odrzucenia", "many": "%lld odrzuceń", "other": "%lld odrzucenia"},
        "pt-BR": {"one": "%lld rejeição", "other": "%lld rejeições"},
        "pt-PT": {"one": "%lld rejeição", "other": "%lld rejeições"},
        "ro": {"one": "%lld respingere", "few": "%lld respingeri", "other": "%lld de respingeri"},
        "ru": {"one": "%lld отказ", "few": "%lld отказа", "many": "%lld отказов", "other": "%lld отказа"},
        "sk": {"one": "%lld odmietnutie", "few": "%lld odmietnutia", "many": "%lld odmietnutia", "other": "%lld odmietnutí"},
        "sv": {"one": "%lld avslag", "other": "%lld avslag"},
        "th": {"other": "การถูกปฏิเสธ %lld ครั้ง"},
        "tr": {"one": "%lld ret", "other": "%lld ret"},
        "uk": {"one": "%lld відмова", "few": "%lld відмови", "many": "%lld відмов", "other": "%lld відмови"},
        "vi": {"other": "%lld lần từ chối"},
        "zh-Hans": {"other": "%lld 次拒绝"},
        "zh-Hant": {"other": "%lld 次拒絕"},
    },
)

# ============================================================
# OUTPUT — Generate Localizable.xcstrings
# ============================================================

def plural_categories_for(lang):
    return PLURAL_CATEGORIES.get(lang, ["one", "other"])


def build_xcstrings():
    """Build the Xcode 15+ .xcstrings JSON structure."""
    strings = {}

    # Flat strings
    for key, translations in T.items():
        localizations = {
            "en": {"stringUnit": {"state": "translated", "value": key}}
        }
        for lang in LANGUAGES:
            if lang in translations:
                value = translations[lang]
            elif lang in ("en-AU", "en-GB"):
                # English variants fall back to the base English source string.
                value = key
            else:
                continue
            localizations[lang] = {
                "stringUnit": {"state": "translated", "value": value}
            }
        strings[key] = {
            "extractionState": "manual",
            "localizations": localizations,
        }

    # Plural strings (stringsDict-style variations)
    for key, spec in P.items():
        en_one = spec["en_one"]
        en_other = spec["en_other"]
        variations = spec["variations"]

        def make_plural_unit(forms):
            return {
                "variations": {
                    "plural": {
                        cat: {"stringUnit": {"state": "translated", "value": val}}
                        for cat, val in forms.items()
                    }
                }
            }

        localizations = {
            "en": make_plural_unit({"one": en_one, "other": en_other})
        }
        for lang in LANGUAGES:
            forms = variations.get(lang)
            if forms:
                # keep only categories valid for the language, falling back to other
                cats = plural_categories_for(lang)
                kept = {c: forms[c] for c in cats if c in forms}
                if "other" not in kept and "other" in forms:
                    kept["other"] = forms["other"]
                localizations[lang] = make_plural_unit(kept)

        strings[key] = {
            "extractionState": "manual",
            "localizations": localizations,
        }

    return {
        "sourceLanguage": "en",
        "strings": strings,
        "version": "1.0",
    }


if __name__ == "__main__":
    data = build_xcstrings()
    output_path = os.path.join(os.path.dirname(__file__), "Localizable.xcstrings")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=False)
    total = len(T) + len(P)
    print(f"Wrote {total} strings × {len(LANGUAGES) + 1} locales → {output_path}")
