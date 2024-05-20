# Význam hlaviček

```py
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
```

1.	Accept
	•	Klíč: "accept"
	•	Hodnota: "application/json"
	•	Význam: Tato hlavička informuje server o tom, jaký typ odpovědi klient očekává. V tomto případě klient říká, že očekává odpověď ve formátu JSON. Server tak ví, že by měl odpovědět daty ve formátu JSON, pokud to je možné.
2.	Content-Type
	•	Klíč: "Content-Type"
	•	Hodnota: "application/json"
	•	Význam: Tato hlavička informuje server o tom, jaký typ dat je posílán v těle požadavku. V tomto případě klient říká, že tělo požadavku obsahuje data ve formátu JSON. Server tak ví, jak má interpretovat data obsažená v těle požadavku.

## Kdy se tyto hlavičky používají

•	Accept: Používá se hlavně u GET požadavků, kde klient očekává odpověď v určitém formátu. Může se ale použít i u jiných typů požadavků (POST, PUT, DELETE), pokud klient očekává, že server vrátí odpověď v konkrétním formátu.
•	Content-Type: Používá se u požadavků, které obsahují data v těle požadavku, tedy hlavně u POST a PUT požadavků. Říká serveru, jaký je formát těchto dat (např. JSON, XML, HTML, text).


```py
headers = {
    "accept": "application/json",  # Specifikuje, že klient očekává odpověď ve formátu JSON.
    "Content-Type": "application/json",  # Určuje typ dat odesílaných v těle požadavku, v tomto případě JSON.
    "Authorization": "Bearer your_access_token",  # Posílá autentizační token pro ověření uživatele.
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",  # Identifikuje klienta, který odesílá požadavek (zde konkrétní webový prohlížeč).
    "Accept-Language": "en-US,en;q=0.5",  # Specifikuje preferovaný jazyk odpovědi, zde angličtina (USA).
    "Cache-Control": "no-cache",  # Řídí ukládání do mezipaměti, zde žádá, aby nebyla použita mezipaměť.
    "Referer": "https://example.com/page",  # Posílá URL adresu stránky, ze které byl požadavek odeslán.
    "X-Requested-With": "XMLHttpRequest",  # Označuje, že požadavek byl odeslán pomocí AJAX (obvykle hodnotou XMLHttpRequest).
    "Content-Length": "348",  # Určuje velikost těla požadavku v bajtech.
    "Accept-Encoding": "gzip, deflate, br",  # Specifikuje typy kompresních algoritmů, které klient akceptuje.
    "Host": "example.com",  # Specifikuje doménu, na kterou je požadavek směrován.
    "Connection": "keep-alive",  # Udržuje spojení otevřené pro další požadavky.
    "DNT": "1",  # Indikuje, že uživatel si nepřeje být sledován (Do Not Track).
    "Origin": "https://example.com"  # Specifikuje původní server, ze kterého požadavek pochází.
}
```

```py
response = requests.post(url, headers=headers, json=data)
```