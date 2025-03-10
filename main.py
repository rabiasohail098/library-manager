import streamlit as st
import json
import os
import time

# 📂 Load Library Data from File (if exists)
LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# 📚 Library Data (Load from File)
library = load_library()

# 🎨 Streamlit Page Config
st.set_page_config(page_title="📖 Personal Library Manager", layout="centered")

# 🎉 UI Header
st.title("📚 Personal Library Manager")

# 🔄 Menu Selection
menu = st.sidebar.radio("📌 Select an Option", ["Add a Book", "Remove a Book", "Search a Book", "View Library"])

# 📝 1️⃣ **Add a Book**
if menu == "Add a Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍ Author Name")
    year = st.number_input("📅 Publication Year", min_value=1000, max_value=2025, step=1)
    genre = st.text_input("🎭 Genre")
    read_status = st.radio("✅ Have you read this book?", ["Yes", "No"])

    if st.button("📥 Add Book"):
        if title and author and genre:
            new_book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read_status == "Yes"
            }
            library.append(new_book)
            save_library()
            st.success(f"✅ Book '{title}' added successfully!")
            time.sleep(0.5)
            st.snow()  # ❄️ Animation for adding book
        else:
            st.warning("⚠ Please fill all fields before adding.")

# ❌ 2️⃣ **Remove a Book**
elif menu == "Remove a Book":
    st.subheader("🗑 Remove a Book")
    if library:
        book_titles = [book["title"] for book in library]
        remove_title = st.selectbox("📖 Select a book to remove", book_titles, key="remove_book")

        if st.button("🗑 Remove Book"):
            library = [book for book in library if book["title"] != remove_title]
            save_library()
            st.error(f"🚮 '{remove_title}' removed from the library!")
            time.sleep(0.5)
            st.snow()  # ❄️ Animation for removing book
    else:
        st.warning("⚠ No books available to remove!")

# 🔍 3️⃣ **Search for a Book**
elif menu == "Search a Book":
    st.subheader("🔍 Search for a Book")
    if library:
        search_title = st.selectbox("📖 Select a book to search", [book["title"] for book in library], key="search_book")
        found_book = next((book for book in library if book["title"] == search_title), None)

        if found_book:
            st.success(f"📖 **Title:** {found_book['title']}")
            st.write(f"✍ **Author:** {found_book['author']}")
            st.write(f"📅 **Year:** {found_book['year']}")
            st.write(f"🎭 **Genre:** {found_book['genre']}")
            st.write(f"✅ **Read:** {'Yes' if found_book['read'] else 'No'}")
            time.sleep(0.5)
            st.balloons()  # 🎈 Animation for search
    else:
        st.warning("⚠ No books available to search!")

# 📋 4️⃣ **View Library**


# 📊 5️⃣ **Library Statistics**
elif menu == "View Library":
    st.subheader("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])

    if total_books > 0:
        read_percentage = (read_books / total_books) * 100
    else:
        read_percentage = 0

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books}")
    st.write(f"📊 **Percentage Read:** {read_percentage:.2f}%")

    if read_percentage == 100:
        time.sleep(0.5)
        st.snow()  # ❄️ Snow effect
        time.sleep(0.5)
        st.balloons()  # 🎈 Balloons
        time.sleep(0.5)
        st.success("🎉 Congratulations! You have read all the books in your library!")

# 🔄 Save Library on Exit
save_library()
