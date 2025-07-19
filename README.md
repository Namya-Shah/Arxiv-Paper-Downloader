# 📄 Arxiv Paper Downloader

This Python script allows you to **search, preview, and download recent research papers** from [arXiv.org](https://arxiv.org/) using the `arxiv` Python API. You can either:
- Download the latest papers by **topic or keyword**
- Download a paper using its **arXiv ID**

---

## 🔧 Requirements

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

---

## 📁 How to Use

### 1. **Set Your Download Directory**

Before running the script, set your desired download location by editing this line:

```python
directory = "<Enter full directory>"
```

Replace `"<Enter full directory>"` with a valid folder path, e.g.:

```python
directory = "/Users/yourname/Documents/ArxivPapers"
```

---

## ✅ What the Script Does

### 🔍 Search and Download 10 Most Recent Papers

```python
search = Search(
    query="Artificial Intelligence",
    max_results=10,
    sort_by=SortCriterion.SubmittedDate
)
```

- Searches arXiv for the 10 most recent papers on *Artificial Intelligence*
- Downloads them as PDFs into your specified folder

> You can change the search topic and number of papers easily.

---

### 📥 How the Download Works

```python
for r in tqdm(results):
    print(r.title)
    r.download_pdf(dirpath=directory, filename=f"{r.title}.pdf")
```

- Each paper is printed and downloaded with its title as the filename.

> The `tqdm` progress bar shows real-time download progress.

---

### 🔍 Search by arXiv ID

```python
search_by_id = Search(id_list=["1804.07612"])
```

- Searches for a **specific paper** using its arXiv ID.
- Checks if the PDF already exists in the folder.
- If not, downloads it.
---

## 📚 References

- [`arxiv` Python library](https://pypi.org/project/arxiv/)
- [arXiv API documentation](https://info.arxiv.org/help/api/)

---

## 📌 Example Output

```bash
[INFO] Downloading paper: Deep Learning for AI
[INFO] Downloading paper: Generative Models for Language
...
```

> This won't be showed but it is a backend thing