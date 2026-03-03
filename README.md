# 🌐 Python Site Connectivity Checker

A simple command-line tool built with Python that checks website connectivity and returns HTTP response status codes.

---

## 🚀 Features

- Check if a website is reachable
- Display HTTP status code
- Handle connection errors
- Automatically adds https:// if missing

---

## 🛠️ Technologies Used

- Python 3
- urllib

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/site-connectivity-checker.git
cd site-connectivity-checker
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

Enter a website URL when prompted.

Example:

```
Input the URL of the site you want to check: google.com
```

---

## 📄 Example Output

```
Checking connectivity checker program
Connected to https://google.com successfully
Response code: 200
```

---

## ⚠️ Error Handling

The program handles:
- HTTP errors (404, 500...)
- Connection errors
- Invalid URLs

---

## 📌 Future Improvements

- Add response time measurement
- Monitor multiple sites
- Save logs to file
- Add GUI version
- Convert to web app (Flask)


